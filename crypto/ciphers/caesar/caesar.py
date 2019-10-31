from crypto import __version__
from crypto.cipher import Cipher


class caesar (Cipher):
    """
    This is the caesar module
    """
    shift = 0
    message = ""

    def run(self, args):
        self.shift = args.shift
        self.message = args.message
        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            print(self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def encrypt(self):
        cipher = ''
        for char in self.message:
            if char == ' ':
                cipher = cipher + char
            elif  char.isupper():
                cipher = cipher + chr((ord(char) + self.shift - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + self.shift - 97) % 26 + 97)
        return cipher

    def decrypt(self):
        cipher = ''
        for char in self.message:
            if char == ' ':
                cipher = cipher + char
            elif  char.isupper():
                cipher = cipher + chr((ord(char) + (-self.shift) - 65) % 26 + 65)
            else:
                cipher = cipher + chr((ord(char) + (-self.shift) - 97) % 26 + 97)
        return cipher
