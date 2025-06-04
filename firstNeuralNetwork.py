import numpy as np

# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

inputNode = np.array([1,2,3,4,5])
def learningSlowly (inputNode ) :        
    # Node Initialization
    # inputNode = np.array([1, 2, 3, 4, 5])           # Shape: (5,)
    hiddenNode = np.array([5, 3, 4, 2, 1])          # Not used in forward pass
    outputNode = np.array([1, 4, 2, 5, 3])          # Target values (optional for training)

    # Weight Matrices
    w1 = np.random.random((5, 5))  # Shape: (input_dim, hidden_dim)
    w2 = np.random.random((5, 5))  # Shape: (hidden_dim, output_dim)

    # Forward Pass
    inputToHidden = np.dot(inputNode, w1)          # Shape: (5,)
    outputFromHidden = sigmoid(inputToHidden)      # Apply sigmoid

    inputToOutput = np.dot(outputFromHidden, w2)   # Shape: (5,)
    outputFromOutput = sigmoid(inputToOutput)      # Final prediction

    print (outputFromOutput)

    print ("if you wanna stop click 1")
    a = int (input ())
    if a != 1 : 
        learningSlowly (outputFromOutput)



learningSlowly (inputNode)
