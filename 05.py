import os
import sys
import string

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/05input.txt"

def main(ex, file):
    with open(file, "r") as f:
        header_complete = 0
        nr_stacks = 0
        for line in f:
            if line.strip() == "":
                continue
            if line[1] == "1":
                header_complete = 1
            if not header_complete:
                if not nr_stacks:
                    nr_stacks = len(line)//4
                    stacks = [[] for i in range (0, nr_stacks)]
                parts = [line[i:i+4] for i in range(0, len(line), 4)]
                for i, s in enumerate(parts):
                    if s[1] != " ":
                        stacks[i].append(s[1])
            else:
                if line[0] == "m":
                    line_parts = line.split(" ")
                    nr_crates = int(line_parts[1])
                    index1 = int(line_parts[3])-1
                    index2 = int(line_parts[5])-1
                    if ex == 1:
                        for i in range(0, nr_crates):
                            stacks[index2].insert(0, stacks[index1][0])
                            del stacks[index1][0]
                    else:
                        stacks[index2] = stacks[index1][0:nr_crates] + stacks[index2]
                        stacks[index1] = stacks[index1][nr_crates:]
        print("".join([stacks[i][0] for i in range(0, nr_stacks)]))

main(1, input_file)
main(2, input_file)


