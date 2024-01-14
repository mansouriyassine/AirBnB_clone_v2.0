#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import env, run, put, local
from datetime import datetime
import os

# Define the remote servers
env.hosts = ["441617-web-01", "441617-web-02"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Create a compressed archive of the web_static folder.
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path (str): Local path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_folder = archive_name.replace('.tgz', '') \
                                     .replace('.tar.gz', '')

        put(archive_path, '/tmp')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_name, archive_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(
                archive_folder, archive_folder))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(archive_folder))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Full deployment process.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
