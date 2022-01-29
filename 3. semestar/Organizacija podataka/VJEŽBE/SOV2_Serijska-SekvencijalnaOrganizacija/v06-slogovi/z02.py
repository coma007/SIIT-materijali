import struct

IN_FILE = "points.bin"
FORMAT_HEADER = "ii"
FORMAT = "ff"
RECORD_SIZE_HEADER = struct.calcsize(FORMAT_HEADER)
RECORD_SIZE = struct.calcsize(FORMAT)

if __name__ == '__main__':

    with open(IN_FILE, "rb") as file_in:

        record_bytes_header = file_in.read(RECORD_SIZE_HEADER)
        record_header = struct.unpack(FORMAT_HEADER, record_bytes_header)
        record_header = [data for data in record_header]
        num_of_points, dimensions = record_header

        for point in range(num_of_points):
            line = file_in.seek(RECORD_SIZE*(1+point))
            record_bytes = file_in.read(RECORD_SIZE)
            record = struct.unpack(FORMAT, record_bytes)
            print(record)

