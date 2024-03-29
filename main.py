import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest

from plotting_utils import scatter_plot
from utils import assign_scores
from constants import scoring_features, house_type

rng = np.random.RandomState(42)

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
# we get ordinal values of the house types. I have ranked the house types in the following way:
# 'SRU': 0, 'APT': 1, 'MSNT': 2, 'BLW': 3. The higher the value, the 'better' the house type
# IsolationForest require categorical values to be encoded this way
cat = pd.Categorical(house_prices_copy['house_type'], 
                    categories=['SRU', 'APT', 'MSNT', 'BLW'],
                    ordered=True)
labels, unique = pd.factorize(cat, sort=True)
house_prices_copy['house_type_ordinal'] = labels

# double checking to ensure our data is OK
print(house_prices_copy[scoring_features + ['house_type_ordinal']].info())  # all features are numerical
print(house_prices_copy[scoring_features].describe()) # values range from '0' to '1'

# for scoring_feature in scoring_features:
# 	scatter_plot(house_prices_copy[scoring_feature], house_prices_copy['rental_price'])

# SCORING the zones and assigning score to each example based on the score of the zone
assign_scores(house_prices_copy)

# Now we are ready to model
# since there is no information about outliers in the dataset, I have selected unsupervised learning model
# using IsolationForest to detect outliers, which 'isolates' outliers since outliers are always 'few and different'
# we will only use the required features i.e 'zone_ranking', 'house_type_ordinal' and 'total_area'
training_features = ['zone_rank', 'house_type_ordinal', 'total_area']

train_data = house_prices_copy[training_features]

# the training model
# detecting 5% of data to be outliers. I have only assumed this but I should have investigated the best
# value to use
clf = IsolationForest(behaviour='new', n_estimators=50, max_samples=100,
                      random_state=rng, contamination=0.05)

# fit the model and use it to detect outliers
clf.fit(train_data)
pred = clf.predict(train_data)

# outliers predicted as '-1' and inliers as '1', but want 'True' and 'False' for presentation
outliers = pred == -1
house_prices_copy['outlier'] = outliers

# a scatter plot of a few data points marked as outliers and inliers
sampled = house_prices_copy.sample(1000)
scatter_plot(sampled, training_features[0], training_features[1], training_features[2])

# add the outlier column to the original data and create a csv file
house_prices['outlier'] = outliers
house_prices.to_csv('output/house_prices_with_outliers.csv', index=False)
