import sys

current_trade = ""
trade = ""
max_up = 0
max_down = 0
last_val = 0

for line in sys.stdin:
    line = line.strip()
    key, val = line.split("\t")
    trade, date = key.split("-")
    try:
        val = float(val)
    except Exception:
        continue
    if current_trade == trade:
        diff = val - last_val
        if diff > max_up:
            max_up = diff
        if diff < max_down:
            max_down = diff
        last_val = val
    else:
        if current_trade:
            print("%s:\t%s\t%s" % (current_trade, max_up, max_down))
        current_trade = trade
        last_val = val
        max_up = 0
        max_down = 0

if current_trade == trade:
    print("%s:\t%s\t%s" % (current_trade, max_up, max_down))

