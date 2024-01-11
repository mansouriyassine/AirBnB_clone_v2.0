#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Ngixn
config_content="location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
}"

sudo sh -c "echo '$config_content' > /etc/nginx/sites-available/default"

# Restart Nginx
sudo service nginx restart

# Exit
exit 0
