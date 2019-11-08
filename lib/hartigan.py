# https://github.com/dawenl/stochastic_PMF/blob/master/code/HartiganOnline.py
# Modified for Python 3

import numpy as np
from sklearn.base import BaseEstimator


class HartiganOnline(BaseEstimator):
    """Online Hartigan clustering algorithm."""

    def __init__(self, n_clusters: int = 2, max_iter: int = 10, shuffle: bool = True, verbose: bool = False):
        """Initialize a Hartigan clusterer.

        :param int n_clusters: The number of clusters
        :param int max_iter: Maximum number of passes through the data
        :param bool shuffle: Shuffle the data between each pass
        :param bool verbose: Display debugging output
        """

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.shuffle = shuffle
        self.verbose = verbose

        self.cluster_sizes_ = np.zeros(self.n_clusters)

    def fit(self, X: np.array):
        """Fit the cluster centers.

        :param np.array X: The data to be clustered (NxD)
        """
        N, D = X.shape

        # Initialize the cluster centers, costs, sizes
        self.cluster_centers_ = np.zeros((self.n_clusters, D), dtype=X.dtype)

        step = 0

        i = np.arange(N)
        while step < self.max_iter:
            step += 1

            if self.shuffle:
                np.random.shuffle(i)

            self.partial_fit(X[i])

    def partial_fit(self, X: np.array):
        """Partial fit the cluster centers

        :param np.array X: The data to be clustered (NxD)
        """
        N, D = X.shape

        if not hasattr(self, "cluster_centers_"):
            self.cluster_centers_ = np.zeros((self.n_clusters, D), dtype=X.dtype)

        balances = self.cluster_sizes_ / (1.0 + self.cluster_sizes_)
        norms = np.sum(self.cluster_centers_ ** 2, axis=1)

        for x in X:
            # Get the closest cluster center
            j = np.argmin(balances * (np.sum(x ** 2) + norms - 2 * self.cluster_centers_.dot(x)))

            # Update the center
            self.cluster_centers_[j] = (self.cluster_sizes_[j] * self.cluster_centers_[j] + x) / (
                    1.0 + self.cluster_sizes_[j])

            # Update the counter
            self.cluster_sizes_[j] += 1.0

            # Update the balance
            balances[j] = self.cluster_sizes_[j] / (1.0 + self.cluster_sizes_[j])

            # Update the norms
            norms[j] = np.sum(self.cluster_centers_[j] ** 2)