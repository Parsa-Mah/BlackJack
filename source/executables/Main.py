import random


def deal_cards():  # Deals Cards for a player
    dealt_cards = ""

    for i in range(2):

        a = random.randint(1, 13)

        if a < 11:
            dealt_cards += str(a)
        elif a == 11:
            dealt_cards += "J"
        elif a == 12:
            dealt_cards += "Q"
        elif a == 13:
            dealt_cards += "K"
        else:  # Just for check
            print("Error in dealers_hand function, out of bounds")
        dealt_cards += " "

    return dealt_cards

print(deal_cards())