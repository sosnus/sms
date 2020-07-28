import requests
import time
import json
import paho.mqtt.client as mqtt

# todo: secrets, method parameters, http requests, docker, logger
# requests: https://requests.readthedocs.io/en/master/user/quickstart/#more-complicated-post-requests

localhost = 'eu.thethings.network'
port = 1883
timeout = 60
topic = '+/devices/+/up'


def mqtt_to_http(node_name, node_payload_fields, node_db = 'orchard_jaroszki', node_time=-1):
  print('node_db=', node_db,  ' node_name=', node_name, ' node_payloads=', node_payload_fields, ' time=', node_time)
  # print("body parse")
#  print(type( node_payload_fields))
  for k,v in  node_payload_fields.items():
    payload = k + ' device=' + node_name + ' value=' + str(v) + ' ' + str(node_time)
    print('payload',payload)

    url = "http://sms-influxdb-container:8086/write?db="+node_db
    r = requests.post(url, data=payload)
    print(r.status_code)
  #  response = requests.request("POST", url, headers= {'Content-Type': 'text/plain'}, data = payload)
  #  print(response.code)
  #  print(response.text.encode('utf8'))

def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))
  client.subscribe(topic)

def on_message(client, userdata, msg):
  print("msg!")
  print(msg.payload)
  print("extract data...")
#  print(type(msg.payload))
  message = json.loads(msg.payload)
  mqtt_to_http(node_name =  message['dev_id'], node_payload_fields= message['payload_fields'])

  
#  print(type(message))
#  print('database', message['app_id'])
#  print('device', message['dev_id'])
#  print('payload_fields', message['payload_fields'])
#  for x in message['payload_fields']:
#    print('\t',x, message['payload_fields'][x])

  print('-------END-----')



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('arduino-mkr-1310-test','ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ')
client.connect(localhost, port, timeout)

client.loop_forever()