
# This model represents the player that are going to play BlackJack
# This model has all the attributes related to a real player
# things like its name, its cards and cards value

class Player:
    def __init__(self, player_num: int):

        self.player_num = player_num
        self.hand: list = []
        self.value: int = 0

    def add_card(self, card: str):  # list is a call by object reference and doesnt need to return anything

        self.hand.append(card)
