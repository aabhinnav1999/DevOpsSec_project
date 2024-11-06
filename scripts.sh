#!/bin/bash
sudo cp .env /home/ubuntu/cicd/workspace/django_pipeline
cd /home/ubuntu/cicd/workspace/django_pipeline
sudo apt update
sudo apt install python3-venv -y
sudo apt-get install pkg-config libmysqlclient-dev python3-dev -y
python3 -m venv env
source env/bin/activate
sudo apt install python3-pip -y
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate