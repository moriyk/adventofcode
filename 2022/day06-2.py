import sys

with open(sys.argv[1], 'r') as f:
    data = f.read()

    for i in range(0, len(data)-13):
        if len(set(data[i:i+14])) == 14:
            print(f'first marker after character {i+14}')
            break
