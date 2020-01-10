from crypto import __version__
from crypto.cipher import Cipher
import random
import string
import sys


class cupid (Cipher):
    """
    This is the cupid module
    """

    # Order of the columns
    order = ""
    message = ""

    def print_short_description(self):
        print("cupid:\n\tCupid Cipher\n\tA column shifting cipher.\n")

    def print_long_description(self):
        print("Cupid Cipher:\n\t Long description coming soon")

    def run(self, args):
        if args.Action == 'info':
            return self.print_long_description()
        if not args.message:
            self.message = sys.stdin.read().strip()
        else:
            self.message = args.message
        if args.Action == 'encrypt':
            print(self.encrypt())
        elif args.Action == 'decrypt':
            self.order = args.order
            print(self.decrypt())
        #elif args.Action == 'break':
        #    for i in range(0, 26):
        #        self.shift = i
        #        print("n=%2d" % i, self.decrypt())
        else:
            print("unknown action: "+args.Action)

    def encrypt(self):
        cipher = ''
        num_columns = len(self.message)
        avail_nums = dict()
        c_order = []
        grid = {}

        c_order = list(range(num_columns))
        random.shuffle(c_order)

        cipher += '\n'

        # Make the grid
        for col in range(num_columns):
            col_list = []
            for row in range(num_columns):
                if col == row:
                    col_list.append(self.message[col].upper())
                else:
                    col_list.append(random.choice(string.ascii_uppercase))
            grid[c_order[col]] = col_list

        # Build the string
        for col in range(num_columns):
            cipher += '  '.join(grid[int(col)]) + '\n'

        c_order = [str(x) for x in c_order]
        cipher += '\n' + ' '.join(c_order) +'\n'
                    
        return cipher

    def decrypt(self):
        cipher = ''
        return cipher
