# docker rm sms-node-emulator-container
# docker build -t sms-node-emulator ../sms-node-emulator/

docker start sms-influxdb-container
# docker run -d --name=sms-influxdb-container --network sms-net -v v-sms-influx:/var/lib/influxdb influxdb:1.7
# todo Influx 1.8
docker start sms-grafana-container
docker start sms-app-container
