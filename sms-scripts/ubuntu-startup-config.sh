echo "config firewall"
sudo apt-get install ufw
sudo ufw status
sudo ufw allow 22 # ssh
sudo ufw allow 3000 # grafana
sudo ufw status
sudo ufw enable
sudo ufw status

wget https://github.com/jesseduffield/lazydocker/releases/download/v0.3/lazydocker_0.3_Linux_x86_64.tar.gz
tar xvzf lazydocker*.tar.gz
sudo install lazydocker /usr/local/bin/