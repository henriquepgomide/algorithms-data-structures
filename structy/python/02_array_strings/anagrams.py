"""
ANAGRAMS

Write a function, anagrams, that takes in two strings as arguments. The
function should return a boolean indicating whether or not the strings are
anagrams. Anagrams are strings that contain the same characters, but in any
order.

"""
from typing import Dict


def count_words(s1: str) -> Dict[str, int]:
    counter = {}
    for s in s1:
        if s not in counter:
            counter[s] = 0
        counter[s] += 1
    return counter


def is_anagram(s1: str, s2: str) -> bool:
    return count_words(s1) == count_words(s2)
