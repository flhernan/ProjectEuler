"""
Problem 54
----------
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

def rank(hand):
    getSuit  = lambda pair: pair[1]
    suits    = list(map( getSuit, hand ))

    getValue = lambda pair : dict(zip('23456789TJQKA', range(2,15)))[pair[0]]
    values   = sorted(map( getValue, hand ))

    getValueCount = lambda value: values.count( value )
    valueCounts   = list(map( getValueCount, set(values) ))

    tieBreaker = sorted( zip( valueCounts, set(values) ) , reverse =True )

    tail = values[1:]
    head = values[:4]
    differences = list(zip(head,tail))
    getDiff     = lambda diff: (diff[1] - diff[0]) == 1
    consecutive = all(map( getDiff, differences ))

    sameSuit = len(set(suits)) == 1

    royalFlush    = sameSuit and values == range(10,15)
    straightFlush = sameSuit and consecutive
    fourOfAKind   = 4        in  valueCounts
    fullHouse     = [2,3]    in  valueCounts
    flush         = sameSuit
    straight      = consecutive
    threeOfAKind  = 3        in  valueCounts
    twoPairs      = [1,2,2]  ==  sorted(valueCounts)
    onePair       = 2        in  valueCounts

    if   royalFlush:    rank = 9
    elif straightFlush: rank = 8
    elif fourOfAKind:   rank = 7
    elif fullHouse:     rank = 6
    elif flush:         rank = 5
    elif straight:      rank = 4
    elif threeOfAKind:  rank = 3
    elif twoPairs:      rank = 2
    elif onePair:       rank = 1
    else:               rank = 0

    return [rank, tieBreaker]

def P1Win(games):
    P1Wins = 0
    for game in games:
        hand1 = game[:14].split()
        hand2 = game[15:].split()
        rank1, tiebreaker1 = rank(hand1)
        rank2, tiebreaker2 = rank(hand2)

        if rank1 == rank2:
            for i in range(0,len(tiebreaker1)):
                if tiebreaker1[i] != tiebreaker2[i]:
                    P1Wins += (tiebreaker1[i] > tiebreaker2[i])
                    break
        else:
            P1Wins+= (rank1 > rank2)

    return P1Wins

with open("../EulerFiles/p054_poker.txt", "r") as poker_file:
    games  = poker_file.read().split('\n')

print(P1Win(games))
