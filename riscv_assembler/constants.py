_INSTR_NAME_TO_OPCODE_RV32I_Base = {
    'LUI': 0b0110111,
    'AUIPC': 0b0010111,
    'JAL': 0b1101111,
    'JALR': 0b1100111,
    'BEQ': 0b1100011,
    'BNE': 0b1100011,
    'BLT': 0b1100011,
    'BGE': 0b1100011,
    'BLTU': 0b1100011,
    'BGEU': 0b1100011,
    'LB': 0b0000011,
    'LH': 0b0000011,
    'LW': 0b0000011,
    'LBU': 0b0000011,
    'LHU': 0b0000011,
    'SB': 0b0100011,
    'SH': 0b0100011,
    'SW': 0b0100011,
    'ADDI': 0b0010011,
    'SLTI': 0b0010011,
    'SLTIU': 0b0010011,
    'XORI': 0b0010011,
    'ORI': 0b0010011,
    'ANDI': 0b0010011,
    'SLLI': 0b0010011,
    'SRLI': 0b0010011,
    'SRAI': 0b0010011,
    'ADD': 0b0110011,
    'SUB': 0b0110011,
    'SLL': 0b0110011,
    'SLT': 0b0110011,
    'SLTU': 0b0110011,
    'XOR': 0b0110011,
    'SRL': 0b0110011,
    'SRA': 0b0110011,
    'OR': 0b0110011,
    'AND': 0b0110011,
    'FENCE': 0b0001111,
    'ECALL': 0b1110011,
    'EBREAK': 0b1110011,
    'CSRRW': 0b1110011,
    'CSRRS': 0b1110011,
    'CSRRC': 0b1110011,
    'CSRRWI': 0b1110011,
    'CSRRSI': 0b1110011,
    'CSRRCI': 0b1110011,
    'FENCE.I': 0b0001111,
}

_INSTR_NAME_TO_OPCODE_RV64I_Base = {
    'LWU': 0b0000011,
    'LD': 0b0000011,
    'SD': 0b0100011,
    'SLLI': 0b0010011,
    'SRLI': 0b0010011,
    'SRAI': 0b0010011,
    'ADDIW': 0b0011011,
    'SLLIW': 0b0011011,
    'SRLIW': 0b0011011,
    'SRAIW': 0b0011011,
    'ADDW': 0b0111011,
    'SUBW': 0b0111011,
    'SLLW': 0b0111011,
    'SRLW': 0b0111011,
    'SRAW': 0b0111011,
}

_INSTR_NAME_TO_OPCODE_RV32M_Standard_Extension = {
    'MUL': 0b0110011,
    'MULH': 0b0110011,
    'MULHSU': 0b0110011,
    'MULHU': 0b0110011,
    'DIV': 0b0110011,
    'DIVU': 0b0110011,
    'REM': 0b0110011,
    'REMU': 0b0110011,
}

_INSTR_NAME_TO_OPCODE_RV64M_Standard_Extension = {
    'MULW': 0b0111011,
    'DIVW': 0b0111011,
    'DIVUW': 0b0111011,
    'REMW': 0b0111011,
    'REMUW': 0b0111011,
}

_INSTR_NAME_TO_OPCODE_RV32A_Standard_Extension = {
    'LR.W': 0b0101111,
    'SC.W': 0b0101111,
    'AMOSWAP.W': 0b0101111,
    'AMOADD.W': 0b0101111,
    'AMOXOR.W': 0b0101111,
    'AMOAND.W': 0b0101111,
    'AMOOR.W': 0b0101111,
    'AMOMIN.W': 0b0101111,
    'AMOMAX.W': 0b0101111,
    'AMOMINU.W': 0b0101111,
    'AMOMAXU.W': 0b0101111,
}

_INSTR_NAME_TO_OPCODE_RV64A_Standard_Extension = {
    'LR.D': 0b0101111,
    'SC.D': 0b0101111,
    'AMOSWAP.D': 0b0101111,
    'AMOADD.D': 0b0101111,
    'AMOXOR.D': 0b0101111,
    'AMOAND.D': 0b0101111,
    'AMOOR.D': 0b0101111,
    'AMOMIN.D': 0b0101111,
    'AMOMAX.D': 0b0101111,
    'AMOMINU.D': 0b0101111,
    'AMOMAXU.D': 0b0101111,
}

_INSTR_NAME_TO_OPCODE_RV32F_Standard_Extension = {
    'FLW': 0b0000111,
    'FSW': 0b0100111,
    'FMADD.S': 0b1000011,
    'FMSUB.S': 0b1000111,
    'FNMSUB.S': 0b1001011,
    'FNMADD.S': 0b1001111,
    'FADD.S': 0b1010011,
    'FSUB.S': 0b1010011,
    'FMUL.S': 0b1010011,
    'FDIV.S': 0b1010011,
    'FSQRT.S': 0b1010011,
    'FSGNJ.S': 0b1010011,
    'FSGNJN.S': 0b1010011,
    'FSGNJX.S': 0b1010011,
    'FMIN.S': 0b1010011,
    'FMAX.S': 0b1010011,
    'FCVT.W.S': 0b1010011,
    'FCVT.WU.S': 0b1010011,
    'FMV.X.W': 0b1010011,
    'FEQ.S': 0b1010011,
    'FLT.S': 0b1010011,
    'FLE.S': 0b1010011,
    'FCLASS.S': 0b1010011,
    'FCVT.S.W': 0b1010011,
    'FCVT.S.WU': 0b1010011,
    'FMV.W.X': 0b1010011,
}

_INSTR_NAME_TO_OPCODE_RV64F_Standard_Extension = {
    'FCVT.L.S': 0b1010011,
    'FCVT.LU.S': 0b1010011,
    'FCVT.S.L': 0b1010011,
    'FCVT.S.LU': 0b1010011,
}

_INSTR_NAME_TO_OPCODE_RV32D_Standard_Extension = {
    'FLD': 0b0000111,
    'FSD': 0b0100111,
    'FMADD.D': 0b1000011,
    'FMSUB.D': 0b1000111,
    'FNMSUB.D': 0b1001011,
    'FNMADD.D': 0b1001111,
    'FADD.D': 0b1010011,
    'FSUB.D': 0b1010011,
    'FMUL.D': 0b1010011,
    'FDIV.D': 0b1010011,
    'FSQRT.D': 0b1010011,
    'FSGNJ.D': 0b1010011,
    'FSGNJN.D': 0b1010011,
    'FSGNJX.D': 0b1010011,
    'FMIN.D': 0b1010011,
    'FMAX.D': 0b1010011,
    'FCVT.S.D': 0b1010011,
    'FCVT.D.S': 0b1010011,
    'FEQ.D': 0b1010011,
    'FLT.D': 0b1010011,
    'FLE.D': 0b1010011,
    'FCLASS.D': 0b1010011,
    'FCVT.W.D': 0b1010011,
    'FCVT.WU.D': 0b1010011,
    'FCVT.D.W': 0b1010011,
    'FCVT.D.WU': 0b1010011,
}

_INSTR_NAME_TO_OPCODE_RV64D_Standard_Extension = {
    'FCVT.L.D': 0b1010011,
    'FCVT.LU.D': 0b1010011,
    'FMV.X.D': 0b1010011,
    'FCVT.D.L': 0b1010011,
    'FCVT.D.LU': 0b1010011,
    'FMV.D.X': 0b1010011,
}

_REGISTER_NAME_TO_NUMBER =\
    {f'x{i}': i for i in range(32)}\
  | {f'a{i}': i + 10 for i in range(8)}\
  | {f's{i}': i + 18 - 2 for i in range(2, 12)}\
  | {
        'zero': 0,
        'ra': 1,
        'sp': 2,
        'gp': 3,
        'tp': 4,
        't0': 5,
        't1': 6,
        't2': 7,
        's0': 8,
        'fp': 8,
        's1': 9,
        't3': 28,
        't4': 29,
        't5': 30,
        't6': 31,
    }

_REGISTER_NAME_TO_NUMBER_FP = \
    {f'f{i}': i for i in range(32)}\
  | {f'ft{i}': i for i in range(8)}\
  | {f'fa{i}': i + 10 for i in range(8)}\
  | {f'fs{i}': i + 18 - 2 for i in range(2, 12)}\
  | {
        'fs0': 8,
        'fs1': 9,
        'ft8': 28,
        'ft9': 29,
        'ft10': 30,
        'ft11': 31,
    }


_INSTR_NAME_TO_TYPE_RV32I_Base = {
    'LUI': 'U',
    'AUIPC': 'U',
    'JAL': 'J',
    'JALR': 'I',
    'BEQ': 'B',
    'BNE': 'B',
    'BLT': 'B',
    'BGE': 'B',
    'BLTU': 'B',
    'BGEU': 'B',
    'LB': 'I',
    'LH': 'I',
    'LW': 'I',
    'LBU': 'I',
    'LHU': 'I',
    'SB': 'S',
    'SH': 'S',
    'SW': 'S',
    'ADDI': 'I',
    'SLTI': 'I',
    'SLTIU': 'I',
    'XORI': 'I',
    'ORI': 'I',
    'ANDI': 'I',
    'SLLI': '0000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '0000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '0100000 shamt rs1 101 rd 0010011 SRAI',
    'ADD': 'R',
    'SUB': 'R',
    'SLL': 'R',
    'SLT': 'R',
    'SLTU': 'R',
    'XOR': 'R',
    'SRL': 'R',
    'SRA': 'R',
    'OR': 'R',
    'AND': 'R',
    'FENCE': '0000 pred succ 00000 000 00000 0001111 FENCE',
    'FENCE.I': '0000 0000 0000 00000 001 00000 0001111 FENCE.I',
    'ECALL': '000000000000 00000 000 00000 1110011 ECALL',
    'EBREAK': '000000000001 00000 000 00000 1110011 EBREAK',
    'CSRRW': 'csr rs1 001 rd 1110011 CSRRW',
    'CSRRS': 'csr rs1 010 rd 1110011 CSRRS',
    'CSRRC': 'csr rs1 011 rd 1110011 CSRRC',
    'CSRRWI': 'csr zimm 101 rd 1110011 CSRRWI',
    'CSRRSI': 'csr zimm 110 rd 1110011 CSRRSI',
    'CSRRCI': 'csr zimm 111 rd 1110011 CSRRCI',
}

_INSTR_NAME_TO_TYPE_RV64I_Base = {
    'LWU': 'I',
    'LD': 'I',
    'SD': 'S',
    'SLLI': '000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '010000 shamt rs1 101 rd 0010011 SRAI',
    'ADDIW': 'I',
    'SLLIW': '0000000 shamt rs1 001 rd 0011011 SLLIW',
    'SRLIW': '0000000 shamt rs1 101 rd 0011011 SRLIW',
    'SRAIW': '0100000 shamt rs1 101 rd 0011011 SRAIW',
    'ADDW': 'R',
    'SUBW': 'R',
    'SLLW': 'R',
    'SRLW': 'R',
    'SRAW': 'R',
}

_INSTR_NAME_TO_TYPE_RV32M_Standard_Extension = {
    'MUL': 'R',
    'MULH': 'R',
    'MULHSU': 'R',
    'MULHU': 'R',
    'DIV': 'R',
    'DIVU': 'R',
    'REM': 'R',
    'REMU': 'R',
}

_INSTR_NAME_TO_TYPE_RV64M_Standard_Extension = {
    'MULW': 'R',
    'DIVW': 'R',
    'DIVUW': 'R',
    'REMW': 'R',
    'REMUW': 'R',
}

_INSTR_NAME_TO_TYPE_RV32A_Standard_Extension = {
    'LR.W': '00010 aq rl 00000 rs1 010 rd 0101111 LR.W',
    'SC.W': '00011 aq rl rs2 rs1 010 rd 0101111 SC.W',
    'AMOSWAP.W': '00001 aq rl rs2 rs1 010 rd 0101111 AMOSWAP.W',
    'AMOADD.W': '00000 aq rl rs2 rs1 010 rd 0101111 AMOADD.W',
    'AMOXOR.W': '00100 aq rl rs2 rs1 010 rd 0101111 AMOXOR.W',
    'AMOAND.W': '01100 aq rl rs2 rs1 010 rd 0101111 AMOAND.W',
    'AMOOR.W': '01000 aq rl rs2 rs1 010 rd 0101111 AMOOR.W',
    'AMOMIN.W': '10000 aq rl rs2 rs1 010 rd 0101111 AMOMIN.W',
    'AMOMAX.W': '10100 aq rl rs2 rs1 010 rd 0101111 AMOMAX.W',
    'AMOMINU.W': '11000 aq rl rs2 rs1 010 rd 0101111 AMOMINU.W',
    'AMOMAXU.W': '11100 aq rl rs2 rs1 010 rd 0101111 AMOMAXU.W',
}

_INSTR_NAME_TO_TYPE_RV64A_Standard_Extension = {
    'LR.D': '00010 aq rl 00000 rs1 011 rd 0101111 LR.D',
    'SC.D': '00011 aq rl rs2 rs1 011 rd 0101111 SC.D',
    'AMOSWAP.D': '00001 aq rl rs2 rs1 011 rd 0101111 AMOSWAP.D',
    'AMOADD.D': '00000 aq rl rs2 rs1 011 rd 0101111 AMOADD.D',
    'AMOXOR.D': '00100 aq rl rs2 rs1 011 rd 0101111 AMOXOR.D',
    'AMOAND.D': '01100 aq rl rs2 rs1 011 rd 0101111 AMOAND.D',
    'AMOOR.D': '01000 aq rl rs2 rs1 011 rd 0101111 AMOOR.D',
    'AMOMIN.D': '10000 aq rl rs2 rs1 011 rd 0101111 AMOMIN.D',
    'AMOMAX.D': '10100 aq rl rs2 rs1 011 rd 0101111 AMOMAX.D',
    'AMOMINU.D': '11000 aq rl rs2 rs1 011 rd 0101111 AMOMINU.D',
    'AMOMAXU.D': '11100 aq rl rs2 rs1 011 rd 0101111 AMOMAXU.D',
}

_INSTR_NAME_TO_TYPE_RV32F_Standard_Extension = {
    'FLW': 'I',
    'FSW': 'S',
    'FMADD.S': 'rs3 00 rs2 rs1 rm rd 1000011 FMADD.S',
    'FMSUB.S': 'rs3 00 rs2 rs1 rm rd 1000111 FMSUB.S',
    'FNMSUB.S': 'rs3 00 rs2 rs1 rm rd 1001011 FNMSUB.S',
    'FNMADD.S': 'rs3 00 rs2 rs1 rm rd 1001111 FNMADD.S',
    'FADD.S': '0000000 rs2 rs1 rm rd 1010011 FADD.S',
    'FSUB.S': '0000100 rs2 rs1 rm rd 1010011 FSUB.S',
    'FMUL.S': '0001000 rs2 rs1 rm rd 1010011 FMUL.S',
    'FDIV.S': '0001100 rs2 rs1 rm rd 1010011 FDIV.S',
    'FSQRT.S': '0101100 00000 rs1 rm rd 1010011 FSQRT.S',
    'FSGNJ.S': 'R',
    'FSGNJN.S': 'R',
    'FSGNJX.S': 'R',
    'FMIN.S': 'R',
    'FMAX.S': 'R',
    'FCVT.W.S': '1100000 00000 rs1 rm rd 1010011 FCVT.W.S',
    'FCVT.WU.S': '1100000 00001 rs1 rm rd 1010011 FCVT.WU.S',
    'FMV.X.W': '1110000 00000 rs1 000 rd 1010011 FMV.X.W',
    'FEQ.S': 'R',
    'FLT.S': 'R',
    'FLE.S': 'R',
    'FCLASS.S': '1110000 00000 rs1 001 rd 1010011 FCLASS.S',
    'FCVT.S.W': '1101000 00000 rs1 rm rd 1010011 FCVT.S.W',
    'FCVT.S.WU': '1101000 00001 rs1 rm rd 1010011 FCVT.S.WU',
    'FMV.W.X': '1111000 00000 rs1 000 rd 1010011 FMV.W.X',
}

_INSTR_NAME_TO_TYPE_RV64F_Standard_Extension = {
    'FCVT.L.S': '1100000 00010 rs1 rm rd 1010011 FCVT.L.S',
    'FCVT.LU.S': '1100000 00011 rs1 rm rd 1010011 FCVT.LU.S',
    'FCVT.S.L': '1101000 00010 rs1 rm rd 1010011 FCVT.S.L',
    'FCVT.S.LU': '1101000 00011 rs1 rm rd 1010011 FCVT.S.LU',
}

_INSTR_NAME_TO_TYPE_RV32D_Standard_Extension = {
    'FLD': 'I',
    'FSD': 'S',
    'FMADD.D': 'rs3 01 rs2 rs1 rm rd 1000011 FMADD.D',
    'FMSUB.D': 'rs3 01 rs2 rs1 rm rd 1000111 FMSUB.D',
    'FNMSUB.D': 'rs3 01 rs2 rs1 rm rd 1001011 FNMSUB.D',
    'FNMADD.D': 'rs3 01 rs2 rs1 rm rd 1001111 FNMADD.D',
    'FADD.D': '0000001 rs2 rs1 rm rd 1010011 FADD.D',
    'FSUB.D': '0000101 rs2 rs1 rm rd 1010011 FSUB.D',
    'FMUL.D': '0001001 rs2 rs1 rm rd 1010011 FMUL.D',
    'FDIV.D': '0001101 rs2 rs1 rm rd 1010011 FDIV.D',
    'FSQRT.D': '0101101 00000 rs1 rm rd 1010011 FSQRT.D',
    'FSGNJ.D': 'R',
    'FSGNJN.D': 'R',
    'FSGNJX.D': 'R',
    'FMIN.D': 'R',
    'FMAX.D': 'R',
    'FCVT.S.D': '0100000 00001 rs1 rm rd 1010011 FCVT.S.D',
    'FCVT.D.S': '0100001 00000 rs1 rm rd 1010011 FCVT.D.S',
    'FEQ.D': 'R',
    'FLT.D': 'R',
    'FLE.D': 'R',
    'FCLASS.D': '1110001 00000 rs1 001 rd 1010011 FCLASS.D',
    'FCVT.W.D': '1100001 00000 rs1 rm rd 1010011 FCVT.W.D',
    'FCVT.WU.D': '1100001 00001 rs1 rm rd 1010011 FCVT.WU.D',
    'FCVT.D.W': '1101001 00000 rs1 rm rd 1010011 FCVT.D.W',
    'FCVT.D.WU': '1101001 00001 rs1 rm rd 1010011 FCVT.D.WU',
}

_INSTR_NAME_TO_TYPE_RV64D_Standard_Extension = {
    'FCVT.L.D': '1100001 00010 rs1 rm rd 1010011 FCVT.L.D',
    'FCVT.LU.D': '1100001 00011 rs1 rm rd 1010011 FCVT.LU.D',
    'FMV.X.D': '1110001 00000 rs1 000 rd 1010011 FMV.X.D',
    'FCVT.D.L': '1101001 00010 rs1 rm rd 1010011 FCVT.D.L',
    'FCVT.D.LU': '1101001 00011 rs1 rm rd 1010011 FCVT.D.LU',
    'FMV.D.X': '1111001 00000 rs1 000 rd 1010011 FMV.D.X',
}


_INSTR_NAME_TO_FUNC3_RV32I_Base = {
    'LUI': 'imm[31:12] rd 0110111 LUI',
    'AUIPC': 'imm[31:12] rd 0010111 AUIPC',
    'JAL': 'imm[20|10:1|11|19:12] rd 1101111 JAL',
    'JALR': 0b000,
    'BEQ': 0b000,
    'BNE': 0b001,
    'BLT': 0b100,
    'BGE': 0b101,
    'BLTU': 0b110,
    'BGEU': 0b111,
    'LB': 0b000,
    'LH': 0b001,
    'LW': 0b010,
    'LBU': 0b100,
    'LHU': 0b101,
    'SB': 0b000,
    'SH': 0b001,
    'SW': 0b010,
    'ADDI': 0b000,
    'SLTI': 0b010,
    'SLTIU': 0b011,
    'XORI': 0b100,
    'ORI': 0b110,
    'ANDI': 0b111,
    'SLLI': '0000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '0000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '0100000 shamt rs1 101 rd 0010011 SRAI',
    'ADD': 0b000,
    'SUB': 0b000,
    'SLL': 0b001,
    'SLT': 0b010,
    'SLTU': 0b011,
    'XOR': 0b100,
    'SRL': 0b101,
    'SRA': 0b101,
    'OR': 0b110,
    'AND': 0b111,
    'FENCE': '0000 pred succ 00000 000 00000 0001111 FENCE',
    'FENCE.I': '0000 0000 0000 00000 001 00000 0001111 FENCE.I',
    'ECALL': '000000000000 00000 000 00000 1110011 ECALL',
    'EBREAK': '000000000001 00000 000 00000 1110011 EBREAK',
    'CSRRW': 'csr rs1 001 rd 1110011 CSRRW',
    'CSRRS': 'csr rs1 010 rd 1110011 CSRRS',
    'CSRRC': 'csr rs1 011 rd 1110011 CSRRC',
    'CSRRWI': 'csr zimm 101 rd 1110011 CSRRWI',
    'CSRRSI': 'csr zimm 110 rd 1110011 CSRRSI',
    'CSRRCI': 'csr zimm 111 rd 1110011 CSRRCI',
}


_INSTR_NAME_TO_FUNC3_RV64I_Base = {
    'LWU': 0b110,
    'LD': 0b011,
    'SD': 0b011,
    'SLLI': '000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '010000 shamt rs1 101 rd 0010011 SRAI',
    'ADDIW': 0b000,
    'SLLIW': '0000000 shamt rs1 001 rd 0011011 SLLIW',
    'SRLIW': '0000000 shamt rs1 101 rd 0011011 SRLIW',
    'SRAIW': '0100000 shamt rs1 101 rd 0011011 SRAIW',
    'ADDW': 0b000,
    'SUBW': 0b000,
    'SLLW': 0b001,
    'SRLW': 0b101,
    'SRAW': 0b101,
}

_INSTR_NAME_TO_FUNC3_RV32M_Standard_Extension = {
    'MUL': 0b000,
    'MULH': 0b001,
    'MULHSU': 0b010,
    'MULHU': 0b011,
    'DIV': 0b100,
    'DIVU': 0b101,
    'REM': 0b110,
    'REMU': 0b111,
}

_INSTR_NAME_TO_FUNC3_RV64M_Standard_Extension = {
    'MULW': 0b000,
    'DIVW': 0b100,
    'DIVUW': 0b101,
    'REMW': 0b110,
    'REMUW': 0b111,
}


_INSTR_NAME_TO_FUNC3_RV32A_Standard_Extension = {
    'LR.W': '00010 aq rl 00000 rs1 010 rd 0101111 LR.W',
    'SC.W': '00011 aq rl rs2 rs1 010 rd 0101111 SC.W',
    'AMOSWAP.W': '00001 aq rl rs2 rs1 010 rd 0101111 AMOSWAP.W',
    'AMOADD.W': '00000 aq rl rs2 rs1 010 rd 0101111 AMOADD.W',
    'AMOXOR.W': '00100 aq rl rs2 rs1 010 rd 0101111 AMOXOR.W',
    'AMOAND.W': '01100 aq rl rs2 rs1 010 rd 0101111 AMOAND.W',
    'AMOOR.W': '01000 aq rl rs2 rs1 010 rd 0101111 AMOOR.W',
    'AMOMIN.W': '10000 aq rl rs2 rs1 010 rd 0101111 AMOMIN.W',
    'AMOMAX.W': '10100 aq rl rs2 rs1 010 rd 0101111 AMOMAX.W',
    'AMOMINU.W': '11000 aq rl rs2 rs1 010 rd 0101111 AMOMINU.W',
    'AMOMAXU.W': '11100 aq rl rs2 rs1 010 rd 0101111 AMOMAXU.W',
}

_INSTR_NAME_TO_FUNC3_RV64A_Standard_Extension = {
    'LR.D': '00010 aq rl 00000 rs1 011 rd 0101111 LR.D',
    'SC.D': '00011 aq rl rs2 rs1 011 rd 0101111 SC.D',
    'AMOSWAP.D': '00001 aq rl rs2 rs1 011 rd 0101111 AMOSWAP.D',
    'AMOADD.D': '00000 aq rl rs2 rs1 011 rd 0101111 AMOADD.D',
    'AMOXOR.D': '00100 aq rl rs2 rs1 011 rd 0101111 AMOXOR.D',
    'AMOAND.D': '01100 aq rl rs2 rs1 011 rd 0101111 AMOAND.D',
    'AMOOR.D': '01000 aq rl rs2 rs1 011 rd 0101111 AMOOR.D',
    'AMOMIN.D': '10000 aq rl rs2 rs1 011 rd 0101111 AMOMIN.D',
    'AMOMAX.D': '10100 aq rl rs2 rs1 011 rd 0101111 AMOMAX.D',
    'AMOMINU.D': '11000 aq rl rs2 rs1 011 rd 0101111 AMOMINU.D',
    'AMOMAXU.D': '11100 aq rl rs2 rs1 011 rd 0101111 AMOMAXU.D',
}

_INSTR_NAME_TO_FUNC3_RV32F_Standard_Extension = {
    'FLW': 0b010,
    'FSW': 0b010,
    'FMADD.S': 'rs3 00 rs2 rs1 rm rd 1000011 FMADD.S',
    'FMSUB.S': 'rs3 00 rs2 rs1 rm rd 1000111 FMSUB.S',
    'FNMSUB.S': 'rs3 00 rs2 rs1 rm rd 1001011 FNMSUB.S',
    'FNMADD.S': 'rs3 00 rs2 rs1 rm rd 1001111 FNMADD.S',
    'FADD.S': '0000000 rs2 rs1 rm rd 1010011 FADD.S',
    'FSUB.S': '0000100 rs2 rs1 rm rd 1010011 FSUB.S',
    'FMUL.S': '0001000 rs2 rs1 rm rd 1010011 FMUL.S',
    'FDIV.S': '0001100 rs2 rs1 rm rd 1010011 FDIV.S',
    'FSQRT.S': '0101100 00000 rs1 rm rd 1010011 FSQRT.S',
    'FSGNJ.S': 0b000,
    'FSGNJN.S': 0b001,
    'FSGNJX.S': 0b010,
    'FMIN.S': 0b000,
    'FMAX.S': 0b001,
    'FCVT.W.S': '1100000 00000 rs1 rm rd 1010011 FCVT.W.S',
    'FCVT.WU.S': '1100000 00001 rs1 rm rd 1010011 FCVT.WU.S',
    'FMV.X.W': '1110000 00000 rs1 000 rd 1010011 FMV.X.W',
    'FEQ.S': 0b010,
    'FLT.S': 0b001,
    'FLE.S': 0b000,
    'FCLASS.S': '1110000 00000 rs1 001 rd 1010011 FCLASS.S',
    'FCVT.S.W': '1101000 00000 rs1 rm rd 1010011 FCVT.S.W',
    'FCVT.S.WU': '1101000 00001 rs1 rm rd 1010011 FCVT.S.WU',
    'FMV.W.X': '1111000 00000 rs1 000 rd 1010011 FMV.W.X',
}

_INSTR_NAME_TO_FUNC3_RV64F_Standard_Extension = {
    'FCVT.L.S': '1100000 00010 rs1 rm rd 1010011 FCVT.L.S',
    'FCVT.LU.S': '1100000 00011 rs1 rm rd 1010011 FCVT.LU.S',
    'FCVT.S.L': '1101000 00010 rs1 rm rd 1010011 FCVT.S.L',
    'FCVT.S.LU': '1101000 00011 rs1 rm rd 1010011 FCVT.S.LU',
}

_INSTR_NAME_TO_FUNC3_RV32D_Standard_Extension = {
    'FLD': 0b011,
    'FSD': 0b011,
    'FMADD.D': 'rs3 01 rs2 rs1 rm rd 1000011 FMADD.D',
    'FMSUB.D': 'rs3 01 rs2 rs1 rm rd 1000111 FMSUB.D',
    'FNMSUB.D': 'rs3 01 rs2 rs1 rm rd 1001011 FNMSUB.D',
    'FNMADD.D': 'rs3 01 rs2 rs1 rm rd 1001111 FNMADD.D',
    'FADD.D': '0000001 rs2 rs1 rm rd 1010011 FADD.D',
    'FSUB.D': '0000101 rs2 rs1 rm rd 1010011 FSUB.D',
    'FMUL.D': '0001001 rs2 rs1 rm rd 1010011 FMUL.D',
    'FDIV.D': '0001101 rs2 rs1 rm rd 1010011 FDIV.D',
    'FSQRT.D': '0101101 00000 rs1 rm rd 1010011 FSQRT.D',
    'FSGNJ.D': 0b000,
    'FSGNJN.D': 0b001,
    'FSGNJX.D': 0b010,
    'FMIN.D': 0b000,
    'FMAX.D': 0b001,
    'FCVT.S.D': '0100000 00001 rs1 rm rd 1010011 FCVT.S.D',
    'FCVT.D.S': '0100001 00000 rs1 rm rd 1010011 FCVT.D.S',
    'FEQ.D': 0b010,
    'FLT.D': 0b001,
    'FLE.D': 0b000,
    'FCLASS.D': '1110001 00000 rs1 001 rd 1010011 FCLASS.D',
    'FCVT.W.D': '1100001 00000 rs1 rm rd 1010011 FCVT.W.D',
    'FCVT.WU.D': '1100001 00001 rs1 rm rd 1010011 FCVT.WU.D',
    'FCVT.D.W': '1101001 00000 rs1 rm rd 1010011 FCVT.D.W',
    'FCVT.D.WU': '1101001 00001 rs1 rm rd 1010011 FCVT.D.WU',
}


_INSTR_NAME_TO_FUNC3_RV64D_Standard_Extension = {
    'FCVT.L.D': '1100001 00010 rs1 rm rd 1010011 FCVT.L.D',
    'FCVT.LU.D': '1100001 00011 rs1 rm rd 1010011 FCVT.LU.D',
    'FMV.X.D': '1110001 00000 rs1 000 rd 1010011 FMV.X.D',
    'FCVT.D.L': '1101001 00010 rs1 rm rd 1010011 FCVT.D.L',
    'FCVT.D.LU': '1101001 00011 rs1 rm rd 1010011 FCVT.D.LU',
    'FMV.D.X': '1111001 00000 rs1 000 rd 1010011 FMV.D.X',
}

_INSTR_NAME_TO_FUNC7_RV32I_Base = {
    'LUI': 'imm[31:12] rd 0110111 LUI',
    'AUIPC': 'imm[31:12] rd 0010111 AUIPC',
    'JAL': 'imm[20|10:1|11|19:12] rd 1101111 JAL',
    'JALR': 'imm[11:0] rs1 000 rd 1100111 JALR',
    'BEQ': 'imm[12|10:5] rs2 rs1 000 imm[4:1|11] 1100011 BEQ',
    'BNE': 'imm[12|10:5] rs2 rs1 001 imm[4:1|11] 1100011 BNE',
    'BLT': 'imm[12|10:5] rs2 rs1 100 imm[4:1|11] 1100011 BLT',
    'BGE': 'imm[12|10:5] rs2 rs1 101 imm[4:1|11] 1100011 BGE',
    'BLTU': 'imm[12|10:5] rs2 rs1 110 imm[4:1|11] 1100011 BLTU',
    'BGEU': 'imm[12|10:5] rs2 rs1 111 imm[4:1|11] 1100011 BGEU',
    'LB': 'imm[11:0] rs1 000 rd 0000011 LB',
    'LH': 'imm[11:0] rs1 001 rd 0000011 LH',
    'LW': 'imm[11:0] rs1 010 rd 0000011 LW',
    'LBU': 'imm[11:0] rs1 100 rd 0000011 LBU',
    'LHU': 'imm[11:0] rs1 101 rd 0000011 LHU',
    'SB': 'imm[11:5] rs2 rs1 000 imm[4:0] 0100011 SB',
    'SH': 'imm[11:5] rs2 rs1 001 imm[4:0] 0100011 SH',
    'SW': 'imm[11:5] rs2 rs1 010 imm[4:0] 0100011 SW',
    'ADDI': 'imm[11:0] rs1 000 rd 0010011 ADDI',
    'SLTI': 'imm[11:0] rs1 010 rd 0010011 SLTI',
    'SLTIU': 'imm[11:0] rs1 011 rd 0010011 SLTIU',
    'XORI': 'imm[11:0] rs1 100 rd 0010011 XORI',
    'ORI': 'imm[11:0] rs1 110 rd 0010011 ORI',
    'ANDI': 'imm[11:0] rs1 111 rd 0010011 ANDI',
    'SLLI': '0000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '0000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '0100000 shamt rs1 101 rd 0010011 SRAI',
    'ADD': 0b0000000,
    'SUB': 0b0100000,
    'SLL': 0b0000000,
    'SLT': 0b0000000,
    'SLTU': 0b0000000,
    'XOR': 0b0000000,
    'SRL': 0b0000000,
    'SRA': 0b0100000,
    'OR': 0b0000000,
    'AND': 0b0000000,
    'FENCE': '0000 pred succ 00000 000 00000 0001111 FENCE',
    'FENCE.I': '0000 0000 0000 00000 001 00000 0001111 FENCE.I',
    'ECALL': '000000000000 00000 000 00000 1110011 ECALL',
    'EBREAK': '000000000001 00000 000 00000 1110011 EBREAK',
    'CSRRW': 'csr rs1 001 rd 1110011 CSRRW',
    'CSRRS': 'csr rs1 010 rd 1110011 CSRRS',
    'CSRRC': 'csr rs1 011 rd 1110011 CSRRC',
    'CSRRWI': 'csr zimm 101 rd 1110011 CSRRWI',
    'CSRRSI': 'csr zimm 110 rd 1110011 CSRRSI',
    'CSRRCI': 'csr zimm 111 rd 1110011 CSRRCI',
}

_INSTR_NAME_TO_FUNC7_RV64I_Base = {
    'LWU': 'imm[11:0] rs1 110 rd 0000011 LWU',
    'LD': 'imm[11:0] rs1 011 rd 0000011 LD',
    'SD': 'imm[11:5] rs2 rs1 011 imm[4:0] 0100011 SD',
    'SLLI': '000000 shamt rs1 001 rd 0010011 SLLI',
    'SRLI': '000000 shamt rs1 101 rd 0010011 SRLI',
    'SRAI': '010000 shamt rs1 101 rd 0010011 SRAI',
    'ADDIW': 'imm[11:0] rs1 000 rd 0011011 ADDIW',
    'SLLIW': '0000000 shamt rs1 001 rd 0011011 SLLIW',
    'SRLIW': '0000000 shamt rs1 101 rd 0011011 SRLIW',
    'SRAIW': '0100000 shamt rs1 101 rd 0011011 SRAIW',
    'ADDW': 0b0000000,
    'SUBW': 0b0100000,
    'SLLW': 0b0000000,
    'SRLW': 0b0000000,
    'SRAW': 0b0100000,
}

_INSTR_NAME_TO_FUNC7_RV32M_Standard_Extension = {
    'MUL': 0b0000001,
    'MULH': 0b0000001,
    'MULHSU': 0b0000001,
    'MULHU': 0b0000001,
    'DIV': 0b0000001,
    'DIVU': 0b0000001,
    'REM': 0b0000001,
    'REMU': 0b0000001,
}

_INSTR_NAME_TO_FUNC7_RV64M_Standard_Extension = {
    'MULW': 0b0000001,
    'DIVW': 0b0000001,
    'DIVUW': 0b0000001,
    'REMW': 0b0000001,
    'REMUW': 0b0000001,
}

_INSTR_NAME_TO_FUNC7_RV32A_Standard_Extension = {
    'LR.W': '00010 aq rl 00000 rs1 010 rd 0101111 LR.W',
    'SC.W': '00011 aq rl rs2 rs1 010 rd 0101111 SC.W',
    'AMOSWAP.W': '00001 aq rl rs2 rs1 010 rd 0101111 AMOSWAP.W',
    'AMOADD.W': '00000 aq rl rs2 rs1 010 rd 0101111 AMOADD.W',
    'AMOXOR.W': '00100 aq rl rs2 rs1 010 rd 0101111 AMOXOR.W',
    'AMOAND.W': '01100 aq rl rs2 rs1 010 rd 0101111 AMOAND.W',
    'AMOOR.W': '01000 aq rl rs2 rs1 010 rd 0101111 AMOOR.W',
    'AMOMIN.W': '10000 aq rl rs2 rs1 010 rd 0101111 AMOMIN.W',
    'AMOMAX.W': '10100 aq rl rs2 rs1 010 rd 0101111 AMOMAX.W',
    'AMOMINU.W': '11000 aq rl rs2 rs1 010 rd 0101111 AMOMINU.W',
    'AMOMAXU.W': '11100 aq rl rs2 rs1 010 rd 0101111 AMOMAXU.W',
}

_INSTR_NAME_TO_FUNC7_RV64A_Standard_Extension = {
    'LR.D': '00010 aq rl 00000 rs1 011 rd 0101111 LR.D',
    'SC.D': '00011 aq rl rs2 rs1 011 rd 0101111 SC.D',
    'AMOSWAP.D': '00001 aq rl rs2 rs1 011 rd 0101111 AMOSWAP.D',
    'AMOADD.D': '00000 aq rl rs2 rs1 011 rd 0101111 AMOADD.D',
    'AMOXOR.D': '00100 aq rl rs2 rs1 011 rd 0101111 AMOXOR.D',
    'AMOAND.D': '01100 aq rl rs2 rs1 011 rd 0101111 AMOAND.D',
    'AMOOR.D': '01000 aq rl rs2 rs1 011 rd 0101111 AMOOR.D',
    'AMOMIN.D': '10000 aq rl rs2 rs1 011 rd 0101111 AMOMIN.D',
    'AMOMAX.D': '10100 aq rl rs2 rs1 011 rd 0101111 AMOMAX.D',
    'AMOMINU.D': '11000 aq rl rs2 rs1 011 rd 0101111 AMOMINU.D',
    'AMOMAXU.D': '11100 aq rl rs2 rs1 011 rd 0101111 AMOMAXU.D',
}

_INSTR_NAME_TO_FUNC7_RV32F_Standard_Extension = {
    'FLW': 'imm[11:0] rs1 010 rd 0000111 FLW',
    'FSW': 'imm[11:5] rs2 rs1 010 imm[4:0] 0100111 FSW',
    'FMADD.S': 'rs3 00 rs2 rs1 rm rd 1000011 FMADD.S',
    'FMSUB.S': 'rs3 00 rs2 rs1 rm rd 1000111 FMSUB.S',
    'FNMSUB.S': 'rs3 00 rs2 rs1 rm rd 1001011 FNMSUB.S',
    'FNMADD.S': 'rs3 00 rs2 rs1 rm rd 1001111 FNMADD.S',
    'FADD.S': '0000000 rs2 rs1 rm rd 1010011 FADD.S',
    'FSUB.S': '0000100 rs2 rs1 rm rd 1010011 FSUB.S',
    'FMUL.S': '0001000 rs2 rs1 rm rd 1010011 FMUL.S',
    'FDIV.S': '0001100 rs2 rs1 rm rd 1010011 FDIV.S',
    'FSQRT.S': '0101100 00000 rs1 rm rd 1010011 FSQRT.S',
    'FSGNJ.S': 0b0010000,
    'FSGNJN.S': 0b0010000,
    'FSGNJX.S': 0b0010000,
    'FMIN.S': 0b0010100,
    'FMAX.S': 0b0010100,
    'FCVT.W.S': '1100000 00000 rs1 rm rd 1010011 FCVT.W.S',
    'FCVT.WU.S': '1100000 00001 rs1 rm rd 1010011 FCVT.WU.S',
    'FMV.X.W': '1110000 00000 rs1 000 rd 1010011 FMV.X.W',
    'FEQ.S': 0b1010000,
    'FLT.S': 0b1010000,
    'FLE.S': 0b1010000,
    'FCLASS.S': '1110000 00000 rs1 001 rd 1010011 FCLASS.S',
    'FCVT.S.W': '1101000 00000 rs1 rm rd 1010011 FCVT.S.W',
    'FCVT.S.WU': '1101000 00001 rs1 rm rd 1010011 FCVT.S.WU',
    'FMV.W.X': '1111000 00000 rs1 000 rd 1010011 FMV.W.X',
}

_INSTR_NAME_TO_FUNC7_RV64F_Standard_Extension = {
    'FCVT.L.S': '1100000 00010 rs1 rm rd 1010011 FCVT.L.S',
    'FCVT.LU.S': '1100000 00011 rs1 rm rd 1010011 FCVT.LU.S',
    'FCVT.S.L': '1101000 00010 rs1 rm rd 1010011 FCVT.S.L',
    'FCVT.S.LU': '1101000 00011 rs1 rm rd 1010011 FCVT.S.LU',
}

_INSTR_NAME_TO_FUNC7_RV32D_Standard_Extension = {
    'FLD': 'imm[11:0] rs1 011 rd 0000111 FLD',
    'FSD': 'imm[11:5] rs2 rs1 011 imm[4:0] 0100111 FSD',
    'FMADD.D': 'rs3 01 rs2 rs1 rm rd 1000011 FMADD.D',
    'FMSUB.D': 'rs3 01 rs2 rs1 rm rd 1000111 FMSUB.D',
    'FNMSUB.D': 'rs3 01 rs2 rs1 rm rd 1001011 FNMSUB.D',
    'FNMADD.D': 'rs3 01 rs2 rs1 rm rd 1001111 FNMADD.D',
    'FADD.D': '0000001 rs2 rs1 rm rd 1010011 FADD.D',
    'FSUB.D': '0000101 rs2 rs1 rm rd 1010011 FSUB.D',
    'FMUL.D': '0001001 rs2 rs1 rm rd 1010011 FMUL.D',
    'FDIV.D': '0001101 rs2 rs1 rm rd 1010011 FDIV.D',
    'FSQRT.D': '0101101 00000 rs1 rm rd 1010011 FSQRT.D',
    'FSGNJ.D': 0b0010001,
    'FSGNJN.D': 0b0010001,
    'FSGNJX.D': 0b0010001,
    'FMIN.D': 0b0010101,
    'FMAX.D': 0b0010101,
    'FCVT.S.D': '0100000 00001 rs1 rm rd 1010011 FCVT.S.D',
    'FCVT.D.S': '0100001 00000 rs1 rm rd 1010011 FCVT.D.S',
    'FEQ.D': 0b1010001,
    'FLT.D': 0b1010001,
    'FLE.D': 0b1010001,
    'FCLASS.D': '1110001 00000 rs1 001 rd 1010011 FCLASS.D',
    'FCVT.W.D': '1100001 00000 rs1 rm rd 1010011 FCVT.W.D',
    'FCVT.WU.D': '1100001 00001 rs1 rm rd 1010011 FCVT.WU.D',
    'FCVT.D.W': '1101001 00000 rs1 rm rd 1010011 FCVT.D.W',
    'FCVT.D.WU': '1101001 00001 rs1 rm rd 1010011 FCVT.D.WU',
}

_INSTR_NAME_TO_FUNC7_RV64D_Standard_Extension = {
    'FCVT.L.D': '1100001 00010 rs1 rm rd 1010011 FCVT.L.D',
    'FCVT.LU.D': '1100001 00011 rs1 rm rd 1010011 FCVT.LU.D',
    'FMV.X.D': '1110001 00000 rs1 000 rd 1010011 FMV.X.D',
    'FCVT.D.L': '1101001 00010 rs1 rm rd 1010011 FCVT.D.L',
    'FCVT.D.LU': '1101001 00011 rs1 rm rd 1010011 FCVT.D.LU',
    'FMV.D.X': '1111001 00000 rs1 000 rd 1010011 FMV.D.X',
}


# syntax for I-type instructions is `<name> rd, rs1, imm`
# except for memory access instructions where syntax is `<name> rd, imm(rs1)`
I_TYPE_MEM_INSTRUCTIONS = {
    # RV32I_Base
    'LB',
    'LH',
    'LW',
    'LBU',
    'LHU',
    'SB',
    'SH',
    'SW',
    # RV64I_Base
    'LWU',
    'LD',
    'SD',
}


INSTR_NAME_TO_OPCODE = (
          _INSTR_NAME_TO_OPCODE_RV32I_Base
        | _INSTR_NAME_TO_OPCODE_RV64I_Base
        | _INSTR_NAME_TO_OPCODE_RV32M_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV64M_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV32A_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV64A_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV32F_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV64F_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV32D_Standard_Extension
        | _INSTR_NAME_TO_OPCODE_RV64D_Standard_Extension
)

INSTR_NAME_TO_TYPE = (
    _INSTR_NAME_TO_TYPE_RV32I_Base
  | _INSTR_NAME_TO_TYPE_RV64I_Base
  | _INSTR_NAME_TO_TYPE_RV32M_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV64M_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV32A_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV64A_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV32F_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV64F_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV32D_Standard_Extension
  | _INSTR_NAME_TO_TYPE_RV64D_Standard_Extension
)

INSTR_NAME_TO_FUNC3 = (
      _INSTR_NAME_TO_FUNC3_RV32I_Base
    | _INSTR_NAME_TO_FUNC3_RV64I_Base
    | _INSTR_NAME_TO_FUNC3_RV32M_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV64M_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV32A_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV64A_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV32F_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV64F_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV32D_Standard_Extension
    | _INSTR_NAME_TO_FUNC3_RV64D_Standard_Extension
)

INSTR_NAME_TO_FUNC7 = (
      _INSTR_NAME_TO_FUNC7_RV32I_Base
    | _INSTR_NAME_TO_FUNC7_RV64I_Base
    | _INSTR_NAME_TO_FUNC7_RV32M_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV64M_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV32A_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV64A_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV32F_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV64F_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV32D_Standard_Extension
    | _INSTR_NAME_TO_FUNC7_RV64D_Standard_Extension
)

REGISTER_NAME_TO_NUMBER = (
    _REGISTER_NAME_TO_NUMBER
  | _REGISTER_NAME_TO_NUMBER_FP
)
