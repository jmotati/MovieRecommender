# Movie Recommender Program 
# CNIT 481 Group Project
#Jacob Hessler, Jitesh Motati
import pandas as pd

# import data here...
url = 'https://raw.githubusercontent.com/jmotati/MovieRecommender/main/movies_metadata.csv'
df = pd.read_csv(url, error_bad_lines=False)

# clean data
clean_df = df[['title', 'overview', 'vote_average', 'vote_count']]
print(clean_df)

# train data

