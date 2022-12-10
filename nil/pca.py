import numpy as np

def pca(X, num_components):
  # Calculate the covariance matrix
  covariance_matrix = np.cov(X.T)

  # Calculate the eigenvectors and eigenvalues of the covariance matrix
  eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

  # Sort the eigenvalues in descending order
  eigenvalues_sorted = np.argsort(eigenvalues)[::-1]

  # Select the top `num_components` eigenvectors
  eigenvectors = eigenvectors[eigenvalues_sorted[:num_components]]

  # Project the data onto the selected eigenvectors
  reduced_data = np.dot(X, eigenvectors.T)

  return reduced_data

"""
The function takes as input the data matrix X and the number of PCA components to keep.
It calculates the covariance matrix of X, and then uses it to compute the eigenvectors and eigenvalues of X.
The eigenvectors are sorted by their corresponding eigenvalues in descending order, and the top num_components
eigenvectors are selected. Finally, the data is projected onto the selected eigenvectors to obtain the reduced data matrix.

To find the optimal number of PCA components, we can calculate the covariance between the features in the data matrix X.
We can then use this information to choose the number of components that captures a significant amount of the variance in the data.
For example, we could choose the number of components such that at least 95% of the variance in the data is retained.

Here is how this could be implemented:

"""

def find_optimal_num_components(X, variance_threshold):
  # Calculate the covariance matrix
  covariance_matrix = np.cov(X.T)

  # Calculate the eigenvectors and eigenvalues of the covariance matrix
  eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

  # Sort the eigenvalues in descending order
  eigenvalues_sorted = np.argsort(eigenvalues)[::-1]

  # Cumulative sum of the explained variances
  cum_sum_explained_variances = np.cumsum(eigenvalues[eigenvalues_sorted])

  # Normalize the cumulative sum of explained variances
  cum_sum_explained_variances = cum_sum_explained_variances / cum_sum_explained_variances[-1]

  # Find the index of the first explained variance that is greater than the variance threshold
  index = np.argmax(cum_sum_explained_variances >= variance_threshold)

  return index + 1


"""
The function takes as input the data matrix X and a variance threshold. It calculates the covariance matrix of X,
and then uses it to compute the eigenvectors and eigenvalues of X. The explained variances are calculated and sorted in descending order.
The cumulative sum of the explained variances is then normalized, and the index of the first explained
"""