import os


file1 = open('input/input.txt', 'r')
Lines = file1.readlines()
  
elves = {}
elves[1] = 0
count = 1
max_calories_count = 0
max_calorie_elves_index = 0
for line in Lines:
    str_count = str(count)
    
    if not line.strip():
        if max_calories_count < elves[count]:
            max_calories_count = elves[count]
            max_calorie_elves_index = count
        count += 1
        continue

    if count not in elves:
        elves[count] = 0
    elves[count] += int(line.strip())

print("elf {0} with calories {1}".format(max_calorie_elves_index, max_calories_count))

# part2
sorted_elves = {k: v for k, v in sorted(elves.items(), key=lambda elf: elf[1], reverse=True)[:3]}
print("elves {0}".format(sum(sorted_elves.values())))