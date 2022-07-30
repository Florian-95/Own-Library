def abs(number): #this function returns the absolute value of a number

    """
    The absolute value of a number.

    This function returns the absolute value of a real number.

    Parameters:
    -----------
    number: int or float
        Number to take the absolute value of.

    Returns:
    --------
    int or float
        The absolute value of number.
    """

    absn = 0 #initialize absolute value number
    try: #try-except errors
        if isinstance(number, complex): #raise ValueError if provided number is complex
            raise ValueError('ValueError: abs() only takes real numbers not complex')

        if number < 0:
            absn = -number
        else:
            absn = number

    except TypeError: #this is executed for all TypeErrors in the try statement
        print('TypeError: abs() expects number-type') #TypeError is probably raised because input is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: abs() raised an unexpected error') #we print this for all other errors above
        exit()

    return(absn) #return absolute value
