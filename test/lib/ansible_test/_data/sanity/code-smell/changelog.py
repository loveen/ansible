#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import sys
import subprocess


def main():
    paths = sys.argv[1:] or sys.stdin.read().splitlines()

    allowed_extensions = ('.yml', '.yaml')

    has_config = False
    paths_to_check = []
    for path in paths:
        if path == 'changelogs/config.yaml':
            has_config = True
            continue

        if path.startswith('changelogs/fragments/.'):
            continue

        ext = os.path.splitext(path)[1]

        if ext not in allowed_extensions:
            print('%s:%d:%d: extension must be one of: %s' % (path, 0, 0, ', '.join(allowed_extensions)))

        paths_to_check.append(path)

    if not has_config:
        print('changelogs/config.yaml:0:0: config file does not exist')
        return

    if not paths_to_check:
        return

    cmd = [sys.executable, '-m', 'antsibull_changelog', 'lint'] + paths_to_check
    subprocess.check_call(cmd)


if __name__ == '__main__':
    main()
