print('Введите количество чисел в списке') # Кол-во элементов в списке
count_el = int(input())
list = [] # Будущий список
i = 0
el = 0
while i < count_el: # Создание цикла счётчика элементов
    list.append(input('Введите значение списка'))
    i += 1
for el in range(int(len(list)/2)): # Присвоение циклу формулы ревёрса элементов
    list[el], list[el+1] = list[el+1], list[el] # Присвоение равенства первого списка и списка с ревёрсом элементов
el += 2 # Шаг списка
print(list)
