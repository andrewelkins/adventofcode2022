import os


file1 = open('input/input.txt', 'r')
Lines = file1.readlines()
  
elves = {}
elves["1"] = 0
count = 1
max_calories_count = 0
max_calorie_elves_index = 0
for line in Lines:
    str_count = str(count)
    
    if not line.strip():
        if max_calories_count < elves[str_count]:
            max_calories_count = elves[str_count]
            max_calorie_elves_index = count
        count += 1
        continue

    if str_count not in elves:
        elves[str_count] = 0
    elves[str_count] += int(line.strip())

print("elf {0} with calories {1}".format(max_calorie_elves_index, max_calories_count))