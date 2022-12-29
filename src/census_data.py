import pandas as pd

# Working with Paris Census Data
class ParisCensusData:
    def __init__(self, famille_path, population_path, revenus_path):
        # Load Files
        self.familleDF = pd.read_csv(famille_path, encoding = "utf-8")
        self.populationDF = pd.read_csv(population_path, encoding = "utf-8")
        self.revenusDF = pd.read_csv(revenus_path, encoding = "utf-8")
        
        self.bad_iris = [751124577, 751124677, 751166177, 751166277, 751166377]

    def build(self):
        self._select_paris()
        self._set_index()
        self._delete_bad_iris()
        self._filter_data()

    def _select_paris(self):
        # Choose only Paris Data
        self.familleDF = self.familleDF[self.familleDF['IRIS'].astype(str).str.startswith('75', na=False)]
        self.populationDF = self.populationDF[self.populationDF['IRIS'].astype(str).str.startswith('75', na=False)]
        self.revenusDF = self.revenusDF[self.revenusDF['IRIS'].astype(str).str.startswith('75', na=False)]
    
    def _set_index(self):
        # Set IRIS as index
        self.familleDF = self.familleDF.set_index('IRIS')
        self.populationDF = self.populationDF.set_index('IRIS')
        self.revenusDF = self.revenusDF.set_index('IRIS')
        
    def _delete_bad_iris(self):
        # Delete Paris Wood
        self.familleDF = self.familleDF.drop(self.bad_iris)
        self.populationDF = self.populationDF.drop(self.bad_iris)
        #self.revenusDF = self.revenusDF.drop(bad_iris, axis = 0)

    def _filter_data(self):    
        # Dejar a todos con la misma cantiadad de Iris
        # self.familleDF = self.familleDF[self.familleDF.index.isin(self.revenusDF.index)]
        # self.populationDF = self.populationDF[self.populationDF.index.isin(self.revenusDF.index)]

        # Transform values NAN to 0
        self.familleDF = self.familleDF.fillna(value = 0, axis = 1)
        self.populationDF = self.populationDF.fillna(value = 0, axis = 1)
        self.revenusDF = self.revenusDF.fillna(value = 0, axis = 1)
