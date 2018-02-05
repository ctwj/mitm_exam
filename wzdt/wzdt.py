#encoding=utf-8
import json
from mitmproxy import ctx
from urllib.parse import quote
import string
import requests
from RedisHelper import RedisHelper
obj = RedisHelper()

def writeIndex():
    pass

def readIndex():
    pass

def writeQuestion():
    pass

def writeAnswer():
    pass

def response(flow):
    path = flow.request.path
    if path == '/question/list':
        ctx.log.info(flow.request.text)
        try:
            data = json.loads(flow.response.text)
            question = data['data']['title']
            options = data['data']['options']
            ctx.log.info('question : %s, options : %s'%(question, options))
            options = ask(question, options)
            data['data']['options'] = options
            flow.response.text = json.dumps(data)
            obj.push(json.dumps(data))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        except Exception as e:
            print(e)
            ctx.log.info(e)



def ask(question, options):
    url = quote('https://www.baidu.com/s?wd=' + question, safe = string.printable)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    content = requests.get(url, headers=headers).text
    answer = []
    for option in options:
        key = option['name']
        count = content.count(key)
        ctx.log.info('option : %s, count : %s'%(option, count))
        answer.append(key + ' [' + str(count) + ']')
    return answer