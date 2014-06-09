

# May 2013
# Kartikeya Menon


# Defining a simple comparison function for integers.
def compare_func(a, b):
    return a <= b

# A function for swapping the indices of a list.
def swap(the_list, i1, i2):

    temp = the_list[i1] # Storing one list element as a temporary variable.
    
    the_list[i1] = the_list[i2]
    the_list[i2] = temp
    
    
# Partition function.

def partition(the_list, p, r, compare_func):
    
    # Setting the pivot as the last item in the list.
    pivot = the_list[r]
    
    # Setting i and j
    i = p - 1
    j = p
    
    # While the index incremented over the sublist of elements smaller than the pivot.
    while j < r:
        
        # Condition 1: If j is bigger than the pivot, don't do anything.
        if compare_func(pivot, the_list[j]):
            j = j + 1
        
        # Condition 2: If j is less than the pivot, move i up, switch i and j and increment j.
        elif compare_func(the_list[j], pivot):
            i = i + 1
            swap(the_list, i, j)
            j = j + 1
    
    # Switch the pivot to the place where it's between the sublists containing > and <= elements to it.       
    swap(the_list, i + 1, r)
    
    q = i + 1
    # Return the location of the pivot.
    return q


def quicksort(the_list, p, r, compare_func):
    
    # If the first index of the list is less than the last index.
    # This effectively takes care of the base case; when p = r, the list has one item in it.
    # So nothing will happen if the list has one item in it, the list will stay the same.
    if p < r:
        
        # Get the value returned from the partition function as the position of the pivot, q.
        q = partition(the_list, p, r, compare_func)
        
        # Recurse on the two halves of the list before q and after q. 
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)
    

# Sorting entire list with quick sort.

def sort(the_list, compare_func):
    # Setting p and r to the following will sort the entire list.
    quicksort(the_list, 0, len(the_list) - 1, compare_func)

