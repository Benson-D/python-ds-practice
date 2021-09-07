def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #new string to capture the mutation
    #loop through old string 
        #if char.lower() == to_swap.lower()
            #new_string += char.swapcase()
        # new_string += char
    # return the new_string

    swapped_chars = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            swapped_chars += char.swapcase()
        else:
            swapped_chars += char
    return swapped_chars
    