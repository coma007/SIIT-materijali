#!/usr/bin/python

import os

from app.binary_file import BinaryFile


class SerialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, empty_key)

    def init_file(self):
        with open(self.filename, "wb") as f:
            block = self.blocking_factor*[self.get_empty_rec()]  # inicijalizacija datoteke podrazumeva unos bloka koji sadrzi prazne slogove
            self.write_block(f, block)

    def insert_record(self, rec):
        if self.find_by_id(rec.get("id")):  # provera da li vec postoji slog sa zadatim id-jem - svakom unosu prethodi pretraga!
            print("Already exists with ID {}".format(rec.get("id")))
            return

        with open(self.filename, "rb+") as f:
            f.seek(-self.block_size, 2)  # citamo poslednji blok
            block = self.read_block(f)

            for i in range(self.blocking_factor):
                if block[i].get("id") == self.empty_key:  # trazimo prvi prazan slog
                    block[i] = rec
                    break

            i += 1

            if i == self.blocking_factor:  # provera da li smo popunili trenutni blok ili ne
                f.seek(-self.block_size, 1)
                self.write_block(f, block)
                block = self.blocking_factor*[self.get_empty_rec()]
                self.write_block(f, block)
            else:
                block[i] = self.get_empty_rec()
                f.seek(-self.block_size, 1)
                self.write_block(f, block)

    def __is_last(self, block):
        for i in range(self.blocking_factor):  # da li blok sadrzi neki slog koji je prazan?
            if block[i].get("id") == self.empty_key:
                return True
        return False

    def print_file(self):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                if not block:
                    break

                i += 1
                print("Block {}".format(i))
                self.print_block(block)

    def find_by_id(self, id):
        i = 0
        with open(self.filename, "rb") as f:
            while True:
                block = self.read_block(f)

                for j in range(self.blocking_factor):
                    if block[j].get("id") == id:
                        return (i, j)
                    elif block[j].get("id") == self.empty_key:  # ukoliko smo naisli na prazan slog - stigli smo do kraja datoteke
                        return None

                i += 1

    def delete_by_id(self, id):
        found = self.find_by_id(id)

        if not found:
            return

        block_idx = found[0]
        rec_idx = found[1]
        next_block = None

        with open(self.filename, "rb+") as f:
            while True:
                f.seek(block_idx * self.block_size)
                block = self.read_block(f)

                i = rec_idx
                while i < self.blocking_factor-1:  # brisemo block[rec_idx] tako sto sve nakon njega pomeramo za jedno mesto ka levo
                    block[i] = block[i+1]
                    i += 1

                if self.__is_last(block):  # ako je poslednji blok - upisemo novi sadrzaj i zavrsavamo
                    f.seek(-self.block_size, 1)
                    self.write_block(f, block)
                    break

                next_block = self.read_block(f)  # ako nije poslednji blok, onda pomeranje mora da se nastavi i u narednim blokovima, dok ne stignemo do poslednjeg
                block[self.blocking_factor-1] = next_block[0]  # poslednji iz trenutnog bloka = prvi iz narednog bloka
                f.seek(-2*self.block_size, 1)
                self.write_block(f, block)

                block_idx += 1
                rec_idx = 0

        if next_block and next_block[0].get("id") == self.empty_key:  # ako smo vrsili pomeranje iz poslednjeg bloka, i ako je sada kod njega na prvom mestu prazan slog - mozemo osloboditi memoriju
            os.ftruncate(os.open(self.filename, os.O_RDWR),
                         block_idx * self.block_size)
