# Basic tkinter template
from tkinter import*

root = Tk()

root.title("Driving_License")
root.geometry("400x200")



# Create all the labels required to be displayed
Label_id = Label(root)
Label_name = Label(root)
Label_birth = Label(root)
Label_adress = Label(root)
Label_author = Label(root)

# Define the function
def show():
    Label_id["text"]="I.D : 1999827709"
    Label_name["text"]="Name: Suryash Jha"
    Label_birth["text"]="Date Of Birth: 18.09.94"
    Label_adress["text"]="Adress: chhoti khanjerpur, Bhagalpur -812001, Bihar"
    Label_author["text"]="this card is issued for : two and for vehicels"
btn = Button(root,text = "show driving license",command=show)
    
    
# Create a button


btn.pack()
Label_id.pack()
Label_name.pack()
Label_birth.pack()
Label_adress.pack()
Label_author.pack()

root.mainloop()
# tkinter basic template end statement
