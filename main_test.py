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
ratings_df = movie_data[['title', 'vote_average']]
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
rand_mov_var=StringVar()
movie_name = Label(root) #empty label for multiple sorting
rand_mov = Label(root)
mov_rating = Label(root)

#program functions
# movie recommendation with ML
def rec_movie_ml():
    global movie_name #global variable
    mov_genre.destroy()
    rand_mov.destroy()
    movie_name.destroy() #deletes variable
    txt_entry1=name_var.get()
    recommend_movie(txt_entry1)
    rec_movie = recommend_movie(txt_entry1)
    movie_name = Label(root, text = rec_movie, font=('calibre',18, 'bold'), relief='sunken', justify='left')
    movie_name.grid(column=4, row=4, padx=10, pady=10)
    name_var.set("")           

        #def sort_rating()
            #read csv file
            #display sorted data based on genre

        #display main frame          
        #frame = Frame(root)
        #frame.pack()

# movie recommendation based on true randomness
def rand_movie():
    
    global rand_mov #global variable
    mov_genre.destroy()
    rand_mov.destroy()
    movie_name.destroy() #deletes variable
    #txt_entry2=rand_mov_var.get()
    row_select = clean_df.sample()
    rand_mov = Label(root, text = row_select, font=('calibre',18, 'bold'), relief='sunken', justify='left')
    rand_mov.grid(column=4, row=4, padx=10, pady=10)
    #rand_mov_var.set("")

def rating_sort():

    global mov_rating #global variable
    mov_rating.destroy()
    rand_mov.destroy()
    movie_name.destroy() #deletes variable
    #txt_entry2=rand_mov_var.get()
    #sorted_df = ratings_df.sort_values(by='vote_average', ascending=False,na_position='first')
    sorted_df = ratings_df.nlargest(10,'vote_average')
    mov_rating = Label(root, text = sorted_df, font=('calibre',18, 'bold'), relief='sunken', justify='left')
    mov_rating.grid(column=4, row=4, padx=(100, 10))

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

btn1 = Button(root,text = 'Recommennd', command = rec_movie_ml) #add sort command func
btn1.grid(column=2, row=1)
        
#Movie Genre Sort
txt_lbl2 = Label(root,text = 'Recommend Random Movie',font = ('Times New Roman', 12))
txt_lbl2.grid(column=0, row=2)
        
#txt_entry2 = Entry(root,width=20, textvariable = rand_mov_var)
#txt_entry2.grid(column=1, row=2)

btn2 = Button(root, text='Generate', command = rand_movie) #add sort command func
btn2.grid(column=2, row=2)

#Movie Rating Sort
txt_lbl4 = Label(root,text = 'Top Rated Movies',font = ('Times New Roman', 12))
txt_lbl4.grid(column=0, row=4)
        
#txt_entry3 = Entry(root,width=20, textvariable = genre_var)
#txt_entry3.grid(column=1, row=3)  

btn4 = Button(root, text='Show', command = rating_sort) #add sort command func
btn4.grid(column=2, row=4)


#display buttons
btn_one = Button(root, text='Exit', command=quit)
btn_one.grid(column=0, row=10)
      
root.mainloop() 