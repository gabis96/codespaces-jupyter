import shapefile
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from scipy.spatial.distance import squareform, pdist

class MapData:
    '''Working with map data'''
    def __init__(self, path):
        self.path = path
        self.bad_iris = [751124577, 751124677, 751166177, 751166277, 751166377]

    def read_map(self, index_name):
        '''Read map and transform it to pandas dataframe.'''
        # load coordenates data
        sf = shapefile.Reader(self.path)
        fields = [x[0] for x in sf.fields][1:]
        records = sf.records()
        shps = [s.points for s in sf.shapes()]
        
        # write into a dataframe
        df_map = pd.DataFrame(columns=fields, data=records)
        df_map = df_map.assign(coords=shps)
        df_map = df_map.set_index(index_name)
        df_map.index = df_map.index.astype(int)

        df_map = df_map.drop(self.bad_iris).fillna(value=0)       
        
        return df_map

    def _centroid(self, arr):
        '''Calculate centroid of coordanates list.'''
        length = len(arr)
        sum_x = sum([elem[0] for elem in arr])
        sum_y = sum([elem[1] for elem in arr])
        return sum_x/length, sum_y/length

    
    def _distance_matrix(self, distances):
        ''' Calculate the distance matrix between centroids of each IRIS.'''
        coordsMatrix = distances['coords'].apply(pd.Series)
        a = pdist(coordsMatrix, 'euclidean')
        return pd.DataFrame(squareform(pdist(coordsMatrix)), columns=coordsMatrix.index.unique(), index=coordsMatrix.index.unique())

    def _distance(self, df_index_map):
        '''Calculate centroid for all IRIS.'''
        centroidsDF = df_index_map
        centroidsDF['coords'] = centroidsDF['coords'].apply(lambda x: self._centroid(x))
        return centroidsDF

    def get_distance_matrix(self, data, index_name):
        '''Generate distance matrix.'''
        df_index_map = self.read_map(index_name)
        # Same index as data
        df_index_map = df_index_map[df_index_map.index.isin(data.index)]
        
        distanceDf = self._distance(df_index_map)
        distanceMatrixDF = self._distance_matrix(distanceDf)
        return distanceMatrixDF
    
    def create_geometry_map(self, index_name):
        '''Draw maps from data.'''
        df_map = self.read_map(index_name)

        # Draw Maps
        geometry = df_map['coords']

        geometry = [Polygon(xy) for xy in geometry]
        gdf = gpd.GeoDataFrame(df_map, crs={'init': 'epsg:4326'}, geometry=geometry)

        return gdf
