from md5decrypt import *
from tkinter import *
from tkinter import messagebox

class App(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        self.sendhash = Button(command=self.check_md5,text="Hesh out!")
        self.sendhash.pack()

        self.sendhash.bind("1", self.check_md5)



    def check_md5 (self):
        md5 = decrypt_main()
        self.password = self.entrythingy.get()
        md5.check_password(self.password)
        self.message = messagebox.showinfo(title="Информация",message=md5.check_password(self.password))

new_app = App()
new_app.master.title("hesh#sakura v0.1")
new_app.master.minsize(250, 50)
new_app.master.resizable(width=False, height=False)
new_app.mainloop()
