import os, sys 
sys.path.append("..")
try:
    from helpers import helpers
except ModuleNotFoundError:
    print("Helpers not found, make sure to run from within the day folder")
    exit()

DAY = os.path.basename(os.getcwd())

DEBUG = True

def part1():
    print("Part 1")
    puzzle = helpers.parse_input('input.txt')
    if DEBUG:
        puzzle = helpers.parse_input('input-test.txt')
    

def part2():
    print("Part 2")
    puzzle = helpers.parse_input('input.txt')
    if DEBUG:
        puzzle = helpers.parse_input('input-test.txt')

if __name__ == "__main__":
    print("Day " + DAY)
    print("=====")
    part1()
    print("=====")
    part2()
    print("=====")