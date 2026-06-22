from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

print("Dataset Overview:")
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nClass Distribution:\n{df['species'].value_counts()}")

# Save dataset to CSV
df.to_csv("iris_dataset.csv", index=False)
print("\nDataset saved to iris_dataset.csv")

# Feature scaling
X = iris.data
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Results
print(f"\nAccuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))
# MY flower to test
my_flower = [[5.1, 3.5, 1.4, 0.2]]
#              ↑       ↑       ↑      ↑
#         sepal  sepal  petal  petal
#         length width  length width

# Scale
my_flower_scaled = scaler.transform(my_flower)

# take Prediction
result = model.predict(my_flower_scaled)

print(f"\nMeri Flower Ka Result: {iris.target_names[result[0]].upper()}")
