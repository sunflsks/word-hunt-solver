#!/usr/bin/env python3

import itertools

def ingest_dictionary():
    print("Ingesting dictionary...")
    return {x.strip().lower() for x in open("enable1.dict", "r+")}
