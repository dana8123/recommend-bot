# recommend lunch slack bot, at hakdong station

### stack

`ec2`  
`python3`  
`ubuntu`

### todo

- [x] slack bot link
- [x] menu data csv
- [x] random function
- [x] crontab

## How to use

### slack api 설정

1. 환경변수 파일에 TOKEN, CHANNEL 필요.

### 배포

1. `git clone https://github.com/dana8123/recommend-bot.git`
2. `pip install requirements.txt`
3. `apt update -y`
4. `apt install -y cron`
5. `sudo service cron start`
6. `sudo systemctl enable cron.service`
7. `crontab -e`
   - 크론 수식 및 실행할 파일 삽입  
     ex : `20 11 \* \* 1-5 /home/ubuntu/bot/start.sh`
8. timezone 설정
   ``
9. 수정한 timezone을 적용시키기 위해 cron restart
   `sudo service cron restart`
