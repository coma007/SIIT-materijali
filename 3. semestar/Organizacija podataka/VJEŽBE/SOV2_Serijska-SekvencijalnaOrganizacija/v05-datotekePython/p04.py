#!/usr/bin/python

import pickle
dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5,
             'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}
filename = 'dogs.bin'

with open(filename, 'wb') as outfile:
    pickle.dump(dogs_dict, outfile)

with open(filename, 'rb') as infile:
    new_dict = pickle.load(infile)

print(new_dict)
print(new_dict == dogs_dict)
print(type(new_dict))

if __name__ == '__main__':
    pass
