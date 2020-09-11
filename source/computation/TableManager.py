# It's basically the dealer
# This class deals cards in the right order from top
# To simulate a real BlackJack game
from typing import List

import source.models.CardsModel as CardsModel
import source.models.PlayerModel as PlayerModel


def deal_cards(cards: CardsModel.Cards, players: List[PlayerModel.Player]):

    for each in players:
        card = cards.cards.pop()
        each.add_card(card)
