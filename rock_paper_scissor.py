import random


def play():
    user = input(
        "what is your choice?, 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

# r>s, p>r, s>p
    if is_win(user, computer):
        return 'YOU WON'
    else:
        return 'you lost!!'


def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


print(play())
