from crypto import __version__
from crypto.cipher import Cipher
import base64
import sys


class b64 (Cipher):
    """
    This is the base64 module
    """
    message = b''

    def print_short_description(self):
        print("base64:\n\tBase64 Cipher (MIME)\n\tUsed to encoded binary into ascii safe text. Often recognized by the ending == or = which is used as padding.\n")

    def print_long_description(self):
        print("Base64:\n\tAlso refered to as MIME, Base64 is primarly used to encode binary values into ascii safe text.\n\tBinary values of characters (normally 8 bits) are split into 6 bit values.\n\t\tPadding is added to the end of the string using either = or == to maintain a size that is a factor of 8")

    def run(self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = str.encode(sys.stdin.read().strip())
        else:
            self.message = str.encode(args.message)
        if args.Action == 'encrypt':
            print(self.encrypt().decode())
        elif args.Action == 'decrypt':
            print(self.decrypt().decode())
        else:
            print("unknown action: "+args.Action)

    def encrypt(self):
        return base64.b64encode(self.message)

    def decrypt(self):
        out = b''
        padding = 0
        while(out == b'' and padding <= 2):
            try:
                out = base64.b64decode(self.message)
            except base64.binascii.Error:
                padding += 1
                self.message = self.message+b'='
        return out
