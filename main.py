#!/usr/bin/env python3

import argparse
import anagrams
import wordhunt

parser = argparse.ArgumentParser(
            description='Program to solve GamePigeon word games (besides Word Bites)'
        )

parser.add_argument('game', choices=['wordhunt', 'anagrams'])

args = parser.parse_args()

if args.game == 'wordhunt':
    wordhunt.main()
elif args.game == 'anagrams':
    anagrams.main()
else:
    print("Game not implemented")

