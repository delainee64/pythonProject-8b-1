# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/27/2023
# Description: Use the time module to write a decorator function named sort_timer that times
# how many seconds it takes the decorated function to run. Since sort functions
# don't need to return anything, have the decorator's wrapper function return
# that elapsed time.

import random
import time
from matplotlib import pyplot


def bubble_count(num_list):
    """Bubble counts and returns the number of comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for index in range(len(num_list)):
        for pass_num in range(index + 1, len(num_list)):
            comparisons += 1
            if num_list[index] > num_list[pass_num]:
                temp = num_list[index]
                num_list[index] = num_list[pass_num]
                num_list[pass_num] = temp
                exchanges += 1
    return comparisons, exchanges


def insertion_count(num_list):
    """Counts by insertion and returns the number of comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for index in range(1, len(num_list)):
        num = num_list[index]
        pos = index - 1
        while pos >= 0:
            comparisons += 1
            if num < num_list[pos]:
                exchanges += 1
                num_list[pos + 1] = num_list[pos]
                pos -= 1
            else:
                break


def sort_timer(func):
    """Function times how many seconds it takes the decorated function to run."""

    def sort_deco(numbers):
        """Decorator function that takes in the list of numbers."""
        start = time.perf_counter()
        func(numbers)
        end = time.perf_counter()
        return end - start

    return sort_deco


def compare_sorts(deco1_bubble, deco2_insert):
    """Function to compare times between bubble sort and insertion sort."""
    x_vals = []
    y_vals_dec1 = []
    y_vals_dec2 = []
    for size in range(1000, 10001, 1000):
        numbers = [random.randint(1, 10000) for val in range(size)]
        copy = list(numbers)
        time_dec1 = deco1_bubble(numbers)
        time_dec2 = deco2_insert(copy)
        x_vals.append(size)
        y_vals_dec1.append(time_dec1)
        y_vals_dec2.append(time_dec2)

    pyplot.plot(x_vals, y_vals_dec1, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(x_vals, y_vals_dec2, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("the x label")
    pyplot.ylabel("the y label")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(sort_timer(bubble_count), sort_timer(insertion_count))
