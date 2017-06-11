#!/usr/bin/env python

from datetime import datetime
import os
import sys

if sys.version_info[:2] >= (2, 7):
    import json
    from collections import OrderedDict
else:
    import simplejson as json
    from ordereddict import OrderedDict

def get_hide_rules(onebpkg):
    try:
        for pkg in onebpkg:
            if pkg['id'] == 'hide-elements':
                return pkg['rules']
    except KeyError:
        return []


def onebpkg_to_filter(onebpkg):
    filters = []
    hide_filters = []
    rules = (r['content'] for r in get_hide_rules(onebpkg))
    hide_rules = (r for r in rules if r['action']['type'] == 'css-display-none')

    for r in hide_rules:
        try:
            urls = ','.join((u.lstrip('*') for u in r['trigger']['if-domain']))
        except KeyError:
            urls = ''
        selectors = r['action']['selector']
        if selectors:
            hide_filters.append(urls + '##' + selectors)

    filters += hide_filters
    return filters


def save_filter(root, filters):
    with open(os.path.join(root, 'tw_float_list.txt'), 'w') as f:
        hdr =  ('[Adblock Plus 2.0]\n'
                '! Checksum: placeholder\n')
        hdr +=  '! Version: ' + datetime.now().strftime('%Y%m%d%H%M') + '\n'
        hdr += ('! Expires: 2 days\n'
                '! Title: TW Float List\n'
                '! Homepage: https://github.com/hanstzou/1blockpkg-to-adblock-filters\n'
                '!\n')
        f.write(hdr + '\n'.join(filters) + '\n')


if __name__ == '__main__':
    root = os.getcwd()
else:
    pwd = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(pwd)

with open(os.path.join(root, 'Rules.1blockpkg')) as f:
    onebpkg = json.load(f)
    filters = onebpkg_to_filter(onebpkg)
    if __name__ == '__main__':
        save_filter(root, sorted(filters))

