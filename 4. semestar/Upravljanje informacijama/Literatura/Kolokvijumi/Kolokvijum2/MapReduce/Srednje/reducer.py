#! /usr/bin/python
import sys

current_group = ""
counter = 0
longest = 0
shortest = 0
group = ""

for line in sys.stdin:
    line = line.strip()
    group, ingredient = line.split("\t", 1)
    if current_group == group:
        counter += 1
        if len(ingredient) > longest:
            longest = len(ingredient)
        if len(ingredient) < shortest:
            shortest = len(ingredient)
    else:
        if current_group:
            print("%s\t%s\t%s\t%s" % (current_group, counter, longest, shortest))
        current_group = group
        counter = 1
        longest = len(ingredient)
        shortest = len(ingredient)

if current_group == group:
    print("%s\t%s\t%s\t%s" % (current_group, counter, longest, shortest))
