import sys

header = True

for line in sys.stdin:
    if header:
        header = False
        continue
    data_line = line.strip()
    data = data_line.split(',')
    card = data[3].strip().upper()
    amount = data[2].strip()
    print('%s\t%s' % (card, amount))
