from tkinter import *
from PIL import Image, ImageTk 
root = Tk()
root.geometry('500x250')
root.title('ZAMNN') 


img = Image.open('woi.ico')
photo = ImageTk.PhotoImage(img)
root.iconphoto(True, photo) 

root.mainloop()

