# Project 2: Data Classification Using AI
# Goal: teach the computer to guess a flower's species from its measurements.

# This brings in the tools we need from scikit-learn.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# STEP 1: Load the data.
# "load_iris" gives us 150 flowers, each with 4 measurements,
# and the correct species already labeled for every one.
iris_data = load_iris()

# "features" holds the measurements (petal length, petal width, etc).
features = iris_data.data

# "labels" holds the correct species for each flower (0, 1, or 2).
labels = iris_data.target

# STEP 2: Split the data into a training set and a testing set.
# The computer will LEARN from the training set,
# and we will TEST it on flowers it has never seen.
# test_size=0.2 means 20% of the flowers are saved for testing.
features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# STEP 3: Scale the features.
# Some measurements have bigger numbers than others.
# Scaling makes sure no single measurement unfairly dominates.
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

# STEP 4: Create the model.
# KNeighborsClassifier is the KNN algorithm.
# n_neighbors=5 means it looks at the 5 closest flowers to make a guess.
model = KNeighborsClassifier(n_neighbors=5)

# STEP 5: Train the model.
# This is the step where the computer actually "learns" the patterns.
model.fit(features_train, labels_train)

# STEP 6: Make predictions on the test flowers (the ones it hasn't seen).
predictions = model.predict(features_test)

# STEP 7: Check how well it did.
# Accuracy = what percent of guesses were correct.
accuracy = accuracy_score(labels_test, predictions)
print("Accuracy:", round(accuracy * 100, 2), "%")

# The confusion matrix shows exactly which species got mixed up with which.
# Rows = the real species. Columns = what the model guessed.
print("\nConfusion Matrix:")
print(confusion_matrix(labels_test, predictions))

# Precision, recall, and F1 score for EACH species separately.
# Precision: when the model said "this species", how often was it right?
# Recall: out of all the real flowers of that species, how many did it catch?
# F1: a single score that balances precision and recall together.
print("\nPrecision / Recall / F1 Report:")
print(classification_report(labels_test, predictions, target_names=iris_data.target_names))

# STEP 8: Try predicting one new flower by hand, just to see it in action.
# These 4 numbers are: sepal length, sepal width, petal length, petal width.
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
guess = model.predict(new_flower_scaled)
species_name = iris_data.target_names[guess[0]]
print("\nThe model guesses this new flower is:", species_name)