
# Командп Set-ExecutionPolicy RemoteSigned

# from isOdd import isOdd
# 
# #print(isOdd('1')) # //=> true
# #print(isOdd('5')) # //=> true
# 
# print(isOdd(0)) # //=> false
# print(isOdd(4)) # //=> false


# from progress.bar import Bar
# import time 
# 
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1) # Данным способом мы выставили задержку в 1 секунду перед каждым выполнением цикла.
#     # Do some work
#     bar.next()
# bar.finish()

# import emoji
# 
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))
# # Python is fun ❤
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# # Python is fun ❤️ #red heart, not black heart
# print(emoji.is_emoji("👍"))
# # True

import matplotlib.pyplot as plt
import numpy as np

#                                               Обрец с сайта.

# # Fixing random state for reproducibility
# np.random.seed(19680801)
# 
# 
# plt.rcdefaults()
# fig, ax = plt.subplots()
# 
# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))
# 
# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')
# 
# plt.show()

#                                               Обрец с лекции.

# my_list = [1, 2, 8, 3, 5, 10]
# 
# plt.plot(my_list)
# plt.show()






#                           БОТ.

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater("5704215037:AAFtYNTzAF4Y0_D4XPlOH8NWU1VlEbNojwQ")

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')

updater.start_polling()

updater.idle()