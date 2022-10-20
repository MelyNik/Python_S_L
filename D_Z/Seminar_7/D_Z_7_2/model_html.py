def create():
    with open('guide.csv', 'r', encoding='utf-8') as f_1:
        my_lyst = f_1.readlines()
        result = []
        for i in range(len(my_lyst)):
            a = my_lyst[i]
            a = a[:-1]
            result.append(a)         
        style = 'style="font-size:50px"' 
        html = '<html>\n <head></head>\n  <body>\n'
        html += '    <p {}>Guide: {} </p>\n'\
            .format(style,  result)
        html += '  </body>\n</html>'
        print(html)
        with open('file.html', 'w') as f_2:
            f_2.write(html)

        return html

create()