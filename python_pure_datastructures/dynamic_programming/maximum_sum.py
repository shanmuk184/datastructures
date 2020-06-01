#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    '''

    :param arr:
    :return:
    [maxSubArr, maxSubSeq] maxSubSeq is maximum sum of non contiguous subsequences
    maxSubArr is maximum sum of contiguous subsequences

    '''
    n = len(arr)
    M = [0] * n
    allNegative = True
    for x in arr:
        if x >= 0:
            allNegative = False
    if arr[0] > 0 or allNegative:
        M[0] = arr[0]
        maxSum = arr[0]
    else:
        M[0] = 0
        maxSum = 0

    for i in range(1, n):
        if M[i - 1] + arr[i] > 0:
            M[i] = M[i - 1] + arr[i]
        elif allNegative:
            M[i] = arr[i]
        else:
            M[i] = 0
        if maxSum + arr[i] > maxSum:
            maxSum += arr[i]
        elif maxSum < arr[i]:
            maxSum = arr[i]
    # print(M)

    return [max(M), maxSum]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
