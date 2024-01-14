#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers.
"""

from fabric.api import env, run, put
from os import path

# Define the remote servers
env.hosts = ["441617-web-01", "441617-web-02"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers.

    Args:
        archive_path (str): The local path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not path.exists(archive_path):
        return False

    try:
        archive_name = path.basename(archive_path)
        archive_folder = archive_name.replace('.tgz', '') \
                                     .replace('.tar.gz', '')

        # Upload the archive to the /tmp/ directory on the web servers
        put(archive_path, '/tmp')

        # Create the folder for the new version
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_folder))

        # Uncompress the archive to the specified folder
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_name, archive_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Move the contents of the new version to the web_static folder
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(
                archive_folder, archive_folder))

        # Delete the empty web_static folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_folder))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(archive_folder))

        return True
    except Exception as e:
        return False
