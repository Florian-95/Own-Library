def exp(number): #returns exponential funcion e^number

    """
    Exponential of the given number.

    Evaluates f(x) = e^x for inputs x in the interval [-709,709].
    Assertion error for other x because of over/underflow limit.
    Method uses Taylor approximation.
    Worst case needs 69413 operations.

    Parameters:
    -----------
    number: int or float
        Number to calculate exp(number).

    Returns:
    --------
    float
        Approximation of the euler number raised to number.
    """



    # Check that number is a valid input.
    assert(-709 <= number <= 709) #maybe use try except instead or as well? Catch assert exception?

    try:

        if isinstance(number, complex): #raise ValueError if provided number is complex
            raise ValueError('ValueError: exp() only takes real numbers not complex')

        e = 2.71828182845904523536028747135266249
        exp = pow(e,number) #pow is the build in power function pow(a,b) = a^b

    except TypeError: #this is executed for all TypeErrors in the try block above
        print('TypeError: exp() expects number-type') #TypeError is probably raised because number is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: exp() raised an unexpected error') #we print this for all other errors above
        exit()

    return(exp) #return e^number
