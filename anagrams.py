#!/usr/bin/env python3

import itertools
from common import ingest_dictionary

dictionary = ingest_dictionary()

def solve_anagram(word):
    total_permutations = set()
    matching_words = set()

    for length in range(0, len(word) + 1):
        permutations = {''.join(x) for x in itertools.permutations(word, length)}
        total_permutations.update(permutations)

    for word in total_permutations:
        if word in dictionary:
            matching_words.add(word)

    return matching_words

def organize_matches(matches):
    matched_dict = {}

    for match in matches:
        if len(match) not in matched_dict:
            matched_dict[len(match)] = []

        matched_dict[len(match)].append(match)

    return matched_dict


def main():
    print("type in anagram and hit enter when done:")
    anagram = input()
    matches = solve_anagram(anagram)

    for count,matches in organize_matches(matches).items():
        print(f"Matches for length {count}: {sorted(matches)}")



main()
