from crypto import __version__
from crypto.cipher import Cipher
import sys


class caesar (Cipher):
    """
    This is the caesar module
    """
    shift = 0
    message = ""

    def print_short_description(self):
        print("caesar:\n\tCaesar Cipher\n\tA basic rotation cipher.\n")

    def print_long_description(self):
        print("Caesar Cipher:\n\tGiven a rotation value x. Each character is replaced with the character that is x placed further down in the alphabet (continuing back to the start when we go past the end).\n\tEx. Rotate: 10\n\tHello -> Rovvy")

    def run(self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = sys.stdin.read().strip()
        else:
            self.message = args.message
        if args.Action == 'encrypt':
            self.shift = args.shift
            print(self.encrypt())
        elif args.Action == 'decrypt':
            self.shift = args.shift
            print(self.decrypt())
        elif args.Action == 'break':
            for i in range(0, 26):
                self.shift = i
                print("n=%2d" % i, self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def encrypt(self):
        cipher = ''
        for char in self.message:
            if char == ' ':
                cipher = cipher + char
            elif char.isupper():
                cipher = cipher + chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                cipher = cipher + chr((ord(char) + self.shift - 97) % 26 + 97)
            else:  # assumes non alphabetic character - adds punctuation with no encryption
                cipher = cipher + char
        return cipher

    def decrypt(self):
        cipher = ''
        for char in self.message:
            if char == ' ':
                cipher = cipher + char
            elif char.isupper():
                cipher = cipher + \
                    chr((ord(char) + (-self.shift) - 65) % 26 + 65)
            elif char.islower():
                cipher = cipher + \
                    chr((ord(char) + (-self.shift) - 97) % 26 + 97)
            else:  # assumes non alphabetic character - adds punctuation with no encryption
                cipher = cipher + char
        return cipher
