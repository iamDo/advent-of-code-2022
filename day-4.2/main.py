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


def do_sections_overlap(section_pair):
    first_section, second_section = section_pair
    first_section_set = set(range(first_section[0], first_section[1] + 1))
    second_section_set = set(range(second_section[0], second_section[1] + 1))
    overlap = first_section_set & second_section_set
    return len(overlap) > 0


def main():
    lines = get_input()
    section_pairs = [pair_of_sections(line) for line in lines]
    overlapping_pairs = [section_pair for section_pair in section_pairs if do_sections_overlap(section_pair)]
    print(len(overlapping_pairs))


if __name__ == '__main__':
    main()
