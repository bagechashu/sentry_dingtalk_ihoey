# !/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-dingtalk-ihoey') \
        .version
except Exception as exception:
    del exception

    VERSION = 'UNKNOWN'
