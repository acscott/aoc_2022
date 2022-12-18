from dataclasses import dataclass
from copy import copy

with open("input.txt", "r") as f:
    lines = f.read().splitlines()


@dataclass
class Knot:
    x: int = 0
    y: int = 0
    label: str = ""


def printgrid(g):
    print(f"000000000111111111222222222333333333")
    print(f"012345789012345678901234567890123456")
    for row in g:
        for c in row:
            print(f"{c}", end="")
        print()


def updategrid(g, prevknots_: [Knot], knots_: [Knot]):
    tail_on = True
    try:
        if tail_on:
            for n in range(0, len(knots_)):
                if knots_[n].label == '9':
                    g[knots_[n].y][knots_[n].x] = "#"
        else:
            for n in range(len(knots_) - 1, -1, -1):
                g[prevknots_[n].y][prevknots_[n].x] = "."
            for n in range(len(knots_) - 1, -1, -1):
                g[knots_[n].y][knots_[n].x] = knots_[n].label
    except ValueError:
        raise ValueError(f"cannot set grid[{prevknots_[n].y}][{prevknots_[n].x}]")


def save_prevknots(prevknots_, knots_, ndx):
    prevknots_[ndx].y = copy(knots_[ndx].y)
    prevknots_[ndx].x = copy(knots_[ndx].x)


def moveknots(direct, prevknots_, knots_):
    if direct == "R":
        save_prevknots(prevknots_, knots_, 0)
        knots_[0].x += 1
        for n in range(1, len(knots_)):
            save_prevknots(prevknots_, knots_, n)
            if (
                    abs(knots_[n].x - knots_[n - 1].x) == 2
                    or abs(knots_[n].y - knots_[n - 1].y) == 2
            ):
                if knots_[n].y > knots_[n - 1].y:
                    knots_[n].x += 1
                    knots_[n].y -= 1
                elif knots_[n].y < knots_[n - 1].y:
                    knots_[n].x += 1
                    knots_[n].y += 1
                else:
                    knots_[n].x += 1
                    knots_[n].y += 0

    if direct == "L":
        save_prevknots(prevknots_, knots_, 0)
        knots_[0].x -= 1
        for n in range(1, len(knots_)):
            save_prevknots(prevknots_, knots_, n)
            if (
                    abs(knots_[n].x - knots_[n - 1].x) == 2
                    or abs(knots_[n].y - knots_[n - 1].y) == 2
            ):
                if knots_[n].y > knots_[n - 1].y:
                    knots_[n].x -= 1
                    knots_[n].y -= 1
                elif knots_[n].y < knots_[n - 1].y:
                    knots_[n].x -= 1
                    knots_[n].y += 1
                else:
                    knots_[n].x -= 1
                    knots_[n].y -= 0

    if direct == "U":
        save_prevknots(prevknots_, knots_, 0)
        knots_[0].y -= 1
        for n in range(1, len(knots_) - 1):
            if (
                abs(knots_[n].y - knots_[n - 1].y) == 2
                or abs(knots_[n].x - knots_[n - 1].x) == 2
            ):
                save_prevknots(prevknots_, knots_, n)
                if knots_[n].x < knots_[n - 1].x:
                    knots_[n].x += 1
                    knots_[n].y -= 1
                elif knots_[n].x > knots_[n - 1].x:
                    knots_[n].x -= 1
                    knots_[n].y -= 1
                else:
                    knots_[n].x -= 0
                    knots_[n].y -= 1

    if direct == "D":
        prevknots_[0].y = copy(knots_[0].y)
        save_prevknots(prevknots, knots, 0)
        knots_[0].y += 1
        for n in range(1, len(knots_) - 1):
            if (
                abs(knots_[n].y - knots_[n - 1].y) == 2
                or abs(knots_[n].y - knots_[n - 1].y) == 2
            ):
                save_prevknots(prevknots, knots, n)
                if knots_[n].x < knots_[n - 1].x:
                    knots_[n].x += 1
                    knots_[n].y += 1
                elif knots_[n].x > knots_[n - 1].x:
                    knots_[n].x -= 1
                    knots_[n].y += 1
                else:
                    knots_[n].x -= 0
                    knots_[n].y += 1


knots = [Knot(10, 10, str(x)) for x in range(10)]
knots[0].label = "H"
prevknots = [Knot(10, 10, str(x)) for x in range(10)]

# grid = [['.' for j in range(2520)] for i in range(1350)]
grid = [["." for j in range(40)] for i in range(30)]
updategrid(grid, prevknots, knots)
printgrid(grid)
for move in lines:
    direct, dist = move.split(" ")
    dist = int(dist)

    for x in range(dist):
        moveknots(direct, prevknots, knots)
        updategrid(grid, prevknots, knots)
        printgrid(grid)

total = 0
for row in grid:
    total += row.count("#")
print(total)
