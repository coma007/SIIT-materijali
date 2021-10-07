# v02z07
# Data je platforma	sa tri stuba označena sa a, b i	c. Na stubu	a nalaze se	n diskova složenih po veličini od najmanjeg
# ka najvećem. Napisati	algoritam za prebacivanje diskova sa stuba a na stub b.


def hanoi(disks, source, target, help):

    if disks > 0:
        # Get n - 1 disks out of way, from A to C and B
        hanoi(disks - 1, source, help, target)

        # Move the nth disk from A to B
        target.append(source.pop())
        print(f'\nStick A: {source}\nStick B: {target}\nStick C: {help}')

        # Move disks from B and C to A and B and finally B
        hanoi(disks - 1, help, target, source)


def create_platform(n):

    disks = []
    for i in range(n):
        disks += [i+1]

    return disks, [], []


if __name__ == '__main__':

    print("------The Tower of Hanoi------")
    my_disks = 10
    A, B, C = create_platform(my_disks)
    print(f'\nStick A: {A}\nStick B: {B}\nStick C: {C}')
    hanoi(len(A), A, B, C)
