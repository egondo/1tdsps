estadios = {}

estadios['Sao Paulo'] = 'Morumbi'
estadios['Palmeiras'] = 'Allianz Parque'
estadios['Corinthians'] = 'Arena Corinthians'
estadios['Juventus'] = 'Rua Javari'
estadios['Portuguesa'] = 'Canindé'

for chave in estadios.keys():
    print(f'{chave} => {estadios[chave]}')


for valor in estadios.values():
    print(valor)
