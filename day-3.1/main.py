#!/usr/bin/env python3

INPUT_FILE = 'input.txt'

ALPHABET_LOWERCASE = [chr(i) for i in range(97, 123)]
ALPHABET_UPPERCASE = [chr(i) for i in range(65, 91)]
ALPHABET = ALPHABET_LOWERCASE + ALPHABET_UPPERCASE


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    return lines


def get_item_priority(item):
    return ALPHABET.index(item) + 1


def line_to_ruckack(line):
    compartment_size = int(len(line)/2)
    return [line[:compartment_size], line[compartment_size:]]


def find_duplicate(rucksack):
    return (set(rucksack[0]) & set(rucksack[1])).pop()


def main():
    lines = get_input()
    rucksacks = [line_to_ruckack(line) for line in lines]
    duplicates = [find_duplicate(rucksack) for rucksack in rucksacks]
    print(sum((get_item_priority(item) for item in duplicates)))


if __name__ == '__main__':
    main()
