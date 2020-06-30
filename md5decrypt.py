#используем моудль hashlib
import hashlib
import json

class decrypt_main:
    hash_get = "none"
    #
    def check_password(self, hash_get):
        #пробуем прочитать файл с паролями
        try:
            pswdfile = open('hashes.txt','r')
            #начинаем генерировать хэши из файла (построчно)
            for password in pswdfile:
                gen_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

                #справниваем хэши, при удачном совпадении, выводим результат
                if hash_get == gen_hash:
                    print('\nхэш подобран, его значение :', password)
                    dump_jfile = 'validhash.json'
                    with open(dump_jfile, 'w') as pws_obj:
                        json.dump("hash : " + hash_get + " значение: " + password, pws_obj, ensure_ascii=False)
                        break
                elif hash_get == "none":
                    print("вы не ввели хэш")
            else :
                print("хэш не найден")
        except:
            print("\nфайл hashes.txt не найден\n")
            print("пожалуйста создайте файл с хешами\n")
