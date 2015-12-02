def dealHands(game):
    player1hand = game[:14].split()
    player2hand = game[15:].split()
    return [player1hand, player2hand]

def rank(hand):
    royalFlush    = sameSuit(hand) and values(hand) == range(10,15)
    straightFlush = consecutive(hand) and sameSuit(hand)
    fourOfAKind   = 4 in valueCounts(hand)
    fullHouse     = [2,3] in valueCounts(hand)
    flush         = sameSuit(hand)
    straight      = consecutive(hand)
    threeOfAKind  = 3 in valueCounts(hand)
    twoPairs      = [1,2,2] == sorted(valueCounts(hand))
    onePair       = 2 in valueCounts(hand)

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

    return [rank, tieBreaker(hand)]

def suits(hand):
    getSuit = lambda pair: pair[1]
    return sorted(map( getSuit, hand ))

def values(hand):
    getCharValue = lambda pair: pair[0]
    charValues = list(map( getCharValue, hand ))
    charToValue = lambda char: '23456789TJQKA'.index(char) + 2
    return sorted(map( charToValue, charValues ))

def valueCounts(hand):
    getValueCount = lambda value: values(hand).count( value )
    return list(map( getValueCount, set(values(hand)) ))

def tieBreaker(hand):
    unsortedTieBreakers = zip( valueCounts(hand), set(values(hand)) )
    return sorted( unsortedTieBreakers, reverse = True )

def consecutive(hand):
    tail = values(hand)[1:]
    head = values(hand)[:4]
    differences = list(zip(head,tail))
    getDiff = lambda diff: (diff[1] - diff[0]) == 1
    return all(map( getDiff, differences ))

def sameSuit(hand):
    handSuits = suits(hand)
    repeatedSuit = handSuits[:1]*5
    return (repeatedSuit == handSuits)

def P1Win(hands):
    hand1, hand2 = hands
    rankNum1, tiebreaker1 = rank(hand1)
    rankNum2, tiebreaker2 = rank(hand2)

    if rankNum1 == rankNum2:
        for i in range(0,len(tiebreaker1)):
            if tiebreaker1[i] != tiebreaker2[i]:
                return(tiebreaker1[i] > tiebreaker2[i])

    return (rankNum1 > rankNum2)

with open("p054_poker.txt", "r") as poker_file:
    games  = poker_file.read().split('\n')

P1wins = 0
for game in games:
    hands = dealHands(game)
    P1wins += P1Win(hands)
print(P1wins)
