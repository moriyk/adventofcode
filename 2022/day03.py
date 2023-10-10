import sys

def priority(ch):
    if ch.islower():
        return ord(ch) - ord('a') + 1
    return ord(ch) - ord('A') + 27

with open(sys.argv[1], 'r') as f:
    total = 0
    for line in f:
        line = line.strip()
        L = len(line)
        a, b = set(line[:L//2]), set(line[L//2:])
        c = a.intersection(b)
        total += priority(c.pop())
    print(total)