import pandas as pd
import sys
import random
from dotenv import load_dotenv

load_dotenv()

LIMITNUM = os.environ['LIMITNUM']

sys.path.append('/home/ubnutu/bot')

randomNum = random.randrange(0,int(LIMITNUM))

def getMenu(random):
    data = pd.read_csv('/home/ubuntu/bot/data.csv')
    name = data.loc[:, 'name'][random]
    menu = data.loc[:, 'menu'][random]
    return {'name': name, 'menu':  menu}

return getMenu(randomNum)
