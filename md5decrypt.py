#используем моудль hashlib
import hashlib
import json

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
                print(password)
                #справниваем хэши, при удачном совпадении, выводим результат
                if hash_get == gen_hash:
                    print('пароль найден :', password)
                    dump_jfile = 'password.json'
                    with open(dump_jfile, 'w') as pws_obj:
                        json.dump(password, pws_obj)
                        break
            else :
                print("не нашли пароль")
        except:
            print("\nфайл password.txt не найден\n")
            print("пожалуйста создайте файл с паролями\n")
