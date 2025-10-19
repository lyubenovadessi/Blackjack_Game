import blackjack_logo, random

def deal_card():
    """Returns  random card from the dekc"""
    cards = [random.randint(2, 12)]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the sum of calculated cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_s, comp_s):
    """Compare the user and computer score"""
    if user_s == comp_s:
        return "Draw!🙌"
    elif comp_s == 0:
        return "Lose, opponent has Blackjack😭"
    elif user_s == 0:
        return "Win with a Blackjack🏆"
    elif user_s > 21:
        return "You went over. You lose!😭"
    elif comp_s > 21:
        return "Opponent went over. You win!🏆"
    elif user_s > comp_s:
        return "You win!🏆"
    else:
        return "You lose!😭"

def play_game():
    print(blackjack_logo.logo)
    user_cards = []
    comp_cards = []
    comp_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == 'y':
    print("\n" * 20)
    play_game()


