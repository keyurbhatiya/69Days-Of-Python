################################## Day 25: 69 Days of Python #####################################


# Importing Required Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_classification

# Generate synthetic dataset for demonstration
X, y = make_classification(n_samples=500, n_features=5, n_classes=2, random_state=42)

######################################
# Confusion Matrix
######################################
# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic Regression for classification
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Visualizing the Confusion Matrix
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

######################################
# Hierarchical Clustering
######################################
# Creating a model
hc = AgglomerativeClustering(n_clusters=2, linkage='ward')
hc_labels = hc.fit_predict(X)

# Plotting a dendrogram
linkage_matrix = linkage(X[:50], 'ward')  # Dendrogram for a subset
dendrogram(linkage_matrix)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()

######################################
# Logistic Regression
######################################
# Logistic Regression Model
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
print("Logistic Regression Accuracy:", logistic_model.score(X_test, y_test))

######################################
# Grid Search
######################################
# Grid Search for Logistic Regression
param_grid = {'C': [0.1, 1, 10], 'solver': ['liblinear']}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X, y)

# Displaying best parameters and score
print("Best Parameters from Grid Search:", grid.best_params_)
print("Best Grid Search Score:", grid.best_score_)

######################################
# Categorical Data
######################################
# Encoding Categorical Data
data = ['cat', 'dog', 'mouse', 'cat', 'dog']
encoder = LabelEncoder()
encoded_data = encoder.fit_transform(data)

print("Original Categorical Data:", data)
print("Encoded Data:", encoded_data)

######################################
# K-means Clustering
######################################
# K-means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Displaying Cluster Centers
print("K-Means Cluster Centers:\n", kmeans.cluster_centers_)

# Plotting K-means Clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis")
plt.title("K-Means Clustering")
plt.show()

######################################
# Bootstrap Aggregation (Bagging)
######################################
# Bagging Classifier
bagging_model = BaggingClassifier(estimator=LogisticRegression(), n_estimators=10, random_state=42)
bagging_model.fit(X_train, y_train)

# Displaying Bagging Classifier Score
print("Bagging Classifier Accuracy:", bagging_model.score(X_test, y_test))


# Displaying Bagging Classifier Score
print("Bagging Classifier Accuracy:", bagging_model.score(X_test, y_test))

######################################
# Cross Validation
######################################
# Cross Validation with Logistic Regression
cv_scores = cross_val_score(LogisticRegression(), X, y, cv=5)

# Displaying Cross-Validation Scores
print("Cross-Validation Scores:", cv_scores)
print("Mean Cross-Validation Score:", cv_scores.mean())

######################################
# AUC - ROC Curve
######################################
# Predicting Probabilities for ROC Curve
y_prob = model.predict_proba(X_test)[:, 1]

# Computing ROC Curve and AUC
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Plotting ROC Curve
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

# K-nearest Neighbors (KNN)
######################################
# KNN Classifier
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Displaying KNN Classifier Score
print("KNN Classifier Accuracy:", knn_model.score(X_test, y_test))


# This tutorial covers advanced topics in machine learning, including confusion matrices, clustering, grid search, and more.
# By running this script, you can understand and apply these concepts to real-world datasets.


''' Next Topic Python MySQL ---> Day_26.py '''