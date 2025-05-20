#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
    z_count = 0
    for char in string:
        if char == 'z':
            print('z', end='')
            z_count += 1
    if z_count > 0:
        print()
    else:
        print("none")
else:
    print("none")
