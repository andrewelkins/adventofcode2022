import argparse
import helpers.helpers as helpers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', action='store_true')
    args = parser.parse_args()
    if args.init:
        helpers.create_folder_structure()