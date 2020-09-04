import source.models.PlayerModel as Player


def calculate_cards_value(player: Player.Player):  # Calculates the value of the player's hand

    for card in player.hand:
        if card == 'J' or card == 'Q' or card == 'K':
            player.value += 10
        else:
            player.value += int(card)  # This directly puts the value of hand in the Player Object


def calculate_single_card_value(player: Player.Player, card_number: int):

    card = player.hand[card_number]

    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)


def winner_players_list(*players: Player.Player):

    winner_players: list = []
    winner_player_temp: Player.Player = Player.Player(0)

    for player in players:  # To find the highest hand value in the game
        if player.value > winner_player_temp.value:
            winner_player_temp = player

    for player in players:  # If there are more than one player having the highest value
        if player.value == winner_player_temp.value:
            winner_players.append(player)

    return winner_players














