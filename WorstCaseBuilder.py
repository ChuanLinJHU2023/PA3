import math
from tools import *

def WorstCaseBuilder_quickSort(n):
    return [i for i in range(n)]


dict_for_convert={}
def WorstCaseBuilder_quickSortM3(n):
    global dict_for_convert
    dict_for_convert = {}
    A = [i for i in range(n)]
    # print(A)
    quickSortM3_forBuild(A,0,None)
    # print(A)
    # print(dict_for_convert)
    A = [i for i in range(n)]
    for i in range(n):
        if A[i] in dict_for_convert:
            A[i]=dict_for_convert[A[i]]
    return A


def quickSortM3_forBuild(A, p=0, r=None):
    global dict_for_convert
    # The initial call to quicksort sets r to the last index.
    if r is None:
        r = len(A) - 1
    if p < r:
        # Partition around the pivot, which ends up in A[q].
        q = partitionM3_forBuild(A, p, r)
        quickSortM3_forBuild(A, p, q - 1)  # recursively sort the low side
        quickSortM3_forBuild(A, q + 1, r)  # recursively sort the high side


def partitionM3_forBuild(A, p, r):
    global dict_for_convert
    k = math.floor((p + r) / 2)
    middle = get_median_forBuild(A, p, k, r)
    A[r], A[middle] = A[middle], A[r]

    x = A[r]  # select the last element as the pivot

    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        if A[j] <= x:  # does this element belong on the low side?
            i += 1  # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]  # put this element there

    A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
    return i + 1  # return the new index of the pivot


def get_median_forBuild(A, p, k, r):
    global dict_for_convert
    former=A[k]
    later=append_1_at_tail(A[p])
    while later in A:
        later=append_1_at_tail(later)
    A[k]=later
    dict_for_convert[former]=later
    # print("convert {} into {}".format(former, later))
    return k


# print(WorstCaseBuilder_quickSortM3(5))
# The original array is A=[0, 1, 2, 3, 4]
# After conversion using dict {2: 0.1, 3: 4.1, 4: 4.11}
# The array is A= [0, 1, 0.1, 4.1, 4.1]

# print(WorstCaseBuilder_quickSortM3(10))
# The original array is A=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# After conversion using dict {4: 0.1, 5: 2.1, 2: 2.11, 7: 3.1, 8: 9.1, 9: 9.11}
# The array is  A= [0, 1, 2.11, 3, 0.1, 2.1, 6, 3.1, 9.1, 9.11]

