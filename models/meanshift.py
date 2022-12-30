import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

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