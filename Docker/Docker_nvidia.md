curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu16.04/amd64/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvida-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGUP dockerd
docker pull nvidia/cuda:9.0-cudnn7-devel
docker run --runtime=nvidia --rm nvidia/cuda:9.0-cudnn7-devel nvidia-smi
docker run -it --runtime=nvidia --rm nvidia/cuda:9.0-cudnn7-devel bash

apt-get update
apt-get install -y python3-pip python3-dev
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip
pip install --upgrade tensorflow-gpu==1.8.0
pip install keras


https://github.com/fchollet/keras/tree/master/docker