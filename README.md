# RISC-V instruction encoder

Minimalistic encoder from assembly instruction to hex.

I needed encoder for my school project, so I wrote this tool.
I only support instruction I needed for my project,
so many instruction with special format like FENCE, ECALL are not supported.
Pseudo-instructions are also not supported.
File [constants.py](riscv_assembler/constants.py)
contains all instructions from [RISC-V Instruction Set Manual: Chapter 19](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf),
but for un-supported instructions the values are not filled properly.

Based on "[The RISC-V Instruction Set Manual
Volume I: User-Level ISA
Document Version 2.2](https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf)".
