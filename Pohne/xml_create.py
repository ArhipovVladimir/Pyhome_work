
def xml_create(data):
    n, l_n, t = data
    xml = '<xml>\n'
    xml += '       <name>{}</name>\n'\
        .format(n)
    xml += '       <last_name>{}</last_name>\n' \
        .format(l_n)
    xml += '       <pohne>{}</pohne>\n'\
        .format(t)
    xml += '</xml>'

    with open('Pohne.xml', 'a') as page:
        page.write(xml)

    return data