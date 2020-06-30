from md5decrypt import *
from tkinter import *

class App(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        self.sendbutton = Button(command=self.check_md5,text="Hesh out!")
        self.sendbutton.pack()

        self.sendbutton.bind("1", self.check_md5)


    def check_md5 (self):
        md5 = decrypt_main()
        self.password = self.entrythingy.get()
        md5.check_password(self.password)
        print(md5.hash_get)

new_app = App()
new_app.master.title("md5decrypt")
new_app.master.minsize(250, 50)
new_app.master.resizable(width=False, height=False)
new_app.mainloop()
