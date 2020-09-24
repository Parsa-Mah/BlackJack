# It's basically the dealer
# This class deals cards in the right order from top
# To simulate a real BlackJack game
from typing import List  # To define the type of list()

import source.models.CardsModel as CardsModel
import source.models.PlayerModel as PlayerModel


def deal_cards(cards: CardsModel.Cards, players: List[PlayerModel.Player]):

    for i in range(2):
        for each in players[1:]:
            card = cards.cards.pop()
            each.add_card(card)
        card = cards.cards.pop()
        players[0].add_card(card)


def deal_card_for_player(cards: CardsModel.Cards, player: PlayerModel.Player):
    player.add_card(cards.cards.pop())
