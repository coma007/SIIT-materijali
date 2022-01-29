#!/usr/bin/python

import struct


class Record:
    def __init__(self, attributes, format, coding):
        self.attributes = attributes
        self.format = format
        self.coding = coding

    def encoded_tuple_to_dict(self, binary_data):
        t = struct.unpack(self.format, binary_data)
        return {self.attributes[i]: t[i].decode(self.coding).strip('\x00') if isinstance(t[i], bytes) else t[i] for i in range(len(t))}

    def dict_to_encoded_values(self, d):
        values = [v.encode(self.coding) if isinstance(v, str) else v for v in d.values()]
        return struct.pack(self.format, *values)
