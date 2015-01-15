#!/usr/bin/env python

import argparse
# from . import vol_backer
from odoo.odoo.backer import db_backer


def main():
    mode_dict = {"bash": ["/usr/bin/supervisord", "-c",
                          "/etc/supervisor/conf.d/bash_supervisord.conf"],
                 "odoo": ["/usr/bin/supervisord", "-c",
                          "/etc/supervisor/conf.d/odoo_supervisord.conf"],
                 "postgresql": ["/usr/bin/supervisord", "-c",
                                "/etc/supervisor/conf.d/postgresql_supervisord.conf"],
                 "all": ["/usr/bin/supervisord", "-c",
                         "/etc/supervisor/conf.d/all_supervisord.conf"]}

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",
                        choices=mode_dict.keys(),
                        help="define container mode")

    args = parser.parse_args()
    mode = args.mode
    cmd = mode_dict.get(mode, "bash")
    run_cmd(cmd)


if __name__ == '__main__':
    main()
