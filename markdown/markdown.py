"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
        then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
    line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    return line

def convertEm(line):
    line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return line


isBlockquote = False
for line in fileinput.input():
    # print '###' + line + '###'
    if line[0] == '>':
        if not isBlockquote:
            isBlockquote = True
            print '<blockquote>'
        line = line[1:]
    elif line == '\n' and isBlockquote:
        isBlockquote = False
        print '</blockquote>'
        continue
    line = line.rstrip()
    line = convertStrong(line)
    line = convertEm(line)
    if len(line) > 0 and line[0] == '#':
        line = re.sub(r'###(.*)$', r'<h3>\1</h3>', line)
        line = re.sub(r'##(.*)$', r'<h2>\1</h2>', line)
        line = re.sub(r'#(.*)$', r'<h1>\1</h1>', line)
        print line
    else:
        print '<p>' + line + '</p>',
