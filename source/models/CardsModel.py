# This model represents the actual cards for dealer to deal with
# They are exactly one complete hand of 52 cards
# with 4 of each cards in a normal BlackJack game

import random


class Cards:
    def __init__(self, number_of_decks: int):

        self.number_of_decks = number_of_decks
        self.cards = self.create_card_deck(number_of_decks)
        self.id = 0

    def create_card_deck(self, number_of_decks):

        temp_card_list = []

        for i in range(1, 11):
            for j in range(4 * number_of_decks):  # There is 4 of each card
                temp_card_list.append(str(i))

        for i in range(4 * number_of_decks):
            temp_card_list.append("J")

        for i in range(4 * number_of_decks):
            temp_card_list.append("Q")

        for i in range(4 * number_of_decks):
            temp_card_list.append("K")

        return temp_card_list

    def shuffle_cards(self):

        temp_cards_list: list = []

        # random.sample returns a unique set of numbers
        shuffled_indexes = random.sample(range(0, len(self.cards)), len(self.cards))

        for each in shuffled_indexes:
            temp_cards_list.append(self.cards[each])

        self.cards = temp_cards_list
