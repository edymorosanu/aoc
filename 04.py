import os
import sys
import string

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/04input.txt"

def main(ex, file):
    with open(file, "r") as f:
        total = 0
        for line in f:
            line = line.strip()
            pairs = line.split(",")
            pair1 = pairs[0]
            pair2 = pairs[1]
            interval1 = pair1.split("-")
            start1 = int(interval1[0])
            end1 = int(interval1[1])
            interval2 = pair2.split("-")
            start2 = int(interval2[0])
            end2 = int(interval2[1])
            if ex == 1:
                if ( start1 <= start2 and end2 <= end1 ) or (start2 <= start1 and end1 <= end2):
                    # print(f"{start1}-{end1},{start2}-{end2}")
                    total += 1
            else:
                if ( start1 <= end2 <= end1 ) or (start1 <= start2 <= end1) or (start2 <= end1 <= end2) or (start2 <= start1 <= end2):
                    # print(f"{start1}-{end1},{start2}-{end2}")
                    total += 1
        print(total)

main(1, input_file)
main(2, input_file)


