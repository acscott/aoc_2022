with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def priority(char):
    o = ord(char)
    if o in range(97, 123):
        return o - 96
    if o in range(65, 91):
        return o - 38


priority_sum = 0
rndx = 0
group = ["", "", ""]
for rucksack in lines:
    group[rndx] = rucksack
    rndx += 1
    if rndx == 3:
        priority_sum += priority(list(set(group[0]) & set(group[1]) & set(group[2]))[0])
        group = ["", "", ""]
        rndx = 0

print(f"priority sum={priority_sum}")
