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
from tkinter import *

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

# GUI configurations
root = Tk()                   
root.title('Movie Reccomendation Application')   
root.minsize(900,600)
 
name_var=StringVar() #name variable
movie_name = Label(root) #empty label for multiple sorting

#program functions
def submit():
    global movie_name #global variable
    movie_name.destroy() #deletes variable
    txt_entry1=name_var.get()
    recommend_movie(txt_entry1)
    rec_movie = recommend_movie(txt_entry1)
    movie_name = Label(root, text = rec_movie, font=('calibre',18, 'bold'), relief='sunken', justify='left')
    movie_name.grid(column=4, row=4, padx=10, pady=10)
    name_var.set("")                


        #def sort_genre()
            #read csv file
            #display sorted data based on genre

        #def sort_rating()
            #read csv file
            #display sorted data based on genre

        #display main frame          
        #frame = Frame(root)
        #frame.pack()
        
#display Menu
menu = Menu(root)
menu.add_command(label='File')
menu.add_command(label='About')
root.config(menu=menu)
        
#Movie Title Sort
txt_lbl1 = Label(root,text = 'Movie Title',font = ('Times New Roman', 12))
txt_lbl1.grid(column=0, row=1)
        
txt_entry1 = Entry(root, width=20, textvariable = name_var)
txt_entry1.grid(column=1, row=1) 

btn1 = Button(root,text = 'Sort', command = submit) #add sort command func
btn1.grid(column=2, row=1)
        
#Movie Genre Sort
txt_lbl2 = Label(root,text = 'Movie Genre',font = ('Times New Roman', 12))
txt_lbl2.grid(column=0, row=2)
        
txt_entry2 = Entry(root,width=20)
txt_entry2.grid(column=1, row=2)

btn2 = Button(root, text='Sort') #add sort command func
btn2.grid(column=2, row=2)

#Movie Rating Sort
txt_lbl3 = Label(root,text = 'Movie Rating',font = ('Times New Roman', 12))
txt_lbl3.grid(column=0, row=3)
        
txt_entry3 = Entry(root,width=20)
txt_entry3.grid(column=1, row=3)  

btn3 = Button(root, text='Sort') #add sort command func
btn3.grid(column=2, row=3)


#display buttons
btn_one = Button(root, text='Exit', command=quit)
btn_one.grid(column=0, row=10)
      
root.mainloop() 