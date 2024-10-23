from riscv_assembler import instruction_factory


def instr_assert(instruction: str, expected: int) -> None:
    assert int(instruction_factory(instruction)) == expected

# R-type
instr_assert('add x0, x1, x2', 0x00208033)
instr_assert('sub a0, t1, sp', 0x40230533)

# I-type
instr_assert('addi x5, x1, 10', 0x00a08293)
instr_assert('lw x6, 8(x2)', 0x00812303)
instr_assert('jalr x1, x2, 8', 0x008100e7)

# S-type
instr_assert('sw x5, 8(x2)', 0x00512423)
instr_assert('sh x5, 4(x1)', 0x00509223)
instr_assert('sb x7, 2(x3)', 0x00718123)

# B-type
# todo: label resolution not implemented
instr_assert('bne x3, x4, label', 0x00419063)
instr_assert('blt x5, x6, label', 0x0062c063)
instr_assert('bge x7, x8, label', 0x0083d063)

# U-type
instr_assert('lui x5, 0x12345', 0x123452b7)
instr_assert('auipc x6, 0x2', 0x00002317)

# J-type
# todo: label resolution not implemented
instr_assert('jal x1, label', 0x000000ef)
