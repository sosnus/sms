docker network create -d bridge sms-net

# docker container run -d --net sms-net grafana/grafana

# docker run -d -p 8086:8086 --name=sms-influxdb --network sms-net -v influxdb:/var/lib/influxdb influxdb:latest
# docker run -d -p 3000:3000 --name=sms-grafana --network sms-net -v v-sms-grafana:/var/lib/grafana grafana/grafana

docker rm sms-node-emulator-container
docker build -t sms-node-emulator ../sms-node-emulator/


docker run -d --name=sms-influxdb-container --network sms-net -v v-sms-influx:/var/lib/influxdb influxdb:1.7
docker run -d -p 3000:3000 --name=sms-grafana-container --network sms-net -v v-sms-grafana:/var/lib/grafana grafana/grafana
docker run -d --name=sms-node-emulator-container --network sms-net sms-node-emulator

# test container (with )
docker run -d -itd --name=ubuntu-test --network sms-net ubuntu
# connect bash to container
docker container exec -it ubuntu-test bash

# apt-get update && apt-get install -y iputils-ping
apt update && apt upgrade
apt install curl -y