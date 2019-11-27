from constants import feature_importance, scoring_features

def get_score(row):
	score = 0
	for feature, importance in feature_importance.items():
		score += (row[feature] * importance)

	return score

def get_zone_scores(df, by):
	grouped_df = df.groupby(by).mean()

	grouped_df['score'] = grouped_df.apply(lambda row: get_score(row), axis=1)
	grouped_df.sort_values('score', ascending=False, inplace=True)

	grouped_df[['score']].to_csv('output/scored_zones.csv')

	return grouped_df

def assign_score(row, scored_zones):
	zone_score = scored_zones.loc[row['zone']]
	return zone_score['score']

def assign_scores(df, score_by='zone'):
	scored_zones = get_zone_scores(df, score_by)

	df['score'] = df.apply(lambda row: assign_score(row, scored_zones), axis=1)
