
"""
ECE 590
Project 1
Fall 2022

Partner 1: Xu (Jordan) Han, netID:xh123
Partner 2: Can Pei, netID:cp357
Date: Nov 13 2022
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    n = len(listToSort)
    # outer loop: iterate the index(i) separating the sorted and unsorted elements
    for i in range(0,n):
        # inner loop: SELECT the minimal element in the rest unsorted elements
        idx_min = i
        for j in range(i+1,n):
            if (listToSort[j] < listToSort[idx_min]):
                idx_min = j
        # place the minimal element at i
        listToSort[i], listToSort[idx_min] = listToSort[idx_min], listToSort[i]
    return

"""
InsertionSort
"""
def InsertionSort(listToSort):
    n = len(listToSort)
    # outer loop: find the element(k) that needs to be inserted
    for k in range(1,n):
        # inner loop: iterate backward from k-1 to 0(inclusive),
        # find the right place to insert k
        idx_insert = k
        for i in range(k-1,-1,-1):
            if(listToSort[i] > listToSort[k]):
                idx_insert-=1
            else:
                break
        # insert k to i
        val_insert = listToSort[k]
        listToSort[idx_insert + 1 : k + 1] = listToSort[idx_insert : k]
        listToSort[idx_insert] = val_insert
    return

"""
BubbleSort
"""
def BubbleSort(listToSort):
    n = len(listToSort)
    # If no swap occured during a inner loop, exit the outer loop
    swap_flag = True
    while (swap_flag):
        swap_flag = False
        # inner loop: if every two adjacent elements are out of order, swap them
        for i in range(0,n-1):
            if (listToSort[i] > listToSort[i+1]):
                listToSort[i], listToSort[i+1] = listToSort[i+1], listToSort[i]
                swap_flag = True
    return

"""
MergeSort
"""
def MergeSort(listToSort):
    n = len(listToSort)
    # base case
    if (n == 1):
        return listToSort
    elif (n == 2):
        if (listToSort[0] > listToSort[1]):
            listToSort[0],listToSort[1] = listToSort[1],listToSort[0]
            return listToSort
    # recursion: divide and conquer
    else:
        mid = n // 2
        sub_listA = MergeSort(listToSort[0:mid])
        sub_listB = MergeSort(listToSort[mid:n])
        # merge the two sublists
        for i in range(0,n):
            if (len(sub_listA) == 0):
                listToSort[i:n] = sub_listB
                break
            elif (len(sub_listB) == 0):
                listToSort[i:n] = sub_listA
                break
            elif (sub_listA[0] < sub_listB[0]):
                listToSort[i] = sub_listA.pop(0)
            else:
                listToSort[i] = sub_listB.pop(0)
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    # base case
    if (j - i <= 1): return
    # choose the pivot randomly, and place it at the beginning
    p = random.randrange(i,j)
    listToSort[p], listToSort[i] = listToSort[i], listToSort[p]
    pivot = listToSort[i]
    # two pointer, le & ri, iterate from two ends towards each other until they meet
    le = i
    ri = j-1
    while (le < ri):
        # ri points to the last element smaller than pivot
        while (le < ri and listToSort[ri] >= pivot): ri -= 1
        # le points to the first element larger than pivot
        while (le < ri and listToSort[le] <= pivot): le += 1
        # if they haven't met, swap these two elements
        if (le!=ri): listToSort[le], listToSort[ri] = listToSort[ri], listToSort[le]
    # at this moment, le & ri point to the same place
    # swap this element with the pivot
    listToSort[i], listToSort[le] = listToSort[le], listToSort[i]
    # divide and conquer: quicksort the subsequences on either side of the pivot 
    QuickSort(listToSort,i,ri)
    QuickSort(listToSort,ri+1,j)
    return

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
