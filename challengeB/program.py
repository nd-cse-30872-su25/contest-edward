#!/usr/bin/env python3
import sys

def iso(word1: str, word2: str)->bool:
    if len(word1) != len(word2):
        return False
    letters = {}
    for index, letter in enumerate(word1):
        if letter not in letters:
            letters[letter] = word2[index]
        else:
            if letters[letter] != word2[index]:
                return False
    return True

def main():
    for line in sys.stdin:
        word1, word2 = line.strip().split()
        is_iso = iso(word1, word2)
        if is_iso:
            print("Isomorphic")
        else:
            print("Not Isomorphic")

if __name__ == "__main__":
    main()
