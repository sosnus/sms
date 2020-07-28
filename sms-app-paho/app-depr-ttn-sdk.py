import time
import ttn

app_id = "arduino-mkr-1310-test"
access_key = "ttn-account-v2.1yNpDkRAfRnEvrh2fwxO5a4IfrCszOyFEFwTj-DY8rQ"

print("TTN parse to influxDB=================== 03:28 28.07.2020")

def thread_function(name):
  print("start "+name+" thread")
  print("end "+name+"thread")


def writeToInfluxDb(node_data,node_time,node_name):
  for k,v in node_data.items():
    print(">",node_name, " t=", node_time, "msg:", k, ":",v)
    db="orchard_jaroszki" # mv from app_name in future
    url = "http://sms-influxdb-container:8086/write?db="+db
    payload = k + ",device=" + node_name + " value="+ str(v)
    ##payload = "temperature,device="+ node_name +" value="+str(v)
    headers = {
    'Content-Type': 'text/plain'
    }
    print(url)
    print(payload)
 #   print('EXEC!')
#    execfile('simple.py')
#    x = threading.Thread(target=thread_function, args=(1,))
#    x.start()
#    response = requests.request("POST", url, headers=headers, data = payload, timeout=5)
#  execfile('simple.py')
#    print(response.text.encode('utf8'))
#    print('response: ', response)
###    print(payload)
###    print(response.text.encode('utf8'))


def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  # print(msg)
  print("----------------------------------")


  node_time = msg.metadata.time
  node_name = msg.dev_id
  node_data = msg.payload_fields._asdict()

  writeToInfluxDb(node_data,node_time,node_name)
  print("end callback")

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
while True:
        time.sleep(60)
mqtt_client.close()
