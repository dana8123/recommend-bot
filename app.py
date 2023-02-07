import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from getMenu import getMenu
import random
from dotenv import load_dotenv

load_dotenv()

BOTTOKEN = os.environ['TOKEN']
APPTOKEN = os.environ['APPTOKEN']
LIMITNUM = os.environ['LIMITNUM']

randomNum = random.randrange(0,int(LIMITNUM))
recommend = getMenu(randomNum)
menu = recommend['menu']
name = recommend['name']


app = App(token=BOTTOKEN)

# Listen to incoming message that contain 'hello'
@app.message('다시')
def message_again(message, say):
    say(f"🔊다른 추천 메뉴는 ⭐️ {menu}, 추천 식당은 ✅ {name} 입니다, <@{message['user']}>님🫠")
    

if __name__ == "__main__":
    SocketModeHandler(app, APPTOKEN).start()
    
    