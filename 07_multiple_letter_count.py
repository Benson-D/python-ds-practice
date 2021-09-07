def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #create a dictionary
    # loop through phrase
    # dictionary[letter] = (dictionary.get(letter) or 0) + 1
    # return dictionary

    # get has a default method when looking for values 

    frequency_counter = {}
    for character in phrase: 
        frequency_counter[character] = frequency_counter.get(character, 0) + 1
    
    return frequency_counter

    
