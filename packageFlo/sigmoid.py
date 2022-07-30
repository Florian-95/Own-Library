from exp import exp

def sigmoid(number):

    """
    The sigmoid function.

    Returns the sigmoid function of a real number, sigmoid(x)= 1/(1+exp(-x)).

    Parameters:
    -----------
    number: int or float
        Number to take the sigmoid function of.

    Returns:
    --------
    float
        The value of the sigmoid function of number.
    """

    try: #try-except errors
        if isinstance(number, complex): #raise ValueError if provided number is complex
            raise ValueError('ValueError: sigmoid() only takes real numbers not complex')

        z = 1/(1+exp(-number))

    except TypeError: #this is executed for all TypeErrors in the try statement
        print('TypeError: sigmoid() expects number-type') #TypeError is probably raised because input is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: sigmoid() raised an unexpected error') #we print this for all other errors above
        exit()

    return z
