#!/usr/bin/python3
"""Full deployment"""

from fabric.api import *
from os import path
from os.path import isdir
from datetime import datetime

env.hosts = ['35.237.105.160', '54.221.65.216']


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


def do_deploy(archive_path):
    """Fabric script distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        burger = archive_path.split('/')[-1]
        filedir = burger.split('.')[0]
        pathf = "/data/web_static/releases/" + filedir
        run("mkdir -p " + pathf)
        run("tar -xzf /tmp/" + burger + " -C " + pathf)
        run("rm /tmp/" + burger)
        run("mv " + pathf + "/web_static/* " + pathf)
        run("rm -rf " + pathf + "/web_static/")
        run("rm -rf /data/web_static/current")
        run("ln -sf " + pathf + "/" + " /data/web_static/current")

        return True
    except:
        return False


def deploy():
    """Fabric script creates + distributes files to your web servers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
