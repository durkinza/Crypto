from crypto import __version__
from crypto.cipher import Cipher

class rsa (Cipher):
    """
    This is the RSA module
    """

    def run (self):
        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            print(self.decrypt())
        else:
            print("unknown action: "+args.Action)
