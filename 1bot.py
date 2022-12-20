# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# игрок и бот

from random import randint

def printgame(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, у него {counter}. Осталось разыграть {value} конфет.")

def get_candies(name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Ошибка, повторите ввод: "))
    return x


candies = 101
seq = randint(0,2)
if seq:
    print(f"По жребьевке первый игрок 1")
else:
    print(f"По жребьевке первый бот")

count1 = 0 
count2 = 0

while candies > 28:
    if seq == True:
        k = get_candies('игрок 1')
        count1 += k
        candies -= k
        seq = False
        printgame('игрок 1', k, count1, candies)
    else:
       # k = get_candies_bot('игрок 2')//
        k=randint(1,28)
        if candies <= 28:
            k=candies
        else:
            if candies<55:
                k=candies%28-1
        if candies == 57:
            k=27
        if candies == 57:
            k=28
        count2 += k
        candies -= k
        seq = True
        printgame('бот', k, count2, candies)

if seq:
    print(f"Выиграл игрок 1")
else:
    print(f"Выиграл бот")