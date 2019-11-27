import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

from plotting_utils import scatter_plot
from utils import assign_scores
from constants import scoring_features, house_type

house_prices = pd.read_csv('data/house_prices.csv')

# columns of the data
# ['id', 'house_type', 'zone', 'total_area', 'rental_price', 'num_bedrooms', 'num_baths', 'security_level', 'air_quality_index', 'num_key_amenities']
print(house_prices.columns.tolist())

# a copy of the data to play with
house_prices_copy = house_prices.copy(deep=True)

# preview data
# we only need 'security_level', 'air_quality_index', 'num_key_amenities' and 'house_type'
# features in this analysis
# 'security_level', 'air_quality_index' and 'num_key_amenities' need to have the same scale
# to be used in scoring zones.
# 'house_type' need to be numerical to be used in our model 
print(house_prices_copy.info()) # 10010 rows and 10 columns
analysis_features = house_type + scoring_features
print(house_prices_copy[ scoring_features].describe())


# Cleaning data: correcting, completing, creating, converting

# 1. correcting
# we are not going to correct any data points. We will leave our data the way it is to be
# able to dicover outliers

# 2. completing
# we look for any missing values. If we have any missing values, we should attempt to
# fill tha blank data points with some appropriate values
# our relevant features do not have any missing values
print(house_prices_copy[analysis_features].isnull().sum())

# 3. creating
# we are not going to do any feature engineering as we do not need any new features here

# 4. converting
# we going to convert 'security_level', 'air_quality_index', 'num_key_amenities' to be in scale 0-1 so as
# to use them to score the 7 zones using their weighted averages (avoid comparing apples to oranges)
scaler = MinMaxScaler()
house_prices_copy[scoring_features] = scaler.fit_transform(house_prices_copy[scoring_features])
# we now encode the 'house_type' to have values between '0' and '3' as our
# learning model works with numericals only
encoder = LabelEncoder()
house_prices_copy['house_type_code'] = encoder.fit_transform(house_prices_copy['house_type'])

# double checking to ensure our data is OK
print(house_prices_copy[scoring_features + ['house_type_code']].info())  # all features are numerical
print(house_prices_copy[scoring_features].describe()) # values range from '0' to '1'

# for scoring_feature in scoring_features:
# 	scatter_plot(house_prices_copy[scoring_feature], house_prices_copy['rental_price'])

# SCORING the zones
assign_scores(house_prices_copy[['zone'] + scoring_features])
