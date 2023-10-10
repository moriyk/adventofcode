import sys

with open(sys.argv[1], 'r') as f:
    calories = [map(int, t.split("\n")) for t in f.read().split("\n\n")]
    totals = map(sum, calories)
    print(max(totals))