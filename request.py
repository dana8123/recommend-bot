from getMenu import getMenu
import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
CHANNEL = os.environ['CHANNEL']

print(CHANNEL, TOKEN)

def post_message(token, channel, answer):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+str(token)},
        data={"channel": str(channel),"text": str(answer)}
    )

    print(str(channel) + '로 전송 완료')
randomNum = random.randrange(0,29)
recommend = getMenu(randomNum)
menu = recommend['menu']
name = recommend['name']

message = f'오늘의 랜덤 메뉴는 {menu} 입니다~ 추천 식당은 {name} 입니다~'
# slack.chat.post_message(channel, answer)  // post_message으로 대체
post_message(TOKEN, CHANNEL, message)
