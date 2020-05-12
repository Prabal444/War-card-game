#####################################
### WELCOME TO YOUR WAR #####
#####################################

from random import shuffle

suit = "S H D C".split()
rank = "2,3,4,5,6,7,8,9,10,J,Q,K,A".split(",")
#list comprehension
##  mycards = [(s,r) for s in suit for r in rank]  ##
'''
#same as above
mycards = []
for s in suit:
    for r in rank:
        mycards.append((s,r))
'''

class Deck():

    def __init__(self):
        self.mycards = [(s,r) for s in suit for r in rank]

    def shuffle(self):
        shuffle(self.mycards)

    def divide_half(self):
        return (self.mycards[:26],self.mycards[26:])#this will retirn a tuple we used tuple unpacking

class Hand():

    def __init__(self,cards):
        self.cards = cards
#printing the no of cards in player/comp hand
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_card = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_card.append(self.hand.cards.pop()) # could aso be done by remove_card function
            return war_card

    def still_has_cards(self):
        '''
        return true if player still has cards left
        '''
        return len(self.hand.cards) != 0

# Run the main GAME

print("Welcome to War, Let's begin")

#Create a new deck and split in half

d = Deck()
d.shuffle()
# A tuple object for splitting the deck h1 is first half and h2 is second
h1,h2 = d.divide_half()

#creaating a computer player
comp = Player("comp",Hand(h1))
#asking the name of player
name = input("Enter your name: ")
#distributing the cards
user = Player(name,Hand(h2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds = total_rounds+1
    print("Time for a new round")
    print("There are the current standings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []
#computer cars
    c_card = comp.play_card()
    #user card
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    #check if there is a war
    #we only compare rank of cards and not suit therefore we use index 1 in list which denotes the index of tuple
    if c_card[1] == u_card[1]:
        war_count = war_count+1

        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if rank.index(c_card[1])<rank.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
#checking of any two cards
    else:
        if rank.index(c_card[1])<rank.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over!! , number of rounds : "+str(total_rounds))
print("A war happened "+str(war_count)+" times")
print("computer has : " + str(comp.still_has_cards()))
print("does user still has cards : "+ str(user.still_has_cards()))
