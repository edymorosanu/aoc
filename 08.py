import os

curr_dir = os.path.dirname(os.path.realpath(__file__))
input_file = f"{curr_dir}/08input.txt"

def main(ex, file):
    trees = []
    visible = []
    with open(file, "r") as f:
        for line in f:
            trees.append([int(tree) for tree in line.strip()])
        row_len = len(trees[0])
        col_len = len(trees)
        if ex == 1:
            for i in range(col_len):
                if i == 0 or i == col_len-1:
                    visible.append([1 for j in range(row_len)])
                else:
                    visible.append([0 for j in range(row_len)])
                    visible[i][0] = visible[i][row_len-1] = 1
                    _max = trees[i][0]
                    for j in range(1,row_len-1):
                        if trees[i][j] > _max:
                            visible[i][j] = 1
                            _max = trees[i][j]
                    _max = trees[i][row_len-1]
                    for j in range(row_len-2, 0, -1):
                        if trees[i][j] > _max:
                            visible[i][j] = 1
                            _max = trees[i][j]
            for j in range(1,row_len-1):
                _max = trees[0][j]
                for i in range(1,col_len-1):
                    if trees[i][j] > _max:
                        visible[i][j] = 1
                        _max = trees[i][j]
                _max = trees[col_len-1][j]
                for i in range(col_len-2, 0, -1):
                    if trees[i][j] > _max:
                        visible[i][j] = 1
                        _max = trees[i][j]
            visible_trees = sum([sum(el) for el in visible])
            print(visible_trees)
        else:
            scenic_score = [[0 for j in range(row_len)] for i in range(col_len)]
            for i in range(1, col_len-1):
                for j in range(1, row_len-1):
                    scenic_score[i][j] = 1
                    score = 0
                    for k in range(j-1, -1, -1):
                        score += 1
                        if trees[i][j] <= trees[i][k]:
                            break
                    if score > 0:
                        scenic_score[i][j] *= score
                    score = 0
                    for k in range(j+1, row_len):
                        score += 1
                        if trees[i][j] <= trees[i][k]:
                            break
                    if score > 0:
                        scenic_score[i][j] *= score
                    score = 0
                    for k in range(i-1, -1, -1):
                        score += 1
                        if trees[i][j] <= trees[k][j]:
                            break
                    if score > 0:
                        scenic_score[i][j] *= score
                    score = 0
                    for k in range(i+1, col_len):
                        score += 1
                        if trees[i][j] <= trees[k][j]:
                            break
                    if score > 0:
                        scenic_score[i][j] *= score
            max_scenic_score = max([max(scenic_score[i]) for i in range(col_len)])
            print(max_scenic_score)

main(1, input_file)
main(2, input_file)


