from md5decrypt import *
from tkinter import Tk, Entry, Button
from tkinter import messagebox

md5 = decrypt_main()
def lhandclick(event):
    if True:
        md5.check_password(enter_hash.get())
#создаем графический интерфейс используя tkinter
mainfraim = Tk()
#создаем окно размером 450x150
mainfraim.resizable(width=False,height=False)
mainfraim.geometry("321x32")
#добавляем титул
mainfraim.title("md5 encrypted")
#делаем окно ввода нашего хэша
enter_hash = Entry(mainfraim, width=20)
input_button = Button(mainfraim, text="отправить хэш")
enter_hash.grid(row=0,column=0,columnspan=3)
input_button.grid(row=0, column=6,columnspan=5)
input_button.bind("<1>", lhandclick)
mainfraim.mainloop()
