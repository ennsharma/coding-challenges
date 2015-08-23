"""
Problem Statement:
You are given an HTML code snippet of N lines.
Your task is to detect and print all HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]

If an HTML tag has no attribute then simply print the name of the tag.
"""

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]

parser = MyHTMLParser()


num_lines = int(input())
html = ""
for _ in range(num_lines):
    html += raw_input()
parser = MyHTMLParser()
parser.feed(html)
parser.close()