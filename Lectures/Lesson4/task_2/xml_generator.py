# create - так скажем кнопочка создать.


from model_user_interface import temperature_view
from model_user_interface import pressure_view
from model_user_interface import wind_speed_view

def create(device = 1):
    xml = '<xml>\n' 
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(wind_speed_view(device))
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(pressure_view(device))
    xml += '</xml>'

    with open('data.xml', 'w') as page: # page - перевод как страница.
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n' 
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(w)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page: # page - перевод как страница.
        page.write(xml)

    return data