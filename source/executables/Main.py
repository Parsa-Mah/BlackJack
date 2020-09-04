import source.models.PlayerModel as PlayerModel
import source.computation.Calculations as Calc
import source.models.CardsModel as CardsModel

print()
print("Welcome to my Blackjack game")
print("Now dealer will deal cards...\n")

players_list = []

dealer = PlayerModel.Player(0)
Calc.calculate_cards_value(dealer)
players_list.append(dealer)
player_1 = PlayerModel.Player(1)
Calc.calculate_cards_value(player_1)
players_list.append(player_1)
player_2 = PlayerModel.Player(2)
Calc.calculate_cards_value(player_2)
players_list.append(player_2)

dealer_cards_value = 0


for player in players_list:

    if player.player_num == 0:
        print("{:10} cards are: {:2} {:2} of the value: {}".format("dealer's",
                                                                   "*",
                                                                   player.hand[1],
                                                                   Calc.calculate_single_card_value(player, 1)))
    else:
        print("Player{:2}'s cards are: {:2} {:2} of the value: {}".format(player.player_num,
                                                                          player.hand[0],
                                                                          player.hand[1],
                                                                          player.value))

print("dealers cards are:  {:2} {:2} of the value: {}".format(
                                                              dealer.hand[0],
                                                              dealer.hand[1],
                                                              dealer.value
                                                              ))  # todo remove this line
winners = Calc.winner_players_list(dealer, player_1, player_2)

for each in winners:
    print("{}".format(each.player_num))
cards = CardsModel.Cards(2)
print(cards.cards)
cards.shuffle_cards()
print(cards.cards)
cards.shuffle_cards()
print(cards.cards)
