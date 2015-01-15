#!/usr/bin/env python

import subprocess
from datetime import datetime


def backup_postgresql(database, backup_path, host="localhost", port="5432",
                      user="postgres", password="postgres"):

    now = datetime.now()
    cmd = ['pg_dump', '-U', user, '-Fc', database, '-f', backup_path]
    subprocess.call(cmd, stdout=subprocess.PIPE)
