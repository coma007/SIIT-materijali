#! /usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    ingredient, group = line.split(',')
    ingredient = ingredient.strip()
    group = group.strip()
    if ingredient.upper() == "NULL" or group.upper() == "NULL":
        continue
    print("%s\t%s" % (group, ingredient))
