with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def rotate_rows_to_cols(matrix):
    colndx = 0
    newm = []
    width = len(matrix[0])
    for _ in range(0, width):
        col = [x[colndx] for x in matrix]
        colndx += 1
        newm.append(col)
    return newm


get_moves = False
moves = []
stacks_buf = []
for line in lines:
    if line == "":
        get_moves = True
    else:
        if get_moves:
            parts = line.split(" ")
            move = [int(parts[1]), int(parts[3]), int(parts[5])]
            moves.append(move)
        else:  # get crates setup
            stacks_buf.append(line)

read_pos_flg = True
pos = 0
row_ndx = 0
col_positions = {}
all_stacks = []
rows = []
for scanning_row in reversed(stacks_buf):
    if read_pos_flg:
        for c in scanning_row:
            if c != '':
                col_positions[pos] = int(c) if c != ' ' else -1
            pos += 1
        read_pos_flg = False
        last_column = int(col_positions[max(col_positions, key=col_positions.get)])
    else:
        row = []
        pos = 0
        for c in scanning_row:
            if c not in ('[', ']'):
                if col_positions[pos] != -1:
                    row.append(c)
            pos += 1
        rows.append(row)


cols = rotate_rows_to_cols(rows)
print(cols)
for move in moves:
    for n in range(0, move[0]):
        crate = ' '
        while crate == ' ':
            try:
                crate = cols[move[1]-1].pop()
            except IndexError:
                crate = []
            cols[move[2]-1].append(crate)

print(cols)
for r in cols:
    top = ' '
    while top == ' ':
        top = r.pop()
    print(top, end='')


