import os
import sys
import string

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/03input.txt"
prio = {}
for i, ch in enumerate(list(string.ascii_lowercase) + list(string.ascii_uppercase)):
    prio[ch] = i+1

def one(file):
    with open(file, "r") as f:
        sum = 0
        for line in f:
            line = line.strip()
            half = len(line)//2
            str1 = line[:half]
            str2 = line[half:]
            for p in set(str1).intersection(str2):
                sum += prio[p]
        print(sum)

def two(file):
    with open(file, "r") as f:
        sum = 0
        group = []
        for i, line in enumerate(f):
            group.append(line.strip())
            if i%3 == 2:
                ch = set(group[0]).intersection(group[1]).intersection(group[2])
                for p in ch:
                    sum += prio[p]
                group = []
        print(sum)

one(input_file)
two(input_file)
