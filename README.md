# Building My Own Python Package From Scratch Using Only Pythons Standard Library

I'm a huge fan of learning by doing and this is why I did this project. In this project I wrote my own Python package using only Pythons standard library. Among other things this package contains a module for a simple artificial neural network. Doing this project I had two learning goals in mind. First, I wanted to get a better understanding of how Python libraries, packages, etc. are built. Often one just takes functions/classes from packages/frameworks like NumPy, Keras, TensorFlow etc. without knowing what has to be considered for such modules to be built. Second, I wanted to learn how packages work and what better way to do that then to write my own package, right?  
This is enough about my motivation. Let's see what's actually included in the package.


## The package

The package that I wrote is named packageFlo and it comes with a setup.py file, thus, the package can actually be installed. Furthermore the package contains the following modules:

- abs.py contains abs(): the absolute value
- ceil.py contains ceil(): returns the smallest integer bigger than the given number
- exp.py contains exp(): the exponential function
- multiply.py contains multiply(): componentwise multiplication of two lists
- prime.py contains prime(): checks if a number is prime
- randomMatrix.py contains randomMatrix(): generates a Matrix containing pseudo random numbers
- sigmoid.py contains sigmoid(): the sigmoid function
- snn.py contains the class ShallowNeuralNetwork: the neural network class
- sqrt.py contains sqrt(): the square root function

The square root function is implemented using Newton's algorithm and is used together with the ceil function in the prime module. I wrote those two modules just for fun ;)  
The abs, exp, multiply, randomMatrix and sigmoid functions on the other hand are necessary functions for the neural network module snn. The snn module contains a class ShallowNeuralNetwork which implements a feedforward neural network with one hidden layer and the sigmoid activation functioin. The idea for this network comes from Rashid Tariq's book ["Make Your Own Neural Network"](https://www.amazon.de/Make-Your-Own-Neural-Network/dp/1530826608). I basically implemented his [code](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork) but without using any libraries other than the standard library, instead I wrote my own functions.  
I wrote docstrings for each module, hence, you can use the help function to for a better documentation of what each module does.

## Examples and Tests

This folder contains some jupyter notebooks that I wrote to test my functions by "hand". Also I applied the network to hand written digit recognition following again [Rashid Tariq](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork). One can see that other than just being really slow the neural network is capable of recognizing hand written digits up to some degree.

## Final Words

This project is by no means meant to be useful of any sort other than to improve my personal understanding of Python and writing code. That's also why I didn't spend a lot of time to make this project as perfect as possible. I'm sure this project could have been done in a more efficient way. Furthermore, the documentation and remarks could be improved such that it would be better understandable for other people than me ^^ But as already mentioned this project is not really useful other than for my own educational purposes and hence I didn't want to waste a lot of time perfecting everything. Nonetheless, I hope this project can be used as an inspirational source for other people and their own projects.
