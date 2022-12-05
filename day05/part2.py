import string, os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input_file = open(filename, 'r')
lines = input_file.readlines()
    

def parse_move(string):
    moves = string.split(' ')
    print("moves {}".format(moves))
    move = int(moves[1])
    move_from = int(moves[3])
    move_to = int(moves[5])
    return (move, move_from, move_to)

contain_count = 0
stacks = {}
for i in range(1, 10):
    stacks[i]=[]

check = True
for line in lines:
    print("line {}".format(line))
    if check and line.strip() == '':
        check = False
        for i in stacks:
            stacks[i].reverse()
    elif check:
        if '1   2   3   4   5   6   7   8   9' in line:
            print("skipping line ")
            continue
        for i in range(1, 10):
            line_from = (i-1)*4
            line_to = line_from+3
            print("stacks {}".format(stacks))
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
        
answer = ''
for i in stacks:
    print("{}".format(stacks[i][len(stacks[i])-1]))
    answer += stacks[i][len(stacks[i])-1]

print("answer {}".format(answer.replace('[', '').replace(']', '').replace(' ', '')))