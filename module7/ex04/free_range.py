#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        # Create a list including both start and end
        arr = list(range(start, end + 1)) if start <= end else list(range(start, end - 1, -1))
        print(arr)
    except ValueError:
        print("none")
else:
    print("none")
