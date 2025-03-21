import os

import requests

"""
https://www.geeksforgeeks.org/how-to-download-files-from-urls-with-python/
"""

# Base URL
BASE_URL = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/'

# Set up directory
os.mkdir('data')

for year in range(2015, 2025):
    os.mkdir(f'data/{year}')

    # Get Cincinnati data
    response = requests.get(f'{BASE_URL}/{year}/72429793812.csv')
    if response.status_code == 200:
        with open(f'data/{year}/72429793812.csv', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Could not fetch Cincinnati data for {year}')

    # Get Florida data
    response = requests.get(f'{BASE_URL}/{year}/99495199999.csv')
    if response.status_code == 200:
        with open(f'data/{year}/99495199999.csv', 'wb') as file:
            file.write(response.content)
    else:
        print(f'Could not fetch Florida data for {year}')
