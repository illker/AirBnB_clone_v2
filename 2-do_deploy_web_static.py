#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import *
from os import path

env.hosts = ['35.237.105.160', '54.221.65.216']


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
