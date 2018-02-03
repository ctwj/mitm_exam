#encoding=utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "this is test for wzdt"


@app.route("/question/list")
def question_list():
    return u'{"code": "SUCCESS", "data": {"answerFalse": 0, "answerRight": 0, "countdown": 10, "integral": 0, "isover": 0, "options": [{"id": "A", "name": "65"}, {"id": "B", "name": "66"}, {"id": "C", "name": "68"} ], "title": "柯南道尔写了多少部侦探小说", "totalQuestion": 8, "uaId": "1691961"}, "msg": "成功"}'

@app.route("/question/answer")
def question_answer():
    return u'{"code": "SUCCESS", "data": {"answer": "C", "result": 0 }, "msg": "完成"}'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
