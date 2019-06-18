#!/usr/bin/python3
""" Author: Mathew McDade
    Date: 1/17/2019
    Class: CS325.400 Winter 2019
    Assignment: HW1: merge sort --timed
    Description: A simple Python implementation of 4-way-merge sort.
    Times the execution of the sort on arrays of random integers of increasing size and prints
        the results to the terminal.
"""
from timeit import timeit
from random import randint


# Define merge4
def merge4(array, start, first_quarter, midpoint, third_quarter, end):
    leftest_array = array[start:first_quarter + 1]  # separate the subarrays to be merged.
    left_array = array[first_quarter + 1:midpoint + 1]
    right_array = array[midpoint + 1:third_quarter + 1]
    rightest_array = array[third_quarter + 1:end + 1]
    leftest_array.append(float("inf"))
    left_array.append(float("inf"))
    right_array.append(float("inf"))
    rightest_array.append(float("inf"))

    i = j = l = m = 0
    for k in range(start, end + 1):  # merge the partial arrays to a combined, ordered array.
        if leftest_array[i] <= left_array[j] and leftest_array[i] <= right_array[l] and leftest_array[i] <= \
                rightest_array[m]:
            array[k] = leftest_array[i]
            i += 1
        elif left_array[j] <= right_array[l] and left_array[j] <= rightest_array[m]:
            array[k] = left_array[j]
            j += 1
        elif right_array[l] <= rightest_array[m]:
            array[k] = right_array[l]
            l += 1
        else:
            array[k] = rightest_array[m]
            m += 1


def mergesort4(array, start, end):
    if end - start > 0:
        midpoint = (start + end) // 2  # floor division --Python3
        fq = (start + midpoint) // 2
        tq = (midpoint + end) // 2
        mergesort4(array, start, fq)
        mergesort4(array, fq + 1, midpoint)
        mergesort4(array, midpoint + 1, tq)
        mergesort4(array, tq + 1, end)
        merge4(array, start, fq, midpoint, tq, end)


# MAIN
if __name__ == "__main__":
    for x in range(0, 1000001, 10000):
        rand_ints = []
        for y in range(x):
            rand_ints.append(randint(0, 10000))
        time = timeit(lambda: mergesort4(rand_ints.copy(), 0, len(rand_ints) - 1), number=10)
        print("n: %i  time: %f seconds" % (x, time))
