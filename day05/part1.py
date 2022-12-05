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
        for i in range(1, 10):
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
        print("count {} move_from {} move_to {}".format(count, move_from, move_to))
        print("else stacks {}".format(stacks))
        print("from {} to {}".format(stacks[move_from], stacks[move_to]))
        for i in range(0, count):
            moving = stacks[move_from].pop()
            stacks[move_to].append(moving)  
        
        print("from {} to {}".format(stacks[move_from], stacks[move_to]))


answer = ''
for i in range(1, 10):
    print("{}".format(stacks[i][len(stacks[i])-1]))
    answer += stacks[i][len(stacks[i])-1]

print("answer {}".format(answer.replace('[', '').replace(']', '').replace(' ', '')))