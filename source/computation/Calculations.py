import source.models.Player as Player


def calculate_cards_value(player: Player.Player):  # Calculates the value of the player

    if player.card_number > 0:  # the value of a specific card and not negative
        card = player.hand[player.card_number]
        if card == 'J' or card == 'Q' or card == 'K':
            player.value += 10
        else:
            player.value += int(card)

    for card in player.hand[1:]:
        if card == 'J' or card == 'Q' or card == 'K':
            player.value += 10
        else:
            player.value += int(card)


def winner_hand(*player: Player.Player):
    for hand in player:
        hands = hand.hand

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