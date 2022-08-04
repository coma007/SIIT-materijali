import sys

current_friends = ""
current_owners = ""
owners = ""

for line in sys.stdin:
    line = line.strip()
    owners, friend = line.split('\t', 1)
    if current_owners == owners:
        current_friends += friend + ","
    else:
        if current_owners:
            print(f'{current_owners}\t{current_friends}')
        current_friends = friend + ","
        current_owners = owners

if current_friends == owners:
    print(f'{current_owners}\t{current_friends}')
