# TODO:
# CLEAN CODE
# REMOVE TIME DELAY
# REMOVE PRINT DEBUG
# REMOVE SLEEP
# ADD TIMER IN REQUESTS
# MAYBE USE PYTHON LIBRARY


# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:46:39 2020

@author: sosnus
"""

import time
import ttn

#from smsendpoints import *
import smsendpoints as smsendpoints
import smsvariables as smsvariables
# as smsendpoints



print("smsapp")
print("sms app - application for rewrite data from MQTT to endpoints (like HTTP requests or data logger)")


smsendpoints.init()

request_tasklist = []

def messageParser(node_data,node_time,node_name):
    for k,v in node_data.items():
        smsendpoints.writeToInfluxDB( messageTime = node_time, measurementParameter = k, measurementValue = v, measurementNodeName = node_name)
 #       request_tasklist.append(threading.Thread(target=smsendpoints.writeToInfluxDb, args=(measurementParameter = k, measurementValue = v)))
#        request_tasklist[-1].start()
      #  smsendpoints.writeToInfluxDB(measurementParameter = k, measurementValue = v)
    #    print(">",node_name, " t=", node_time, "msg:", k, ":",v)
 


    print("TODO")
 # print(node_name)
 # print(node_time)
 # print(node_data)


def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  # print(msg)
  print("----------------------------------")


  node_time = msg.metadata.time
  node_name = msg.dev_id
  node_data = msg.payload_fields._asdict()
  messageParser(node_data,node_time,node_name)

 ### request_tasklist.append(threading.Thread(target=writeToInfluxDb, args=(77,node_name,node_time,k,v)))
###  request_tasklist[-1].start()

  

handler = ttn.HandlerClient(smsvariables.app_id, smsvariables.access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
	time.sleep(60)
mqtt_client.close()