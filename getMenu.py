import pandas as pd

def getMenu(random):
    data = pd.read_csv('./data.csv')
    name = data.loc[:, 'name'][random]
    menu = data.loc[:, 'menu'][random]
    return {'name': name, 'menu':  menu}

