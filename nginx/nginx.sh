#!/bin/bash
sudo apt update
sudo apt install nginx -y
sudo cp devopssec /etc/nginx/sites-available/devopssec
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/devopssec /etc/nginx/sites-enabled
sudo systemctl restart nginx