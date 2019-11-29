# Detecting outliers in house prices
In this repo, I have detected outliers in housing dataset. The dataset is in ```data/house_prices.csv```.
Only 3 features are used in detecting outliers. These are ```zone_rank```, ```house_type_ordinal``` and ```total_area```. ```zone_rank``` and ```house_type_ordinal``` are not in the original dataset.
```zone_rank``` is oubtained from the rank of the score of a zone based on weighted average of ```security_level```, ```air_quality_index``` and ```num_key_amenities```.
```house_type_ordinal``` is outained be encoding the house type codes ordinally.
I have used an ```IsolationForest``` model of sklearn. This works by getting the most 'different' datapoints in the dataset. The forest has 50 trees. Each tree splits data at each node by randomly selecting one of the 3 features above and then randomly selecting a value in the feature to be used in splitting the data into two subsets. Outliers are detected by taking the smallest average heights from the root node to the node where a datapoint finally end up.

A few datapoints are randomly selected and plotted with outliers marked.

The final file of of the original dataset with an outlier column added can be found at ```output/house_prices_with_outliers.csv```. ```outlier``` column values ```True``` indcate the datapoint is an outlier.

To try this, run
pip install -r requirements.txt
apt-get install python-tk
finally run ```main.py```
