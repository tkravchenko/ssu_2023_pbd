import zipfile
import pandas as pd

# Get the necessary data from the archives and unzip them
oil_and_wti = zipfile.ZipFile('../task/datasets/oil-prices.zip')
population = zipfile.ZipFile('../task/datasets/population.zip')
ppp = zipfile.ZipFile('../task/datasets/ppp.zip')

# Extract files
oil_and_wti.extract('oil-prices-master/data/brent-year.csv', '../data/')
oil_and_wti.extract('oil-prices-master/data/wti-year.csv', '../data/')
oil_and_wti.close()
population.extract('population-master/data/population.csv', '../data/')
population.close()
ppp.extract('ppp-master/data/ppp-gdp.csv', '../data/')
ppp.close()

# Paths to data
oil_prices_wti_path = '../data/oil-prices-master/data/'
population_path = '../data/population-master/data/'
ppp_path = '../data/ppp-master/data/'

# Save data in 3 formats
def save_3_formats(data, path, name):
    data.to_csv('{0}{1}.csv'.format(path, name), index=False)
    data.to_excel('{0}{1}.xlsx'.format(path, name), index=False)
    data.to_json('{0}{1}.json'.format(path, name), orient='table', index=False)

# Read the data
oil_prices_data = pd.read_csv(oil_prices_wti_path + '/brent-year.csv')
wti_year_data = pd.read_csv(oil_prices_wti_path + '/wti-year.csv')
population_data = pd.read_csv(population_path + 'population.csv')
ppp_data = pd.read_csv(ppp_path + 'ppp-gdp.csv')

# Change and adjust the date format for oil prices and wti
oil_prices_data['Date'] = pd.to_datetime(oil_prices_data.Date)
oil_prices_data['Date'] = oil_prices_data['Date'].dt.strftime('%Y')
wti_year_data['Date'] = pd.to_datetime(wti_year_data.Date)
wti_year_data['Date'] = wti_year_data['Date'].dt.strftime('%Y')

# Change and adjust the date format for population and ppp
population_data['Year'] = pd.to_datetime(population_data.Year, format='%Y')
population_data['Year'] = population_data['Year'].dt.strftime('%Y')
ppp_data['Year'] = pd.to_datetime(ppp_data.Year, format='%Y')
ppp_data['Year'] = ppp_data['Year'].dt.strftime('%Y')

# Save data in 3 formats
save_3_formats(oil_prices_data, oil_prices_wti_path, 'brent-year')
save_3_formats(wti_year_data, oil_prices_wti_path, 'wti-year')
save_3_formats(population_data, population_path, 'population')
save_3_formats(ppp_data, ppp_path, 'ppp-gdp')