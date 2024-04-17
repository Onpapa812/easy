import random

def guess_number():
    number = random.randint(1, 100)
    
    print("Давай сыграем в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")
    
    attempts = 0
    while True:
        guess = int(input("Введи свой вариант: "))
        attempts += 1
        
        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_number()