import os
import sys
import functools

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/06input.txt"

def find_sequence(a, b, length):
    if len(a) == length:
        if len(set(a)) == length:
            return a
        else:
            a = a[1:]
    a += b
    return a

def main(pck_len, file):
    with open(file, "r") as f:
        str = "".join(f).split("\n")[0]
        result = functools.reduce(lambda a,b: find_sequence(a,b,pck_len), list(str))
        print(str.find(result)+pck_len)

main(4, input_file)
main(14, input_file)


