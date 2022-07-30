from randomMatrix import randomMatrix
from sigmoid import sigmoid
from multiply import multiply

class ShallowNeuralNetwork:

    """
    A class used to represent a simple feedforward neural network with one hidden layer.

    Detailed Explenation:
    ---------------------
    This is a code for a simple feedforward network with one hidden layer. It is a modification of the network found in the book
    "Make your own neural network", by T. Rashid. It works as following:
    To set up the network one specifies the number of input, hidden and output neurons and a learnig rate lr>0. Every neuron in
    one layer is connect to all the neurons in the next layer by a weight. Upon initialization the weights are (pseudo) randomly
    chosen between -0.5 and 0.5 by the random function.
    A neuron receives the weighted sum of all the neurons in the previous layer and applies the sigmoid function as the activation
    function. In this network we don't add a bias (constant) to the weighted sum. We also apply the sigmoid function to the output
    layer, i.e., the outputs are numbers between 0 and 1 and hence this network is suitable for classification problems.
    For updating the weights we use gradient descent. For the error function we use 0.5(t_n - o_n)² the square loss function, where
    t_n stands for the target output and o_n for the computed output. We determine how much a change in the weights from the hidden
    layer to the output layer changes the total error (sum), by computing the gradient of the total error with respect to that
    weight. Using that the derivative of the sigmoid function s is given by s' = s(1-s) we get a nice expression for the gradient.
    We use this gradient to update the weights between the hidden and output layer.
    To update the weights between the input and hidden layer, we first assign to every hidden neuron a proportion of the error from
    the output layer and then we proceed in the same way. For the hidden error we could add all the weights of an output neuron
    together and calculate how big is the percentage of each weight with respect to the total weight and add that percentage of the
    error to the hidden neuron. However, this might computationally be too costly and therefore we just multiply the output error
    with the weight to get the hidden error. This computation still reflects the strength of the weights.
    Now we update the weights by subracting the gradient times the learning rate.

    Attributes:
    -----------
    wih: float matrix
        This is a matrix (list in list) containing the neural network weights (float numbers) between the input and hidden layer.
        The rows represent the hiddennodes and the columns the inputnodes.
    who: float matrix
        This is a matrix (list in list) containing the neural network weights (float numbers) between the hidden and output layer.
        The rows represent the outputnodes and the columns the hiddennodes.
    lr: float
        This is the learning rate of the network it is a positive number.

    Methods:
    --------

    __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        Constructs all the necessary attributes for the neural network object.

    train(self, inputs_list, target_list):
        Train the neural network on given learning examples.

    get_output(self, inputs_list):
        Apply the network to a given example and get the result.

    """

    # initial settings for the network, it has the following inputs
    # number of input, hidden, and output nodes and learningrate
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):

        """
        Constructs all the necessary attributes for the neural network object.

        Parameters:
        -----------
        inputnodes: int positive
            This stands for the number of input nodes in our network.
        hiddennodes: int positive
            This stands for the number of hidden nodes in our network.
        outputnodes: int positive
            This stands for the number of output nodes in our network.
        learningrate: float >0
            This stands for the learning rate in our network.
        """

        try: #try-except errors
            if (isinstance(inputnodes, int) == 0) or (inputnodes < 1):
                raise ValueError('ValueError: ShallowNeuralNetwork() needs a positive integer number as number of inputnodes')
            elif (isinstance(hiddennodes, int) == 0) or (hiddennodes < 1):
                raise ValueError('ValueError: ShallowNeuralNetwork() needs a positive integer number as number of hiddennodes')
            elif (isinstance(outputnodes, int) == 0) or (outputnodes < 1):
                raise ValueError('ValueError: ShallowNeuralNetwork() needs a positive integer number as number of outputnodes')
            elif (isinstance(learningrate, (int, float)) == 0) or (learningrate <= 0):
                raise ValueError('ValueError: ShallowNeuralNetwork() needs a positive number as learning rate')


            # create random sets of weights
            # wih: weights from input to hidden layer
            self.wih = randomMatrix(hiddennodes, inputnodes)
            # who: weights from hidden to output layer
            self.who = randomMatrix(outputnodes, hiddennodes)

            # set learning rate
            self.lr = learningrate

        except ValueError as ve: #this is executed for all ValueErrors in the try block above
            print(ve) #we print the same message as raised in the ValueError above
            exit()
        except:
            print('Error: ShallowNeuralNetwork() raised an unexpected error') #we print this for all other errors above
            exit()


        pass



    # train the network
    # training needs inputs and the desired targets
    def train(self, inputs_list, target_list):

        """
        Training the network.

        This function trains the network using labeled examples, i.e.,
        the network weights get updated.

        Parameters:
        -----------
        input_list: float list
            This list represents one input for our network where each
            number stands for a feature of the input.
        target_list: float list
            This list contains the desired output for the given input
            object.
        """

        try: #try-except errors
            if (isinstance(inputs_list, list) == 0) or (isinstance(target_list, list) == 0):
                raise ValueError('ValueError: ShallowNeuralNetwork.train() takes two lists as input')
            elif len(inputs_list) != len(self.wih[0]):
                raise ValueError('ValueError: ShallowNeuralNetwork.train(): the input data has to match the number of input nodes')
            elif len(target_list) != len(self.who):
                raise ValueError('ValueError: ShallowNeuralNetwork.train(): the target data has to match the number of output nodes')
            elif (all([isinstance(a, (int, float)) for a in inputs_list]) == 0):
                raise ValueError('ValueError: ShallowNeuralNetwork.train() the inputs_list needs to contain real numbers')
            elif (all([isinstance(a, (int, float)) for a in target_list]) == 0):
                raise ValueError('ValueError: ShallowNeuralNetwork.train() the target_list needs to contain real numbers')

            # calculate signals into hidden layer
            hidden_inputs = [sum(multiply(self.wih[i],inputs_list)) for i in range(len(self.wih))]
            # calculate the signals emerging from hidden layer
            hidden_outputs = [sigmoid(x) for x in hidden_inputs]

            # calculate signals into final output layer
            final_inputs = [sum(multiply(self.who[i],hidden_outputs)) for i in range(len(self.who))]
            # calculate the signals emerging from final output layer
            final_outputs = [sigmoid(x) for x in final_inputs]

            # calculate output error (target - actual output)
            output_errors = [target_list[i]-final_outputs[i] for i in range(len(target_list))]
            # hidden layer error
            whoT = [[row[i] for row in self.who] for i in range(len(self.who[0]))] #transpose weights
            hidden_errors = [sum(multiply(whoT[i],output_errors)) for i in range(len(whoT))]

            # update weights who
            negative_gradient_ho = [[multiply(multiply(output_errors, final_outputs),[1-final_outputs[i]
                                    for i in range(len(final_outputs))])[j]*hidden_outputs[k] for k in range(len(hidden_outputs))]
                                    for j in range(len(final_outputs))]
            self.who = [[self.who[i][j]+ self.lr * negative_gradient_ho[i][j] for j in range(len(self.who[0]))] for i in range(len(self.who))]

            # update weights wih
            negative_gradient_ih = [[multiply(multiply(hidden_errors, hidden_outputs),[1-hidden_outputs[i]
                                    for i in range(len(hidden_outputs))])[j]*inputs_list[k] for k in range(len(inputs_list))]
                                    for j in range(len(hidden_outputs))]
            self.wih = [[self.wih[i][j]+ self.lr * negative_gradient_ih[i][j] for j in range(len(self.wih[0]))] for i in range(len(self.wih))]


        except ValueError as ve: #this is executed for all ValueErrors in the try block above
            print(ve) #we print the same message as raised in the ValueError above
            exit()
        except:
            print('Error: SchallowNeuralNetwork.train() raised an unexpected error') #we print this for all other errors above
            exit()

        pass


    # use the neural network
    def get_output(self, inputs_list):

        """
        Get output from neural network.

        This function takes an example as an input and returns an output
        calculated by the current state of the network.

        Parameters:
        -----------
        input_list: float list
            Each number in the list stands for a feature of an input object.

        Returns:
        --------
        final_outputs: float list
            List containing the calculated output.
        """


        try: #try-except errors
            if (isinstance(inputs_list, list) == 0):
                raise ValueError('ValueError: ShallowNeuralNetwork.get_output() takes a list as input')
            elif len(inputs_list) != len(self.wih[0]):
                raise ValueError('ValueError: ShallowNeuralNetwork.get_output(): the input data has to match the number of input nodes')
            elif (all([isinstance(a, (int, float)) for a in inputs_list]) == 0):
                raise ValueError('ValueError: ShallowNeuralNetwork.get_output() the inputs_list needs to contain real numbers')



            #calculate signals into hidden layer
            hidden_inputs = [sum(multiply(self.wih[i],inputs_list)) for i in range(len(self.wih))]

            # calculate the signals emerging from hidden layer
            hidden_outputs = [sigmoid(x) for x in hidden_inputs]

            # calculate signals into final output layer
            final_inputs = [sum(multiply(self.who[i],hidden_outputs)) for i in range(len(self.who))]

            # calculate the signals emerging from final output layer
            final_outputs = [sigmoid(x) for x in final_inputs]

        except ValueError as ve: #this is executed for all ValueErrors in the try block above
            print(ve) #we print the same message as raised in the ValueError above
            exit()
        except:
            print('Error: SchallowNeuralNetwork.train() raised an unexpected error') #we print this for all other errors above
            exit()

        return final_outputs
