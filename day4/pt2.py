with open("input.txt", "r") as f:
    lines = f.read().splitlines()

partial_overlap = 0
line_cnt = 0
for pair in lines:
    line_cnt += 1
    sections = pair.split(",")
    s1start, s1end = sections[0].split('-')
    s2start, s2end = sections[1].split('-')
    s1start = int(s1start)
    s2start = int(s2start)
    s1end = int(s1end)
    s2end = int(s2end)

    if s2start <= s1start <= s2end:
        partial_overlap += 1
    elif s1start <= s2start <= s1end:
        partial_overlap += 1

print(f"{partial_overlap}")
