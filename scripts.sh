#!/bin/bash
cd /home/ubuntu/cicd/workspace/django_pipeline
sudo apt update
sudo apt install python3-venv
sudo apt-get install pkg-config libmysqlclient-dev python3-dev
python3 -m venv env
source env/bin/activate
sudo apt install python3-pip
pip install -r requirements.txt