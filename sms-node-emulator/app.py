import requests
import random
import time


print("HI!")
print("Python 3.8-slim, sms-node-emulator 4 nodes every 5 seconds ")
time.sleep(5)
print("Wait for other containers...")


def writeToInfluxDb( db, device, value):
    # print(random.randint(3, 9)) 
    url = "http://sms-influxdb-container:8086/write?db="+db
    # url = "http://172.21.0.3:8086/write?db="+db

    payload = "temperature,device="+ device +" value="+str(value)
    #  + string(random.randint(3, 9))"
    headers = {
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(payload)
    print(response.text.encode('utf8'))



while True:
    print("new loop!")
    writeToInfluxDb("greenhouse_jaroszki", "node02", random.randint(15,30))
    writeToInfluxDb("greenhouse_jaroszki", "node03", random.randint(5,10))
    writeToInfluxDb("greenhouse_jaroszki", "node04", random.randint(5,10))
    writeToInfluxDb("greenhouse_jaroszki", "outdoor", random.randint(5,30))
    time.sleep(5)