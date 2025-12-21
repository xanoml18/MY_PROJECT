from tkinter import *
from PIL import Image, ImageTk  # ini penting!

root = Tk()
root.geometry('500x250')
root.title('Test Icon Gw')  # optional, biar keliatan judul

# Baris ini yang set icon
img = Image.open('woi.ico')
photo = ImageTk.PhotoImage(img)
root.iconphoto(True, photo)  # True biar apply ke semua window

root.mainloop()
