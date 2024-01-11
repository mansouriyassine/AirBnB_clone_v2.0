#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import local, env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['ubuntu@3.90.85.41', 'ubuntu@54.174.187.4']
env.key_filename = ['my_ssh_private_key']


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split("/")[-1]
        release_path = "/data/web_static/releases/{}".format(archive_filename.split(".")[0])
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
