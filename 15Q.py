# Decision Tree Implementation

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example dataset
# Features: [Hours Studied, Sleep Hours]
X = [
    [2, 8],
    [4, 6],
    [6, 5],
    [8, 4],
    [1, 9],
    [7, 3],
    [5, 6],
    [3, 7]
]

# Labels: 0 = Fail, 1 = Pass
y = [0, 0, 1, 1, 0, 1, 1, 0]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test)
print("Accuracy:", accuracy)
