echo "config firewall"
sudo apt-get install ufw
sudo ufw status
sudo ufw allow 22 # ssh
sudo ufw allow 3000 # grafana
sudo ufw status
sudo ufw enable
sudo ufw status