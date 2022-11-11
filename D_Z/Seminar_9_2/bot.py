from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from random import choice

fld = list(range(1,10))
x = chr(10060)
o = chr(11093)
count = 9
player = x
CHOISE = 0

def show_field(field):
    txt = ''
    for i in range(len(field)):
        if not i % 3:
            txt += f'\n{"-" * 25}\n'
        txt += f'{field[i]:^8}'
    txt += f"\n{'_' * 25}"
    return txt 

def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    n = [field[x[0]] for x in win_coord if field[x[0]] == field[x[1]] == field[x[2]]]
    return n[0] if n else n

def start(update, _):
    global fld, player, count
    fld = list(range(1,10))
    count = 9
    player = x
    update.massage.reply_text("Hi, let's play tic-tac-toe")
    update.massage.reply_text(show_field(fld))
    update.massage.reply_text(f'Go first {chr(10060)}')
    return CHOISE

def cancel(update, _):
    update.massage.reply_text('Bye', reply_markup = ReplyKeyboardRemove)
    return ConversationHandler.END

if __name__ == '__main__':
    updater =  Updater(token)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [ConversationHandler('start', start)],
        states = {
            CHOISE: [MessageHandler(Filters.text, choice)]
        },    
        fallbacks = [CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()
