#!/usr/bin/env python3

INPUT_FILE = 'input.txt'

def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]

    return lines


def pair_of_sections(line):
    section_pair = line.split(',')
    section_pair = [section.split('-') for section in section_pair]
    return [[int(section_pair) for section_pair in section] for section in section_pair]


def does_section_contain_other(sections):
    first_section = sections[0]
    second_section = sections[1]
    return first_section[0] <= second_section[0] and first_section[1] >= second_section[1] or \
        second_section[0] <= first_section[0] and second_section[1] >= first_section[1]


def main():
    lines = get_input()
    section_pairs = [pair_of_sections(line) for line in lines]
    overlapping_pairs = [section_pair for section_pair in section_pairs if does_section_contain_other(section_pair)]
    print(len(overlapping_pairs))


if __name__ == '__main__':
    main()
