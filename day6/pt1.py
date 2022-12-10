with open("input.txt", "r") as f:
    signal = f.read().splitlines()[0]

pos = 0
while True:
    if len(set(signal[pos:(pos+4)])) == 4:
        break
    pos += 1
print(f"pos={pos+4}")
