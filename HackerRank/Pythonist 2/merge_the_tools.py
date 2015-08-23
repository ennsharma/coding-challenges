"""
Problem Statement:
In this task, you would be given a string S of length N. You 
have to divide this string into N/K equal parts.

Let us consider the string thus obtained in part i as T_i. For 
each string T_i thus obtained, you have to make a modified 
string such that each character that occurs in T_i occurs exactly
once.

Suppose the first occurrence of ch_1 was before the first occurrence
of ch_2 in the modified string of T_i too. Output N/K lines each containing
the modified string for the corresponding chunk T_i
"""

s = input()
k = int(input())

i = 0
map, to_print = {}, ""
while i < len(s):
    if i % k == 0 and i != 0:
        print(to_print)
        map, to_print = {}, ""
    if s[i] not in map.keys():
        map[s[i]] = 0
        to_print += s[i]
    i += 1
print(to_print)
