import sys

with open(sys.argv[1], 'r') as f:
    fully_contained = 0
    overlaps = 0
    
    for line in f:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if not ((a2 < b1) or (b2 < a1)):
            overlaps += 1

    print(f"overlaps: {overlaps}")