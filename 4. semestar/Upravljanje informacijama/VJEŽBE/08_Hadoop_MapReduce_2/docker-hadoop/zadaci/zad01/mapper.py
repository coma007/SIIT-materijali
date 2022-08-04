import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(',')
    variable = data[0].strip().lower()
    value = data[1].strip()
    print('%s\t%s\t%s' % (variable, value, 1))
