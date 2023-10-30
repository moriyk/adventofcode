import sys

with open(sys.argv[1], 'r') as f:
    fully_contained = 0
    overlaps = 0
    
    for line in f:
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        if (b1 <= a1 and a2 <= b2) or (a1 <= b1 and b2 <= a2):
            fully_contained += 1

    print(f"fully contained: {fully_contained}")
