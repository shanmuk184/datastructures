from math import ceil, log2

class SegmentTree(object):
    def __init__(self, n):
        self.n = n
        self.height = int(ceil(log2(n)))
        self.max_length = 2*int(2 ** self.height) - 1
        self.st = [0]*self.max_length
        self.arr = [0]*n

    @staticmethod
    def get_mid(a, b):
        return a + (b - a) // 2

    def updateValueUtil(self, start, end, diff, i, si):
        if start < end:
            return
        self.st[si] = self.st[si]+diff
        if start != end:
            mid = self.get_mid(start, end)
            self.updateValueUtil(start, mid, diff, i, 2*si+1)
            self.updateValueUtil(start, mid, diff, i, 2 * si + 2)

    def updateValue(self, n,i, val ):
        if i< 0 or i> n:
            return
        diff = val - self.arr[i]
        self.arr[i] = val
        self.updateValueUtil(0,n-1, diff, i,0)

    def constructSegmentTreeUtil(self, arr, st, se, si):
        if si > self.max_length:
            return 0
        if st == se:

            self.st[si] = arr[st]
            return  arr[st]
        mid = self.get_mid(st, se)
        self.st[si] = self.constructSegmentTreeUtil(arr, st, mid, 2*si+1)+\
                      self.constructSegmentTreeUtil(arr, mid, se, 2*si+2)
        return self.st[si]

    def get_sum_util(self, ss, se, qs, qe, si):
        if (qs <= ss or qe >= se):
            return self.st[si]
        if (se < qs or ss > qe):
            return 0
        mid = self.get_mid(ss, se)
        return self.get_sum_util(ss,mid,qs,qe, 2*si+1)+\
               self.get_sum_util(mid,se, qs, qe, 2*si+2)


    def get_sum(self, st, n, qs, qe):
        if (qs < st or qe > n - 1 or qs > qe):
            print("Invalid Input", end="")
            return -1
        return self.get_sum_util(st, n, qs, qe, 0)

    def construct(self, arr):
        self.arr = arr
        self.constructSegmentTreeUtil(arr, 0, self.n -1, 0)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
    seg = SegmentTree(n)

    # Build segment tree from given array
    seg.construct(arr)
    # Print sum of values in array from index 1 to 3
    print("Sum of values in given range = ",
          seg.get_sum(0, n, 1, 3))

    # Update: set arr[1] = 10 and update
    # corresponding segment tree nodes
    seg.updateValue(n, 1, 10)

    # Find sum after the value is updated
    print("Updated sum of values in given range = ",
          seg.get_sum(0, n, 1, 3), end="")
