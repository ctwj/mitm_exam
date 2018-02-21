#WZDT

1. redis
2. mongo
3. mitmproxy
4. flask
5. websocket
6. docker

系统启动
```
docker-compose up
#第一次启动后导入题目
docker cp ./docker/quizzes.json wzdt_mongo:/root/quizzes.json
docker exec -it wzdt_mongo mongoimport -d wzdt -c questions --file /root/quizzes.json --jsonArray --drop
docker exec -it wzdt_mongo rm /root/quizzes.json
```
1. 系统启动后,手机连上wifi设置代理为8080
2. 访问http://mitm.it,并安装证书(第一次使用需要安装)
3. 访问http://localhost:5000






















POST https://api.ttzhongqian.com/question/free
{
    "code": "SUCCESS",
    "data": {
        "hasCount": 870,
        "isChance": 1,
        "islimit": 0,
        "surplusCount": 130
    },
    "msg": "success"
}
 POST https://api.ttzhongqian.com/question/list
{
    "code": "SUCCESS",
    "data": {
        "answerFalse": 0,
        "answerRight": 0,
        "countdown": 10,
        "integral": 0,
        "isover": 0,
        "options": [
            {
                "id": "A",
                "name": "65"
            },
            {
                "id": "B",
                "name": "66"
            },
            {
                "id": "C",
                "name": "68"
            }
        ],
        "title": "柯南道尔写了多少部侦探小说",
        "totalQuestion": 8,
        "uaId": "1691961"
    },
    "msg": "成功"
}
POST https://api.ttzhongqian.com/question/answer

loginKey: 19c1b2d8039c3775f0aac47c72009024
uaId:     1691961
answer:   B

{
    "code": "SUCCESS",
    "data": {
        "answer": "C",
        "result": 0
    },
    "msg": "完成"
}

POST https://api.ttzhongqian.com/account/over