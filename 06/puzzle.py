import os, sys 
sys.path.append("..")
try:
    from helpers import helpers
except ModuleNotFoundError:
    print("Helpers not found, make sure to run from within the day folder")
    exit()

DAY = os.path.basename(os.getcwd())

def part1():
    print("Part 1")
    puzzle = helpers.parse_input('input.txt')[0]
    input_length = len(puzzle)
    for i in range(3, input_length):
        scan = puzzle[i-3:i+1]
        scan_set = set(scan)
        if len(scan_set) == 4:
            print("Found a match {}".format(i+1))
            break


def part2():
    print("Part 2")
    puzzle = helpers.parse_input('input.txt')[0]
    input_length = len(puzzle)
    for i in range(13, input_length+1):
        scan = puzzle[i-13:i+1]
        scan_set = set(scan)
        if len(scan_set) == 14:
            print("Found a match {}".format(i+1))
            break

if __name__ == "__main__":
    print("Day " + DAY)
    print("=====")
    part1()
    print("=====")
    part2()
    print("=====")