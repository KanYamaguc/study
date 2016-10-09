#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    for arg in args :
        print u"args {}".format(arg)

    sys.exit(0);

