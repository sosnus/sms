# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:55:18 2020

@author: sosnus
"""


import requests
from datetime import datetime
import time
import smsvariables as smsvariables

def init():
  print ("sms-endpoints init")
  
def writeToInfluxDB(databasePort = smsvariables.default_port, databaseUrl =smsvariables.default_url ,databaseName = smsvariables.default_database , messageTime = datetime.now(), measurementParameter = "temporaryTemp", measurementValue = 42, measurementNodeName = "defaultNode"):
    
    print("PARAMETERS:")
    print(databasePort)
    print(databaseUrl)
    print(databaseName)
    print(messageTime)
    print(measurementParameter)
    print(measurementValue)
    print(measurementNodeName)
    print("-------")
   
    print("all")
    payload = "k,device=" + measurementNodeName + " value="+ str(measurementValue)
    
#    headers = {
#    'Content-Type': 'text/plain'
#    }
    
    print(payload)
#    print(response.text.encode('utf8'))


   ### response = requests.request("POST", url, headers=headers, data = payload)
    
#   time.sleep(2)
  ###  print(response.text)
