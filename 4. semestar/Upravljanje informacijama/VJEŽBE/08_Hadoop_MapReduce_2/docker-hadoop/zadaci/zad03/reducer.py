import sys

current_friend = ""
current_owners = []
friend = ""

for line in sys.stdin:
    line = line.strip()
    friend, owner = line.split('\t', 1)
    if current_friend == friend:
        current_owners.append(owner)
    else:
        if current_friend:
            current_owners.sort()
            for i in range(len(current_owners)):
                for j in range(i+1, len(current_owners)):
                    print(f'{current_owners[i]}{current_owners[j]}\t{current_friend}')
        current_friend = friend
        current_owners = [owner]

if current_friend == friend:
    current_owners.sort()
    for i in range(len(current_owners)):
        for j in range(i+1, len(current_owners)):
            print(f'{current_owners[i]}{current_owners[j]}\t{current_friend}')
