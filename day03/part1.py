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
for line in lines:
    first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
    diff = first.intersection(second)
    priority_count += matrix[diff.pop()]
    
print("priority_count {}".format(priority_count))