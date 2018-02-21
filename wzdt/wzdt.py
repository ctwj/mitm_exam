#encoding=utf-8
import json
from mitmproxy import ctx
from urllib.parse import quote
import string
import requests
from RedisHelper import RedisHelper
from MongoModel import  DataController
obj = RedisHelper()
db = DataController()

def writeIndex():
    pass

def readIndex():
    pass

def writeQuestion():
    pass

def writeAnswer():
    pass

def request(flow):
    pass
    # print ('request:')
    # print(flow.request.content)
    # print(type(flow.request.content))
    # flow.request.content = flow.request.content.replace('type=1','type=2')
    # print(flow.request.content)

def websocket_message(flow):
    ctx.log.info(flow)

def response(flow):
    path = flow.request.path
    # if 'findQuiz' in path:
    #         #匹配上后证明抓到的是问题了, 查答案
    #         data = flow.response.content
    #         quiz = json.loads(data)
    #         #获取问题，当前数据是模拟的，有可能和实际处理不一致
    #         question = quiz['quiz']
    #         print(question)

    #         #获取答案
    #         answer = self.answer_set.find_one({"quiz":question})
    #         if answer is None:
    #             print('no answer')
    #         else:
    #             answerIndex = int(answer['answer'])-1
    #             options = answer['options']
    #             print(options[answerIndex])
    
    if 'findQuiz' in path:
        ctx.log.info(path)
        try:
            print('start~~~~~~~~~~~~~~~~~~~~~~~~~~~start')
            print(flow.response.text)
            # decode response
            data = json.loads(flow.response.text)
            
            # get question and options
            question = data['data']['quiz']
            options = data['data']['options']
            ctx.log.info('question : %s, options : %s'%(question, options))

            data['data']['question'] = question
            # find answer from mongo
            answer = db.find_answer(question)
            if answer != False:
                data['data']['answer'] = answer
            else:
                # search result and put it in data
                result = ask(question, options)
                data['data']['result'] = result
                

            # push result to redis
            obj.public(json.dumps(data))
            ctx.log.info(json.dumps(data))
            print('over~~~~~~~~~~~~~~~~~~~~~~~~~~~over')

        except Exception as e:
            print(e)
            ctx.log.info(e)



def ask(question, options):
    url = quote('https://www.baidu.com/s?wd=' + question, safe = string.printable)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    content = requests.get(url, headers=headers).text
    answer = []
    for option in options:
        # key = option['name']
        key = option
        count = content.count(key)
        # count = 5
        ctx.log.info('option : %s, count : %s'%(option, count))
        answer.append({'name':option,'count':count})
    return answer