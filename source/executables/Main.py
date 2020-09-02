import random
import source.classes.Cards as Cards

print("Welcome to my Blackjack game")
print("Now dealer will deal cards...\n")


def calculate_cards_value(dealt_cards: list, card_number: int = 0):  # Calculates the value of the cards

    value = 0

    if card_number > 0:  # the value of a specific card and not negative
        card = dealt_cards[card_number]
        if card == 'J' or card == 'Q' or card == 'K':
            value += 10
        else:
            value += int(card)
        return value

    for card in dealt_cards[1:]:
        if card == 'J' or card == 'Q' or card == 'K':
            value += 10
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


dealer_cards = Cards.Cards(0).hand
dealer_cards_value = calculate_cards_value(dealer_cards, 2)
dealer_cards_value_full = calculate_cards_value(dealer_cards, 0)  # todo remove this line it's a test

player_cards = Cards.Cards(1).hand
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