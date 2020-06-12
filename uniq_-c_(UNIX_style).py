#!/usr/bin/python3

# Implement a function which behaves like the 'uniq -c' command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance together with the number of times a duplicate elements occurred in the original array.

# Example:

# ['a','a','b','b','c','a','b','c'] --> [('a',2),('b',2),('c',1),('a',1),('b',1),('c',1)]

def uniq_c(seq): 
    # initialize the first pair
    if(not seq):
        return([])
    el = prev = seq.pop(0)
    result = list()
    counter = 1
    while seq:
        el = seq.pop(0) # iterate over elements
        if (el == prev):
            counter+=1
        else:
            result += [(prev, counter)]
            counter = 1
            prev = el

    result += [(el, counter)]
    return (result)

print(uniq_c(['a','a','b','b','c','a','b','c']))
