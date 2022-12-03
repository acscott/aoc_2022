
with open("input.txt", "r") as f:
    lines = f.read().splitlines()


rpsvals = {'A': 1, 'B': 2, 'C': 3,
           'X': 1, 'Y': 2, 'Z': 3}


def decide_score(object1, object2):
    if rpsvals[object1] == rpsvals[object2]:  # draw
        return 3
    if rpsvals[object1] == 1:
        return 6 if rpsvals[object2] == 2 else 0
    if rpsvals[object1] == 2:
        return 6 if rpsvals[object2] == 3 else 0
    if rpsvals[object1] == 3:
        return 6 if rpsvals[object2] == 1 else 0


totalscore = 0
for round_ in lines:
    totalscore += decide_score(round_[0], round_[2]) + rpsvals[round_[2]]

print(f"totalscore={totalscore}")
