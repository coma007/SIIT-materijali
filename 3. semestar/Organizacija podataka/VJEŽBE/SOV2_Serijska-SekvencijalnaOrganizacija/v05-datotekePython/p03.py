#!/usr/bin/python

S = "Neki string"

with open("p3_out.bin", "wb") as f:
    # prilikom pretvaranja stringa u niz bajtova
    # neophodno je proslediti naziv kodnog standarda
    f.write(S.encode("ASCII"))

with open("p3_out.bin", "rb") as f1, open("p3_out2.bin", "wb") as f2:
    p = f1.read()
    p = p.decode("ascii") + " \u0416 \u0402 \u015A"

    # drugi nacin pretvaranja stringa u bytes
    f2.write(bytes(p, "utf8"))

with open("p3_out2.bin", "rb") as f:
    print("Initial position" + str(f.tell()))
    f.seek(-8, 2)
    print("Position after position change" + str(f.tell()))
    p = f.read()
    p = p.decode("utf8")
    print(p)

if __name__ == '__main__':
    pass