## 1 Задание 
высота = int(input("Введите высоту прямоугольника:"))
ширина = int(input("Введите ширину прямоугольника:"))

for i in range(высота):
    for j in range(ширина):
        print("*", end="")
    print ()
## 2 Задание 
N = int(input("Введите N (до какого числа):"))
M = int(input("Введите M (до какой степени):"))

for i in range(1,N+1):
    for j in range(1, M+1):
        print(f"{i}^{j} = {i ** j}", end  =", ")
    print()
## 3 Задание
seconds = int(input("Введите количество секунд: "))

while seconds > 0:
    print(seconds)
    seconds -= 1

print("Время истекло!")
## 4 Задание 
import random  
secret_number = random.randint(1, 100) 
guess = None  
while guess != secret_number:
    guess = int(input("Ваше число: "))
    
    if guess < secret_number:
        print("Загаданное число больше!")
    elif guess > secret_number:
        print("Загаданное число меньше!")
    else:
        print("Вы угадали число!")

