#3.7
print('#3.7')
familly=['mama', 'papa', 'gitler']
massege1 = f'Приглашаю вас на ужин, {familly[0].title()}.'
massege2 = f'Приглашаю вас на ужин, {familly[1].title()}.'
massege3 = f'Приглашаю вас на ужин, {familly[2].title()}.'
print(massege1)
print(massege2)
print(massege3)
del_name=familly.pop(2)
print(del_name + ' не захотели прийти :(')
familly.insert(0, 'Дедуля')
familly.insert(2, 'Тётя')
familly.append('Бабуля')
massege4 = f'Приглашаю вас на ужин, {familly[0].title()}.'
massege5 = f'Приглашаю вас на ужин, {familly[1].title()}.'
massege6 = f'Приглашаю вас на ужин, {familly[2].title()}.'
massege7 = f'Приглашаю вас на ужин, {familly[3].title()}.'
massege8 = f'Приглашаю вас на ужин, {familly[4].title()}.'
print(familly)
print(massege4)
print(massege5)
print(massege6)
print(massege7)
print(massege8)
nep1=familly.pop(0)
nep2=familly.pop(1)
nep3=familly.pop(2)
print('Соболезнуем, '+nep1)
print('Соболезнуем, '+nep2)
print('Соболезнуем, '+nep3)
massege9 = f'Приглашаю вас на ужин, {familly[0].title()}.'
massege10 = f'Приглашаю вас на ужин, {familly[1].title()}.'
print(massege9)
print(massege10)
print('Всего: ')
print(len(familly))
