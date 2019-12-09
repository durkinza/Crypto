from crypto import __version__
from crypto.cipher import Cipher
import sys
from math import gcd as bltin_gcd
from crypto.utils import coprime, egcd, modinv

class affine (Cipher):
    """
    This is the affine module
    """
    a = 0 # first half of key (a,b)
    b = 0 # second half of key (a, b)
    message = "" # message for encryption or decryption
    m = 26 # size of alphabet

    # if true, will format output nicely. if false, will just print ciphertext or plaintext
    nice_output = False 
	
    def print_short_description(self):
        print("affine:\n\tAffine Cipher\n\tConverts characters to numeric values, performs a mathematic operation on the values, and then converts the numbers back into characters.\n")

    def print_long_description(self):
        print("Affine Cipher:\n\tCharacters are converted to numeric values (a=0, ..., z=25).\n\tA mathematic operation (α*M + β) mod 26 = C  is perfomed using the given alpha (α) and beta (β).\n\t\tWhere M is the plaintext numeric value of the character and C is the encoded numeric value.\n\tFinally the encoded value is converted from a numeric value back into a character.")
    

    def run (self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = sys.stdin.read().strip()
            self.lowercase_message = str.lower(self.message)
        else:
            self.message = args.message
            self.lowercase_message = str.lower(self.message)
        if args.Action == 'encrypt':
            self.a = args.a
            if not coprime(self.a, self.m): # checks for if a is coprime to 26
                print("a = " + str(self.a) + " is not relatively prime to " + str(self.m))
                exit()
            self.b = args.b
            if self.nice_output: # checks for which output to use - if true, prints nicely
                print("\nAffine Encryption")
                print("---------------------")
                print("Given Plaintext: \t" + self.message)
                print("Encrypted Ciphertext: \t" + self.encrypt())
                print("---------------------")
            else: # otherwise, prints just plaintext or ciphertext to allow for piping
                print(self.encrypt())
        elif args.Action == 'decrypt':
            self.a = args.a
            if not coprime(self.a, self.m): # checks if a is coprime to 26
                print("a = " + str(self.a) + " is not relatively prime to " + str(self.m))
                exit()
            self.b = args.b
            if self.nice_output: # checks for which output to use - if true, prints nicely
                print("\nAffine Decryption")
                print("--------------------")
                print("Given Ciphertext: \t" + self.message)
                print("Decrypted Plaintext: \t" + self.decrypt())
                print("--------------------")
            else: # otherwise, prints just plaintext or ciphertext to allow for piping
                print(self.decrypt())
        else:
            print("unknown action: " + args.Action)

    def encrypt(self):
        """
        Encrypt the message
        Ciphertext = ((a * char) + b) mod(m)
        """
        ciphertext = '' # ciphertext string to be built and returned
        
        for char in self.message: # checks every character in the plaintext
            if char == ' ': # checks if the character is a space
                    ciphertext = ciphertext + char
            elif char >= 'A' and char <= 'z': # checks if the character is a letter
                if char.isupper(): # checks for uppercase letter
                    tmp = ord(char) - 65
                    if tmp in range(0, self.m):
                        ciphertext = ciphertext + chr(((self.a * tmp) + self.b) % self.m + 65)
                else: # assumes lowercase letter
                    tmp = ord(char) - 97
                    if tmp in range(0, self.m):
                        ciphertext = ciphertext + chr(((self.a * tmp) + self.b) % self.m + 97)
            else: # assumes non alphabetic character - adds punctuation with no encryption
                ciphertext = ciphertext + char
                
        return ciphertext

    def decrypt(self):
        """
        Decrypt the message
        Plaintext = (a^(-1) * (char - b) mod(m)
        """

        plaintext = '' # plaintext string to be built and returned
        a_inverse = modinv(self.a, self.m) # modular inverse of a
        
        for char in self.message:
            if char == ' ':
                plaintext = plaintext + char
            elif char >= 'A' and char <= 'z':
                if char.isupper(): # checks if the letter is uppercase
                    tmp = ord(char) - 65
                    if tmp in range(0, self.m):    
                        plaintext = plaintext + chr((a_inverse * (tmp - self.b) % self.m + 65))
                else: # assumes lowercase letter
                    tmp = ord(char) - 97
                    if tmp in range(0, self.m):
                        plaintext = plaintext + chr((a_inverse * (tmp - self.b) % self.m + 97))
            else: # assumes non alphabetic character - adds punctuation with no decryption
                plaintext = plaintext + char
                
        return plaintext
                            
        
