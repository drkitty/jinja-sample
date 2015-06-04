#!/usr/bin/env python2

from __future__ import unicode_literals
from sys import stdout

import ipaddr
import jinja2


# Set up the jinja environment, which stores jinja settings and knows how to
# load and render templates.
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


# This is a decorator that registers a filter so it can be used from any
# template we load.
def register_filter(f):
    env.filters[f.__name__] = f
    return f


# Register a filter called 'get_first_ip' that we can use in templates.
@register_filter
def get_first_ip(subnet):
    return unicode(ipaddr.IPv4Address(subnet) + 1)


def main():
    # Render the template named 'sample.conf' with the variable 'subnets' as
    # context, and print the result.
    subnets = [
        ('8.8.0.0', '255.255.254.0'),
        ('10.0.0.0', '255.0.0.0'),
        ('192.168.0.0', '255.255.255.0'),
    ]
    stdout.write(env.get_template('sample.conf').render(subnets=subnets))


if __name__ == '__main__':
    main()
