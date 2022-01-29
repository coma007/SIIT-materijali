if __name__ == '__main__':

    IN_FILE = "in.txt"

    with open(IN_FILE) as f:
        lines = f.readlines()

    chars = letters = digits = words = sentences = 0
    for line in lines:
        for char in line[:-1]:
            chars += 1
            if char.isdigit():
                digits += 1
            if char.isalpha():
                letters += 1
            elif char == ' ':
                words += 1
            elif char == '.' or char == '!':
                sentences += 1



