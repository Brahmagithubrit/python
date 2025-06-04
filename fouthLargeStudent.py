import pandas as pd
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Step 1: Load CSV with pandas
df = pd.read_csv('student_performance_max.csv')

# Step 2: Extract features and labels as numpy arrays
X_raw = df[['StudyHours', 'Attendance', 'SleepHours', 'AssignmentDone', 'GradePercentage']].to_numpy()
y_raw = df['Pass'].to_numpy().reshape(-1,1)

# Step 3: Normalize features (using max values you defined)
max_values = np.array([12, 100, 12, 1, 100])
X = X_raw / max_values

# Labels are already 0/1 so no need to change y
y = y_raw

# Step 4: Initialize weights
np.random.seed(42)
input_size = X.shape[1]
hidden_size = 4
output_size = 1

w1 = 2 * np.random.random((input_size, hidden_size)) - 1
w2 = 2 * np.random.random((hidden_size, output_size)) - 1

learning_rate = 0.1
epochs = 10000

# Step 5: Training loop
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

    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch} - Loss: {loss:.4f}")

print("\nTraining complete.\n")

# Step 6: Predict function for new student
def predict(new_data_raw):
    new_data = new_data_raw / max_values
    hidden = sigmoid(np.dot(new_data, w1))
    output = sigmoid(np.dot(hidden, w2))
    return output

# Test example: new student
new_student = np.array([10.5, 100, 4, 0, 100])
prob = predict(new_student)
print(f"Pass Probability for new student: {prob[0]:.2f}")
