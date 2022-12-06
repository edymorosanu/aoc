import os
import sys
import functools

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/01input.txt"

def main(ex, file):
    with open(file, "r") as f:
        elf_sums = list(
            map(
                lambda scores :
                    functools.reduce(
                        lambda a, b : a + b,
                        map(int,
                            filter(
                                lambda l : l != "",
                                scores.split("\n")
                            )
                        )
                    ),
                "".join(f).split("\n\n")
            )
        )
        elf_sums.sort()
        if ex == 1:
            print(elf_sums[-1])
        else:
            print(sum(elf_sums[-3:]))

main(1, input_file)
main(2, input_file)
