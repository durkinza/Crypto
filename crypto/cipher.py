# this is a base class for all cipher classes


class Cipher(object):
    """
    A template class for all ciphers.
    """

    def __init__(self, parser):
        self.parser = parser

    def run(self, args):
        print(args)

    def print_short_description(self):
        print("A short description not implemented yet")

    def print_long_description(self):
        print("A long description not implemented yet")

    def encrypt(self):
        print("cipher encrypt not implemented yet")
        pass

    def decrypt(self):
        print("cipher decrypt not implemented yet")
        pass
