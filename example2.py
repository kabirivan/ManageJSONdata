#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:08:19 2020

@author: Xavier Aguas
"""


import json
import jsonpickle
from json import JSONEncoder

class Student(object):
    def __init__(self, rollNumber, name, marks):
        self.rollNumber = rollNumber
        self.name = name
        self.marks = marks

class Marks(object):
    def __init__(self,english,geometry):
        self.english = english
        self.geometry = geometry
        
        
marks = Marks(82,74)
student = Student(1,"Ivan",marks)


print("Encode Object into JSON formatted Data using jsonpickle")
studentJSON = jsonpickle.encode(student)
print(studentJSON)


print("Decode and Convert JSON into Object using jsonpickle")
studentObject = jsonpickle.decode(studentJSON)
print("Object type is: ", type(studentObject))




