grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

vals = {}
cells = []


for i, row in enumerate(grid):
    for j, num in enumerate(row):
        if i % 3 == 0 and j % 3 == 0:
            val = grid[i][j: j + 3]
            val.extend(grid[i + 1][j: j + 3])
            val.extend(grid[i + 2][j: j + 3])
            cells.append(val)

        if num == 0:
            xmod = j % 3
            ymod = i % 3
            the = [i for i in range(1, 10)]
            for x in range(9):
                xval = grid[i][x]
                yval = grid[j][x]
                if xval != 0 and xval in the:
                    the.remove(xval)
                if yval != 0 and yval in the:
                    the.remove(yval)

            vals[(i, j)] = the

print(cells)






print(vals)


