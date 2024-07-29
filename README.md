# LexAI: A Multilingual AI Assistant

## How to replicate this work
1. Clone the github repository.

2. Create and activate a conda environment 
```bash
conda create -n {name} python=3.10 -y
```
```bash
conda activate {name}
```
3. Install the requirements and dependencies
```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory and add GOOGLE_API_KEY credentials as follows:
```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
4. Finally, run the streamlit app
```bash 
streamlit run app.py
```

# Deploy streamlit app on EC2 instance

1. Login with your AWS console and launch an EC2 instance

2. Run the following commands
```bash
sudo apt update
```
```bash
sudo apt-get update
```
```bash
sudo apt upgrade -y
```
```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```
```bash
git clone the github repository
```
```bash
sudo apt install python3-pip
```
```bash
pip3 install -r requirements.txt
```
```bash
#Temporary running
python3 -m streamlit run app.py
```
```bash
#Permanent running
nohup python3 -m streamlit run app.py
```
Note: Streamlit runs on this port: 8501: Don't forget the port mapping to 8501.

