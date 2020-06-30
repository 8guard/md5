from md5decrypt import *
from tkinter import *
from tkinter import messagebox

#создаем класс для мэйнфрейма
class App(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()
#создаем поле для ввода хэша
        self.entrythingy = Entry()
#располагаем поле
        self.entrythingy.pack()
#создаем кнопку для отправки хэша
        self.sendhash = Button(command=self.check_md5,text="Hesh out!")
#располагаем кнопку
        self.sendhash.pack()
#связываем кнопку с функцией вызывающую обработку вводимого значения (наш хэша)
        self.sendhash.bind("1", self.check_md5)


#функция создающая объект на осонове модуля md5decrypt.py
    def check_md5 (self):
#инициализируем функцию дешифрования
        md5 = decrypt_main()
        self.password = self.entrythingy.get()
        self.message = messagebox.showinfo(title="Информация",message=md5.check_password(self.password))

new_app = App()
new_app.master.title("hesh#sakura v0.1")
new_app.master.minsize(250, 50)
new_app.master.resizable(width=False, height=False)
new_app.mainloop()
