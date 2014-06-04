# -*- coding: utf-8 -*-

import argparse

from .ip import find


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="ip or domain")
    args = parser.parse_args()

    if not args.ip:
        return

    print(find(args.ip))


if __name__ == '__main__':
    main()
