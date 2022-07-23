import math
import os
import random
import re
import sys
# Complete the 'insertionSort1' function below.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
def insertionSort1(n, arr):
    # Write your code here
    lst = arr[n-1]
    N = n-2
    while(N >= 0 and lst <= arr[N]):
        arr[N+1] = arr[N]
        st = str(arr)[1:-1].replace(',', '')
        print(st)
        N -= 1
    arr[N+1] = lst
    st = str(arr)[1:-1].replace(',', '')
    print(st)     
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)