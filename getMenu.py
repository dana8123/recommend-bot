import pandas as pd
import sys
print(sys.path)
sys.path.append('/home/ubnutu/bot')
def getMenu(random):
    data = pd.read_csv('/home/ubuntu/bot/data.csv')
    name = data.loc[:, 'name'][random]
    menu = data.loc[:, 'menu'][random]
    return {'name': name, 'menu':  menu}

