#!/usr/bin/python

import sys

N = 12345

with open("p2_out.bin", "wb") as f:
    # koliko N ima bajtova?
    n_size = sys.getsizeof(N)
    # pretvaranje int u niz bajtova
    n_bytes = N.to_bytes(n_size, "little")
    print(n_bytes)
    f.write(n_bytes)

with open("p2_out.bin", "rb") as f1, open("p2_out1.bin", "wb") as f2:
    n_bytes = f1.read(sys.getsizeof(N))
    # pretvaranje niza bajtova u int
    m = int.from_bytes(n_bytes, "little")
    print(m)
    m *= 2
    f2.write(m.to_bytes(sys.getsizeof(m), "little"))

if __name__ == '__main__':
    pass