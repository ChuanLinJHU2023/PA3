# This program reads all the records of test cases (each record is a triple n,m,time)
# and generate a graph to show the asymptotic behavior of our program
# The filename of input record and the filename of the output graph should be specified here:
filename_of_record = "test_for_timing_record.txt"
filename_of_graph = "test_time_record_graph"
# Execute the following instruction to generate the graph
# python record_drawing.py

import matplotlib.pyplot as plt
from data_reader import *
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def quadric_fit(list_n,list_time):
    # This function performs a quadratic regression for the x-value list (list_n) and y-value list (list_time)
    x_train=np.array(list_n).reshape(-1, 1)
    y_train=np.array(list_time).reshape(-1, 1)
    poly = PolynomialFeatures(degree=2)
    x_train_poly = poly.fit_transform(x_train)
    lr = LinearRegression()
    lr.fit(x_train_poly, y_train)
    y_train_predict = lr.predict(x_train_poly)
    list_n=x_train
    list_time_predicted = y_train_predict
    return list_n,list_time_predicted

record=reader_for_record(filename_of_record)
m=record[0][1]

list_n=[single_record[0] for single_record in record]
list_time=[single_record[2] for single_record in record]
plt.plot(list_n,list_time,label="code running time")

list_n,list_time_predicted =quadric_fit(list_n,list_time)
plt.plot(list_n,list_time_predicted,label="quadratic fit for all of n")

list_n,list_time_predicted =quadric_fit(list_n[10:60],list_time[10:60])
plt.plot(list_n,list_time_predicted,label="quadratic fit for n<=6000")

plt.xlabel("n")
plt.ylabel("running time (ms)")
plt.legend()
plt.title("n versus running time under m={0}".format(m))
plt.savefig(filename_of_graph,dpi=1500)
plt.show()
