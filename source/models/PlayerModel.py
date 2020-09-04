
# This model represents the player that are going to play BlackJack
# This model has all the attributes related to a real player
# things like its name, its cards and cards value
import random


class Player:
    def __init__(self, player_num: int):

        self.player_num = player_num
        self.hand = self.deal_cards()
        self.value: int = 0

    def deal_cards(self):  # Deals Player for a Player

        dealt_cards = []

        for i in range(2):

            a = random.randint(1, 13)

            if a < 11:
                dealt_cards.append(str(a))
            elif a == 11:
                dealt_cards.append('J')
            elif a == 12:
                dealt_cards.append('Q')
            elif a == 13:
                dealt_cards.append('K')
            else:  # Just for check
                print("Error in dealers_hand function, out of bounds")

        return dealt_cards

    def add_card(self):  # list is a call by object reference and doesnt need to return anything

        a = random.randint(1, 13)

        if a < 11:
            self.hand.append(str(a))
        elif a == 11:
            self.hand.append('J')
        elif a == 12:
            self.hand.append('Q')
        elif a == 13:
            self.hand.append('K')
        else:  # Just for check
            print("Error in add_card function, out of bounds")
