# This is a file for all the data readers
# including reader_for_record and reader_for_dataset

def reader_for_record(record_filename):
    # This function reads the record of test cases for the asymptotical behavior of program
    # Each record is a triple (n,m,t). It costs the program t time to find the m shortest distances among n points
    with open(record_filename, mode="r") as file_of_record:
        lines = file_of_record.readlines()
        for index_of_line in range(len(lines)):
            line=lines[index_of_line]
            lines[index_of_line]=eval(line)
        return lines

def reader_for_dataset(dataset_filename, index_of_line):
    # This  function reads the line index_of_line in file ataset_filename
    # and generate the corresponding point list for a test case
    with open(dataset_filename, mode="r") as file_of_dataset:
        lines = file_of_dataset.readlines()
        test_case=eval(lines[index_of_line])
        return test_case


