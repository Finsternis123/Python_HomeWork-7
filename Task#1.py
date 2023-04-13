poem = input("Enter poem:").split()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
item = list()
for i in poem:
    k = 0
    for a in i:
        if a in volwes:
            k += 1
    item.append(k)
if len(set(item)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')