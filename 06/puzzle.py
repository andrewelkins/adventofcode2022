import os, sys, time
sys.path.append("..")
try:
    from helpers import helpers
except ModuleNotFoundError:
    print("Helpers not found, make sure to run from within the day folder")
    exit()

DAY = os.path.basename(os.getcwd())

colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[92m', '\033[91m', '\033[90m', '\033[0m', '\033[1m', '\033[4m']

def clear_lines():
    _ = os.system('clear')   # delete the last line

def parse_scan(puzzle, scan_length):
    input_length = len(puzzle)
    scan_length_index = scan_length - 1
    for i in range(scan_length_index, input_length):
        scan = puzzle[i-scan_length_index:i+1]
        clear_lines()
        print(colors[5]+puzzle[:i-scan_length_index]+'\033[0m  '+colors[2]+scan+'  \033[0m'+puzzle[i+1:]+'\033[0m')
        scan_set = set(scan)
        if len(scan_set) == scan_length:
            return i+1
        time.sleep(0.01)

def part1():
    print("Part 1")
    puzzle = helpers.parse_input('input.txt')[0]
    print("Found a match {}".format(parse_scan(puzzle, 4)))


def part2():
    print("Part 2")
    puzzle = helpers.parse_input('input.txt')[0]
    print("Found a match {}".format(parse_scan(puzzle, 14)))

if __name__ == "__main__":
    print("Day " + DAY)
    print("=====")
    part1()
    time.sleep(2)
    print("=====")
    part2()
    print("=====")