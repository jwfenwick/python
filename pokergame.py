import random
from collections import Counter

class Deck(object):
    """ create new shuffled deck: 10 cards in 4 suits
        method to deal hands of 5 cards
    """
    def __init__(self):
        self._deck = [j for j in range(10) for i in range(4) ]
        random.shuffle(self._deck)
        # for j in range(40):
        #    print(self._deck [j])
        return

    def deal(self,hand1=[],hand2=[]):
        for index in range(5):
            hand1.append(self._deck[index])
            hand2.append(self._deck[index+1])
            index = index + 1
        print "Hand1:"
        for index in range(5):
            print hand1[index]
        print "Hand2:"
        for index in range(5):
            print hand2[index]
        return



def score(hand1,hand2):
    match1 = Counter(hand1)                    # number matches of each card 
    match2 = Counter(hand2)
    print match1, match2
    # res = list(sorted(theDict, key=theDict.__getitem__, reverse=True))
    score1 = {v: k for k, v in match1.items()} # 4321 matches by card value
    score2 = {v: k for k, v in match2.items()}
    print "Hand1 score:", score1
    print "Hand2 score:", score2

    sorted1=sorted(score1,reverse=True)
    sorted2=sorted(score2,reverse=True)
    print sorted1
    print sorted2

    if sorted1[0] > sorted2[0]:
        return 1
    elif sorted1[0] < sorted2[0]:
        return 2
    elif sorted1[1] > sorted2[1]:
        return 1
    elif sorted1[1] < sorted2[1]:
        return 2 
    else:
        return 0
    
def main():

    hand1 = []
    hand2 = []
    newDeck = Deck()

    newDeck.deal(hand1,hand2)

    result = score (hand1,hand2)

    print "Winner is {}".format(result)


if __name__ == "__main__":
    main()
