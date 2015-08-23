"""
Problem Statement:
Kevin and Stuart, wants to play 'The Minion Game'.
Bob is the match referee. Bob's task is to declare the winner and ensure that no rules are broken.
Stuart is Player 1 and Kevin is Player 2.

About Game:

Rules:
The game is a two player game. Players are given a string S.
Both the players have to make words using the letters of string S.
Player 1 has to make words starting with consonants.
Player 2 has to make words starting with vowels. 
Game ends when both player have made all possible substrings. 

Scoring
Player get +1 Point for each occurence of the word in the string S.
Example:
If string S = BANANA
Word made by Player 2 = ANA
'ANA' is occuring twice in 'BANANA'. Hence, Player 2 will get 2 Points. 

Your task is to help Bob.
"""

s = input()
N = len(s)
c_count, v_count = 0, 0
i = 0
while i < N:
    if s[i] in ['A', 'E', 'I', 'O', 'U']:
        v_count += len(s) - i
    else:
        c_count += len(s) - i
    i += 1
if c_count == v_count:
    print("Draw")
elif c_count > v_count:
    print("Stuart " + str(c_count))
else:
    print("Kevin " + str(v_count))