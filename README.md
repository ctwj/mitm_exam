# mitm_exam



## 版本和文档
###**python** *2.7*   +    **mitmproxy** *0.18.2*

*   [文档][http://docs.mitmproxy.org/en/v0.18.2/index.html](http://docs.mitmproxy.org/en/v0.18.2/index.html)
*   [事件][http://docs.mitmproxy.org/en/v0.18.2/scripting/events.html](http://docs.mitmproxy.org/en/v0.18.2/scripting/events.html)
*   [API][http://docs.mitmproxy.org/en/v0.18.2/scripting/api.html](http://docs.mitmproxy.org/en/v0.18.2/scripting/api.html)
*   [mitmproxy.models.http.HTTPRequest](http://docs.mitmproxy.org/en/v0.18.2/scripting/api.html#mitmproxy.models.http.HTTPRequest)
*   [mitmproxy.models.http.HTTPResponse](http://docs.mitmproxy.org/en/v0.18.2/scripting/api.html#mitmproxy.models.http.HTTPResponse)
*   [mitmproxy.models.http.HTTPFlow](http://docs.mitmproxy.org/en/v0.18.2/scripting/api.html#mitmproxy.models.http.HTTPFlow)

###**python** *3.x*   +    **mitmproxy** *stable*  
对应的文档改下版本就行了, mitmproxy最新版，和*0.18.2*及之前的版本相比，多了**websocket**的能力, 在 [事件文档](http://docs.mitmproxy.org/en/stable/scripting/events.html) 里面可以看到，多了很多事件的支持

- websocket_handshake(flow)
- websocket_start(flow)
- websocket_message(flow)
- websocket_end(flow)
- websocket_error(flow)

### 使用virtualenv管理多版本python环境
1. 安装python2.7，virtualenv， 设置环境变量，为主python
2. 安装python3.x，不设置环境变量
3. 安装 vc++2015
4. `virtualenv venv` 默认安装python2.7
5. `virtualenv -p c:\\python36\python.exe venv3` 安装为python3 

>D:\workspace\mitm_exam>.\venv3\Scripts\activate
>
>(venv3) D:\workspace\mitm_exam>python --version
>
Python 3.6.4

>(venv3) D:\workspace\mitm_exam>.\venv\Scripts\activate
>
>(venv) D:\workspace\mitm_exam>python --version
>
>Python 2.7.14

注意事项：
>如果报etree.so的错误，解决办法 lxml安装4.0.0 `pip uninstall lxml && pip install lxml==4.0.0`

(**python** *2.7*   +    **mitmproxy** *0.18.2*)  
1. tnwz/quiz.py
	头脑王者抓取问题查询答案脚本
	![answer.png](http://upload-images.jianshu.io/upload_images/5941869-37a7251ef2168fe5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


(**python** *3.x*   +    **mitmproxy** *last*)
1. syq/syq.py
   抓取损友圈websorcket数据
2. wzdt 
   知乎答题王辅助web版