import json
import paho.mqtt.client as mqtt

localhost = 'eu.thethings.network'
port = 1883
timeout = 60
topic = '+/devices/+/up'

def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))
  client.subscribe(topic)

def on_message(client, userdata, msg):
  print("msg!")
  print(msg.payload)
  print("extract data")
  print(type(msg.payload))
  message = json.loads(msg.payload)
  print(type(message))
  print('database', message['app_id'])
  print('device', message['dev_id'])
  print('payload_fields', message['payload_fields'])
  for x in message['payload_fields']:
    print('\t',x, message['payload_fields'][x])

  print('-------END-----')



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('arduino-mkr-1310-test','ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ')
client.connect(localhost, port, timeout)

client.loop_forever()
