import source.models.PlayerModel as Player


def calculate_cards_value(player: Player.Player):  # Calculates the value of the player's hand

    for card in player.hand:
        if card == 'J' or card == 'Q' or card == 'K':
            player.value += 10
        else:
            player.value += int(card)


def calculate_single_card_value(player: Player.Player, card_number: int):

    card = player.hand[card_number]

    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)


def winner_players_list(*players: Player.Player):

    winner_players: list = []
    winner_hand_value = 0

    for player in players:
        if player.value > winner_hand_value:
            if len(winner_players) != 0:
                winner_players.remove(winner_hand_value)
            winner_hand_value = player.value
            winner_players.append(player)
        elif player.value == winner_hand_value:
            winner_players.append(player)

    return winner_players
