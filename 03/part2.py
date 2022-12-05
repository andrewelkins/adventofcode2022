import string, os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')
input_file = open(filename, 'r')
lines = input_file.readlines()

matrix = {}
alpha_lowercase = list(string.ascii_lowercase)
alpha_uppercase = list(string.ascii_uppercase)
count = 1
for i in range(0, len(alpha_lowercase)):
    matrix[alpha_lowercase[i]] = count
    count += 1
for i in range(0, len(alpha_uppercase)):
    matrix[alpha_uppercase[i]] = count
    count += 1
print("matrix {}".format(matrix))

priority_count = 0
loop = 0
loop_sets = []
for line in lines:
    loop_sets.append(set(line.strip()))
    
    loop += 1
    if loop == 3:
        unique = set.intersection(*loop_sets)
        priority_count += matrix[unique.pop()]
        loop = 0
        loop_sets = []
    
print("priority_count {}".format(priority_count))