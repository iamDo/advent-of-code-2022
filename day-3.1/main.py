#!/usr/bin/env python3

INPUT_FILE = 'input.txt'


def get_input():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()

    return lines
