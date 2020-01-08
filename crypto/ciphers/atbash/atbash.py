from crypto import __version__
from crypto.cipher import Cipher
import sys
from math import gcd as bltin_gcd
from crypto.utils import coprime, egcd, modinv


class atbash (Cipher):
    """
    This is the affine module
    """
    a = 25  # first half of key (a,b)
    b = 25  # second half of key (a, b)
    message = ""  # message for encryption or decryption
    m = 26

    def print_short_description(self):
        print("atbash:\n\tAtbash Cipher\n\tCharacters are converted to their alphabetic opposite. A <--> Z, B <--> Y, etc.\n")

    def print_long_description(self):
        print("Atbash Cipher:\n\tCharacters are converted to their alphabetic opposites. A becomes Z, B becomes Y, etc.\n\tThe same effect can be made by using an Affine cipher with a and b set to 25")

    def run(self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = sys.stdin.read().strip()
            self.lowercase_message = str.lower(self.message)
        else:
            self.message = args.message
            self.lowercase_message = str.lower(self.message)
        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            print(self.decrypt())
        else:
            print("unknown action: " + args.Action)

    def encrypt(self):
        """
        Encrypt the message
        Ciphertext = ((a * char) + b) mod(m)
        """
        ciphertext = ''  # ciphertext string to be built and returned

        for char in self.message:  # checks every character in the plaintext
            if char == ' ':  # checks if the character is a space
                ciphertext = ciphertext + char
            elif char >= 'A' and char <= 'z':  # checks if the character is a letter
                if char.isupper():  # checks for uppercase letter
                    tmp = ord(char) - 65
                    if tmp in range(0, self.m):
                        ciphertext = ciphertext + \
                            chr(((self.a * tmp) + self.b) % self.m + 65)
                else:  # assumes lowercase letter
                    tmp = ord(char) - 97
                    if tmp in range(0, self.m):
                        ciphertext = ciphertext + \
                            chr(((self.a * tmp) + self.b) % self.m + 97)
            else:  # assumes non alphabetic character - adds punctuation with no encryption
                ciphertext = ciphertext + char

        return ciphertext

    def decrypt(self):
        """
        Decrypt the message
        Plaintext = (a^(-1) * (char - b) mod(m)
        """

        plaintext = ''  # plaintext string to be built and returned
        a_inverse = modinv(self.a, self.m)  # modular inverse of a

        for char in self.message:
            if char == ' ':
                plaintext = plaintext + char
            elif char >= 'A' and char <= 'z':
                if char.isupper():  # checks if the letter is uppercase
                    tmp = ord(char) - 65
                    if tmp in range(0, self.m):
                        plaintext = plaintext + \
                            chr((a_inverse * (tmp - self.b) % self.m + 65))
                else:  # assumes lowercase letter
                    tmp = ord(char) - 97
                    if tmp in range(0, self.m):
                        plaintext = plaintext + \
                            chr((a_inverse * (tmp - self.b) % self.m + 97))
            else:  # assumes non alphabetic character - adds punctuation with no decryption
                plaintext = plaintext + char

        return plaintext
