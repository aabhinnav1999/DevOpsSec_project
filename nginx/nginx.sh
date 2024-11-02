#!/bin/bash
sudo apt update
sudo apt install nginx -y
cp /home/ubuntu/cicd/workspace/django_pipeline/nginx/devopssec /etc/nginx/sites-available/devopssec
sudo ln -s /etc/nginx/sites-available/devopssec /etc/nginx/sites-enabled
sudo systemctl restart nginx