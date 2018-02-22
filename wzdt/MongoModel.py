#!/usr/bin/env python
#coding=utf-8

from pymongo import MongoClient


class DataController:

    def __init__(self):
        self.conn = MongoClient('mongo_server', 27017)
        self.db = self.conn.wzdt
        self.answer_set = self.db.questions


    def add_question(self, data):
        if not self.is_exists_question(data.quiz):
            self.answer_set.insert(data)


    def is_exists_question(self, question):
        answer = self.answer_set.find_one({"quiz":question})
        if answer is None:
            return False
        return True


    def find_answer(self, question):
        answer = self.answer_set.find_one({"quiz":question})
        if answer is None:
            return False
        else:
            answerIndex = int(answer['answer'])-1
            options = answer['options']
            print(options[answerIndex])
            return options[answerIndex]