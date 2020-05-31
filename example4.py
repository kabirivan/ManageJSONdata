#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:05:20 2020

@author: Xavier Aguas

"""
import json
import jsonpickle
from json import JSONEncoder








class User:
    def __init__(self, generalInfo, synchronizationGesture, userInfo):
        self.generalInfo = generalInfo
        self.synchronization = synchronizationGesture
        self.userInfo = userInfo
        
    @classmethod
    def from_json(cls, json_string):
        with open(json_string, 'r') as json_file:
            json_dict = json.loads(json_file.read())
        return cls(**json_dict)
        


user =  User.from_json('user1test.json')        


print(user.generalInfo)