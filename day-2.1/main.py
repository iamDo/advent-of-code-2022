#!/usr/bin/env python3

INPUT_FILE = 'input.txt'
VICTORY_POINTS = 6
DRAW_POINTS = 3
DEFEAT_POINTS = 0
RULES = {
    'X': {
        'A': DRAW_POINTS,
        'B': DEFEAT_POINTS,
        'C': VICTORY_POINTS,
    },
    'Y': {
        'A': VICTORY_POINTS,
        'B': DRAW_POINTS,
        'C': DEFEAT_POINTS,
    },
    'Z': {
        'A': DEFEAT_POINTS,
        'B': VICTORY_POINTS,
        'C': DRAW_POINTS,
    },
}
POINTS_FOR_MOVE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    return [tuple(line.split()) for line in lines]


def resolve_match(_match):
    my_move = _match[1]
    opponent_move = _match[0]


    points_for_move = POINTS_FOR_MOVE[my_move]
    points_for_resolution = RULES[my_move][opponent_move]

    return points_for_move + points_for_resolution


def main():
    strategy = get_input()
    resolved_matches = [resolve_match(_match) for _match in strategy]
    print(resolved_matches)


if __name__ == '__main__':
    main()
