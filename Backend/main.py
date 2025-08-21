from eel import init, expose, start # Python eel library to create GUI

import algorithms as algo # algorithms.py file to get all the sorted algorithms
import numpy as np
import time

init('Frontend') # Initialize the eel functionality to generate the GUI

@expose() # Makes the function accessible through the javascript frontend
def array_generator(val, select):
    '''
    Function generates a random numpy array or arrays with variable lengths acccording to the 'select' boolean supplied.
    These are further converted to lists to simplify the usability in javascript.
    '''
    if not select:
        return np.random.randint(0, 100000, val).tolist()
    return [np.random.randint(0, 100000, (val // i)).tolist() for i in range(1, 11)][::-1]

@expose()
def sorting_algorithm(numbers, array, multiple):
    '''
    Sorting_algorithm function manages all the sorting algorithms in the algorithms file. This function passes the sorting algorithm to the
    next function to calculate the time and returns the required data through a variable 'return_array' and sorted array.
    Params =>   numbers: represent the numbers associated with algos dictionary.
                array: takes in one or multiple unsorted arrays to sort
                multiple: Boolean variable | '0' -> Multiple Functions comparison | '1' -> Single function comparison
    '''
    # Library which stores the sorting algorithm function
    algos = {
        1: algo.bubble_sort,
        2: algo.selection_sort,
        3: algo.insertion_sort,
        4: algo.merge_sort,
        5: algo.heap_sort,
        6: algo.basic_quick_sort,
        7: algo.quick_sort_three_medians
    }

    return_array = []
    if multiple:
        for number in numbers:
            unsorted_array = array[:]
            process_time, sorted_array = time_algo(algos[number], unsorted_array)
            return_array.append((process_time, len(array), number, algos[number]))
    else:
        for arr in array:
            process_time, sorted_array = time_algo(algos[numbers], arr)
            return_array.append(((len(arr)), process_time))

    return return_array, sorted_array

def time_algo(func, unsorted_array):
    '''
    Function uses time library to simply calculate the elapsed time between the execution of the sorting function.
    This function also makes sure the sorted array returned by the sorting algorithm is correctly sorted.
    Returns -1 is the array is not sorted.
    '''
    start = time.time()
    array = func(unsorted_array[:])
    end = time.time()

    if array == sorted(unsorted_array[:]):
        number = (end - start)
        return round(number=number, ndigits=5), array
    else:
        return -1

start('index.html') # Starts the GUI