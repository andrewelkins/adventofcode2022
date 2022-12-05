import string, os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input_file = open(filename, 'r')
lines = input_file.readlines()

contain_count = 0
for line in lines:
    elf1, elf2 = line.split(',')

    elf1_1, elf1_2 = map(int, elf1.split('-'))
    elf2_1, elf2_2 = map(int, elf2.split('-'))

    if elf1_1 <= elf2_1 <= elf1_2 or elf1_1 <= elf2_2 <= elf1_2 or elf2_1 <= elf1_1 <= elf2_2 or elf2_1 <= elf1_2 <= elf2_2:
        contain_count += 1

print("contain_count {}".format(contain_count))