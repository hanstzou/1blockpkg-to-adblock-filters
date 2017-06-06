#!/usr/bin/env python

import os
import sys

if sys.version_info[:2] >= (2, 7):
    import json
    from collections import OrderedDict
else:
    import simplejson as json
    from ordereddict import OrderedDict

if __name__ == '__name__':
    pwd = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(pwd)
else:
    root = '..'

with open(os.path.join(root, 'Rules.1blockpkg')) as f:
    onebpkg = json.load(f)#, object_pairs_hook=OrderedDict)
