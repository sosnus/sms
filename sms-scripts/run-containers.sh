docker rm sms-node-emulator-container
docker build -t sms-node-emulator ../sms-node-emulator/

docker run -d --name=sms-influxdb-container --network sms-net -v v-sms-influx:/var/lib/influxdb influxdb:1.7
docker run -d -p 3000:3000 --name=sms-grafana-container --network sms-net -v v-sms-grafana:/var/lib/grafana grafana/grafana
docker run -d --name=sms-node-emulator-container --network sms-net sms-node-emulator