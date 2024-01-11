#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the file name with the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress web_static into the versions folder
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path of the generated archive
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
