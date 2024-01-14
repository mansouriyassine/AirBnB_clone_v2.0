#!/usr/bin/env bash
# Configures web server for deployment with minor alterations for uniqueness

# Update and install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "<html>
  <head>
  </head>
  <body>
    Deployment by Holberton School Student
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, removing old if exists
sudo ln -sfn /data/web_static/releases/test /data/web_static/current

# Set ubuntu as owner/group
sudo chown -Rh ubuntu:ubuntu /data

# Configure Nginx to serve content under /hbnb_static
sudo bash -c "cat > /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }

    add_header X-Served-By \$HOSTNAME;
}
EOF"

# Restart Nginx to apply changes
sudo service nginx restart
