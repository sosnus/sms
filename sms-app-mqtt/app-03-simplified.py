import time
import ttn

app_id = "arduino-mkr-1310-test"
access_key = "ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ"

print("TTN parse to influxDB===================")

def writeToInfluxDb(node_data,node_time,node_name):
  for k,v in node_data.items():
    print(">",node_name, " t=", node_time, "msg:", k, ":",v)
    db="orchard_jaroszki" # mv from app_name in future
    url = "http://sms-influxdb-container:8086/write?db="+db
    payload = "k,device=" + node_name + " value="+ str(v)

    headers = {
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(payload)
    print(response.text.encode('utf8'))




  print("TODO")
  print(node_name)
  print(node_time)
  print(node_data)


def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  # print(msg)
  print("----------------------------------")


  node_time = msg.metadata.time
  node_name = msg.dev_id
  node_data = msg.payload_fields._asdict()

  writeToInfluxDb(node_data,node_time,node_name)

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
	time.sleep(60)
mqtt_client.close()
