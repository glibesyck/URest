"""
Additional functions for work (transformation of data).

      ! converting
      ! sorting_tuples
      ! random_choice
      ! first_elements
"""

import random

def converting (dictionary : dict) -> list :
    '''
    Return the keys : values as list of tuples (keys, values).
    >>> converting ({'a' : 3, 'b' : 4, 'c' : 5})
    [('a', 3), ('b', 4), ('c', 5)]
    '''
    list_of_smth = [(keys, values) for keys, values in dictionary.items()]
    return list_of_smth

def sorting_tuples (list_of_tuples : list) -> list :
    '''
    Return the sorted list with values of tuples from maximum to minimum.
    >>> sorting_tuples ([('a', 3), ('b', 4), ('c', 2)])
    [('b', 4), ('a', 3), ('c', 2)]
    '''
    for bottom in range (len(list_of_tuples) - 1) :
        idx = bottom
        for itr in range (bottom+1, len(list_of_tuples)) :
            if list_of_tuples[itr][1] > list_of_tuples[idx][1] :
                idx = itr
        list_of_tuples[bottom], list_of_tuples[idx] = list_of_tuples[idx],\
             list_of_tuples[bottom]
    return list_of_tuples

def first_elements (list_of_tuples : list) -> list :
    '''
    Return 5 first elements of list or less if len of list is less than 5.
    >>> first_elements ([('a', 3), ('b', 4), ('c', 2)])
    ['a', 'b', 'c']
    '''
    new_list = []
    if len(list_of_tuples) < 5 :
        for elem in list_of_tuples :
            new_list.append(elem[0])
    else :
        for idx in range (5) :
            new_list.append(list_of_tuples[idx][0])
    return new_list

def random_choice (list_of_smth : list) -> list :
    '''
    Return 5 random elements from list.
    '''
    if len(list_of_smth) < 5 :
        return random.sample(list_of_smth, len(list_of_smth))
    else :
        return random.sample(list_of_smth, 5)
