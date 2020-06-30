#используем моудль hashlib
import hashlib
import json

class decrypt_main:
    def check_password(self, hash_get):
        self.hash_get = hash_get
        #проба открытия файла hashes.txt
        try:
            pswdfile = open('hashes.txt','r')
            #берем значение переменной из списка, и переводим её в md5 построчно
            for password in pswdfile:
                gen_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

                #сравнение результата из списка с введеным через функцию
                if hash_get == gen_hash:
                    #создаем файл с валидным хешем
                    dump_jfile = 'validhash.json'
                    with open(dump_jfile, 'w') as pws_obj:
                        #заносим значение password
                        json.dump("hash : " + hash_get + " значение: " + password, pws_obj, ensure_ascii=False)
                        #возвращаем подобранный хэш, для использования в tkinter
                        return password
                        break
                # если колличество символов равно 0, выводим сообщение о том что пользователь не задал хэш
                if len(hash_get) == 0:
                    return "Вы не задали хэш"
            #возвращаемся при неудачном подборе хэша
            else:
                return "Хэш не удалось подобрать"
            #если файл hashes.txt не найден в директории
        except:
            return "файл hashes.txt не найден\n"
