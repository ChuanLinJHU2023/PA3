import math
from WorstCaseBuilder import *

count_for_quicksort, count_for_quicksortM3 = 0, 0
count_for_partition, count_for_partitionM3 = 0, 0
count_for_partition_comparison, count_for_partitionM3_comparison = 0, 0


def quicksort(A, p=0, r=None, isPrint=False, isCount=False):
    # The initial call to quicksort sets r to the last index.
    if isCount:
        global count_for_quicksort
        count_for_quicksort += 1
    if r is None:
        r = len(A) - 1
    if p < r:
        if isPrint:
            information = "A[r]={}".format(A[r])
            print(information)
        # Partition around the pivot, which ends up in A[q].
        q = partition(A, p, r, isPrint=isPrint, isCount=isCount)
        if isPrint:
            information = "The partition element for A[{}:{}] is: {}".format(p, r, A[q])
            print(information)
            print(A)
            print("")
        quicksort(A, p, q - 1, isPrint=isPrint, isCount=isCount)  # recursively sort the low side
        quicksort(A, q + 1, r, isPrint=isPrint, isCount=isCount)  # recursively sort the high side


def partition(A, p, r, isPrint=False, isCount=False):
    if isCount:
        global count_for_partition
        count_for_partition += 1
    x = A[r]  # select the last element as the pivot
    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        if isCount:
            global count_for_partition_comparison
            count_for_partition_comparison += 1
        if A[j] <= x:  # does this element belong on the low side?
            i += 1  # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]  # put this element there

    A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
    return i + 1  # return the new index of the pivot


def quicksortM3(A, p=0, r=None, isPrint=False, isCount=False):
    # The initial call to quicksort sets r to the last index.
    if isCount:
        global count_for_quicksortM3
        count_for_quicksortM3 += 1
    if r is None:
        r = len(A) - 1
    if p < r:
        if isPrint:
            k = math.floor((p + r) / 2)
            information = "A[{}]={},A[{}]={},A[{}]={}".format(p, A[p], k, A[k], r, A[r])
            print(information)
        # Partition around the pivot, which ends up in A[q].
        q = partitionM3(A, p, r)
        if isPrint:
            information = "The partition element for A[{}:{}] is: {}".format(p, r, A[q])
            print(information)
            print(A)
            print("")

        quicksortM3(A, p, q - 1, isPrint=isPrint)  # recursively sort the low side
        quicksortM3(A, q + 1, r, isPrint=isPrint)  # recursively sort the high side


def partitionM3(A, p, r, isCount=False):
    if isCount:
        global count_for_partitionM3
        count_for_partitionM3 += 1
    k = math.floor((p + r) / 2)
    middle = get_median(A, p, k, r)
    A[r], A[middle] = A[middle], A[r]

    x = A[r]  # select the last element as the pivot

    i = p - 1  # highest index into the low side
    for j in range(p, r):  # process each element other than the pivot
        if isCount:
            global count_for_partitionM3_comparison
            count_for_partitionM3_comparison += 1
        if A[j] <= x:  # does this element belong on the low side?
            i += 1  # index of a new slot in the low side
            A[i], A[j] = A[j], A[i]  # put this element there
    A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
    return i + 1  # return the new index of the pivot


def get_median(A, p, k, r):
    if A[k] <= A[r]:
        if A[p] <= A[k]:
            return k
        else:
            if A[r] <= A[p]:
                return r
            else:
                return p
    else:
        if A[k] <= A[p]:
            return k
        else:
            if A[r] <= A[p]:
                return p
            else:
                return r


def get_TestRunForQuickSort(n):
    global count_for_quicksort, count_for_partition, count_for_partition_comparison
    count_for_quicksort, count_for_partition, count_for_partition_comparison = 0, 0, 0
    A = WorstCaseBuilder_quickSort(n)
    quicksort(A, 0, None, isCount=True)
    result = [n, n * (n - 1) / 2, count_for_partition_comparison]
    print(result)


# A= [0, 1, 2.11, 3, 0.1, 2.1, 6, 3.1, 9.1, 9.11]
# print("The input array is:")
# print(A)
# print("")
# quicksortM3(A, 0, None, isPrint=True)