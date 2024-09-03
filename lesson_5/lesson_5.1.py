import string
import keyword
punctuation = string.punctuation.replace('_', '')
keyword = keyword.kwlist
while True:

    log = input('Введите логин ')
    if log[0].isdigit():
        print(False)
        print('Логин не может начинаться с цифры')
    elif any(simbol.isupper() for simbol in log):
        print(False)
        print('Логин не может содержать заглавные буквы')
    elif any(simbol in punctuation for simbol in log):
        print(False)
        print('логин не может соддержать знаков пунктуации, кроме \'_\'')
    elif log in keyword:
         print(False)
    elif log.count('_') >= 2:
         print(False)
    else:
         print(True)
         break