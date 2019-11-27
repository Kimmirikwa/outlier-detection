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

	return grouped_df.reset_index()  # will enable us get the rank of zone

def assign_score(row, scored_zones):
	rank = scored_zones.index[scored_zones['zone'] == row['zone']].tolist()[0] + 1
	return rank

def assign_scores(df, score_by='zone'):
	scored_zones = get_zone_scores(df, score_by)

	#scored_zones = scored_zones.reset_index()

	df['zone_rank'] = df.apply(lambda row: assign_score(row, scored_zones), axis=1)
