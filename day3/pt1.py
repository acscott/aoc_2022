with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def priority(char):
    o = ord(char)
    if o in range(97, 123):
        return o - 96
    if o in range(65, 91):
        return o - 38


priority_sum = 0
for items in lines:
    midway = int(len(items) / 2)
    compartment1 = items[0:midway]
    compartment2 = items[midway:]
    common = list(set(compartment1) & set(compartment2))
    for item in common:
        priority_sum += priority(item)

print(f"priority sum={priority_sum}")
