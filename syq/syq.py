#/bin/env python
#coding=utf-8

import json

# 抓取损友圈,websocket信息并写入日志
# 从日志里面可以看到,只要找到token算法是可以自定义色子点数的

def websocket_message(flow):
    with open('/script/log', mode='a+', encoding='utf-8') as f:
        content_list = [str(x.content,encoding='utf-8') for x in flow.messages]
        for x in content_list:
            js = json.loads(x, encoding='utf-8')
            print(type(js))
            if 'cmd' in js and js['cmd'] in ['keepLive', 'tolog', 'suc', 'MSG', 'MOC']:
                #丢弃一些不关心的数据
                pass
            else:
                f.writelines(x + "\n")
