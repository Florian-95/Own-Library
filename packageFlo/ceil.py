def ceil(number): #returns the smalles integer bigger equal than the numbers

    """
    Integer ceiling from above.

    Returns the smallest integer bigger or equal than the given real number.

    Parameters:
    -----------
    number: int or float
        Number to ceil.

    Returns:
    --------
    int
        Smallest integer bigger or equal than number.
    """

    try: #try-except errors
        if isinstance(number, complex): #raise ValueError if provided number is complex
            raise ValueError('ValueError: ceil() only takes real numbers not complex')

        ceil = int(number) #int has rounding towards zero behaviour

        if number - ceil > 0:
            ceil += 1

    except TypeError: #this is executed for all TypeErrors in the try statement
        print('TypeError: ceil() expects number-type') #TypeError is probably raised because input is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: ceil() raised an unexpected error') #we print this for all other errors above
        exit()

    return(ceil) #return ceil of number
