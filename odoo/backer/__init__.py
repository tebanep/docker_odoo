#!/usr/bin/env python

import argparse
# from . import vol_backer
from odoo.odoo.backer import db_backer


def main():
    type_dict = {"database": [],
                 "volume": [],
                 "all": []}

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type",
                        choices=type_dict.keys(),
                        help="define container mode")

    args = parser.parse_args()
    type = args.mode
    cmd = type_dict.get(type, "bash")


if __name__ == '__main__':
    main()
