#!/usr/bin/env python
import sys
import getopt
import subprocess


def show_help():
    print 'Show the help Esteban - yes, you wrote this!'

def init_bash():
    cmd = ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/bash_supervisord.conf"]
    subprocess.call(cmd)

def init_odoo():
    cmd = ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/odoo_supervisord.conf"]
    subprocess.call(cmd)


def init_postgresql():
    cmd = ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/postgresql_supervisord.conf"]
    subprocess.call(cmd)


def init_all():
    cmd = ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/all_supervisord.conf"]
    subprocess.call(cmd)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'bopah', ['bash', 'odoo', 'postgresql', 'all', 'help'])
    except getopt.GetoptError:
        show_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        elif opt in ('-b', '--bash'):
            init_bash()
        elif opt in ('-o', '--odoo'):
            init_odoo()
        elif opt in ('-p', '--postgresql'):
            init_postgresql()
        elif opt in ('-a', '--all') or not opt:
            init_all()


if __name__ == '__main__':
    main(sys.argv[1:])
