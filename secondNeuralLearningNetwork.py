import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)  # derivative assuming input x is sigmoid output

# Training Data (input: 5 features, output: 1 target)
X = np.array([
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Seed random for reproducibility
np.random.seed(42)

# Initialize weights randomly (5 input nodes -> 4 hidden nodes)
w1 = 2 * np.random.random((5, 4)) - 1
w2 = 2 * np.random.random((4, 1)) - 1

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # Forward pass
    hidden_input = np.dot(X, w1)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, w2)
    final_output = sigmoid(final_input)

    # Calculate error
    error = y - final_output

    # Backpropagation
    d_final_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = d_final_output.dot(w2.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_output)

    # Update weights
    w2 += hidden_output.T.dot(d_final_output) * learning_rate
    w1 += X.T.dot(d_hidden_output) * learning_rate

    # Print loss every 1000 epochs
    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch} - Loss: {loss:.4f}")

print("\nTraining complete.\n")
print("Predictions after training:")
print(final_output)
