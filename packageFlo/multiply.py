def multiply(x,y):

    """
    Componentwise multiplication of two number lists.

    This function returns a list containing real numbers. These numbers
    represent the elementwise multiplication of two given real numbers lists
    of the same length.

    Parameters:
    -----------
    x: list of length n containing int or float numbers
        First list for elementwise multiplication.
    y: list of length n containing int or float numbers
        Second list for elementwise multiplication.

    Returns:
    --------
    list of length n containing int or float numbers
        List containing the elementwise multiplication result.
    """

    try:
        if isinstance(x,list) == 0:
            raise ValueError('ValueError: multiply() expects 2 lists')
        elif isinstance(y,list) == 0:
            raise ValueError('ValueError: multiply() expects 2 lists')
        elif len(x) != len(y):
            raise ValueError('ValueError: multiply() the two lists are not of equal length')
        elif (all([(isinstance(a, float) or isinstance(a, int)) for a in x]) == 0):
            raise ValueError('ValueError: multiply() the lists need to contain real numbers')
        elif (all([(isinstance(a, float) or isinstance(a, int)) for a in y]) == 0):
            raise ValueError('ValueError: multiply() the lists need to contain real numbers')

        z = [a*b for a,b in zip(x,y)] #The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.


    except TypeError: #this is executed for all TypeErrors in the try statement
        print('TypeError: multiply() expects 2 lists containing numbers') #TypeError is probably raised because input is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: multiply() raised an unexpected error') #we print this for all other errors above
        exit()

    return z
