import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def detect_bias(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    accuracy = accuracy_score(y, predictions)
    print(f"Accuracy: {accuracy}")
    
    positive_rate = np.mean(predictions)
    print(f"Positive prediction rate: {positive_rate}")
    if positive_rate > 0.6:  # Adjust threshold based on fairness criteria
        print("Warning: Potential bias detected!")
    return predictions

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 1, 1, 0])
    detect_bias(X, y)
