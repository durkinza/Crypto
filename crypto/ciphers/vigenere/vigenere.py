from crypto import __version__
from crypto.cipher import Cipher
import sys

# largely based on work from
# https://stackoverflow.com/questions/41080325/vigen%C3%A8re-cipher-function-in-python


class vigenere (Cipher):
    """
    This is the caesar module
    """
    shift = 0
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = {}
    message = ""

    def print_short_description(self):
        print("vigenere:\n\tVigenère Cipher\n\tA series of caesar ciphers unique for each characters.\n")

    def print_long_description(self):
        print("Vigenère Cipher:\n\tThe Vigenère Cipher takes a string of characters as a key.\n\tEach character in the message is ran through a caesar, using the offset of the key as the shift number for that character.")

    def run(self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = sys.stdin.read().strip()
        else:
            self.message = args.message

        self.passphrase = args.passphrase
        if args.key:
            if len(args.key) != 26:
                raise Exception("Key must be 26 characters long")
            self.key = args.key

        self.key_to_table()

        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            print(self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def key_to_table(self):
        i = 0
        for letter in self.key:
            self.table[letter.lower()] = i
            i += 1

    def encrypt(self):
        encrypted = []
        starting_index = 0
        for letter in self.message:
            # if it's a space or non-alphabetical character, append and move on
            if not letter.lower() in self.table:
                encrypted.append(letter)
            elif letter.isalpha():
                c = (self.table[letter.lower()] +
                     self.table[self.passphrase[starting_index]] + 26) % 26
                if letter.islower():
                    encrypted.append(self.key[c].lower())
                else:
                    encrypted.append(self.key[c].upper())
            # if we've reached last index, reset to zero, otherwise + by 1
            if starting_index == (len(self.passphrase) - 1):
                starting_index = 0
            else:
                starting_index += 1

        return ''.join(encrypted)

    def decrypt(self):
        decrypted = []
        starting_index = 0
        for letter in self.message:
            # if it's a space or non-alphabetical character, append and move on
            if not letter.lower() in self.table:
                decrypted.append(letter)
            elif letter.isalpha():
                c = (self.table[letter.lower()] -
                     self.table[self.passphrase[starting_index]] + 26) % 26
                if letter.islower():
                    decrypted.append(self.key[c].lower())
                else:
                    decrypted.append(self.key[c].upper())

            # if we've reached last index, reset to zero, otherwise + by 1
            if starting_index == (len(self.passphrase) - 1):
                starting_index = 0
            else:
                starting_index += 1

        return ''.join(decrypted)
