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
#import tkinter for GUI creation and management.
# from tkinter import *

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

# movie_input = input("Please enter movie title: ")
# print(recommend_movie(movie_input))


# Program to make a simple
# login screen 
 
 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    password=passw_var.get()
    recommend_movie(name)
    rec_movie = recommend_movie(name)
    movie_name = tk.Label(root, text = rec_movie, font=('calibre',20, 'bold'))
    movie_name.grid(row=5,column=5)
    name_var.set("")
    passw_var.set("")
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Movie Title', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()