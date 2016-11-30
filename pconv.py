#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import codecs
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 5):
        print('usage: python pconv.py <enc_from> <inputfile> <enc_to> <outputfile>')
        sys.exit(1)

    for arg in sys.argv:
        print(arg)

    output = codecs.open(sys.argv[4], 'w', sys.argv[3])

    for line in codecs.open(sys.argv[2], 'r', sys.argv[1]):
        try:
            output.write(line)
        except UnicodeEncodeError:
            print('UnicodeEncodeError')
            break

    output.close()
