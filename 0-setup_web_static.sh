#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
# install packages
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
# create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
# html contents
sudo echo "<html>
  <head>
  <title> Holberton School</title>
  </head>
  <body>
    AirBnB_clone_v2 web_static deployment
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
# user group rights
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# restart the server
sudo service nginx restart
