import sys

with open(sys.argv[1], 'r') as f:
    data = f.read()

    for i in range(0, len(data)-3):
        if len(set(data[i:i+4])) == 4:
            print(f'first marker after character {i+4}')
            break
