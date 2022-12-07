import os, sys 
from anytree import Node, RenderTree, search, AsciiStyle, LevelOrderIter

sys.path.append("..")
try:
    from helpers import helpers
except ModuleNotFoundError:
    print("Helpers not found, make sure to run from within the day folder")
    exit()

DAY = os.path.basename(os.getcwd())

def parse_tree(puzzle):
    tree = None
    cursor = None
    for line in puzzle:
        command = line.split(' ')
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] ==  '/':
                    if tree is None:
                        tree = Node("root", files=[], directory_size=0, directory_large=False, total_directory_size=0)
                        cursor = tree
                    else:
                        cursor = cursor.root
                elif command[2] == '..':
                    cursor = cursor.parent
                else:
                    for i in cursor.children:
                        if i.name == command[2]:
                            cursor = i
            else:
                # ls - do nothing
                pass
        else:
            if command[0] == 'dir':
                Node(command[1], parent=cursor, files=[], directory_size=0, directory_large=False, total_directory_size=0)
            else:
                cursor.files.append(line) 
                cursor.directory_size += int(command[0])
                if cursor.directory_size > 100000:
                    cursor.directory_large = True
    return tree

def part1():
    print("Part 1")
    puzzle = helpers.parse_input('input.txt')

    tree = parse_tree(puzzle)

    print(RenderTree(tree, style=AsciiStyle()).by_attr())
    size = 0
    for node in LevelOrderIter(tree):
        for sub_node in LevelOrderIter(node):
            node.total_directory_size += sub_node.directory_size
    large_subdirectories = search.findall(tree, filter_=lambda node: node.total_directory_size < 100000 )
    for i in large_subdirectories:
        size += i.total_directory_size
    print(f"size: {size}")

def part2():
    print("Part 2")
    puzzle = helpers.parse_input('input.txt')

    tree = parse_tree(puzzle)

    print(RenderTree(tree, style=AsciiStyle()).by_attr())
    for node in LevelOrderIter(tree):
        for sub_node in LevelOrderIter(node):
            node.total_directory_size += sub_node.directory_size

    directory_catch = 2800000
    large_subdirectories = search.findall(tree, filter_=lambda node: node.total_directory_size > directory_catch )
    span_directory =  None
    span_diff = 0
    for i in large_subdirectories:
        print(i)
        if span_diff == 0 or ((i.total_directory_size-directory_catch) < span_diff):
            span_diff = i.total_directory_size-directory_catch
            span_directory = i
    print(f"directory: {span_directory}")
    print(f"directory size: {span_directory.total_directory_size}")
    print(f"directory: {span_diff}")

if __name__ == "__main__":
    print("Day " + DAY)
    print("=====")
    part1()
    print("=====")
    part2()
    print("=====")