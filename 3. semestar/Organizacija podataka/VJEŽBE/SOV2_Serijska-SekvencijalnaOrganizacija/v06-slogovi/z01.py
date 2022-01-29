import struct

IN_FILE = "points.txt"
OUT_FILE = "points.bin"
DELIMITER = ","
FORMAT_HEADER = "ii"
FORMAT = "ff"

if __name__ == '__main__':

    with open(IN_FILE) as file_in, open(OUT_FILE, "wb") as file_out:

        record_header = (3, 2)
        record_bytes_header = struct.pack(FORMAT_HEADER, *record_header)
        file_out.write(record_bytes_header)

        while True:
            line = file_in.readline()
            if not line:
                break

            fields = line.strip().split(DELIMITER)
            record = [float(fields[0]), float(fields[1])]
            print(record)
            record_bytes = struct.pack(FORMAT, *record)
            file_out.write(record_bytes)

