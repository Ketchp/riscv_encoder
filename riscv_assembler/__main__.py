from riscv_assembler.instruction import instruction_factory


def main():
    while line := input():
        instr = instruction_factory(line)
        print(hex(instr))


if __name__ == "__main__":
    main()
