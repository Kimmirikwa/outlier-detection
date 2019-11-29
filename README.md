# Detecting outliers in house prices
In this repo, I have detected outliers in housing dataset. The dataset is in ```data/house_prices.csv```. <br/> <br/>
Only 3 features are used in detecting outliers. These are ```zone_rank```, ```house_type_ordinal``` and ```total_area```. ```zone_rank``` and ```house_type_ordinal``` are not in the original dataset.
```zone_rank``` is oubtained from the rank of the score of a zone based on weighted average of ```security_level```, ```air_quality_index``` and ```num_key_amenities```.
```house_type_ordinal``` is outained be encoding the house type codes ordinally.<br/> <br/>
I have used an [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html) model of sklearn. This works by getting the most 'different' datapoints in the dataset. The forest has 50 trees. Each tree splits data at each node by randomly selecting one of the 3 features above and then randomly selecting a value in the feature to be used in splitting the data into two subsets. Outliers are detected by taking the smallest average heights from the root node to the node where a datapoint finally end up.

A few datapoints are randomly selected and plotted with outliers marked as shown below.
![outliers](https://user-images.githubusercontent.com/19263794/69857086-28fda400-12a0-11ea-9556-442d43367e24.png)

From the scatter plot, it can be seen clearly that outliers(marked red). <br/>For example, we have outliers around the region with the following values: ```zone_rank: 5``` - (indicating a low score obtained above), ```house_type_ordinal: 3```- (for ```Bungalow```) and ```total_area: 100``` - (which is quite small for a bungalow in this dataset). <br/>
There are other outliers around the region with the following values: ```zone_rank: 1``` - (indicating a high score obtained above), ```house_type_ordinal: 1```- (for ```Apartments/flats ```) and ```total_area: around 3000``` - (which is quite large for a Apartments/flats  in this dataset).<br/>
From the scatter plot, it can generally be seen that the better the score of the zone (low rank for high score), the bigger the ```total_area``` and the better the house type, and off course the higher the price.
<br/><br/>

The final file of of the original dataset with an outlier column added can be found at ```output/house_prices_with_outliers.csv```. ```outlier``` column values ```True``` indcate the datapoint is an outlier.

To try this, clone the repo then do the following:
1. pip install -r requirements.txt
2. install python-tk
3. run ```main.py```
