import math
count_for_quicksort, count_for_quicksortM3, count_for_partition, count_for_partitionM3=0, 0, 0, 0

def quicksort(A, p=0, r=None, isCount=False):
	# The initial call to quicksort sets r to the last index.
	if r is None:
		r = len(A) - 1
	if isCount:
		global count_for_quicksort
		count_for_quicksort+=1
	if p < r:
		# Partition around the pivot, which ends up in A[q].
		q = partition(A, p, r, isCount=isCount)
		quicksort(A, p, q-1, isCount=isCount)  # recursively sort the low side
		quicksort(A, q+1, r, isCount=isCount)  # recursively sort the high side


def partition(A, p, r, isCount=False):
	x = A[r]  # select the last element as the pivot

	i = p - 1  # highest index into the low side
	for j in range(p, r):  # process each element other than the pivot
		if isCount:
			global count_for_partition
			count_for_partition += 1
		if A[j] <= x:  # does this element belong on the low side?
			i += 1  # index of a new slot in the low side
			A[i], A[j] = A[j], A[i]  # put this element there

	A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
	return i + 1  # return the new index of the pivot


def quicksortM3(A, p=0, r=None, isPrint=False, isCount=False):
	# The initial call to quicksort sets r to the last index.
	if r is None:
		r = len(A) - 1
	if isCount:
		global count_for_quicksortM3
		count_for_quicksortM3 += 1
	if p < r:
		# Partition around the pivot, which ends up in A[q].
		if isPrint:
			k=math.floor((p+r)/2)
			information = "A[{}]={},A[{}]={},A[{}]={}".format(p,A[p],k,A[k],r,A[r])
			print(information)
		q = partitionM3(A, p, r)
		if isPrint:
			information="The partition element for A[{}:{}] is: {}".format(p,r,A[q])
			print(information)
			print(A)
			print("")

		quicksortM3(A, p, q-1, isPrint=isPrint)  # recursively sort the low side
		quicksortM3(A, q+1, r, isPrint=isPrint)  # recursively sort the high side


def partitionM3(A, p, r, isCount=False):
	k=math.floor((p+r)/2)
	middle=get_median(A,p,k,r)
	A[r],A[middle]=A[middle],A[r]

	x = A[r]  # select the last element as the pivot

	i = p - 1  # highest index into the low side
	for j in range(p, r):  # process each element other than the pivot
		if isCount:
			global count_for_partitionM3
			count_for_partitionM3+=1
		if A[j] <= x:  # does this element belong on the low side?
			i += 1  # index of a new slot in the low side
			A[i], A[j] = A[j], A[i]  # put this element there

	A[i + 1], A[r] = A[r], A[i + 1]  # the pivot does just to the right of the low side
	return i + 1  # return the new index of the pivot


def get_median(A,p,k,r):
	if A[k]<A[r]:
		if A[p]<A[k]:
			return k
		else:
			if A[r]<A[p]:
				return r
			else:
				return p
	else:
		if A[k]<A[p]:
			return k
		else:
			if A[r]<A[p]:
				return p
			else:
				return r


