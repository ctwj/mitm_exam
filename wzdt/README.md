###用到的东西

1. redis
2. mongo
3. mitmproxy
4. tornado
5. websocket
6. docker

###环境需求
1. docker
###代码
```
https://github.com/ctwj/mitm_exam/tree/master/wzdt
```

###启动方法
```
docker-compose up
#第一次启动后导入题目
docker cp ./docker/quizzes.json wzdt_mongo:/root/quizzes.json
docker exec -it wzdt_mongo mongoimport -d wzdt -c questions --file /root/quizzes.json --jsonArray --drop
docker exec -it wzdt_mongo rm /root/quizzes.json
```
###使用方法
1. 系统启动后,手机连上wifi设置代理为8080
2. 访问http://mitm.it,并安装证书*(第一次使用需要安装)*
3. 访问http://localhost:5000
如下图, 开始答题后,浏览器会自动显示答案, 系统有答案的话会显示一个勾,没有答案会百度问题,系统答案出现次数
![demo](http://upload-images.jianshu.io/upload_images/5941869-167d8df4ae044fb5.gif?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###系统关闭
`Ctrl`+`C`停止系统, `docker-compose down` 移除系统


