import os
import sys

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/02input.txt"
score1 = {
    "A X": 4,
    "B X": 1,
    "C X": 7,
    "A Y": 8,
    "B Y": 5,
    "C Y": 2,
    "A Z": 3,
    "B Z": 9,
    "C Z": 6
}
score2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}
def main(score, file):
    with open(file, "r") as f:
        total_score = 0
        for line in f:
            total_score += score[line.strip()]
        print(total_score)
main(score1, input_file)
main(score2, input_file)
