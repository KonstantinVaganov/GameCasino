import random
from time import sleep


player_choice = []
result = []


def bot_sleep():
    # Функция для искуственного замедления выбора варианта бота
    return sleep(random.choice(list(range(2, 5))))


def random_red_of_white():
    return random.choice(['красное', 'белое'])


def game_red_or_white(player_money):
    # Реализации игры
    print(f'На вашем счету {player_money}$')
    if player_money <= 0:
        print('К сожалению у вас закончились деньги')
        exit()
    else:
        bet = int(input('Введите вашу ставку: '))
    if bet < 0 or bet > player_money:
        game_red_or_white(player_money)
    deposit = player_money - bet
    run_game = int(input('\nЕсли хотите выбрать Красное введите 1, Белое 2: '))
    if run_game == 1:
        player_choice.append('красное')
    elif run_game == 2:
        player_choice.append('белое')
    else:
        print('Нужно бырать один из вариантов')
        game_red_or_white()
    print(f'Вы выбрали: {player_choice}, запускаем рулетку!')
    bot_sleep()
    result.append(random_red_of_white())
    print(f'Выпало: {result}\n')
    if player_choice == result:
        print('Поздравляем вы выйграли!\n')
        deposit += (bet * 2)
        print(f'Hа вышем счету: {deposit}$')
    else:
        print('К сожалению ваша ставка не сыграла\n')
        print(f'Hа вышем счету: {deposit}$')
    player_choice.clear()
    result.clear()
    if deposit > 0:
        continue_the_game = int(input('Желаете продолжить игру? 1 это да, 2 это нет: '))
        if continue_the_game == 1:
            game_red_or_white(deposit)
        else:
            print('Будем рады видеть вас снова')
    else:
        print('Будем рады видеть вас снова')
        exit()
