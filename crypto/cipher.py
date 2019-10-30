# this is a base class for all cipher classes


class Cipher(object):
    """
    A template class for all ciphers.
    """
    def __init__(self):
        pass

    def setup(self, args):
        print(args)

    def encrypt(self):
        print("cipher encrypt not implemented yet")
        pass

    def decrypt(self):
        print("cipher decrypt not implemented yet")
        pass
