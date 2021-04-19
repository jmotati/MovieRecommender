from tkinter import *
class Application:
    def __init__(self, master):
    
        #program functions


        #display main frame          
        frame = Frame(master)
        frame.pack()
        
        #display Menu
        menu = Menu(master)
        menu.add_command(label='File')
        menu.add_command(label='About')
        master.config(menu=menu)

        #display title label
        title_label = Label(master,
            text = 'Movie Reccommender Application',
            font = ('Bebas Neue', 18),
            justify="left")
        title_label.pack(pady=20)

        #Textboxes
        txt_lbl1 = Label(master,text = 'Name',font = ('Times New Roman', 12))
        txt_lbl1.pack()
        
        txt_entry = Entry(master,width=10)
        txt_entry.pack()
        
        #display Movie Dataset
        lbl = Label(master,
            text = 'Display Movie Dataset Here',
            font = ('Times New Roman', 12))
        lbl.pack()

        #display buttons
        btn_one = Button(master, text='Exit', command=quit)
        btn_one.pack(side=BOTTOM)

# GUI configurations
root = Tk()                
app = Application(root)    
root.title('Movie Reccomendation Application')   
root.minsize(500,500)      
root.mainloop()            