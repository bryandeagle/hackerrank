import math


def print_formatted(number):
    bits = int(math.log(number, 2))+2
    for x in range(1, number+1):
        print('{:d}'.format(x).rjust(bits-1, ' ') + \
              '{:o}'.format(x).rjust(bits, ' ') + \
              '{:X}'.format(x).rjust(bits, ' ') + \
              '{:b}'.format(x).rjust(bits, ' '))
