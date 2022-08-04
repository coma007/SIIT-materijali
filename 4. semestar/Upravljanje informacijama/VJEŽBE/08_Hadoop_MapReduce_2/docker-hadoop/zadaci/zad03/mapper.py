import sys

for line in sys.stdin:
    line = line.strip()
    owner, friends = line.split(':')
    owner = owner.strip().upper()
    friends = friends.split(',')
    for friend in friends:
        friend = friend.strip().upper()
        print('%s\t%s' % (friend, owner))
