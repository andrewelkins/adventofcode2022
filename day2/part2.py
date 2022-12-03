import os


input_file = open('input.txt', 'r')
lines = input_file.readlines()

# A 1 for Rock, B 2 for Paper, and C 3 for Scissors
# B> A, C> B, A> C
# X for Rock, Y for Paper, and Z for Scissors
# Y>X, Z>Y, X>Z
# dict for options
part1_matrix = {"A": {"X":1+3, "Y":2+6, "Z":3+0}, "B": {"X":1+0, "Y":2+3, "Z":3+6}, "C": {"X":1+6, "Y":2+0, "Z":3+3}}
# x lose, y tie, z win
part2_matrix = {"X": {"A":3+0, "B":1+0, "C":2+0}, "Y": {"A":1+3, "B":2+3, "C":3+3}, "Z": {"A":2+6, "B":3+6, "C":1+6}}
part1_total = 0
part2_total = 0
for line in lines:
    opp = line[0]
    me = line[2]
    part1_total += part1_matrix[opp][me]
    part2_total += part2_matrix[me][opp]

print("part1 {}".format(part1_total))
print("part2 {}".format(part2_total))
