import csv
import scipy.stats as sps
import math

def f(a, b):

    return a * b

b = [1, 2, 3]
a = list(map(f(2, b), b))
print(a)