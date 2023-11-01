# TraceRun2.py is the second trace run to show the correctness of quicksort using median of the three partition
from main import *
import random
Array=[random.randint(0,100) for i in range(20)]
print("The input array is:")
print(Array)
print("")
quicksortM3(Array,0,None,isPrint=True)