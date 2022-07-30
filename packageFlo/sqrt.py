def sqrt(number): #this function returns the square root of a non-negative number

    """
    Returns the square root of a number.

    This function uses Newton's algorithm to calculate the square root of a positive real number.

        Parameters:
        -----------
        number: int or float and number >= 0
            Number to take the square root of.

        Returns:
        --------
        float
            Square root of number.
    """

    try: #try-except errors

        if isinstance(number, complex): #raise ValueError if provided number is complex
            raise ValueError('ValueError: abs() only takes real numbers not complex')
        elif number < 0: #raise error if provided number is negative
            raise ValueError('ValueError: number provided to sqrt() is negative') #mention sqrt() function since except does not return a trace-back log, maybe add even file-name and line number?


        x_0 = 1 #starting value for Newton's algorithm
        x_1 = 1 #initialize next step

        n=100 #number of iterations


        for i in range(n): #Newton's algorithm
            x_1 = x_0 - ((x_0 * x_0 - number)/(2 * x_0))
            x_0 = x_1

    except TypeError: #this is executed for all TypeErrors in the try block above
        print('TypeError: sqrt() expects number-type') #TypeError is probably raised because number is not a number
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: sqrt() raised an unexpected error') #we print this for all other errors above
        exit()

    return x_0 #return square root of number
