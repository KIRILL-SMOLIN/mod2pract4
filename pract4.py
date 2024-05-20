    # Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
cars_mod = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(cars_mod)):
    print('Я езжу на автомабиле марки', cars_mod[i], end=' ')
    cars_count += 10
    print('и счетчик', cars_count)
