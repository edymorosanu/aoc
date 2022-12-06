import os
import sys

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/01input.txt"

def main(ex, file):
    with open(file, "r") as f:
        max_sum = 0
        elf_sum = 0
        elf_sums = []
        for line in f:
            line = line.strip()
            if line != "":
                elf_sum += int(line)
            else:
                elf_sums.append(elf_sum)
                elf_sum = 0
        elf_sums.sort()
        if ex == 1:
            print(elf_sums[-1])
        else:
            print(sum(elf_sums[-3:]))

main(1, input_file)
main(2, input_file)
