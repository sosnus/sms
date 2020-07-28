import time
import ttn

app_id = "arduino-mkr-1310-test"
access_key = "ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)
