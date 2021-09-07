def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    # count = 0 
    # loop if number equals search count ++
    # return count else 0 
    count = [num for num in lst if num == search_term] 
    return len(count) 