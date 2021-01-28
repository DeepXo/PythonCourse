str_1 = input("введите строку ") #Ввод исходных значений
word = [] #Слово
num = 1 #Номер строки
for el in range(str_1.count(' ') + 1):
    word = str_1.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [el]}")
        num += 1
    else:
        print(f" {num} {word [el] [0:10]}")
        num += 1