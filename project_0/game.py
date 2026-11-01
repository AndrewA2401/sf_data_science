import numpy as np
number = np.random.randint(1, 101) # загадываем число
count = 0 # количество попыток
while True:
    count += 1
    predict_number = int(input("Угадайте число от 1 до 100: "))
    if predict_number > number:
        print("Ваше число больше загаданного, попробуйте еще раз.")
    elif predict_number < number:
        print("Ваше число меньше загаданного, попробуйте еще раз.")
    else:
        print(f"Поздравляем! Вы угадали число {number} за {count} попыток.")
        break
