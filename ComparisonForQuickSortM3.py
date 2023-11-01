import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('TkAgg')  # Under the new MacOS, we need this line to make sure that matplotlib works properly

filename_of_graph = "ComparisonForQuickSortM3_Output"


def reader_for_record(record_filename):
    with open(record_filename, mode="r") as file_of_record:
        lines = file_of_record.readlines()
        for index_of_line in range(len(lines)):
            line = lines[index_of_line]
            lines[index_of_line] = eval(line)
        return lines


record_filename = "TestRunForQuickSortM3_Output"
records = reader_for_record(record_filename)
list_n = [single_record[0] for single_record in records][1:]
list_TotalNumberOfExecutionsOfPartition = [single_record[1] for single_record in records][1:]
list_TotalNumberOfExecutionsOfQuickSort = [single_record[2] for single_record in records][1:]
list_TotalNumberOfComparisonsWithinPartition = [single_record[3] for single_record in records][1:]
list_Expression1 = [single_record[4] for single_record in records][1:]
list_Expression2 = [single_record[5] for single_record in records][1:]
list_Expression3 = [single_record[6] for single_record in records][1:]

print(list_n)
print(list_TotalNumberOfExecutionsOfPartition)
plt.plot(list_n, list_TotalNumberOfExecutionsOfPartition, "b", label="TotalNumberOfExecutionsOfPartition")
plt.plot(list_n, list_Expression1,"b--", label="n/2")
plt.plot(list_n, list_TotalNumberOfExecutionsOfQuickSort, "g", label="TotalNumberOfExecutionsOfQuickSort")
plt.plot(list_n, list_Expression2,"g--", label="n")
plt.plot(list_n, list_TotalNumberOfComparisonsWithinPartition, "r", label='TotalNumberOfComparisonsWithinPartition')
plt.plot(list_n, list_Expression3,"r--", label="n*n/5")

plt.xlabel("n")
plt.ylabel("count")
plt.legend()
plt.title("Asymptotical Behavior (n versus counts)")
plt.savefig(filename_of_graph)
# plt.savefig(filename_of_graph, dpi=1500)
plt.show()
