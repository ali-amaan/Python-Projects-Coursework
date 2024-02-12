# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955

MINIMUM = 20


def find_minrun(n):
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 


def insertion_sort(array, left, right):
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array


def merge(array, l, m, r):
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1    


def my_sort(lst):
    """Return the sequence `lst` sorted in-place in ascending order."""

    #​‌​‌‌​​​‌​‌​​​‌ Note: in-place means, that the method shouldn't create and return another
    #​‌​‌‌​​​‌​‌​​​‌ list, but sort the same list object it received, and return it. It is
    #​‌​‌‌​​​‌​‌​​​‌ allowed, however, to copy values to another list and use it to get the
    #​‌​‌‌​​​‌​‌​​​‌ given list sorted. Note that this will take extra memory.

    #​‌​‌‌​​​‌​‌​​​‌ The solution must be fast in order to complete the biggest sorting
    #​‌​‌‌​​​‌​‌​​​‌ problems in time before the time runs out and the evaluator
    #​‌​‌‌​​​‌​‌​​​‌ terminates the attempt.

    #​‌​‌‌​​​‌​‌​​​‌ If you are implementing a recursive mergesort, remember to
    #​‌​‌‌​​​‌​‌​​​‌ divide only up until a certain sublist size, eg. 20, and then sort
    #​‌​‌‌​​​‌​‌​​​‌ the sublist with another method, eg. selection sort. Dividing and
    #​‌​‌‌​​​‌​‌​​​‌ recursing up until sublists of size 1 is not effective!
    n = len(lst)
    if n == 0:
        return lst

    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(lst, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(lst, left, mid, right) 
  
        size = 2 * size 
    
    return lst

