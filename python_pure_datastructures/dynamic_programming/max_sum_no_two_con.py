def max_sum_no_two_continuous(A):
    n = len(A)
    M = [0]*n
    M[0] = A[0]
    if A[1]>A[0]:
        M[1] = A[1]
    else:
        M[1] = A[0]
    for i in range(2, n):
        if M[i-2]+A[i] > M[i-1]:
            M[i] = M[i-2]+A[i]
        else:
            M[i]=M[i-1]
    print(M)
    return max(M)
print(max_sum_no_two_continuous([1,2,3,4,5]))