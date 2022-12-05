import argparse
import helpers.helpers as helpers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', action='store_true')
    parser.add_argument('-d', '--day', type=int, help="Day to pull down")
    parser.add_argument('-y', '--year', type=int, help="AoC year to target")
    args = parser.parse_args()
    if args.init:
        helpers.create_folder_structure()
    # if args.day:
    #     download_problem_for_day(args.day, year=args.year)