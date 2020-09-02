import random


class Cards:
    def __init__(self, temp_id):

        self.temp_id = temp_id
        self.hand = self.deal_cards(self.temp_id)

    def deal_cards(self, temp_id: int):  # Deals Cards for a player

        dealt_cards = [temp_id]

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

        hand = self.hand
        a = random.randint(1, 13)

        if a < 11:
            hand.append(str(a))
        elif a == 11:
            hand.append('J')
        elif a == 12:
            hand.append('Q')
        elif a == 13:
            hand.append('K')
        else:  # Just for check
            print("Error in add_card function, out of bounds")
