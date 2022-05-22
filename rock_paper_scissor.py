import random


def play():
    user = input('(r) for rock, (p) for paper, (s) for scissor')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

# r>s, p>r, s>p


def is_win(player, opponent):
    # return true if player wins
