"""
Problem Statement:
You are given a string S. Your task is to find the three
most common characters in the string S.
"""

import operator

s, map = input(), {}

for c in s:
    if c in map:
        map[c] += 1
    else:
        map[c] = 1
for _ in range(3):
    max_key = max(sorted(map.items()), key=operator.itemgetter(1))[0]
    print(max_key + " " + str(map[max_key]))
    del map[max_key]
