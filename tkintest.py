from tkinter import *
from PIL import Image, ImageTk   # ini tambahan

root = Tk()
root.geometry('500x250')

# Baris baru ini yang ganti icon
img = Image.open('woi.ico')
photo = ImageTk.PhotoImage(img)
root.iconphoto(True, photo)

root.mainloop()
