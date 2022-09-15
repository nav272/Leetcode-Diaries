import collections
from itertools import count
from operator import sub
from typing import Counter

def minWindow(s, t):
    if len(s) < len(t):
        return ""
    substring_lookup = {}
    given_substring = {}
    left, right = 0, 0
    minimum_window = 1000000, 0, 0
    for i, v in enumerate(t):
        given_substring[v] = 1 + given_substring.get(v, 0)
    required = len(given_substring)
    current = 0
    while right < len(s):
        character = s[right]
        substring_lookup[character] = substring_lookup.get(character, 0) + 1 
        if character in given_substring and substring_lookup[character] == given_substring[character]:
            current +=1
        
        while left <= right and required==current:
            character = s[left]
            if right - left + 1 < minimum_window[0]:
                minimum_window = right - left + 1, left, right
            substring_lookup[character] -=1
            if character in given_substring and substring_lookup[character]< given_substring[character]:
                current -=1
            left +=1
        right +=1
    return '' if minimum_window[0] == 1000000 else s[minimum_window[1]:minimum_window[2]+1]




print(minWindow("ADOBECODEBANC", "A"))