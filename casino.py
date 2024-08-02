from Mygames.twenty_one import game_twentyone
from Mygames.red_or_white import game_red_or_white


start_deposit = 100


def game_selection():
    choice_player = int(input('\nКакую игру выбирите? Если 21 очко то введите 1, Красное или белое 2, Выход 3: '))
    if choice_player == 1:
        print('Отлично, вы выбрали игру 21 очко, правила стандартны\n')
        game_twentyone(start_deposit)
        game_selection()
    elif choice_player == 2:
        print('\nОтлично, вы выбрали игру красное или белое.')
        print('Правила просты. Нужно выбрать красное или белое (шанс выйгрыша 50 %).\n')
        game_red_or_white(start_deposit)
        game_selection()
    elif choice_player == 3:
        print('Будем рады видеть вас снова!\n')
    else:
        print('Нужно выбрать одну из игры, попробуйте снова\n')
        game_selection()


print('\nРады вас приветствовать в нашем казино\n')
age_verification = int(input('Введите ваш возраст: '))
if age_verification < 18:
    print('К сожалению доступ к казино закрыт!')
else:
    print(f'При старте выдаётся депозит в размере {start_deposit}$, для каждой из игры')
    game_selection()
