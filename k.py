# K-Means clustering (from scratch)


# ============================================================
# Practical 11 - K-Means clustering
# ============================================================
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv("student_performance.csv")

data.head()

X = data[["StudyHours", "ExamScore"]].values

plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    alpha=0.5
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Before K-Means Clustering")
plt.grid(True)

plt.show()

k = 3

# 4. Select Random Initial Centroids

rd.seed(42)

random_indices = rd.sample(range(len(X)), k)

centroids = X[random_indices].astype(float)

print("Initial Centroids:")
print(centroids)

# 5. K-Means Algorithm
for iteration in range(100):

    # Calculate distance from each point
    # to each centroid

    distances = np.zeros((len(X), k))

    for i in range(len(X)):
        for j in range(k):

            distances[i, j] = np.sqrt(
                np.sum((X[i] - centroids[j]) ** 2)
            )

    # Assign each point to nearest centroid
    clusters = np.argmin(distances, axis=1)

    # Save old centroids
    old_centroids = centroids.copy()

    # Calculate new centroids
    for j in range(k):

        cluster_points = X[clusters == j]

        if len(cluster_points) > 0:
            centroids[j] = np.mean(
                cluster_points,
                axis=0
            )

    # Check convergence
    if np.allclose(old_centroids, centroids):

        print(
            "\nK-Means converged after",
            iteration + 1,
            "iterations"
        )

        break

# 6. Add Cluster to Dataset
data["Cluster"] = clusters

# 7. Display Final Centroids
print("\nFinal Centroids:")
print(centroids)

# 8. Scatter Plot AFTER K-Means
plt.figure(figsize=(8, 6))

for cluster in range(k):

    cluster_points = X[clusters == cluster]

    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        alpha=0.5,
        label=f"Cluster {cluster + 1}"
    )


# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=250,
    label="Centroids"
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("After K-Means Clustering")
plt.legend()
plt.grid(True)

plt.show()

# 9. Display Cluster Counts
print("\nNumber of students in each cluster:")

print(
    data["Cluster"]
    .value_counts()
    .sort_index()
)

# 10. Display Sample Results
print("\nClustered Data:")

print(
    data[
        ["StudyHours", "ExamScore", "Cluster"]
    ].head(20)
)
