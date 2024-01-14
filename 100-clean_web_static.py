#!/usr/bin/python3
# Fabfile to delete out-of-date archives.

# Import necessary libraries and modules
import os
from fabric.api import env, run, local

# Define the list of server IPs
env.hosts = ["3.90.85.41", "54.174.187.4"]


# Function to delete out-of-date archives
def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Delete unnecessary archives in the local 'versions' folder
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Delete unnecessary archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]


# Ensure this script is run only when directly executed
if __name__ == "__main__":
    do_clean()
