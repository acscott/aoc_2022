with open("input.txt", "r") as f:
    lines = f.read().splitlines()

contains_cnt = 0
for pair in lines:
    sections = pair.split(",")
    s1start, s1end = sections[0].split('-')
    s2start, s2end = sections[1].split('-')
    s1start = int(s1start)
    s2start = int(s2start)
    s1end = int(s1end)
    s2end = int(s2end)
    if s1start >= s2start and s1end <= s2end:
        contains_cnt += 1
        print(f"{s2start}-{s2end} fully contains {s1start}-{s1end}")
    else:  # we don't want to count fully matched ranges twice
        if s2start >= s1start and s2end <= s1end:
            contains_cnt += 1
            print(f"{s1start}-{s1end} fully contains {s2start}-{s2end}")

print(f"contains count = {contains_cnt}")
