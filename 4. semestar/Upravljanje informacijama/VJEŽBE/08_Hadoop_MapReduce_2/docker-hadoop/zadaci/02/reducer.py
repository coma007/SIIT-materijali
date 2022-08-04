import sys

current_card = ""
current_amount = ""
card = ""

for line in sys.stdin:
    line = line.strip()
    card, amount = line.split('\t', 1)
    try:
        amount = int(amount)
    except ValueError:
        continue
    if current_card == card:
        current_amount += amount
    else:
        if current_card:
            print('%s\t%s' % (current_card, current_amount))
        current_card = card
        current_amount = amount

if current_card == card:
    print('%s\t%s' % (current_card, current_amount))
