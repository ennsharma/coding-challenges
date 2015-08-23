"""
Problem Statement:
You are given a function f(X)=X^2.

You are also given K lists. The ith list consists of N_i elements.

You have to pick exactly one element from each list such that 
S=(f(X1)+f(X2)+...+f(Xk))%M 
is maximized. Xi denotes the element picked from the ith list. 
Find the maximized value Smax thus obtained.

% denotes the modulo operator.
"""

import itertools

k, m = [int(x) for x in input().split()]
lsts = []

for _ in range(k):
    lsts.append(sorted([(int(x)**2)%m for x in input().split()][1:]))
possibilities = itertools.product(*lsts)
maximum = max([sum(t)%m for t in possibilities])
print(maximum)
