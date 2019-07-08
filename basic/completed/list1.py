#!/usr/bin/python -tt

# Completed!!!

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string match.
# Note: python does not have a ++ operator, but += works.



def match_ends(words): 
    long_words = []
    count = 0

    for word in words:
        if len(word) >= 2:
            long_words += [word]
    
    for word in long_words:
        if word[0] == word[-1]:
            count += 1
    
    return count 


        
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


# REMEMBER - DO NOT MODIFY THE LIST YOU ARE LOOPING OVER INSIDE THE LOOP
# IF YOU NEED TO MAKE A CHANGE MAKE A SHALLOW COPY OF THE LIST AND 
# MODIFY THAT 


def front_x(words):
    x_arr = []
    new_words = words[0:]
    
    for word in words: 
        if word[0] == 'x':
            x_arr += [new_words.pop(new_words.index(word))]
    
    new_words.sort()
    x_arr.sort()

    return x_arr + new_words



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.


# When using sorted, the function takes three arguments, one default and the 
# other two are optional. The default argument is the enumerable that you're iterating
# over (ex: list or tuple). One optional argument 'key', which detemines what you are 
# sorting by - in this case we wanted to sort by the last element in the tuple.

# This argument expects a function definition to a synthetic event in react.js .
# The key argument provides the first argument (enumerable) as an argument to that
# callback function (so it runs custom(tuples)), gets the result from that for each
# item in the array (the last element in each tuple) and sorts the list by that value.

# By default the sorted function sorts numbers and strings in ascending order 'a'<=>'b'
# and 1<=>2 . In order to sort in descending order provide the third optional argument
# 'reverse' and set it equal to True ( ex: sorted(tuples, key=custom, reverse=True) )


def sort_last(tuples):

    def custom(t):
        return t[-1]

    return sorted(tuples, key=custom)    



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
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
