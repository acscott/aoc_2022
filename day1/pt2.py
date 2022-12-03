with open("input.txt", "r") as f:
    lines = f.read().splitlines()

elves = []
total = 0
for line in lines:
    if line == '':
        elves.append(total)
        total = 0
    else:
        total += int(line)
elves.append(total)
elves.sort(reverse=True)

print(f"{sum(elves[0:3])} calories")
