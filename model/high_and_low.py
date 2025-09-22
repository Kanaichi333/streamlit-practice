import random


def card(deck):
    sample = random.sample(deck, 2)
    remaining = list(set(deck) - set(sample))

    return sample[0], sample[1], remaining


def judge(player_choice, base_card, result_card):
    if player_choice == "High":
        if base_card < result_card:
            return "Win"
        elif base_card > result_card:
            return "Lose"
        else:
            return "Draw"
        
    elif player_choice == "Low":
        if base_card > result_card:
            return "Win"
        elif base_card < result_card:
            return "Lose"
        else:
            return "Draw"


def bet(judge, money, bet):
    if judge == "Win":
        return money + bet
    
    elif judge == "Lose":
        return money - bet
    
    else:
        return money
