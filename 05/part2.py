import os, sys

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input_file = open(filename, 'r')
lines = input_file.readlines()

colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[92m', '\033[91m', '\033[90m', '\033[0m', '\033[1m', '\033[4m']

def parse_move(astring):
    moves = astring.split(' ')
    return (int(moves[1]), int(moves[3]), int(moves[5]))

def clear_lines():
    _ = os.system('clear')   # delete the last line

def print_stacks(the_stacks, clear=True):
    if clear:
        clear_lines()
    for i in range(1, 10):
        print(colors[i] + "{}: {}".format(i, ''.join(the_stacks[i])) + colors[i])


contain_count = 0
stacks = {}
for i in range(1, 10):
    stacks[i]=[]
print_stacks(stacks, False)

check = True
for line in lines:
    if check and line.strip() == '':
        check = False
        for i in stacks:
            stacks[i].reverse()
    elif check:
        if '1   2   3   4   5   6   7   8   9' in line:
            continue
        for i in range(1, 10):
            line_from = (i-1)*4
            line_to = line_from+3
            char_set= line[line_from:line_to]
            if char_set.strip() == '':
                continue
            stacks[i].append(char_set)
    else:
        line = line.strip()
        count, move_from, move_to = parse_move(line)
        moving = stacks[move_from][len(stacks[move_from])-count:]
        stacks[move_from] = stacks[move_from][:len(stacks[move_from])-count]
        stacks[move_to] += moving
        print_stacks(stacks)
        
answer = ''
for i in stacks:
    answer += stacks[i][len(stacks[i])-1]

print("Answer {}".format(answer.replace('[', '').replace(']', '').replace(' ', '')))