#!/usr/bin/python3
"""Deploy archive to web servers
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['3.90.85.41', '54.174.187.4']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy the archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Extract the archive to the web_static/releases/ directory
        archive_filename = os.path.basename(archive_path)
        archive_name = archive_filename.split('.')[0]
        remote_path = '/data/web_static/releases/{}'.format(archive_name)
        run('mkdir -p {}'.format(remote_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, remote_path))

        # Remove the uploaded archive file
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents to the web_static/releases/ directory
        run('mv {}/web_static/* {}'.format(remote_path, remote_path))

        # Remove the empty web_static directory
        run('rm -rf {}/web_static'.format(remote_path))

        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(remote_path))

        return True

    except Exception as e:
        return False
