#!/usr/bin/env python
#coding=utf-8
import sys
import json
from mitmproxy import flowfilter
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding('utf-8')

'''
头脑王者即时显示答案脚本
'''

class TNWZ:
    '''
    从抓包可以看到 问题包的链接最后是 findQuiz
    '''
    def __init__(self):
        #添加一个过滤器，只处理问题包
        self.filter = flowfilter.parse('~u findQuiz')
       #连接答案数据库
        self.conn = MongoClient('localhost', 27017)
        self.db = self.conn.tnwz
        self.answer_set = self.db.quizzes

    def request(self, flow):
        '''
        演示request事件效果, 请求的时候输出提示
        :param flow: 
        :return: 
        '''
        if flowfilter.match(self.filter,flow):
            print(u'准备请求答案')

    def responseheaders(self, flow):
         '''
        演示responseheaders事件效果, 添加头信息
        :param flow: 
        :return: 
        '''
        if flowfilter.match(self.filter, flow):
            flow.response.headers['Cache-Control'] = 'no-cache'
            flow.response.headers['Pragma'] = 'no-cache'

    def response(self, flow):
        '''
        HTTPEvent 下面所有事件参数都是 flow 类型 HTTPFlow
        可以在API下面查到 HTTPFlow, 下面有一个属性response 类型 TTPResponse
        HTTPResponse 有个属性为 content 就是response在内容,更多属性可以查看 文档
        :param flow: 
        :return: 
        '''

        if flowfilter.match(self.filter, flow):
            #匹配上后证明抓到的是问题了, 查答案
            data = flow.response.content
            quiz = json.loads(data)
            #获取问题
            question = quiz['quiz']
            print(question)

            #获取答案
            answer = self.answer_set.find_one({"quiz":question})
            if answer is None:
                print('no answer')
            else:
                answerIndex = int(answer['answer'])-1
                options = answer['options']
                print(options[answerIndex])

#这里简单演示下start事件
def start():
    return TNWZ()