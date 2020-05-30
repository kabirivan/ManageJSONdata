#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:47:18 2020

@author: Xavier Aguas
"""
import json



with open('data.json') as access_json:
    read_content = json.load(access_json)
    
question_access = read_content['results']     


print(question_access)
print('\n')   

for question_data in question_access:
    print(question_data)
    
print('\n')   
        
    
replies_access = question_data['replies']
print(replies_access)   
    

def get_user_name():
    question_access = read_content['results']
    for question_data in question_access:
        for replies_data in replies_access:
            user_name = replies_data['user']['display_name']
            print(user_name)
            
            
            
            
get_user_name()            