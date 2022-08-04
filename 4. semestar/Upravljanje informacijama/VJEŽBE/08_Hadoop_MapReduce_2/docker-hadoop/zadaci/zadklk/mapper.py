import sys
for line in sys.stdin:
    line = line.strip()
    date, _, lmt, _, mpx, _, bmp = line.split(",")
    print("lmt-%s\t%s\n" % (date, lmt))
    print("mpx-%s\t%s\n" % (date, mpx))
    print("bmp-%s\t%s\n" % (date, bmp))
