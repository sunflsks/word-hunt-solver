#!/usr/bin/env python3

import itertools
from trie import Trie, TrieNode

trie = Trie()
matched_word_dict = {}

def ingest_dictionary():
    global trie

    print("Ingesting dictionary...")
    with open("words.dict") as dictionary_file:
        for x in dictionary_file:
            trie.insert(x.lower().strip())
    print("Done!")

def matching_words(prefix):
    node = trie.node_for_prefix(prefix)

    if not node:
        return False

    if node.word_end:
        if len(prefix) not in matched_word_dict:
            matched_word_dict[len(prefix)] = []

        matched_word_dict[len(prefix)].append(prefix)

    return True

def solve_wordhunt_for_index(array, first_idx, second_idx, banned_idxs=None, prefix=''):
    if banned_idxs is None:
        banned_idxs = set()

    current_letter = array[first_idx][second_idx]
    new_prefix = prefix + current_letter

    if not matching_words(new_prefix):
        return

    banned_idxs.add((first_idx, second_idx))

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_first_idx = first_idx + i
            new_second_idx = second_idx + j

            if i == j == 0:
                continue

            if new_first_idx < 0 or new_second_idx < 0: 
                continue

            if new_first_idx >= len(array) or new_second_idx >= len(array[new_first_idx]):
                continue

            if (new_first_idx, new_second_idx) in banned_idxs:
                continue

            solve_wordhunt_for_index(array, new_first_idx, new_second_idx, banned_idxs.copy(), new_prefix)

def get_board_from_user():
    print("Type each character seperated by a space, with each row seperated by a newline")

    word_array = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        line_chars = line.strip().split()
        word_array.append(line_chars)

    print("\n")
    return word_array

def main():
    ingest_dictionary()

    word_array = get_board_from_user()

    for i in range(0, len(word_array)):
        for j in range(0, len(word_array[i])):
            solve_wordhunt_for_index(word_array, i, j)

    for length, words in sorted(matched_word_dict.items()):
        words = set(words)
        print(f"Words for count {length}: {words}\n")

if __name__ == "__main__":
    main()
