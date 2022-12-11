with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def tcount(look, tree):
    counter = 0
    for sample in look:
        if sample >= tree:
            return counter + 1
        if sample < tree:
            counter += 1
    return counter


def score(l):
    total = 1
    for n in l:
        if n != 0:
            total *= n
    return total

grid = []
h = -1
for line in lines:
    grid.append(list(line))
    h += 1

w = len(grid[0]) - 1
y = 0
x = 0
v = []
scores = []
for r in grid:
    x = 0
    for t in r:
        v = []
        v.append(tcount(reversed(grid[y][0:x]), t))
        v.append(tcount(grid[y][x+1:], t))

        v.append(tcount([col[x] for col in reversed(grid[:y])], t))
        v.append(tcount([col[x] for col in grid[y+1:]], t))
        scores.append(score(v))
        x += 1
    y += 1

print(scores)
print(max(scores))
