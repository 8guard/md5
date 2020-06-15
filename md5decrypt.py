#используем моудль hashlib
import hashlib

class decrypt_main:
    hash_get = "none"
    #
    def check_password(self, hash_get):
        #пробуем прочитать файл с паролями
        try:
            pswdfile = open('password.txt','r')
            #начинаем генерировать хэши из файла (построчно)
            for password in pswdfile:
                gen_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
                print(gen_hash)
                #справниваем хэши, при удачном совпадении, выводим результат
                if hash_get == gen_hash:
                    print('пароль найден :', password)
                    break

        except:
            print("\nфайл password.txt не найден\n")
            print("пожалуйста создайте файл с паролями\n")
