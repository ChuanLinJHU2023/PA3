from main import *
print(["n",  "TotalNumberOfExecutionsOfPartition", "TotalNumberOfExecutionsOfQuickSort", "TotalNumberOfComparisonsWithinPartition", \
       "n-1", "2n-1", "n(n - 1)/2" ])
for i in range(3,31):
    get_TestRunForQuickSort(i)