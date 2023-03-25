import zipfile
import pandas as pd

# Get the necessary data from the archives and unzip them
oil_and_wti = zipfile.ZipFile('../../results/task/datasets/oil-prices.zip')
population = zipfile.ZipFile('../../results/task/datasets/population.zip')
ppp = zipfile.ZipFile('../../results/task/datasets/ppp.zip')

# Extract files
oil_and_wti.extract('oil-prices-master/data/brent-year.csv', 'data')
oil_and_wti.extract('oil-prices-master/data/wti-year.csv', 'data')
oil_and_wti.close()
population.extract('population-master/data/population.csv', 'data')
population.close()
ppp.extract('ppp-master/data/ppp-gdp.csv', 'data')
ppp.close()