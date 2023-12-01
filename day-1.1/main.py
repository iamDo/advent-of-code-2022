#!/usr/bin/env python3

INPUT_FILE = 'input.txt'


def inventory_iterator(inventory):
    backpack = []
    for item in inventory:
        if item == '\n':
            yield backpack
            backpack = []
        else:
            backpack.append(int(item[:-1]))


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    return lines


def main():
    lines = get_input()
    calories = [sum(backpack) for backpack in list(inventory_iterator(lines))]
    print(max(calories))


if __name__ == '__main__':
    main()
