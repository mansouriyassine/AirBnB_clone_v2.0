#!/usr/bin/python3
"""
Deploy web_static to web servers
"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ["100.25.45.251", "3.90.84.44"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Deploys the archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/{}".format(no_ext)

        # Upload the archive
        put(archive_path, '/tmp/')

        # Create directory for unzipping
        run('sudo mkdir -p {}'.format(path))

        # Unzip the archive
        run('sudo tar -xzvf /tmp/{} -C {}'.format(file_name, path))

        # Delete the archive from the server
        run('sudo rm /tmp/{}'.format(file_name))

        # Move contents to the parent directory
        run('sudo mv {}/web_static/* {}'.format(path, path))

        # Remove the redundant directory
        run('sudo rm -rf {}/web_static'.format(path))

        # Delete current symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create new symbolic link
        run('sudo ln -s {}/ /data/web_static/current'.format(path))

        print("New version deployed!")
        return True
    except:
        return False
