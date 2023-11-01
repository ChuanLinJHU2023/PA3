# main.py implements the quicksort and quicksort using median of the three partition. This program is the core of
# other programs.


from WorstCaseBuilder import *

count_for_quicksort, count_for_quicksortM3 = 0, 0
count_for_partition, count_for_partitionM3 = 0, 0
count_for_partition_comparison, count_for_partitionM3_comparison = 0, 0


def quicksort(A, p=0, r=None, isPrint=False, isCount=False):
    # This function implements quicksort
    if isCount:
        global count_for_quicksort
        count_for_quicksort += 1
    if r is None:
        r = len(A) - 1
    if p < r:
        if isPrint:
            information = "A[r]={}".format(A[r])
            print(information)
        q = partition(A, p, r, isPrint=isPrint, isCount=isCount)
        if isPrint:
            information = "The partition element for A[{}:{}] is: {}".format(p, r, A[q])
            print(information)
            print(A)
            print("")
        quicksort(A, p, q - 1, isPrint=isPrint, isCount=isCount)
        quicksort(A, q + 1, r, isPrint=isPrint, isCount=isCount)


def partition(A, p, r, isPrint=False, isCount=False):
    # This function implements the partition for quicksort
    if isCount:
        global count_for_partition
        count_for_partition += 1
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if isCount:
            global count_for_partition_comparison
            count_for_partition_comparison += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksortM3(A, p=0, r=None, isPrint=False, isCount=False):
    # This function implements quicksort using median of the three partition
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
        q = partitionM3(A, p, r, isCount=isCount)
        if isPrint:
            information = "The partition element for A[{}:{}] is: {}".format(p, r, A[q])
            print(information)
            print(A)
            print("")
        quicksortM3(A, p, q - 1, isPrint=isPrint, isCount=isCount)
        quicksortM3(A, q + 1, r, isPrint=isPrint, isCount=isCount)


def partitionM3(A, p, r, isPrint=False, isCount=False):
    # This function implements the partition for quicksort using median of the three partition
    if isCount:
        global count_for_partitionM3
        count_for_partitionM3 += 1
    k = math.floor((p + r) / 2)
    middle = get_median(A, p, k, r)
    A[r], A[middle] = A[middle], A[r]
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if isCount:
            global count_for_partitionM3_comparison
            count_for_partitionM3_comparison += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def get_median(A, p, k, r):
    # Given an Array A and three indexes p, k, r,
    # this function returns one of these three indexes.
    # The value at the position of this returned index should be the middle of A[p], A[r] and A[k]
    # For example, if A=[1,2,5,4,3], get_median(A,0,2,4)==4 because 3 is the median of 1,5,3
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
    # Given a number n, this function conducts a test run for quicksort
    # This test run is under the worstcase of n elements
    global count_for_quicksort, count_for_partition, count_for_partition_comparison
    count_for_quicksort, count_for_partition, count_for_partition_comparison = 0, 0, 0
    A = WorstCaseBuilder_quickSort(n)
    quicksort(A, 0, None, isCount=True)
    result = [n, count_for_partition, count_for_quicksort, count_for_partition_comparison, \
              n - 1, 2 * n - 1, n * (n - 1) / 2]
    print(result)


def get_TestRunForQuickSortM3(n):
    # Given a number n, this function conducts a test run for quicksort using median of three partition
    # This test run is under the worstcase of n elements
    global count_for_quicksortM3, count_for_partitionM3, count_for_partitionM3_comparison
    count_for_quicksortM3, count_for_partitionM3, count_for_partitionM3_comparison = 0, 0, 0
    A = WorstCaseBuilder_quickSortM3(n)
    quicksortM3(A, 0, None, isCount=True)
    result = [n, count_for_partitionM3, count_for_quicksortM3, count_for_partitionM3_comparison, \
              n / 2, n, n * n / 5]
    print(result)

# A= [0, 1, 2.11, 3, 0.1, 2.1, 6, 3.1, 9.1, 9.11]
# print("The input array is:")
# print(A)
# print("")
# quicksortM3(A, 0, None, isPrint=True)
