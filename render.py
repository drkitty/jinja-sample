#!/usr/bin/env python2

from __future__ import unicode_literals
from sys import stdout

import ipaddr
import jinja2


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


def register_filter(f):
    env.filters[f.__name__] = f
    return f


def main():
    @register_filter
    def get_first_ip(subnet):
        return unicode(ipaddr.IPv4Address(subnet) + 1)

    stdout.write(env.get_template('sample.conf').render(
        subnets=[
            ('8.8.0.0', '255.255.254.0'),
            ('10.0.0.0', '255.0.0.0'),
            ('192.168.0.0', '255.255.255.0'),
        ]
    ))


if __name__ == '__main__':
    main()
