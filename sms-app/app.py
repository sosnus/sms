# TODO:
# CLEAN CODE
# REMOVE TIME DELAY
# REMOVE PRINT DEBUG
# REMOVE SLEEP
# ADD TIMER IN REQUESTS
# MAYBE USE PYTHON LIBRARY


import time
import ttn

import smsendpoints as smsendpoints
import smsvariables as smsvariables

print("SMSAPP")
print("sms app - application for rewrite data from MQTT to endpoints (like HTTP requests or data logger)")

request_tasklist = []

def messageParser(node_data,node_time,node_name):
    for k,v in node_data.items():
        smsendpoints.writeToInfluxDB( messageTime = node_time, measurementParameter = k, measurementValue = v, measurementNodeName = node_name)
 #       request_tasklist.append(threading.Thread(target=smsendpoints.writeToInfluxDb, args=(measurementParameter = k, measurementValue = v)))
#        request_tasklist[-1].start()

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  # print(msg)
  print("----------------------------------")

  messageParser(msg.payload_fields._asdict(),msg.metadata.time,msg.dev_id)

handler = ttn.HandlerClient(smsvariables.app_id, smsvariables.access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
	time.sleep(60)
mqtt_client.close()