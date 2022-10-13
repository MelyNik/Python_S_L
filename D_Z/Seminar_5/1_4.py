# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
# Открывать под VPN
# Ссылка https://informatika.shkolkovo.net/catalog/igry/prostejshie-igry-poisk-vyigryshnoj-strategii

number = int(input('Play with bot 1 - yes, 0 - no\n'))
if number < 2 and number > -1:
    if number == 1:
        print('1 player - human, 2 player - bot')
        
    else:
        print('1 player - human, 2 player - person')
else:
    print('EROR!!! The number does not fit')