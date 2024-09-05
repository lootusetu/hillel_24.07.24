import  string
input data = string.ascii_letters

vvodnie_danie = input('введите диапазон букв \"пример: а-b\"')

start_letter, end_letter = vvodnie_danie.split('-')
start_letter = nabor_bukv.index(start_letter)
end_letter = nabor_bukv.index(end_letter)
print(nabor_bukv[start_letter:end_letter + 1])