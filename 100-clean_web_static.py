#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import local, env, run
from datetime import datetime
from os.path import exists

env.hosts = ['ubuntu@3.90.85.41', 'ubuntu@54.174.187.4']
env.key_filename = ['my_ssh_private_key']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 0:
        return
    try:
        # Local clean
        local("cd versions; ls -1t | tail -n +{} | xargs -I {{}} rm {{}}".format(number + 1))

        # Remote clean
        archives = run("ls -1t /data/web_static/releases/").split('\n')
        archives = archives[:-1] if archives[-1] == '' else archives

        for archive in archives[number:]:
            path = "/data/web_static/releases/{}".format(archive)
            run("rm -rf {}".format(path))

    except Exception:
        return None
