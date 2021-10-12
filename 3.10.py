#3.10
print('#3.10')
list=['1', '5', '4', '3', '2']
print (list)
messege11 = f'Вам нраится цифра {list[0]}.'
print(messege11)
deleted=list.pop(1)
print('Число '+deleted+' было удалено\n')
print('удалил 4-й элемент списка:')
del list[3]
print (list)
print('отсортировано (список):')
print(sorted(list)) #отсортированный
print(list) #дефолтно
print('обратный:')
list.reverse()
print(list) #обратный
list.reverse()
print('отсортировано по списку:')
list.sort()
print(list) #отсортированный
print('обратный и отсортированный:')
list.sort(reverse=1)
print(list) #обратный и отсортированный

