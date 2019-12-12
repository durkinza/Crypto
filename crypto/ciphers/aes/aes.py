# -*- coding: utf-8 -*-
from crypto import __version__
import sys
import base64
from crypto.cipher import Cipher
from hashlib import sha256
from copy import copy
from random import randint


class aes (Cipher):
    """
            This is the AES module

            Implementation largely based on the work by
            Brandon Sterne
            https://gist.github.com/raullenchai/2920069

            AES Standard references
            Avinash Kak from Purdue University
            https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf
    """

    # the number of rounds to run for a given key-size 128-bit = 10 rounds (including final round).
    num_rounds = {128: 10, 192: 12, 256: 14, 240: 14}
    key_blocks = {128: 4, 192: 6, 256: 8, 240: 8}
    key_size = 256
    key = ""
    iv = []

    block_size = 16
    block = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    message_loc = 0

    def unpad(self, s): return s[:-ord(s[len(s) - 1:])]

    sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]

    sboxInv = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]

    rcon = [
        0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39,
        0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
        0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
        0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
        0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
        0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b,
        0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
        0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
        0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
        0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
        0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
        0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
        0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63,
        0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd,
        0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb
    ]

    def __init__(self, parser):
        self.parser = parser

    def print_short_description(self):
        print("aes:\n\tAdvanced Encryption Standard\n\tA block cipher that relys on the difficulty of undoing bitwise XOR operations.\n")

    def print_long_description(self):
        print("Advanced Encryption Standard (AES)\n\tAES uses a block style encryption method.\n\tEach block goes through a 4 step encryption round.\n\t\t1) Sub Bytes: Each byte is replaced with it's corresponding value in a lookup table.\n\t\t2) Shift Rows: Each row is shifted by it's index. ie. Row 0 shifts 0. Row 1 shifts 1\n\t\t3) Mix Columns: Each column of the block is shifted\n\t\t4) Add Round Key: The key is XOR'd with the block.\n\n\tEach round is performed 9, 11, or 13 times on each block.")

    def run(self, args):
        if args.Action == 'info':
            self.a = 'i'
            return self.print_long_description()

        self.key = args.key
        # if args.key_size and args.key_size in ['128', '192', '256']:
        #	self.key_size = args.key_size

        if args.Action == 'encrypt':
            self.a = 'e'
            if not args.message:
                self.message = sys.stdin.read()
            else:
                self.message = args.message
            print(self.encrypt())

        elif args.Action == 'decrypt':
            self.a = 'd'
            if not args.message:
                self.message = sys.stdin.read()
            else:
                self.message = args.message

            print(self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def pad(self, s):
        if len(s) < self.block_size:
            padChar = self.block_size-len(s)
            while len(s) < self.block_size:
                s.append(padChar)
        return s

    # returns a copy of the word shifted n bytes (chars)
    # positive values for n shift bytes left, negative values shift right

    def rotate(self, word, n):
        return word[n:]+word[0:n]

    # takes 4-byte word and iteration number

    def keyScheduleCore(self, word, i):
        # rotate word 1 byte to the left
        word = self.rotate(word, 1)
        newWord = []
        # apply sbox substitution on all bytes of word
        for byte in word:
            newWord.append(self.sbox[byte])
        # XOR the output of the rcon[i] transformation with the first part of the word
        newWord[0] = newWord[0] ^ self.rcon[i]
        return newWord

    # expand 256 bit cipher key into 240 byte key from which
    # each round key is derived

    def expand_key(self, key):
        cipherKeySize = len(key)
        if cipherKeySize != 32:
            # if we aren't given a correct key length, default to a hash of the key
            cipherKeySize = 32
            key = sha256(key.encode()).digest()
        # container for expanded key
        expandedKey = []
        currentSize = 0
        rconIter = 1
        # temporary list to store 4 bytes at a time
        t = [0, 0, 0, 0]

        # copy the first 32 bytes of the cipher key to the expanded key
        for i in range(cipherKeySize):
            expandedKey.append(key[i])
        currentSize += cipherKeySize

        # generate the remaining bytes until we get a total key size
        # of 240 bytes
        while currentSize < 240:
            # assign previous 4 bytes to the temporary storage t
            for i in range(4):
                t[i] = expandedKey[(currentSize - 4) + i]

            # every 32 bytes apply the core schedule to t
            if currentSize % cipherKeySize == 0:
                t = self.keyScheduleCore(t, rconIter)
                rconIter += 1

            # since we're using a 256-bit key -> add an extra sbox transform
            if currentSize % cipherKeySize == 16:
                for i in range(4):
                    t[i] = self.sbox[t[i]]

            # XOR t with the 4-byte block [16,24,32] bytes before the end of the
            # current expanded key.  These 4 bytes become the next bytes in the
            # expanded key
            for i in range(4):
                expandedKey.append(
                    ((expandedKey[currentSize - cipherKeySize]) ^ (t[i])))
                currentSize += 1

        return expandedKey

    # do sbox transform on each of the values in the state table

    def sub_bytes(self, state):
        for i in range(len(state)):
            state[i] = self.sbox[state[i]]
        return state

    # do sub_bytes, but with the inverted table
    def inv_sub_bytes(self, state):
        for i in range(len(state)):
            state[i] = self.sboxInv[state[i]]
        return state

    def shift_rows(self, state):
        for i in range(4):
            state[i*4:i*4+4] = self.rotate(state[i*4:i*4+4], i)
        return state

    def inv_shift_rows(self, state):
        for i in range(4):
            state[i*4:i*4+4] = self.rotate(state[i*4:i*4+4], -i)
        return state

    # Galois Multiplication

    def galoisMult(self, a, b):
        p = 0
        hiBitSet = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256

    def mix_column(self, column):
        temp = copy(column)
        column[0] = self.galoisMult(temp[0], 2) ^ self.galoisMult(temp[3], 1) ^ \
            self.galoisMult(temp[2], 1) ^ self.galoisMult(temp[1], 3)
        column[1] = self.galoisMult(temp[1], 2) ^ self.galoisMult(temp[0], 1) ^ \
            self.galoisMult(temp[3], 1) ^ self.galoisMult(temp[2], 3)
        column[2] = self.galoisMult(temp[2], 2) ^ self.galoisMult(temp[1], 1) ^ \
            self.galoisMult(temp[0], 1) ^ self.galoisMult(temp[3], 3)
        column[3] = self.galoisMult(temp[3], 2) ^ self.galoisMult(temp[2], 1) ^ \
            self.galoisMult(temp[1], 1) ^ self.galoisMult(temp[0], 3)

    def inv_mix_column(self, column):
        temp = copy(column)
        column[0] = self.galoisMult(temp[0], 14) ^ self.galoisMult(temp[3], 9) ^ \
            self.galoisMult(temp[2], 13) ^ self.galoisMult(temp[1], 11)
        column[1] = self.galoisMult(temp[1], 14) ^ self.galoisMult(temp[0], 9) ^ \
            self.galoisMult(temp[3], 13) ^ self.galoisMult(temp[2], 11)
        column[2] = self.galoisMult(temp[2], 14) ^ self.galoisMult(temp[1], 9) ^ \
            self.galoisMult(temp[0], 13) ^ self.galoisMult(temp[3], 11)
        column[3] = self.galoisMult(temp[3], 14) ^ self.galoisMult(temp[2], 9) ^ \
            self.galoisMult(temp[1], 13) ^ self.galoisMult(temp[0], 11)

    def mix_columns(self, state):
        for i in range(4):
            column = []
            # create the column by taking the same item out of each "virtual" row
            for j in range(4):
                column.append(state[j*4+i])

            # apply mix_olumn on our virtual column
            self.mix_column(column)

            # transfer the new values back into the block
            for j in range(4):
                state[j*4+i] = column[j]
        # return state

    def inv_mix_columns(self):
        for i in range(4):
            column = []
            # create the column by taking the same item out of each "virtual" row
            for j in range(4):
                column.append(self.block[j*4+i])
            # apply inverted mix_column on the virtual column
            self.inv_mix_column(column)

            # transfer the new values back to the block
            for j in range(4):
                self.block[j*4+i] = column[j]

    # returns a 16-byte round key based on an expanded key and round number
    def create_round_key(self, expandedKey, n):
        return expandedKey[(n*16):(n*16+16)]

    def add_round_key(self, block, roundKey):
        for i in range(len(block)):
            block[i] = block[i] ^ roundKey[i]
        return block

    def get_block(self):
        end_loc = self.message_loc + self.block_size
        # get the next block from self.message
        section = self.message[self.message_loc:end_loc]

        # return true or false if the block was able to be grabbed
        if len(section) == 0:
            self.gotBlock = False
            return ""
        section = list(section)
        for i in range(len(section)):
            if not isinstance(section[i], int):
                section[i] = ord(section[i])

        if len(section) < self.block_size:
            section = self.pad(section)
        self.message_loc = end_loc
        self.gotBlock = True
        return section

    def encrypt_block(self, block, key):
        state = copy(block)
        exKey = self.expand_key(key)
        # aes main
        roundKey = self.create_round_key(exKey, 0)
        self.add_round_key(state, roundKey)
        self.shift_rows(state)
        self.sub_bytes(state)
        for i in range(self.num_rounds[self.key_size]-1):
            roundKey = self.create_round_key(exKey, i)
            # aes Round
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_column(state)
            self.add_round_key(state, roundKey)
            # end aes Round
        self.roundKey = self.create_round_key(
            exKey, self.num_rounds[self.key_size])
        self.sub_bytes(state)
        self.shift_rows(state)
        self.add_round_key(state, roundKey)
        # end aes Main
        return state

    def decrypt_block(self, block, key):
        state = copy(block)
        exKey = self.expand_key(key)
        # aes main
        roundKey = self.create_round_key(exKey, 0)
        self.add_round_key(state, roundKey)
        self.shift_rows(state)
        self.sub_bytes(state)
        for i in range(self.num_rounds[self.key_size]-1):
            roundKey = self.create_round_key(exKey, i)
            # aes Round
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_column(state)
            self.add_round_key(state, roundKey)
            # end aes Round
        self.roundKey = self.create_round_key(
            exKey, self.num_rounds[self.key_size])
        self.sub_bytes(state)
        self.shift_rows(state)
        self.add_round_key(state, roundKey)
        # end aes Main
        return state

    def encrypt(self):
        output = ''
        temp_block = []
        # Initialization Vector
        for i in range(self.block_size):
            self.iv.append(randint(0, 255))
        self.expand_key(self.key)
        for c in self.iv:
            output = output + chr(c)
        firstRound = True
        self.block = self.get_block()
        while self.gotBlock:
            if firstRound:
                blockKey = self.encrypt_block(self.iv, self.key)
                firstRound = False
            else:
                blockKey = self.encrypt_block(blockKey, self.key)

            temp_block = self.add_round_key(self.block, blockKey)

            for x in temp_block:
                output = output + chr(x)
            self.block = self.get_block()
        if len(output) % 16 == 0:
            output = output+16*chr(16)
        return base64.b64encode(output.encode()).decode()

    def decrypt(self):
        output = ""
        temp_block = []
        self.message = base64.b64decode(self.message.encode())
        self.message = self.message.decode()
        message_len = len(self.message)
        # initalization vector will be the first 16 bytes of the message
        self.iv = self.get_block()
        if not self.gotBlock:
            exit(1)
        self.expand_key(self.key)
        blockKey = self.iv
        firstRound = True
        self.block = self.get_block()
        while self.gotBlock:
            if firstRound:
                blockKey = self.decrypt_block(self.iv, self.key)
                firstRound = False
            else:
                blockKey = self.decrypt_block(blockKey, self.key)
            temp_block = self.add_round_key(self.block, blockKey)
            # unpad
            if self.message_loc >= message_len:
                temp_block = temp_block[0:-(temp_block[-1])]
            # add to output
            for x in temp_block:
                output = output + chr(x)
            self.block = self.get_block()
        # remove extra block of padding
        output = self.unpad(output)
        return output.strip()
