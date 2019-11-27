import pandas as pd
import numpy as np

house_prices = pd.read_csv('data/house_prices.csv')

# columns of the data
# ['id', 'house_type', 'zone', 'total_area', 'rental_price', 'num_bedrooms', 'num_baths', 'security_level', 'air_quality_index', 'num_key_amenities']
print(house_prices.columns.tolist())