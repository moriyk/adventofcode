import sys

# The first column [opponent]:
#   A for Rock, B for Paper, and C for Scissors
# The second column [you]:
#   X for Rock, Y for Paper, and Z for Scissors
# Score:
#   (1 for Rock, 2 for Paper, and 3 for Scissors) + 
#   (0 if you lost, 3 if the round was a draw, and 6 if you won)

SCORES = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

with open(sys.argv[1], 'r') as f:
    total = 0
    for line in f:
        total += SCORES[line.strip()]
    print(total)
