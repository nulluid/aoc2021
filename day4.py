#!/usr/bin/env python3
import argparse
import sys
import numpy as np

def main():
    """The main routine."""
    # Parse arguments
    parser = argparse.ArgumentParser(description='solve puzzles')
    parser.add_argument('part', nargs=1, help='which part to solve. options: 1, 2, A (for all)')
    parser.add_argument('input', nargs=1, help='input file path')
    args = parser.parse_args()

    #read input
    input = readinput(args.input[0])

    order = list(map(int,input[0].split(',')))

    cards,scorecards = createarrays(input[1:])

    #run part 1 if requested
    if args.part[0].lower() in ['1', 'a', 'all']:
        print(play(order,cards,scorecards))

    '''
    #run part 2 if requested
    if args.part[0].lower() in ['2', 'a', 'all']:
        print('Part 2: ' + str(part2(input)))
    '''

    return 0

def play(order,cards,scorecards):
    for call in order:
        print('call: ' + str(call))
        for cardnumber, card in enumerate(cards):
            for rownumber, row in enumerate(card):
                for itemnumber, item in enumerate(row):
                    if cards[cardnumber][rownumber][itemnumber] == call:
                        scorecards[cardnumber][rownumber][itemnumber] = 1
        check, winners = checkcards(scorecards)
        if check:
            print('WINNER WINNER CHICKEN DINNER')
            score = 0
            for rownumber, row in enumerate(scorecards[winners[0]]):
                for itemnumber, item in enumerate(row):
                    if item == 0:
                        score+=cards[cardnumber][rownumber][itemnumber]
            print('score: '+ str(score))
            return(score*call)
    return 1

def checkcards(scorecards):
    winners = []
    for cardnumber, card in enumerate(scorecards):
        if 5 in np.sum(card, axis = 0):
            winners.append(cardnumber)
            print(cardnumber)
        else:
            if 5 in np.sum(card, axis = 1):
                winners.append(cardnumber)
                print(cardnumber)
    if len(winners) > 0:
        return(True, winners)
    else:
        return(False, 0)

def createarrays(input):
    cardnum = 0
    cards = []
    card = []
    scorecards = []
    for c,i in enumerate(input):
        if i == '':
            if len(card)>0:
                cards.append(card)
            card = []
            cardnum += 1
        else:
            #card.append(i.split())
            card.append(list(map(int,i.split())))

    for cardnumber, card in enumerate(cards):
        scorecards.append([])
        for rownumber, row in enumerate(card):
            scorecards[cardnumber].append([])
            for itemnumber, item in enumerate(row):
                scorecards[cardnumber][rownumber].append(0)

    return(cards,scorecards)

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
