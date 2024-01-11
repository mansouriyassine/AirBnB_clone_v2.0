# Puppet script to set up web servers for the deployment of web_static

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create required directories
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Set ownership
file { '/data':
  owner => 'ubuntu',
  group => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n}\n",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
