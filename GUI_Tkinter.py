from tkinter import *
class Application:
    def __init__(self, master):
    
        #program functions


        #display main frame          
        #frame = Frame(master)
        #frame.pack()
        
        #display Menu
        menu = Menu(master)
        menu.add_command(label='File')
        menu.add_command(label='About')
        master.config(menu=menu)

        #display title label
        title_label = Label(master,
            text = 'Movie Reccommendation',
            font = ('Bebas Neue', 18),
            justify="left")
        title_label.grid(column=0, row=0)
        #Textboxes
        txt_lbl1 = Label(master,text = 'Movie Title',font = ('Times New Roman', 12))
        txt_lbl1.grid(column=0, row=1)
        
        txt_entry1 = Entry(master,width=10)
        txt_entry1.grid(column=1, row=1) 
        
        txt_lbl2 = Label(master,text = 'Movie Genre',font = ('Times New Roman', 12))
        txt_lbl2.grid(column=0, row=2)
        
        txt_entry2 = Entry(master,width=10)
        txt_entry2.grid(column=1, row=2)

        txt_lbl3 = Label(master,text = 'Movie Rating',font = ('Times New Roman', 12))
        txt_lbl3.grid(column=0, row=3)
        
        txt_entry3 = Entry(master,width=10)
        txt_entry3.grid(column=1, row=3)  

        #TO DO - Figure out how to add input to csv dataset.

        #display Movie Dataset
        lbl = Label(master,
            text = 'Display Movie Dataset Here',
            font = ('Times New Roman', 12))
        lbl.grid(column=0, row=4)

        #display buttons
        btn_one = Button(master, text='Exit', command=quit)
        btn_one.grid(column=0, row=5)

# GUI configurations
root = Tk()                
app = Application(root)    
root.title('Movie Reccomendation Application')   
root.minsize(500,500)      
root.mainloop()            