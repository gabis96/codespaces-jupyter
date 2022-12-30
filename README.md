
# Residential Segregation Analysis in Python 

This project detects residential segregation using clustering algorithms. Particulary, the city of Paris is analized for the behavior of the variable that reports the proportion of social housing (housing served directly by the government). Public census data is used to extract information.


This study, together with its antecedents, contributes to a large project on urbanization problems; the purpose of which is to be an instrument of interest to city governments. This would allow social power structures to identify areas where public policies are needed to improve the quality of life of the population. 
## Python Stack

**Math & Machine Learning:** sklearn, numpy, scipy

**Data Manipulation:** pandas

**Visualization:** mathplotlib, shapefile, geopandas
## File Description
To structure my project I have followed the *Cookiecutter* template.

- **data**: folder containing all data files.
    - **final**: folder containing final datasets.
        - **paris_social_housing_kmeans.csv**
        - **paris_social_housing_kmeans_centroids.csv**
        - **paris_social_housing_kmeans_map.csv**
        - **paris_social_housing_meanshift.csv**
        - **paris_social_housing_meanshift_centroids.csv**
        - **paris_social_housing_meanshift_map.csv**
    - **processed**:
        - **paris_social_housing.csv**: data after cleaning and filtering important feature.
    - **raw**:
        - **CONTOURS-IRIS_D075.dbf**: database containing data of Paris map. 
        - **CONTOURS-IRIS_D075.shp**: shapefile data of Paris map. 
        - **famillie_2014.csv**: public census data of Paris families.
        - **population_2014.csv**: public census data of Paris population.
        - **revenue_2014.csv**: public census data of Paris revenue.
- **models**: folder containing models definitions.
    - **kmeans**: wrapper class for kmeans model.
    - **meanshift**: wrapper class for meanshift model.
- **notebooks**: folder containing notebooks.
    - **data_analysis.ipynb**: notebook for analysing data using clustering algorithms.
    - **data_cleansing.ipynb**: notebook for cleaning raw data and extracting important measure feature.
    - **visualization.ipynb**: notebook for viasualizing clusters in Paris map.
- **src**: folder storing all python code. 
    - **census_data.py**: file used for cleaning raw data. 
    - **color_maps.py**: file used for defining color schemes for map visualization.
    - **map_data.py**: file used for create mapfrom database.
- **requierements.py**: python dependencies.

## Results
It was affirmed that segregation exists for the variables studied. 
The peripheral area of Paris was identified with the highest concentration of social housing, 
and the northeast of Havana with a high concentration of population over 60 years of age. 
Note that the analysis done for Cuba is not included as the data was collected as an agreement between institutions.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://gabrielarscp.wixsite.com/gabsdatascience/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielasanta/)

- - - -
[Go to top](#TOP)
