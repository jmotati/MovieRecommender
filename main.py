# Movie Recommender Program 
# CNIT 481 Group Project
#Jacob Hessler, Jitesh Motati

# import pandas to import data and clean data
import pandas as pd
# import sklearn to train data
import sklearn
# define the vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# import linear kernel function from sklearn, helps create a similarity matrix (how similar two things are)
from sklearn.metrics.pairwise import linear_kernel

# import data here...
url = 'https://raw.githubusercontent.com/jmotati/MovieRecommender/main/movies_metadata.csv'
movie_data = pd.read_csv(url, error_bad_lines = False, low_memory = False)

# clean data
clean_df = movie_data[['title', 'overview', 'vote_average', 'vote_count']]
#print(clean_df)

# remove words such as 'the' 'a', etc to make it easier to recommend
tfidf_vector = TfidfVectorizer(stop_words = 'english')

# replace null values with empty string
movie_data['overview'] = movie_data['overview'].fillna('')

# construct matrix by fitting and transforming data
tfidf_matrix = tfidf_vector.fit_transform(movie_data['overview'])

# simiilarity matrix
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
# construct map of indices andmovie titles and clean the titles so duplicates are dropped
indices = pd.Series(movie_data.index, index = movie_data['title']).drop_duplicates()
indices[:10]

# function to recommend movies based on similarity
def recommend_movie(title, sim_scores = sim_matrix):
    idx = indices[title]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movie_data['title'].iloc[movie_indices]

movie_input = input("Please enter movie title: ")
print(recommend_movie(movie_input))
