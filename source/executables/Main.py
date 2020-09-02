import source.models.Player as Player

print("Welcome to my Blackjack game")
print("Now dealer will deal cards...\n")


dealer = Player.Player(0)

dealer_cards_value = 0

print("dealers cards are:  *  {:2} of the value: {}".format(dealer.hand[1], dealer_cards_value))

print("dealers cards are:  {:2} {:2} of the value: {}".format(
                                                              dealer.hand[0],
                                                              dealer.hand[1],
                                                              dealer_cards_value
                                                              ))  # todo remove this line

# print("your  player   are:  {:2} {:2} of the value: {}\n".format(player_cards[1], player_cards[2], player_cards_value))
#
# player_won, cards_value = winner_hand(dealer_cards, player_cards)
# print("{} won with the value of {}".format(player_won, cards_value))