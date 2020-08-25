import random

print("Welcome to my Blackjack game")
print("Now dealer will deal cards...\n")


def deal_cards(temp_id: int):  # Deals Cards for a player

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
    print(dealt_cards)  # todo remove debug line
    return dealt_cards


def calculate_cards_value(dealt_cards : list, card_number: int):  # Calculates the value of the cards

    value = 0

    if card_number > 0:  # the value of a specific card and not negative
        card = dealt_cards[card_number]
        if card == 'J' or card == 'Q' or card == 'K':
            value += 11
        else:
            value += int(card)
        return value

    for card in dealt_cards[1:]:
        if card == 'J' or card == 'Q' or card == 'K':
            value += 11
        else:
            value += int(card)
    return value


def winner_hand(*hands: list):

    winner_hand_id: any = 0  # 0 is the dealer, 1+ is the players[1+]
    winner_hand_value = 0

    for hand in hands:
        temp_id = hand[0]
        temp = calculate_cards_value(hand, 0)
        if temp > winner_hand_value:
            winner_hand_value = temp
            if winner_hand_id == 0:
                winner_hand_id = "dealer"
            else:
                winner_hand_id = "Player{}".format(temp_id)

    return winner_hand_id, winner_hand_value


def add_card(hand: list):  # list is a call by object reference and doesnt need to return anything

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
        print("Error in dealers_hand function, out of bounds")


dealer_cards = deal_cards(0)
dealer_cards_value = calculate_cards_value(dealer_cards, 1)
dealer_cards_value_full = calculate_cards_value(dealer_cards, 0)  # todo remove this line it's a test

player_cards = deal_cards(1)
player_cards_value = calculate_cards_value(player_cards, 0)

print("dealers cards are:  *  {:2} of the value: {}".format(dealer_cards[2], dealer_cards_value))

print("dealers cards are:  {:2} {:2} of the value: {}".format(
                                                              dealer_cards[1],
                                                              dealer_cards[2],
                                                              dealer_cards_value_full
                                                              ))  # todo remove this line

print("your  cards   are:  {:2} {:2} of the value: {}\n".format(player_cards[1], player_cards[2], player_cards_value))

player_won, cards_value = winner_hand(dealer_cards, player_cards)
print("{} won with the value of {}".format(player_won, cards_value))

print(player_cards)
print()
print(player_cards)