#!/bin/bash
sudo cp /home/ubuntu/cicd/workspace/django_pipeline/gunicorn_folder/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/cicd/workspace/django_pipeline/gunicorn_folder/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn