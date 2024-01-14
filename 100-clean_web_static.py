#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import env, run, local
from os import path

# Define the remote servers
env.hosts = ["441617-web-01", "441617-web-02"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    try:
        number = int(number)
        if number < 1:
            number = 1

        # Local cleanup
        local("mkdir -p versions")
        local_archives = local("ls -1t versions", capture=True).split('\n')
        to_delete_local = local_archives[number:]
        for archive in to_delete_local:
            local("rm -f versions/{}".format(archive))

        # Remote cleanup
        remote_archives_path = "/data/web_static/releases/"
        releases = run("ls -1t {}".format(remote_archives_path)).split('\n')
        to_delete_remote = releases[number:]
        for release in to_delete_remote:
            if path.join(remote_archives_path, release) != \
               path.join(remote_archives_path, "test"):
                run("rm -rf {}".format(
                    path.join(remote_archives_path, release)
                ))

        return True
    except Exception as e:
        return False
