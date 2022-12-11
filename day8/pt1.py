with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
h = -1
for line in lines:
    grid.append(list(line))
    h += 1

w = len(grid[0]) - 1
y = 0
x = 0
v = 0
for r in grid:
    x = 0
    for t in r:
        if x in (0, w):
            v += 1
        elif y in (0, h):
            v += 1
        elif (
                t > max([row[x] for row in grid[0:y]])
                or t > max([row[x] for row in grid[y+1:]])
                or t > max(grid[y][x + 1:])
                or t > max(grid[y][:x])
        ):
            v += 1
        x += 1

    y += 1

print(v)
