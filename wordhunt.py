#!/usr/bin/env python3

import itertools
from trie import TrieNode
from common import ingest_dictionary

root_node = TrieNode()
matched_word_dict = {}

def setup_trie():
    global trie

    print("Setting up trie...")
    for x in ingest_dictionary():
        root_node.insert(x.lower().strip())

    print("Done with trie!")

def matching_words(prefix, banned_idxs):
    node = root_node.node_for_prefix(prefix)

    if not node:
        return False

    if node.word_end:
        if len(prefix) not in matched_word_dict:
            matched_word_dict[len(prefix)] = []

        matched_word_dict[len(prefix)].append((prefix, tuple(banned_idxs)))

    return True

def solve_wordhunt_for_index(array, first_idx, second_idx, banned_idxs=None, prefix=''):
    if banned_idxs is None:
        banned_idxs = []

    current_letter = array[first_idx][second_idx]
    new_prefix = prefix + current_letter

    banned_idxs.append((first_idx, second_idx))

    if not matching_words(new_prefix, banned_idxs):
        return

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

def print_output(word_array):
    for length, words in sorted(matched_word_dict.items()):
        if length < 5:
            words_only = {word[0] for word in words}
            print(f"Words for count {length}: {words_only}\n")
        else:
            print(f"Words for count {length}: \n")

            deduplicated_words = dict(words).items()
            for word in deduplicated_words:
                print(f"{word[0]}:")

                for i in range(0, len(word_array[0])):
                    for j in range(0, len(word_array)):
                        if (i, j) == word[1][0]:
                            print("🟢", end="")
                        elif (i, j) == word[1][len(word[1]) - 1]:
                            print("🏁", end="")
                        elif (i, j) in word[1]:
                            print("🟨", end="")
                        else:
                            print("⬜", end="")
                    print("")
                print("\n\n")

            

def main():
    setup_trie()

    word_array = get_board_from_user()

    for i in range(0, len(word_array)):
        for j in range(0, len(word_array[i])):
            solve_wordhunt_for_index(word_array, i, j)

    print_output(word_array)

if __name__ == "__main__":
    main()
