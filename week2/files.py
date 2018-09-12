text_modes = [
    'r', # чтение - только для существующих файлов
    'w', # запись - создает файл
    'a', # дозапись
    'r+' # чтение и запись - только для существующих файлов
]
binary_modes = [
    'br',
    'bw',
    'ba',
    'br+'
]

f = open('_test.txt', 'w')
f.write('My first line\nMy second line')
f.close()

f = open('_test.txt', 'r+')
print(f.read()) # весь файл
print(f.tell()) #Сообщает позицию курсора в файле - например 29
print(f.read()) #пустая строка, так как мы в конце
f.seek(0) # перевод курсора в начало файла
print(f.tell()) #теперь будет 0, так что файл снова можно читать
f.close()

f = open('_test.txt', 'r+')
print(f.readline()) #прочитать одну строку (с символом перехода)
f.close()

f = open('_test.txt', 'r+')
f.write("test line 1\rtest line 2\r\ntest line 3\ntest line 4") # \r is also considered as end of line
f.close()
f = open('_test.txt', 'r+')
f2 = open('_test_double.txt', 'w')

for i in range(4):
    line = f.readline() #
    f2.write(line)
    print(line)
f.close()
f2.close()

f = open('_test.txt', 'r+')
lines = f.readlines() #Считывает все строки файла как список - одна строка это один элемент списка
f.close()
print(type(lines))
print(lines)

print("Context manager")
with open('_test.txt') as f: #контекстный менеджер
    print(f.read())

f = open('_test.txt', 'bw') # Чтобы записать не английский текст
f.write('Моя первая строка\nМоя вторая строка'.encode())
f.close()

f = open('_test.txt', 'w', encoding="utf-8") #to work with Unicode
f.write('Моя первая строка\nМоя вторая строка')
f.close()

f = open('_test.txt', 'r+', encoding="utf-8") #to work with Unicode
print(f.readline())
f.close()
