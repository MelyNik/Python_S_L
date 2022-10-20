# Controller - модуль так скажем связующий модуля task1_model.py и view.py(интерфейс)

import model_sub as model # Таким образом мы импортировали эти модули в модуль controller.
import view        # Таким образом мы импортировали эти модули в модуль controller.

def button_click(): # button - так называемае кнопка.
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, model.name())