import sys

for line in sys.stdin:
    line = line.strip()
    owners, friend = line.split('\t')
    owners = owners.strip().upper()
    friend = friend.split(',')
    print('%s\t%s' % (owners, friend))
