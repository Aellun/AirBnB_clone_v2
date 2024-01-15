#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime


""" Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo"""


def do_pack():

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
