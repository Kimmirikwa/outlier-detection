import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

house_prices = pd.read_csv('data/house_prices.csv')

# columns of the data
# ['id', 'house_type', 'zone', 'total_area', 'rental_price', 'num_bedrooms', 'num_baths', 'security_level', 'air_quality_index', 'num_key_amenities']
print(house_prices.columns.tolist())

# a copy of the data to play with
house_prices_copy = house_prices.copy(deep=True)

# preview data
print(house_prices_copy.info()) # 10010 rows and 10 columns

# Cleaning data: correcting, completing, creating, converting

# 1. correcting
# we are not going to correct any data points. We will leave our data the way it is to be
# able to dicover outliers

# 2. completing
# we look for any missing values. If we have any missing values, we should attempt to
# fill tha blank data points with some appropriate values
# we find that both 'num_bedrooms' and 'num_baths' have 3003 missing values, while the rest of the columns
# have all the values. Since we are not interested in these 2 columns, we do not need to waste time completing them
print("The number of columns with missing values: ", house_prices_copy.isnull().sum())

# 3. creating
# we are not going to do any feature engineering as we do not need any new features here

# 4. converting
# we going to convert 'security_level', 'air_quality_index', 'num_key_amenities' to be in scale 0-1 so as
# to use them to score the 7 zones using their weighted averages (avoid comparing apples to oranges)
scaler = MinMaxScaler()
scoring_features = ['security_level', 'air_quality_index', 'num_key_amenities']
scoring_data = house_prices_copy[scoring_features]
house_prices_copy[scoring_features] = scaler.fit_transform(scoring_data)
# we now encode the 'house_type' to have values between '0' and '3' as our
# learning model works with numericals only
encoder = LabelEncoder()
house_prices_copy['house_type_code'] = encoder.fit_transform(house_prices_copy['house_type'])

