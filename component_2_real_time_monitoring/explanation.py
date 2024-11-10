import lime
import lime.lime_tabular
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 1, 0])
model = RandomForestClassifier()
model.fit(X, y)


def explain_decision(data):
    explainer = lime.lime_tabular.LimeTabularExplainer(
        X, feature_names=["feature1", "feature2"], class_names=["negative", "positive"], verbose=True
    )
    explanation = explainer.explain_instance(data, model.predict_proba)
    explanation.show_in_notebook()

if __name__ == "__main__":
    example_data = np.array([3, 4])
    explain_decision(example_data)
