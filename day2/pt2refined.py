
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

rpsvals = {'A': 1, 'B': 2, 'C': 3,
           'X': 1, 'Y': 2, 'Z': 3}


def need(opponent, outcome):
    if outcome == 'Y':  # draw
        return opponent
    if outcome == 'X':  # lose
        if opponent == 'A':
            return 'C'
        if opponent == 'B':
            return 'A'
        if opponent == 'C':
            return 'B'
    if outcome == 'Z':  # win
        if opponent == 'A':
            return 'B'
        if opponent == 'B':
            return 'C'
        if opponent == 'C':
            return 'A'


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
    object_to_play = need(round_[0], round_[2])
    totalscore += decide_score(round_[0], object_to_play) + rpsvals[object_to_play]

print(f"totalscore={totalscore}")
