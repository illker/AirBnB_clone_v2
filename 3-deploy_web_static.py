#!/usr/bin/python3
"""Full deployment"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['35.237.105.160', '54.221.65.216']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None


def do_deploy(archive_path):
    """Fabric script distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return (False)
    try:
        file = archive_path.split("/")[-1]
        x = file.split(".")[0]
        route = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(route, x))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, route, x))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(route, x))
        run('rm -rf {}{}/web_static'.format(route, x))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(route, x))
        return (True)
    except:
        return (False)


def deploy():
    """Fabric script creates + distributes files to your web servers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
