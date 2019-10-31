from crypto import __version__
from crypto.cipher import Cipher
class affine (Cipher):
    """
    This is the affine module
    """

    def run (self, args):
        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            print(self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def encrypt(self):
        """
        Do Encryption
        """
        pass

    def decrypt(self):
        """
        Do Decryption
        """
        pass
