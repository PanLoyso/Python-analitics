name = input(str("Введите свою фамилию, имя, отчество через пробел: "))
stroka = []
for i in name.split():
    stroka.append(i[0].upper())
print('.'.join(stroka))