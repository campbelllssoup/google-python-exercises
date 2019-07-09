#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

# Pseudo-code
# ---------------------------------------------------------------
# first create an empty list to modify while inside the for loop
# then check if the number that you're currently iterating over
# is present inside of the solution array.
# if the number is present in the solution array, do not add it
# to the solution array, else add it to the solution array.
# ---------------------------------------------------------------



def remove_adjacent(nums):
    solution = []

    if nums:
        for num in nums:
            if solution.count(num) == 0:
                solution.append(num)
        return solution   
    else:
        return solution



# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

# Pseudo-code
# ---------------------------------------------------------------
# First create an empty list that will hold the solution for the
# problem. Copy the first list into this list.

# Then iterate over the second list and find the index of the 
# element that is less than this value inside of the solution list.

# When you have found this index, place the number that you are 
# iterating over currently into the next index position.

# The current solution doesn't go into depth of iterating through 
# both of the arrays and then merging them as it iterates through.
# Instead it makes use of the sorted function, which is a sort of
# shortcut to what this problem is asking for in my belief.

# ---------------------------------------------------------------

def linear_merge(list1, list2):
    solution = list1[0:] + list2[0:]

    return sorted(solution)
        


# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
