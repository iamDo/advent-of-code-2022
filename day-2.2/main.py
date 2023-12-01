#!/usr/bin/env python3

INPUT_FILE = 'input.txt'
VICTORY_POINTS = 6
DRAW_POINTS = 3
DEFEAT_POINTS = 0
STRATEGY_MEANING = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'defeat',
    'Y': 'draw',
    'Z': 'victory',
}
REQUIRED_MOVES = {
    'rock': {
        'victory': 'paper',
        'draw': 'rock',
        'defeat': 'scissors',
    },
    'paper': {
        'victory': 'scissors',
        'draw': 'paper',
        'defeat': 'rock',
    },
    'scissors': {
        'victory': 'rock',
        'draw': 'scissors',
        'defeat': 'paper',
    },
}
MOVE_POINTS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}
RESOLUTION_POINTS = {
    'victory': 6,
    'draw': 3,
    'defeat': 0,
}


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    return [tuple(line.split()) for line in lines]


def decrypt_strategy(strategy):
    return tuple([STRATEGY_MEANING[move] for move in strategy])


def resolve_match(_match):
    opponent_move = _match[0]
    desired_resolution = _match[1]

    my_move = REQUIRED_MOVES[opponent_move][desired_resolution]

    move_points = MOVE_POINTS[my_move]
    resolution_points = RESOLUTION_POINTS[desired_resolution]

    return move_points + resolution_points


def main():
    encrypted_strategy_guide = get_input()
    strategy_guide = [decrypt_strategy(strategy) for strategy in encrypted_strategy_guide]
    resolved_matches = [resolve_match(_match) for _match in strategy_guide]
    print(sum(resolved_matches))


if __name__ == '__main__':
    main()
