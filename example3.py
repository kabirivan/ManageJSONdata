#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:41:20 2020

@author: Xavier Aguas
"""


import json

with open('user1test.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print(data)

print('\n')

print(type(data))

print('\n')

question_access = data['synchronizationGesture']  

sample = question_access['sample1']

accelerometer = sample['accelerometer']['x']


synchronizationGesture = data['synchronizationGesture']  

emg_ch1 = synchronizationGesture['sample1']['emg']['ch1']

EMG = []

for i in range(1,5):
   # print(i)
    EMG.append('ch{}'.format(i))   
print(EMG)   


#print(emg_ch1)