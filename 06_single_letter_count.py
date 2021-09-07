def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # count = 0
    # word of lower 
    # loop through the word 
    # if letter startWith(letter) count = count + 1
    # return count


    #lower the word  
    # create a comprehension 
    # variable of counts = 0 
    # for letter in word if l == letter count = count + 1
    # strings have a built 

    count = [character for character in word.lower() if character == letter]
    return len(count)