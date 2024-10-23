from .constants import (
    I_TYPE_MEM_INSTRUCTIONS,
    REGISTER_NAME_TO_NUMBER,
    INSTR_NAME_TO_OPCODE,
    INSTR_NAME_TO_TYPE,
    INSTR_NAME_TO_FUNC3,
    INSTR_NAME_TO_FUNC7,
)


class Immediate:
    def __init__(self, value: str, instr_type: str):
        if value.startswith('0b'):
            base = 2
        elif value.startswith('0o'):
            base = 8
        elif value.startswith('0x'):
            base = 16
        else:
            base = 10

        try:
            self._label = None
            value = int(value, base=base)
        except ValueError:
            # todo check if label is valid
            # todo: decode labels
            self._label = value
            value = 0

        if value >= 2**31 or value < -2**31:
            raise ValueError('Number overflows 32bit signed number.')
        if instr_type in ('I', 'S') and (value >= 2**10 or value < -2**10):
            raise ValueError('Number overflows 11bit immediate.')
        # todo: check B label
        if instr_type == 'U' and (value >= 2**19 or value < -2**19):
            raise ValueError('Number overflows 20bit immediate.')
        # todo: check J label

        value = value & ((1 << 32) - 1)  # cast to 32bit unsigned number
        self.value = value


    def __getitem__(self, items: int | slice | tuple[int | slice, ...]) -> int:
        if not isinstance(items, tuple):
            items = (items,)

        result = 0
        for item in items:
            if isinstance(item, int):
                item = slice(item, item - 1)
            if item.step is not None:
                raise ValueError("Only step 1 possible.")
            size = abs(item.stop - item.start)
            offset = min(item.start, item.stop)
            mask = ((1 << size) - 1) << offset
            piece = (self.value & mask) >> offset
            if item.start < item.stop:
                raise NotImplementedError("Reverse order not implemented.")
            result = (result << size) | piece
        return result


class Instruction:
    def __init__(self, instruction: str):
        self.instruction = instruction
        self.opcode = INSTR_NAME_TO_OPCODE[instruction]

    @staticmethod
    def _split_args(args: str) -> list[str]:
        return [arg.strip() for arg in args.split(',')]

    @staticmethod
    def _reg_name_to_int(name: str) -> int:
        return REGISTER_NAME_TO_NUMBER[name]

    @staticmethod
    def _imm_to_int(number: str) -> int:
        return int(number)  # todo check number size

    def _raise_invalid_format(self, is_rd: bool) -> None:
        raise ValueError(
            f'Instruction {self.instruction} requires format '
            f'`{self.instruction} {"rd" if is_rd else "rs2"}, imm(rs1)`.'
        )

    def _get_reg_imm(self, args: str) -> tuple[int, str]:
        args_split = self._split_args(args)
        if len(args_split) != 2:
            raise ValueError(f'Instruction {self.instruction} requires exactly 3 arguments.')
        return (self._reg_name_to_int(args_split[0]),
                args_split[1])

    def _get_reg_imm_reg(self, args: str, is_rd: bool)\
            -> tuple[int, str, int]:
        rd, _, imm_rs1 = args.partition(',')
        if imm_rs1 == '':
            self._raise_invalid_format(is_rd)
        imm, _, rs1_rp = imm_rs1.strip().partition('(')
        if imm == '' or rs1_rp == '' or rs1_rp[-1] != ')':
            self._raise_invalid_format(is_rd)
        return (self._reg_name_to_int(rd),
                imm,
                self._reg_name_to_int(rs1_rp.rstrip(')')))

    def _get_reg_reg_imm(self, args: str) -> tuple[int, int, str]:
        args_split = self._split_args(args)
        if len(args_split) != 3:
            raise ValueError(f'Instruction {self.instruction} requires exactly 3 arguments.')
        return (self._reg_name_to_int(args_split[0]),
                self._reg_name_to_int(args_split[1]),
                args_split[2])

    def __int__(self) -> int:
        raise NotImplementedError("Subclass must implement __int__().")

    def __index__(self) -> int:
        return int(self)

class RType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        self.func7 = INSTR_NAME_TO_FUNC7[instruction]
        rd, rs1, rs2 = self._get_reg_reg_reg(args)
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2

    def _get_reg_reg_reg(self, args: str) -> tuple[int, int, int]:
        args_split = self._split_args(args)
        if len(args_split) != 3:
            raise ValueError(f'Instruction {self.instruction} requires exactly 3 arguments.')
        reg_nums = tuple(self._reg_name_to_int(reg) for reg in args_split)
        return reg_nums[0], reg_nums[1], reg_nums[2]

    def __int__(self) -> int:
        #  31-25 | 24-20 | 19-15 |  14-12 | 11-7 |  6-0
        # funct7 |  rs2  |  rs1  | funct3 |  rd  | opcode
        return (
              self.opcode
            | self.rd << 7
            | self.func3 << 12
            | self.rs1 << 15
            | self.rs2 << 20
            | self.func7 << 25
        )


class IType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        if instruction in I_TYPE_MEM_INSTRUCTIONS:
            rd, imm, rs1 = self._get_reg_imm_reg(args, is_rd=True)
        else:
            rd, rs1, imm = self._get_reg_reg_imm(args)
        self.rd = rd
        self.rs1 = rs1
        self.imm = Immediate(imm, 'I')

    def __int__(self) -> int:
        #   31-20   | 19-15 |  14-12 | 11-7 |  6-0
        # imm[11:0] |  rs1  | funct3 |  rd  | opcode
        return (
              self.opcode
            | self.rd << 7
            | self.func3 << 12
            | self.rs1 << 15
            | self.imm[11:0] << 20
        )

class SType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        rs2, imm, rs1 = self._get_reg_imm_reg(args, is_rd=False)
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = Immediate(imm, 'S')

    def __int__(self) -> int:
        #   31-25   | 24-20 | 19-15 |  14-12 |    11-7   |  6-0
        # imm[11:5] |  rs2  |  rs1  | funct3 |  imm[4:0] | opcode
        return (
              self.opcode
            | self.imm[4:0] << 7
            | self.func3 << 12
            | self.rs1 << 15
            | self.rs2 << 20
            | self.imm[11:5] << 25
        )


class BType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        rs1, rs2, imm = self._get_reg_reg_imm(args)
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = Immediate(imm, 'B')

    def __int__(self) -> int:
        #    31-25     | 24-20 | 19-15 |  14-12 |    11-7     |  6-0
        # imm[12,10:5] |  rs2  |  rs1  | funct3 | imm[4:1,11] | opcode
        # todo: immediate zero byte must be 0
        return (
              self.opcode
            | self.imm[4:1,11] << 7
            | self.func3 << 12
            | self.rs1 << 15
            | self.rs2 << 20
            | self.imm[12,10:5] << 25
        )

class UType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        rd, imm = self._get_reg_imm(args)
        self.rd = rd
        self.imm = Immediate(imm, 'U')

    def __int__(self) -> int:
        #    31-12   | 11-7 |  6-0
        # imm[31:12] |  rd  | opcode
        return (
              self.opcode
            | self.rd << 7
              # true immediate has bits [12:0] zero filed
              # in assembly we write only top [31:12] bits
              # so we need to shift by 12 bits 31 -> 19 and 12 -> 0
            | self.imm[19:0] << 12
        )

class JType(Instruction):
    def __init__(self, instruction: str, args: str):
        super().__init__(instruction)
        self.func3 = INSTR_NAME_TO_FUNC3[instruction]
        rd, imm = self._get_reg_imm(args)
        self.rd = rd
        self.imm = Immediate(imm, 'J')

    def __int__(self) -> int:
        #         31-12         | 11-7 |  6-0
        # imm[20,10:1,11,19:12] |  rd  | opcode
        return (
              self.opcode
            | self.rd << 7
            | self.imm[20,10:1,11,19:12] << 12
        )


def strip_comment(line: str) -> str:
    return line.split('#')[0]


def instruction_factory(line: str) -> Instruction:
    line = strip_comment(line)

    instruction, _, args = line.partition(' ')
    instruction = instruction.upper()

    instr_type = INSTR_NAME_TO_TYPE.get(instruction)
    if instr_type is None:
        raise ValueError(f'Unknown instruction: {instruction}')

    if instr_type == 'R':
        return RType(instruction, args)
    if instr_type == 'I':
        return IType(instruction, args)
    if instr_type == 'S':
        return SType(instruction, args)
    if instr_type == 'B':
        return BType(instruction, args)
    if instr_type == 'U':
        return UType(instruction, args)
    if instr_type == 'J':
        return JType(instruction, args)
    raise NotImplementedError(f'Instruction {instruction} not (yet) supported.')

