import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from getMenu import getMenu
import random
from dotenv import load_dotenv

load_dotenv()

BOTTOKEN = os.environ['TOKEN']
APPTOKEN = os.environ['APPTOKEN']

recommend = getMenu()
menu = recommend['menu']
name = recommend['name']


app = App(token=BOTTOKEN)

# Listen to incoming message that contain 'hello'
@app.message('λ€μ')
def message_again(message, say):
    say(f"πλ€λ₯Έ μΆμ² λ©λ΄λ β­οΈ {menu}, μΆμ² μλΉμ β {name} μλλ€, <@{message['user']}>λπ« ")
    

if __name__ == "__main__":
    SocketModeHandler(app, APPTOKEN).start()
    
    
