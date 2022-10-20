# main - будет одна кнопка запустить систему.

# Последний шаг.

import model_html_creater as hc
import xml_generator as xg
import model_data_provider as dp

# print(c())
# print(cr())

# hc.create(dp.data_collection())
# xg.create(dp.data_collection())
# hc.new_create(xg.create(dp.data_collection()))
hc.new_create(xg.new_create(dp.data_collection()))

