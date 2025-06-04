import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Real raw data (study hours, attendance %, sleep hours, assignment done (0/1), grade %)
X_raw = np.array([
    [5, 80, 7, 1, 75],   # Pass
    [2, 60, 5, 0, 50],   # Fail
    [6, 90, 6, 1, 80],   # Pass
    [1, 55, 4, 0, 40]    # Fail
])

# Labels
y = np.array([[1], [0], [1], [0]])

# Normalize inputs (min-max scaling)
# For simplicity, define max values for each feature:
max_values = np.array([12, 100, 12, 1, 100])

X = X_raw / max_values  # Scale each feature between 0 and 1

np.random.seed(42)
w1 = 2 * np.random.random((5, 4)) - 1
w2 = 2 * np.random.random((4, 1)) - 1

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    hidden_input = np.dot(X, w1)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, w2)
    final_output = sigmoid(final_input)

    error = y - final_output

    d_final_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = d_final_output.dot(w2.T)
    d_hidden_output = error_hidden_layer * sigmoid_derivative(hidden_output)

    w2 += hidden_output.T.dot(d_final_output) * learning_rate
    w1 += X.T.dot(d_hidden_output) * learning_rate

    if epoch % 100 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch} - Loss: {loss:.4f}")

print("\nTraining complete.\n")

def predict(new_data_raw):
    new_data = new_data_raw / max_values
    hidden = sigmoid(np.dot(new_data, w1))
    output = sigmoid(np.dot(hidden, w2))
    return output

# Test new student real values (e.g., 4.5 hrs study, 70% attendance, 6 hrs sleep, assignment done, 65% grade)
new_student = np.array([10.5, 100, 4, 0, 100])
prob = predict(new_student)
print(f"Pass Probability for new student: {prob[0]:.2f}")
