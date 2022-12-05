import os, sys 
sys.path.append("..")
try:
    from helpers import helpers
except ModuleNotFoundError:
    print("Helpers not found, make sure to run from within the day folder")
    exit()

DAY = '$REPLACE_ME$'

def part1():
    print("Part 1")
    helpers.check_input_exists(DAY)

def part2():
    print("Part 2")
    helpers.check_input_exists(DAY)

if __name__ == "__main__":
    print("Day " + DAY)
    print("=====")
    part1()
    print("=====")
    part2()
    print("=====")