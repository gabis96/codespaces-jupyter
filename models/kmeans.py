import numpy as np
from sklearn.cluster import KMeans

from yellowbrick.cluster.elbow import kelbow_visualizer

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