"""[Extra]"""
def main():
    """Hard - Bowling"""
    game = input()
    frame_10 = len(game.split()[-1])
    game = list(game.replace(' ', ''))
    score = 0
    for i in range(len(game)):
        if game[i] == '-':
            game[i] = [0, '-']
        elif game[i] == 'X':
            game[i] = [10, 'X']
        elif game[i] == '/':
            game[i] = [10 - game[i - 1][0], '/']
        else:
            game[i] = [int(game[i]), game[i]]
    for i in range(len(game) - frame_10):
        if game[i][1] == 'X':
            score += game[i][0] + game[i + 1][0] + game[i + 2][0]
        elif game[i][1] == '/':
            score += game[i][0] + game[i + 1][0]
        else:
            score += game[i][0]
    for i in range(len(game) - frame_10, len(game)):
        score += game[i][0]
    print(score)
main()
