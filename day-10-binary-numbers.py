#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    binary = bin(n)[2:]

    groups = binary.split('0')

    max_count = 0

    for group in groups:
        if len(group) > max_count:
            max_count = len(group)

    print(max_count)
