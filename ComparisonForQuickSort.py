import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
filename_of_graph = "ComparisonForQuickSort_Output"

def reader_for_record(record_filename):
    with open(record_filename, mode="r") as file_of_record:
        lines = file_of_record.readlines()
        for index_of_line in range(len(lines)):
            line = lines[index_of_line]
            lines[index_of_line] = eval(line)
        return lines

record_filename="TestRunForQuickSort_Output"
records=reader_for_record(record_filename)
list_n=[single_record[0] for single_record in records][1:]
list_TotalNumberOfExecutionsOfPartition=[single_record[1] for single_record in records][1:]
list_TotalNumberOfExecutionsOfQuickSort=[single_record[2] for single_record in records][1:]
list_TotalNumberOfComparisonsWithinPartition=[single_record[3] for single_record in records][1:]
list_Expression1=[single_record[4] for single_record in records][1:]
list_Expression2=[single_record[5] for single_record in records][1:]
list_Expression3=[single_record[6] for single_record in records][1:]

# print(list_n)
print(list_TotalNumberOfExecutionsOfPartition)
plt.plot(list_n, list_TotalNumberOfExecutionsOfPartition, label="TotalNumberOfExecutionsOfPartition")

plt.xlabel("n")
plt.ylabel("TotalNumber")
plt.legend()
plt.title("n versus TotalNumber".format(m))
plt.savefig(filename_of_graph,dpi=1500)
plt.show()