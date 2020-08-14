import requests
from datetime import datetime
import time
import smsvariables as smsvariables

  
def writeToInfluxDB(databasePort = smsvariables.default_port, databaseUrl =smsvariables.default_url ,databaseName = smsvariables.default_database , messageTime = datetime.now(), measurementParameter = "temporaryTemp", measurementValue = 42, measurementNodeName = "defaultNode"):
    if False:
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
        
    payload = measurementParameter + ",device=" + measurementNodeName + " value="+ str(measurementValue)
    
    headers = {
    'Content-Type': 'text/plain'
    }
    
    url = databaseUrl + ":" + str(databasePort) + "/write?db="+databaseName

    print(url + "q= ", payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    time.sleep(2)
    print(response.text.encode('utf8'))
    print(response.code)


   ### response = requests.request("POST", url, headers=headers, data = payload)
    
#   time.sleep(2)
  ###  print(response.text)
