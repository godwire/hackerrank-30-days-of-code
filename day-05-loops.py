#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    k = 0
    result = 0
    for k in range(1, 11):        
        result = n * k
        print(f'{n} x {k} = {result}')
        k = k + 1
