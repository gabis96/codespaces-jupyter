import numpy as np
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth
from yellowbrick.cluster import KElbowVisualizer

from yellowbrick.cluster.elbow import kelbow_visualizer

import warnings
warnings.filterwarnings('ignore')

class KmeansClustering:
    """Wrapper class for sklearn Kmeans."""
    def __init__(self, dataframe, column):
        self.X = np.array(dataframe[[column]])

    def fit(self, k):
        kmeans = KMeans(n_clusters = k).fit(self.X)
        centers = kmeans.cluster_centers_ 
        centers = [centers[i][0] for i in range(len(centers))] 
        labels = kmeans.labels_
        
        return (labels, centers)

    def visualize_elbow(self, k = (1, 10), metric = 'distortion'):
        kelbow_visualizer(model = KMeans(), X = self.X, k = k , metric = metric)

class MeanShiftClustering:
    def __init__(self, dataframe, column):
        self.X = np.array(dataframe[[column]])

    def fit(self):
        bandwidth = estimate_bandwidth(self.X, quantile = 0.2, n_samples = 500)
        meanShift = MeanShift(bandwidth = bandwidth).fit(self.X)

        centers = meanShift.cluster_centers_
        centers = [centers[i][0] for i in range(len(centers))] 
        labels = meanShift.labels_
        
        return (labels, centers)