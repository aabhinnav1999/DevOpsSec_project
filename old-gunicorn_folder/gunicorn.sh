#!/bin/bash
sudo cp gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn