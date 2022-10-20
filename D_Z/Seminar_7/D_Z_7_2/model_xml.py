def create():
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        my_lyst = f_1.readlines()
        result = []
        for i in range(len(my_lyst)):
            a = my_lyst[i]
            a = a[:-1]
            result.append(a) 
        xml = '<xml>\n' 
        xml += '    <temperature units = "c">{}</temperature>\n'\
            .format(result)
        xml += '</xml>'

        with open('file_2.xml', 'w') as f_2: 
            f_2.write(xml)

        return xml


create()