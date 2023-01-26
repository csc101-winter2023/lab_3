# Import the 'sys' library - you're going to need it for this lab!

# First, some basic functions to start us off.

# Write a function called 'adds_five' (list to list) that adds 5 to the end of
# a list.

# Write a function called 'adds_lst_five' (list to list) that adds [5] to the
# end of a list.

# REMEMBER: You need to do two of the next five with while loops, and two of
# them with for loops. The fifth one is up to you!

# Write a function called 'get_smallest' (list to int) that returns the 
# smallest integer value in the list, which contains only integers.

# Write a function called 'get_smallest_ind' (list to int) that returns the 
# index of the smallest integer value in the list, which contains only floats.

# Write a function called 'put_smallest_first' (list to list) that returns the
# list that is passed in but switching the first element of the list with the
# smallest element of the list (a call to 'get_smallest_ind' might help here).

# Write a function called 'selection_sort' (list to list) that calls 
# 'put_smallest_first' on ls[:], then calls 'put_smallest_first' on ls[1:], on
# and on until it calls 'put_smallest_first' on ls[-1:]. What is the result?

# Write a function called 'distances_from_origin' (list, list to list) that
# takes in an input list of x coordinates and an input list of y coordinates
# and returns a list of the distances of the point indicated by the x value in
# one list and the respective y value in the other. If one list is longer than
# the other, then you should ignore the remaining data points in that list.

# Write a function called 'zipper' (list, list, to list) that takes in two
# input lists and outputs the lists "zipped" together. For example, if the
# first argument is called x and the second y, then the output list should
# look like [x[0], y[0], x[1], y[1], x[2], y[2], ...]. If one list is longer
# Than the other, then you should add the end of that list onto the end of
# the output list (so your list might end like [...x[-3], x[-2], x[-1]] or
# [...y[-3], y[-2], y[-1]]).

# Write a function called 'rev_list' (list to list) that reverses the elements
# of the input list and returns them in an output list

# These next two functions need to be written with list comprehensions.

# Write a function called 'adds_five_all' (list to list) that adds 5 to every 
# element in a list using a list comprehension.

# Write a function called 'abs_val_all' (list to list) that returns a list of
# the absolute values of the input list. HINT: you are allowed to use either
# abs() or the function you built in Lab 2 to do this.

# Write at least three tests for every one of the functions you wrote above. 
# Be sure to think about edge cases, like an empty list, or a list with only
# one item.