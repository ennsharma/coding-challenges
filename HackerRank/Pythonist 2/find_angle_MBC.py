"""
Problem Statement:
ABC is a right angle triangle, right angled at B.
Therefore angle ABC = 90 degrees.

Point M is the mid-point of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC in degrees.
"""

import math
import dis

ab = int(input())
bc = int(input())
ac2 = ab**2 + bc**2

print(str(round(math.degrees(math.acos(-1*(ab**2 - bc**2 - ac2)/(2*bc*math.sqrt(ac2)))))))