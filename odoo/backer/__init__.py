#!/usr/bin/env python

import argparse
# from . import vol_backer
from odoo.odoo.backer import db_backer


def main():
    mode_dict = {"database": db_backer.backup_postgresql,
                 "volume": [],
                 "all": []}

    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Define backup directory")
    parser.add_argument("-d", "--database", help="PostgreSQL database")
    parser.add_argument("-m", "--mode",
                        choices=mode_dict.keys(),
                        default="database",
                        help="Define backup mode")

    args = parser.parse_args()
    dir = args.dir
    mode = args.mode
    database = args.database

    if mode == "database":
        print "database mode!"
        option_dict = {'dir': dir}
        if database:
            option_dict['database'] = database
        mode_dict.get[mode](**option_dict)
    elif mode == "volume":
        print "volume mode!"



if __name__ == '__main__':
    main()
