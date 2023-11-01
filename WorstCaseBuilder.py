# WorstCaseBuilder.py provides the method to build the worst case for quicksort and the worst case for quicksort
# using median of three partition

import math
from tools import *

def WorstCaseBuilder_quickSort(n):
    # Given a number n, this function provides an example of the worst case for quicksort. This example has size n.
    # For example, WorstCaseBuilder_quickSort(5)=[0,1,2,3,4]
    # To build an example of the worst case for quicksort is relatively easy.
    # Any array that is already sorted is an example of this kind.
    return [i for i in range(n)]


dict_for_convert = {}
def WorstCaseBuilder_quickSortM3(n):
    # Given a number n, this function provides an example of the worst case for quicksort. This example has size n.
    # For example, WorstCaseBuilder_quickSort(10)=[0, 1, 2.11, 3, 0.1, 2.1, 6, 3.1, 9.1, 9.11]
    # To see the details of this example, please refer to WorstCaseBuilder_Example
    # To build an example of the worst case for quicksort using median of three is relatively hard.
    # The idea of simulation is applied for build an example of this kind.
    # Namely, we simulate running quicksort and revise the elements during the simulation.

    global dict_for_convert
    dict_for_convert = {}
    A = [i for i in range(n)]
    # print(A)
    quickSortM3_forBuild(A, 0, None)
    # print(A)
    # print(dict_for_convert)
    A = [i for i in range(n)]
    for i in range(n):
        if A[i] in dict_for_convert:
            A[i]=dict_for_convert[A[i]]
    return A


def quickSortM3_forBuild(A, p=0, r=None):
    # This function helps us to build an example of the worst case for quicksort using median of three.
    global dict_for_convert
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partitionM3_forBuild(A, p, r)
        quickSortM3_forBuild(A, p, q - 1)
        quickSortM3_forBuild(A, q + 1, r)


def partitionM3_forBuild(A, p, r):
    # This function helps us to build an example of the worst case for quicksort using median of three.
    global dict_for_convert
    k = math.floor((p + r) / 2)
    middle = get_median_forBuild(A, p, k, r)
    A[r], A[middle] = A[middle], A[r]
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def get_median_forBuild(A, p, k, r):
    # This function helps us to build an example of the worst case for quicksort using median of three.
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

