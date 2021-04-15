#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    if isdir("versions") is False:
        local("mkdir -p versions")
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    burger = "versions/web_static_{}.tgz".format(d)
    if local("tar -czvf {} web_static/".format(burger)):
        return burger
    else:
        return None
