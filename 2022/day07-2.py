import sys

path = ['']
dirsize = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        p = line.strip().split(' ')
        if p[0] == '$':
            if p[1] == 'cd':
                if p[2] == '/':
                    path = ['']
                elif p[2] == '..':
                    path.pop()
                else:
                    path.append(p[2])
        elif p[0] == 'dir':
            pass
        else:
            for i in range(len(path)):
                key = '/'.join(path[:i+1])
                if key not in dirsize:
                    dirsize[key] = 0
                dirsize[key] += int(p[0])

    increase = min([x for x in dirsize.values() if dirsize[''] - x <= 40000000])
    print(f'The smallest increase: {increase}')