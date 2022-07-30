from sqrt import sqrt
from ceil import ceil


def prime(number):
    """
    Tests if a number is prime.

    Parameters:
    -----------
    number: int >= 0
        Number to test

    Returns:
    --------
    boolean
        True if prime number, False if not.
    """

    try:

        if isinstance(number, int)==0:
            raise TypeError("TypeError: prime() only takes int inputs")
        elif number < 0:
            raise ValueError("ValueError: prime() only takes positive inputs")

        if number < 2: # 0,1 are not prime numbers
            return False
        elif number == 2: # 2 is a prime number
            return True
        elif (number % 2) == 0: # even numbers bigger than 2 are not prime numbers
            return False

        for i in range(3,ceil(sqrt(number))+1,2): # we test for uneven divisors up to the square root of the input number
            if (number % i) == 0:
                return False

    except TypeError as te: #this is executed for all TypeErrors in the try block above
        print(te)
        exit()
    except ValueError as ve: #this is executed for all ValueErrors in the try block above
        print(ve) #we print the same message as raised in the ValueError above
        exit()
    except:
        print('Error: prime() raised an unexpected error') #we print this for all other errors above
        exit()

    return True
