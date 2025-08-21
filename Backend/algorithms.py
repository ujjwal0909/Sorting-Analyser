def bubble_sort(array):
    '''
    Sorts the array by comparing the element with its next element.
    Swaps if the next element is smaller
    Worst Case Time Complexity ==> O(n**2)
    Best Case Time Complexity ==> O(n)
    '''
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def merge_sort(array):
    '''
    Sorts the array using divide and merge technique
    Divides the array into single elements and merges the array by comparing elements
    Worst Case Time Complexity ==> O(nlog(n))
    Best Case Time Complexity ==> O(nlog(n))
    '''
    def merge(array1, array2):
        array3 = []
        while array1 and array2:
            if array1[0] > array2[0]:
                array3.append(array2[0])
                array2.remove(array2[0])
            else:
                array3.append(array1[0])
                array1.remove(array1[0])
        while array1:
            array3.append(array1[0])
            array1.remove(array1[0])
        while array2:
            array3.append(array2[0])
            array2.remove(array2[0])
        return array3

    if len(array) == 1:
        return array

    left = array[0: len(array)//2]
    right = array[len(array)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def insertion_sort(array):
    '''
    Sorts the array inplace by comparing with elements in the array
    Pushes each element to the next position if the previous element is smaller
    Worst Case Time Complexity ==> O(n**2)
    Best Case Time Complexity ==> O(n)
    '''
    for i in range(len(array)):
        element = array[i]
        j = i - 1
        while j >= 0 and element < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


def selection_sort(array):
    '''
    Sorts the array inplace by comparing with elements in the array
    Swaps elements by comparing the value
    Worst Case Time Complexity ==> O(n**2)
    Best Case Time Complexity ==> O(n)
    '''
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[min], array[i] = array[i], array[min]

    return array


def basic_quick_sort(array):
    '''
    Sorts the array using divide and merge algorithm
    Picks one element as a pivot and then sorts the array according to the value of the pivot
    Worst Case Time Complexity ==> O(n**2) 
    Best Case Time Complexity ==> O(nlog(n))
    '''
    def partition(arr, lo, hi):
        pivot = arr[-1]
        i = lo - 1

        for j in range(hi-1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
        return i + 1

    lo = 0
    hi = len(array)

    if lo < hi:
        pi = partition(array, lo, hi)

        array = basic_quick_sort(
            array[:pi]) + [array[pi]] + basic_quick_sort(array[pi+1:])

    return array


def quick_sort_three_medians(array):
    '''
    Sorts the array using divide and merge algorithm
    Sorts into three parts: Greater than pivot, equal to pivot and smaller than pivot
    Worst Case Time Complexity ==> O(n**2) 
    Best Case Time Complexity ==> O(nlog(n))
    '''
    def median_of_three(arr):

        sm = min(arr[0], arr[len(arr)//2], arr[-1])
        lg = max(arr[0], arr[len(arr)//2], arr[-1])
        mid = sum([arr[0], arr[len(arr)//2], arr[-1]]) - sm - lg
        arr[0], arr[len(arr)//2], arr[-1] = sm, lg, mid

        return arr

    def partition(arr):
        if not len(arr):
            return [], 0, 0, []

        pivot = arr.pop()
        gt = []
        st = []

        for element in arr:
            if element > pivot:
                gt.append(element)
            else:
                st.append(element)

        return st + [pivot] + gt, len(st), len(gt), pivot

    if len(array) == 2:
        sm = min(array)
        lg = max(array)
        array = [sm, lg]
        return array
    elif len(array) <= 1:
        return array
    else:
        array = median_of_three(array)
        array, ls, lg, pivot = partition(array)
        if array:
            array = quick_sort_three_medians(array[:ls]) + [pivot] + quick_sort_three_medians(array[ls+1:])

    return array

def heap_sort(array):
    '''
    Builds a max heap and sorts the algorithm by removing the root
    Worst Case Time Complexity ==> O(nlog(n))
    Best Case Time Complexity ==> O(nlog(n))

    Reference ==> 
    https://www.geeksforgeeks.org/heap-sort/
    '''
    def heapify(array, n, i):
        left = 2*i + 1
        right = 2*i + 2

        if left < n and array[i] < array[left]:
            max = left
        else:
            max = i

        if right < n and array[max] < array[right]:
            max = right

        if max != i:
            array[i], array[max] = array[max], array[i]
            heapify(array, n, max)

    for i in range((len(array) // 2), -1, -1):
        heapify(array, len(array), i)

    for i in range((len(array)-1), 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array