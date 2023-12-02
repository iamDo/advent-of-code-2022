#!/usr/bin/env python3

INPUT_FILE = 'input.txt'

ALPHABET_LOWERCASE = [chr(i) for i in range(97, 123)]
ALPHABET_UPPERCASE = [chr(i) for i in range(65, 91)]
ALPHABET = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE
GROUP_SIZE = 3

def group_generator(list_of_elves, group_size):
    for i in range(0, len(list_of_elves), group_size):
        yield list_of_elves[i:i+group_size]


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]

    return lines


def get_item_priority(item):
    return ALPHABET.index(item) + 1


def find_common_item(group):
    sets = [set(group_member) for group_member in group]
    return set.intersection(*sets).pop()


def main():
    list_of_elves = get_input()
    groups = [group for group in group_generator(list_of_elves, GROUP_SIZE)]
    common_items = [find_common_item(group) for group in groups]
    print(sum((get_item_priority(item) for item in common_items)))


if __name__ == '__main__':
    main()
