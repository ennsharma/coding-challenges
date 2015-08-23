"""
Problem Statement:
CSS colors are defined using a hexadecimal (HEX) notation 
for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code
1) It must start with a '#' symbol.
2) It can have 3 or 6 digits.
3) Each digit is in the range of 0 to F. (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
4) A-F letters can be in lower case too. (i.e. a, b, c, d, e and f are also valid digits).

You are given N lines of CSS code. Your task is to print all valid 
Hex Color Codes, in order of their occurence from top to bottom.
"""

num_lines = int(input())
css = ""
for _ in range(num_lines):
    css += input()
    
i = 0
can_search = False
hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
while i < len(css):
    if css[i] == "{":
        can_search = True
    if css[i] == "}":
        can_search = False
    if can_search:
        if css[i] == "#":
            validHex = False
            hex = "#"
            a = 1
            while css[i + a] in hex_digits:
                hex += css[i + a]
                a += 1
            if len(hex) == 4 or len(hex) == 7:
                print(hex)
    i += 1