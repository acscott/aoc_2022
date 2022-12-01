with open("input.txt", "r") as f:
    lines = f.read().splitlines()

ndx = 0
elves = []
total = 0
for line in lines:
    if line == '':
        ndx += 1
        elves.append(total)
        total = 0
    else:
        total += int(line)
elves.append(total)
print(elves)
most = 0
for elf in elves:
    most = elf if elf > most else most

print(f"{most} calories")
