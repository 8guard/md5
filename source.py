#импортируем стандартную библиотеку для работы с md5, tkinter (gui), pil
import hashlib
import time
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()
window.geometry("300x50")
#визуальная составляющая (в процессе)
#canvas = Canvas (window,width=120,heigh=120)
#image = ImageTk.PhotoImage(Image.open("#"))
#canvas.create_image(-100,0,anchor=NW,image=image)
#scanvas.pack()
window.title("general hash md5 v.01")
#logging= Frame(window,heigh=0, width=0)
#ввод данные при лкм (событие)
def handle_click(event):
    if True:
        counter = 0
        #получаем значение введеное в tk entry(passwin)
        letsgo = paswin.get()
        try:

            #открываем файл с нашими паролям
            pswdfiles = open ('password.txt', 'r')
        #если не найден, то завершаем выполнение сценария
        except :
            print("Не найден файл с паролями: " + 'password.txt')
            print("Пожалуйста проверьте директорию: " + 'password.txt')
            quit()

        for password in pswdfiles:
            gen_password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
            start = time.time()
            print("Пробуем подобрать пароль %d : %s " % (counter,password.strip()))

            counter = counter + 1
            end = time.time()
            t_time = end - start
            if gen_password == letsgo:

                messagebox.showinfo("Хэш распознан", "пароль :" + password)
                print("\nПароль найден его значение -  : %s " % password)
                print("Времени потребовалось", t_time,"секунд")
                break
        else :
            messagebox.showinfo("Ничего нет ", "пароль не найден")
            print("Пароль не найден")

paswin = Entry(window, width=25)
btn1 = Button(window, text="Отправить hash")
btn1.bind("<1>", handle_click)
#располагаем кнопки и окно ввода текста
logging.pack()
paswin.pack()
btn1.pack()
window.mainloop()
