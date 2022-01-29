def transform(i):
    return i**2

def filter(i):
    return i % 2 == 0

if __name__ == '__main__':
    imena = [1,2,3,4,5]

    nova_list = [transform(i) for i in imena if filter(i)]
    print(nova_list)
