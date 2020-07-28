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

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('arduino-mkr-1310-test','ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ')
client.connect(localhost, port, timeout)

client.loop_forever()
