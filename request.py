# curl https://jummechu.slack.com/api/auth.test?token=xoxb-4673255390656-4673282943376-bMGm4DkzAAbIGAOqG27a6zvN


from getMenu import getMenu
import requests
import random
 
def post_message(token, channel, answer):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": answer}
    )

    print(response)
randomNum = random.randrange(0,15)
recommend = getMenu(randomNum)
menu = recommend['menu']
name = recommend['name']

message = f'오늘의 랜덤 메뉴는 {menu} 입니다~ 식당은 {name} 입니다~'
# slack.chat.post_message(channel, answer)  // post_message으로 대체
post_message('xoxb-4673255390656-4673282943376-bMGm4DkzAAbIGAOqG27a6zvN', '일반', message)