"""
Problem Statement:
Mr. Vincent works in a door mat manufacturing company. One day, he designed
a new door mat. Design specifications are as follows:

1. Size of mat must be NxM. (N is an odd natural number and M is 3 times N.)
2. Design should have 'WELCOME' written in the center.
3. Design patterns should only use '|', '.', and '-' characters.



##################
# SAMPLE DESIGNS #
##################

Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

N, M = map(int,raw_input().split())
for i in xrange(1,N,2): 
    print int((N//2)*3 - (i//2)*3)*'-' + i*".|." + int((N//2)*3 - (i//2)*3)*'-'
print '-'*((M-7)//2) + 'WELCOME' + '-'*((M-7)//2)
for i in xrange(N-2,-1,-2): 
    print int((N//2)*3 - (i//2)*3)*'-' + i*".|." + int((N//2)*3 - (i//2)*3)*'-'