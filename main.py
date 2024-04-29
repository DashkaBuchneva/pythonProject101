# Игра КАМЕНЬ, НОЖНИЦЫ, БУМАГА
import random
player_score = 0
computer_score = 0
p = 0
player_name = input('Введите имя' '\n')
user_selection = input('Выберите - камень/ножницы/бумага (чтобы покинуть игру пишите "выйти") \n')
var = ['камень', 'ножницы', 'бумага']
comp_var = random.choice(var)

while p != 4:

    print(f"\n Ваш выбор - {user_selection}, выбор компьютера -  {comp_var}. \n")

    if user_selection == comp_var:
       break

    elif user_selection == 'камень':
        if comp_var == "ножницы":
            print("ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print("Общий счёт: у вас ", player_score, "у компьютера ", computer_score, "счёт: у вас ", player_score,
              "у компьютера ", computer_score)
        p = + 1

        break

    elif user_selection == "бумага":
        if comp_var == "камень":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print("Общий счёт: у вас ", player_score, "у компьютера", computer_score)
        p = + 1


        break

    elif user_selection == "бумага":
        if comp_var == "камень":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print("Общий счёт: у вас ", player_score, "у компьютера ", computer_score)
        p = + 1

        break

    elif user_selection == "ножницы":
        if comp_var == "бумага":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print("Обший счёт: у вас", player_score, "у компьютера", computer_score)
        p = + 1

        break

    else:
        player = input("Произошла ошибка ")
