#!/usr/bin/env python
import os
import sys
import pwd
import getopt
import subprocess


def report_ids(msg):
    print 'uid, gid = %d, %d; %s' % (os.getuid(), os.getgid(), msg)


def demote(user_uid, user_gid):
    def result():
        report_ids('starting demotion')
        os.setgid(user_gid)
        os.setuid(user_uid)
        report_ids('finished demotion')

    return result


def show_help():
    print 'Show the help Esteban - yes, you wrote this!'


def init_odoo():
    odoo_uid = pwd.getpwnam('odoo').pw_uid
    odoo_gid = pwd.getpwnam('odoo').pw_gid
    env = os.environ.copy()
    env["HOME"] = "/opt/odoo"

    print 'Odoo running!'
    cmd = '/opt/odoo/odoo/odoo.py -c /etc/odoo/openerp-server.conf'
    subprocess.call(cmd,
                    shell=True,
                    env=env,
                    preexec_fn=demote(odoo_uid, odoo_gid))


def init_postgresql():
    postgres_uid = pwd.getpwnam('postgres').pw_uid
    postgres_gid = pwd.getpwnam('postgres').pw_gid
    cmd = '/usr/lib/postgresql/9.3/bin/postgres --config_file=/etc/postgresql/9.3/main/postgresql.conf -D /var/lib/postgresql/9.3/main'
    env = os.environ.copy()
    env["HOME"] = "/var/lib/postgresql"
    subprocess.call(cmd,
                    shell=True,
                    env=env,
                    preexec_fn=demote(postgres_uid, postgres_gid))
    print 'PostgreSQL running!'


def init_all():
    print "All!"
    # odoo_uid = pwd.getpwnam('odoo').pw_uid
    # odoo_gid = pwd.getpwnam('odoo').pw_gid
    env = os.environ.copy()
    env["HOME"] = "/opt/odoo"
    cmd = (
        'su postgres -c "/usr/lib/postgresql/9.3/bin/postgres --config_file=/etc/postgresql/9.3/main/postgresql.conf -D /var/lib/postgresql/9.3/main" '
        '&& su odoo -c "/opt/odoo/odoo/odoo.py -c /etc/odoo/openerp-server.conf"'
    )
    subprocess.Popen(cmd,
                    shell=True,
                    env=env)  # ,
    # preexec_fn=demote(odoo_uid, odoo_gid))
    print 'Odoo & PostgreSQL running!'


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'opah', ['odoo', 'postgresql', 'all', 'help'])
        print opts, args
    except getopt.GetoptError:
        show_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        elif opt in ('-o', '--odoo'):
            init_odoo()
        elif opt in ('-p', '--postgresql'):
            init_postgresql()
        elif opt in ('-a', '--all') or not opt:
            init_all()


if __name__ == '__main__':
    main(sys.argv[1:])
