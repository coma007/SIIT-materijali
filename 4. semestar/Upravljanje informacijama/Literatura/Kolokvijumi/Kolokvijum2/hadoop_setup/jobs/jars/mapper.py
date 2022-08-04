import sys

for line in sys.stdin:
    line = line.strip()
    date, trades = line.split(",", 1)
    trades = trades.split(",")
    for i in range(0, len(trades), 2):
        print("%s-%s\t%s" % (trades[i].strip().upper(), date, trades[i+1].strip()))
