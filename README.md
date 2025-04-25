# Yolo11-detection-for-cvat
Yolo11 detection for cvat

# WSL
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --install
wsl -d ubuntu
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
	sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
	sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
	
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```
# CVAT and NUCLIO
```
docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
wsl -d ubuntu
wget https://github.com/nuclio/nuclio/releases/download/1.13.0/nuctl-1.13.0-linux-amd64
sudo chmod +x nuctl-1.13.0-linux-amd64
sudo ln -sf ${pwd}/nuctl-1.13.0-linux-amd64 /usr/local/bin/nuctl
sudo ln -sf $(pwd)/nuctl-1.13.0-linux-amd64 /usr/local/bin/nuctl
```
# SERVERLESS
Put the files into serverless/pytorch/...
You must cd into your cvat folder in WSL so that the serverless folder is exposed.
```
wsl -d ubuntu
./serverless/deploy_gpu.sh serverless/pytorch/ultralytics/yolo11
```
