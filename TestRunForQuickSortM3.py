# TestRunForQuickSortM3.py is the test run to measure the asymptotic behavior of quicksort using median of the three partition
from main import *
print(["n",  "TotalNumberOfExecutionsOfPartition", "TotalNumberOfExecutionsOfQuickSort", "TotalNumberOfComparisonsWithinPartition", \
       "n/2", "n", "n*n/5" ])
for i in range(3,31):
    get_TestRunForQuickSortM3(i)