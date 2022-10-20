import model_mistake as mistake
import model_conclusion as mc
import model_search as ms
import model_data as md
import model_change as change
import model_delete as delete
import model_html as mh
import model_xml as mx

def menu():
    number = int(input('Введите 1 для вывода справочника на экран: \n\
Введите 2 для поиска пользователя в спавочнике: \n\
Введите 3 для добавления информации в справочник: \n\
Введите 4 для изменения информации в спавочнике: \n\
Введите 5 для удаления информации из справочника: \n\
Введите 6 для конвертации файла в html: \n\
Введите 7 для конвертации файла в xml: \n'))
    if number < 8 and number > 0:
        if number == 1:
            mc.conclusion()
        elif number == 2:
            ms.search_user()
        elif number == 3:
            t = int(input('Введите количетсво пользователей планируемых к добавлению: \n'))
            while t:
                md.creating_a_directory()
                t-=1
                if t > 0:
                    print('Введите данные следующего пользовтеля: ')
        elif number == 4:
            change.change()
        elif number == 5:
            t = int(input('Введите количетсво пользователей планируемых к удалению: \n'))
            while t:
                delete.delete()
                t-=1
                if t > 0:
                    print('Введите данные следующего пользовтеля: ')
        elif number == 6:
            mh.create()
        else:
            mx.create()
    else:
        mistake.mistake()
