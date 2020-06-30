#используем моудль hashlib
import hashlib
import json

class decrypt_main:
    def check_password(self, hash_get):
        self.hash_get = hash_get
        #пробуем прочитать файл с паролями
        try:
            pswdfile = open('hashes.txt','r')
            #начинаем генерировать хэши из файла (построчно)
            for password in pswdfile:
                gen_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

                #справниваем хэши, при удачном совпадении, выводим результат
                if hash_get == gen_hash:
                    #print('\nхэш подобран, его значение :', password)
                    dump_jfile = 'validhash.json'
                    with open(dump_jfile, 'w') as pws_obj:
                        json.dump("hash : " + hash_get + " значение: " + password, pws_obj, ensure_ascii=False)
                        return password
                        break
                # если колличество символов равно 0, выводим значение о том что пароль не найден
                if len(hash_get) == 0:
                    return "Вы не задали хэш"
            #возвращаемся при неудачном подборе хэша
            else:
                return "Хэш не удалось подобрать"
            #если файл hashes.txt не найден в директории
        except:
            return "файл hashes.txt не найден\n"
            #print("\nфайл hashes.txt не найден\n")
            #print("пожалуйста создайте файл с хешами\n")
