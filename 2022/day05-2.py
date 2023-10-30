import sys

#     [G]         [P]         [M]    
#     [V]     [M] [W] [S]     [Q]    
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9 
stacks = [
    None,
    list('BGSC'), # 1
    list('TMWHJNVG'), # 2
    list('MQS'), # 3
    list('BSLTWNM'), # 4
    list('JZFTVGWP'), # 5
    list('CTBGQHS'), # 6
    list('TJPBW'), # 7
    list('GDCZFTQM'), # 8
    list('NSHBPF'), # 9
]

with open(sys.argv[1], 'r') as f:
    for line in f:
        # e.g. move 2 from 4 to 2
        _, num1, _, num2, _, num3 = line.split()
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)

        tmp = []
        for _ in range(num1):
            tmp.append(stacks[num2].pop())
        stacks[num3].extend(reversed(tmp))

top_of_each_stack = "".join([s[-1] for s in stacks if s is not None])
print(top_of_each_stack)