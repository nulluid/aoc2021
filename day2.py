#!/usr/bin/env python3
import argparse
import sys

def main():
    """The main routine."""
    # Parse arguments
    parser = argparse.ArgumentParser(description='solve puzzles')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='enable debug')
    parser.add_argument('part', nargs=1, help='which part to solve. options: 1, 2, A (for all)')
    parser.add_argument('input', nargs=1, help='input file path')
    args = parser.parse_args()

    #read input
    input = readinput(args.input[0])

    #run part 1 if requested
    if args.part[0].lower() in ['1', 'a', 'all']:
        print('Part 1: ' + str(part1(input)))

    #run part 2 if requested
    if args.part[0].lower() in ['2', 'a', 'all']:
        print('Part 2: ' + str(part2(input)))

    return 0

def part1(content_list):
    hor=0
    dep=0

    for i in content_list:
        dir = i.split()
        if not dir:
            continue
        if dir[0] == 'forward':
            hor+=int(dir[1])
        elif dir[0] == 'down':
            dep+=int(dir[1])
        elif dir[0] == 'up':
            dep-=int(dir[1])
    return(dep*hor)

def part2(content_list):
    aim=0
    hor=0
    dep=0

    for i in content_list:
        dir = i.split()
        if not dir:
            continue
        if dir[0] == 'forward':
            hor+=int(dir[1])
            dep+=aim*int(dir[1])
        elif dir[0] == 'down':
            aim+=int(dir[1])
        elif dir[0] == 'up':
            aim-=int(dir[1])
    return(dep*hor)

def readinput(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return(content_list)

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        print('Exiting due to KeyboardInterrupt!', file=sys.stderr)
