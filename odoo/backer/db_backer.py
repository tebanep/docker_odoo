#!/usr/bin/env python

import subprocess
from datetime import datetime


def backup_postgresql(dir, host="localhost", port="5432",
                      database="postgres", user="postgres", password="postgres"):
    now = datetime.now()
    backup_path = dir + "/" + "{}_{}_{}".format(database,
                                                "db",
                                                now.isoformat().split(".")[0])
    cmd = ['pg_dump', '-U', user, '-Fc', database, '-f', backup_path]
    subprocess.call(cmd, stdout=subprocess.PIPE)
