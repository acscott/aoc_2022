with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def printgrid(g):
    return
    print(f"000000000111111111222222222333333333")
    print(f"012345789012345678901234567890123456")
    for row in g:
        for c in row:
            print(f"{c}", end="")
        print()


def updategrid(g, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty):
    if ty < 1 or tx < 1 or ty > 1349 or tx > 2521:
        print(f"prevhx={prevhx} prevhy={prevhy} hx={hx} hy={hy} tx={tx} ty={ty}")
        raise ValueError(f"Cannot set ty={ty} and tx={tx}")
    try:
        # g[prevhy][prevhx] = "."
        # g[hy][hx] = "H"
        # g[prevty][prevtx] = "."
        # g[ty][tx] = "T"

        g[ty][tx] = "#"
    except:
        print(f"prevhx={prevhx} prevhy={prevhy} hx={hx} hy={hy} tx={tx} ty={ty}")
        raise ValueError(f"Cannot set ty={ty} and tx={tx}")


def movetail(direct, lastheadx, headx, lastheady, heady, tailx, taily):
    if direct == "R":
        if abs(headx - tailx) == 2:
            if heady > taily:
                return 1, 1
            elif heady < taily:
                return -1, 1
            else:
                return 0, 1

    if direct == "L":
        if abs(headx - tailx) == 2:
            if heady > taily:
                return 1, -1
            elif heady < taily:
                return -1, -1
            else:
                return 0, -1

    if direct == "U":
        if abs(heady - taily) == 2:
            if headx > tailx:
                return -1, 1
            elif headx < tailx:
                return -1, -1
            else:
                return -1, 0

    if direct == "D":
        if abs(heady - taily) == 2:
            if headx > tailx:
                return 1, 1
            elif headx < tailx:
                return 1, -1
            else:
                return 1, 0

    return 0, 0


hx = 0
hy = 0
tx = 0
ty = 0

grid = [["." for j in range(2520)] for i in range(1350)]
# grid = [['.' for j in range(40)] for i in range(30)]
prevhx = hx = 575
prevhy = hy = 525
# prevhx = hx = 10
# prevhy = hy = 10
prevtx = tx = hx
prevty = ty = hy
grid[ty][tx] = "T"
grid[hy][hx] = "H"
printgrid(grid)
for move in lines:
    direct, dist = move.split(" ")
    dist = int(dist)

    if direct == "R":
        for x in range(dist):
            prevhx = hx
            prevhy = hy
            hx += 1
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
            prevtx = tx
            prevty = ty
            movety, movetx = movetail(direct, prevhx, hx, prevhy, hy, tx, ty)
            tx += movetx
            ty += movety
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
    if direct == "L":
        for x in range(dist):
            prevhx = hx
            prevhy = hy
            hx -= 1
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
            prevtx = tx
            prevty = ty
            movety, movetx = movetail(direct, prevhx, hx, prevhy, hy, tx, ty)
            tx += movetx
            ty += movety
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
    if direct == "U":
        for y in range(dist):
            prevhx = hx
            prevhy = hy
            hy -= 1
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
            prevtx = tx
            prevty = ty
            movety, movetx = movetail(direct, prevhx, hx, prevhy, hy, tx, ty)
            tx += movetx
            ty += movety
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
    if direct == "D":
        for y in range(dist):
            prevhx = hx
            prevhy = hy
            hy += 1
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)
            prevtx = tx
            prevty = ty
            movety, movetx = movetail(direct, prevhx, hx, prevhy, hy, tx, ty)
            tx += movetx
            ty += movety
            updategrid(grid, prevhx, prevhy, hx, hy, prevtx, prevty, tx, ty)
            printgrid(grid)

# printgrid2(grid)
total = 0
for row in grid:
    total += row.count("#")
print(f"prevhx={prevhx} prevhy={prevhy} hx={hx} hy={hy} tx={tx} ty={ty}")
print(total)
