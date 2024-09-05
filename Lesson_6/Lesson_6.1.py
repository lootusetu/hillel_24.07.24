import  string
input_data = string.ascii_letters

vvodnie_danie = input('введите диапазон букв \"пример: а-b\"')

start_letter, end_letter = vvodnie_danie.split('-')
start_letter = input_data.index(start_letter)
end_letter = input_data.index(end_letter)
print(input_data[start_letter:end_letter + 1])