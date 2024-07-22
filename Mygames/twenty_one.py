import random
from time import sleep


playing_cards = {
    '2 буби': 2, '2 крести': 2, '2 черви': 2, '2 пики': 2,
    '3 буби': 3, '3 крести': 3, '3 черви': 3, '3 пики': 3,
    '4 буби': 4, '4 крести': 4, '4 черви': 4, '4 пики': 4,
    '5 буби': 5, '5 крести': 5, '5 черви': 5, '5 пики': 5,
    '6 буби': 6, '6 крести': 6, '6 черви': 6, '6 пики': 6,
    '7 буби': 7, '7 крести': 7, '7 черви': 7, '7 пики': 7,
    '8 буби': 8, '8 крести': 8, '8 черви': 8, '8 пики': 8,
    '9 буби': 9, '9 крести': 9, '9 черви': 9, '9 пики': 9,
    '10 буби': 10, '10 крести': 10, '10 черви': 10, '10 пики': 10,
    'Валет буби(4)': 4, 'Валет крести(4)': 4, 'Валет черви(4)': 4, 'Валет пики(4)': 4,
    'Дама буби(5)': 5, 'Дама крести(5)': 5, 'Дама черви(5)': 5, 'Дама пики(5)': 5,
    'Король буби(6)': 6, 'Король крести(6)': 6, 'Король черви(6)': 6, 'Король пики(6)': 6,
    'Туз буби(1)': 1, 'Туз крести(1)': 1, 'Туз черви(1)': 1, 'Туз пики(1)': 1,
}
player_result = []
bot_result = []
deposit21 = 0

def bot_choice(a=0, b=15):
    # Функция создана для уменьшения или увеличения шанса.
    return random.choice(list(range(a, b)))


def bot_sleep():
    # Функция для искуственного замедления выбора варианта бота
    return sleep(random.choice(list(range(2, 5))))


def rand_cards():
    ''' Функция преобразует словарь playing_cards в список из ключей.
     Рандомом выбирает ключ, выводит этот ключ.
     Добавляет в список result.
     И удаляет утот ключ, чтобы повторно его не использовать. '''
    cards_keys_list = list(playing_cards.keys())
    random_key = random.choice(cards_keys_list)
    print(f'Вам выпола карта: {random_key}\n')
    player_result.append(playing_cards[random_key])
    del playing_cards[random_key]


def bot_rand_cards():
    ''' Функция аналогична rand_cards,
    но с неболышими изменениями для работы бота'''
    cards_keys_list = list(playing_cards.keys())
    random_key = random.choice(cards_keys_list)
    print(f'\nСопернику выпола карта: {random_key}')
    bot_result.append(playing_cards[random_key])
    del playing_cards[random_key]


def add_cards():
    # Функция реализует раздачу карт
    plus_card = int(input('Желаете еще получить карту? 1 это Да, 2 это Нет '))
    print(plus_card)
    if plus_card == 1:
        rand_cards()
        print(f'У вас на данный момент: {sum(player_result)}')
        add_cards()
    if plus_card == 2:
        print(f'У вас сей час {sum(player_result)}, ждем раздачу сопернику')


def bot_cards():
    # Функция реализует выбор бота с шансом
    bot_rand_cards()
    print('Решение продолжить')
    bot_sleep()
    bot_rand_cards()
    print(f'Счёт соперника: {sum(bot_result)}')
    bot_sleep()
    if sum(bot_result) >= 18:
        if bot_choice(0, 15) == 2:
            bot_rand_cards()
    else:
        bot_rand_cards()
        print(f'Счёт соперника: {sum(bot_result)}')
        if sum(bot_result) == 21:
            print('\nСоперник решил отсановиться')
        elif sum(bot_result) <= 14:
            if bot_choice(2, 3) == 2:
                bot_rand_cards()
        elif 14 < sum(bot_result) < 18:
            if bot_choice(1, 3) == 2:
                bot_rand_cards()
        bot_sleep()
        print(f'Счёт соперника: {sum(bot_result)}')
        print('Соперник принял решение остановиться\n')


def game_twentyone(player_money):
    # Реализации игры
    print(f'На вашем счету {player_money}$')
    if player_money <= 0:
        print('К сожалению у вас закончились деньги')
        exit()
    else:
        bet = int(input('Введите вашу ставку: '))
    if bet < 0 or bet > player_money:
        game_twentyone(player_money)
    deposit = player_money - bet
    print("Раздача карт!")
    rand_cards()
    add_cards()
    print('Раздача карт сопернику\n')
    bot_cards()
    print('Вскрываем карты!\n')
    bot_sleep()
    print(f'Ваш счёт составляет: {sum(player_result)}, счёт соперника: {sum(bot_result)}')
    if (sum(player_result) > sum(bot_result)) and sum(player_result) <= 21:
        print('Поздравляем вы выйграли!')
        deposit += (bet *2)
        print(f'Ваш выйгрыш составил {bet}, на вышем счёту: {deposit}$')
    elif (sum(player_result) > 21 and sum(bot_result) > 21) or (sum(player_result) == sum(bot_result)):
        print("Ничья, и такое тоже бывает!")
        deposit += bet
        print(f'Hа вышем счету: {deposit}$')
    elif sum(bot_result) > 21 >= sum(player_result):
        print('Поздравляем вы выйграли!')
        deposit += (bet * 2)
        print(f'Ваш выйгрыш составил {bet}$, на вышем счету: {deposit}$')
    else:
        print('К сожалению вы проиграли :(')
        print(f'Hа вышем счету: {deposit}$')
    player_result.clear()
    bot_result.clear()
    if deposit > 0:
        continue_the_game = int(input('Желаете продолжить игру? 1 это да, 2 это нет: '))
        if continue_the_game == 1:
            game_twentyone(deposit)
        else:
            print('Будем рады видеть вас снова')
    else:
        print('Будем рады видеть вас снова')
        exit()
