import os


file1 = open('input.txt', 'r')
Lines = file1.readlines()

# A for Rock, B for Paper, and C for Scissors
# B> A, C> B, A> C
# X for Rock, Y for Paper, and Z for Scissors
# Y>X, Z>Y, X>Z
# dict for options
matrix = {"A": {"X":1+3, "Y":2+6, "Z":3+0}, "B": {"X":1+0, "Y":2+3, "Z":3+6}, "C": {"X":1+6, "Y":2+0, "Z":3+3}}
total = 0
for line in Lines:
    opp = line[0]
    me = line[2]
    if not line.strip():
        continue
    total += matrix[opp][me]

print(total)
    
