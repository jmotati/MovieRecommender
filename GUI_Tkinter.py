from tkinter import *

# GUI configurations
root = Tk()                
root.title('Movie Reccomendation Application')   
root.minsize(900,600)      

name_var=StringVar() #define variables

#program functions
def submit(): 
    name=name_var.get()
    print_label = Label(root, text = name,font = ('Times New Roman', 12))
    print_label.grid(column=0, row=4)
    name_var.set("")

        #def sort_title()
            #read csv file
            #display sorted data based on a title

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
        
txt_entry1 = Entry(root, textvariable=name_var, width=10)
txt_entry1.grid(column=1, row=1) 

btn1 = Button(root, text='Sort', command=submit) #add sort command func
btn1.grid(column=2, row=1)
        
#Movie Genre Sort
txt_lbl2 = Label(root,text = 'Movie Genre',font = ('Times New Roman', 12))
txt_lbl2.grid(column=0, row=2)
        
txt_entry2 = Entry(root,width=10)
txt_entry2.grid(column=1, row=2)

btn2 = Button(root, text='Sort') #add sort command func
btn2.grid(column=2, row=2)

#Movie Rating Sort
txt_lbl3 = Label(root,text = 'Movie Rating',font = ('Times New Roman', 12))
txt_lbl3.grid(column=0, row=3)
        
txt_entry3 = Entry(root,width=10)
txt_entry3.grid(column=1, row=3)  

btn3 = Button(root, text='Sort') #add sort command func
btn3.grid(column=2, row=3)

        #TO DO - Figure out how to add input to csv dataset.

#display buttons
btn_one = Button(root, text='Exit', command=quit)
btn_one.grid(column=0, row=10)

root.mainloop()         