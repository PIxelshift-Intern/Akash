# this is to force restart docker service

sudo echo test
sudo systemctl stop docker.socket
sudo systemctl stop docker.service
sudo systemctl stop docker 
sudo systemctl start docker
sudo systemctl start docker.service
sudo systemctl start docker.socket
sudo systemctl status docker
docker ps