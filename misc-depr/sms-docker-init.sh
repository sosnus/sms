# docker volume create v-sms-grafana

# docker run -d -p 3000:3000 --name=sms-grafana -v v-sms-grafana:/var/lib/grafana grafana/grafana

docker run -p 8086:8086 \
      -e INFLUXDB_DB=defaultdb \
      -e INFLUXDB_ADMIN_USER=admin \
      -e INFLUXDB_ADMIN_PASSWORD=adminpass \
      -e INFLUXDB_USER=user \
      -e INFLUXDB_USER_PASSWORD=userpass \
      -v influxdb:/var/lib/influxdb \
      influxdb:latest 


docker run -d -p 8086:8086 --name=sms-influxdb --network sms-net -v influxdb:/var/lib/influxdb influxdb:latest
docker run -d -p 3000:3000 --name=sms-grafana --network sms-net -v v-sms-grafana:/var/lib/grafana grafana/grafana

# docker run --rm -d --network host --name my_nginx nginx


docker run -d -p 8086:8086 


docker network create --driver bridge sms-net




docker inspect ubuntu-test \
  | grep "\"IPAddress\"" -m 1 \
  | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'


