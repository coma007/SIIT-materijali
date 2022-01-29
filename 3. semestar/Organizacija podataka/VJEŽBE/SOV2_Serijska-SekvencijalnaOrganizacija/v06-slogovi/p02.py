#!/usr/bin/python

import struct

IN_FILE = "username.bin"
FORMAT = "12si10s10s"
ENCODING = "ascii"
RECORD_SIZE = struct.calcsize(FORMAT)

with open(IN_FILE, "rb") as fin:
    # skok na 2. slog
    fin.seek(RECORD_SIZE)
    record_bytes = fin.read(RECORD_SIZE)
    record = struct.unpack(FORMAT, record_bytes)
    record = [v.decode(ENCODING).strip('\x00') if isinstance(v, bytes) else v for v in record]
    print(record)

    # skok na 5. slog
    fin.seek(4*RECORD_SIZE)
    record_bytes = fin.read(RECORD_SIZE)
    record = struct.unpack(FORMAT, record_bytes)
    record = [v.decode(ENCODING).strip('\x00') if isinstance(v, bytes) else v for v in record]
    print(record)

if __name__ == '__main__':
    pass
