import math
import numpy as np

grid_test = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(grid):
    copy = grid
    cols = np.transpose(grid)

    vals = {}
    cells = []

    for j, row in enumerate(grid):
        for i, num in enumerate(row):
            if i % 3 == 0 and j % 3 == 0:
                val = grid[j][i: i + 3]
                val.extend(grid[j + 1][i: i + 3])
                val.extend(grid[j + 2][i: i + 3])
                cells.append(val)

            if num == 0:
                the = [i for i in range(1, 10)]
                for x in range(9):
                    xval = cols[i][x]
                    yval = grid[j][x]
                    gridval = cells[i // 3 + j // 3 * 3][x]

                    if xval != 0 and xval in the:
                        the.remove(xval)
                    if yval != 0 and yval in the:
                        the.remove(yval)
                    if gridval != 0 and gridval in the:
                        the.remove(gridval)

                vals[(i, j)] = the

    prev_vals = {}

    while True:
        for j, row in enumerate(grid):
            for i, num in enumerate(row):
                if num == 0:
                    neg_pos = []
                    res_pos = []
                    cas_pos = []
                    pos_val = vals[(i, j)]

                    for position, possible_vals in vals.items():
                        if (position[1] == j and position[0] != i):
                            neg_pos.append(possible_vals)
                        if (position[0] == i and position[1] != j):
                            res_pos.append(possible_vals)
                        if i // 3 + j // 3 * 3 == position[0] // 3 + position[1] // 3 * 3:
                            cas_pos.append(possible_vals)
                    # print([num for sublist in neg_pos for num in sublist])
                    alpos = set([x for y in neg_pos for x in y])
                    elpos = set([x for y in res_pos for x in y])
                    case = set([x for y in cas_pos for x in y])

                    for x in vals[(i, j)]:
                        if x not in alpos or x not in elpos or x not in case:
                            for position, possible_vals in vals.items():
                                if ((position[1] == j and position[0] != i) or
                                    (i // 3 + j // 3 * 3 == position[0] // 3 + position[1] // 3 * 3) or
                                    (position[0] == i and position[1] != j)) and x in possible_vals:
                                    possible_vals.remove(x)
                            vals[(i, j)] = [x]
                            copy[j][i] = x
        if all(len(value) == 1 for value in vals.values()):
            break
        if prev_vals == vals:
            return "No solution Found"
        prev_vals = vals

    return copy


print(solve(grid_test))
