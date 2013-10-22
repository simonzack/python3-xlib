#!/usr/bin/env python3

# Distutils script for python3-xlib

from distutils.core import setup

import Xlib

setup(name = 'python3-xlib',
      version = Xlib.__version_string__,

      description = "Python3 X Library",
      url = 'https://github.com/LiuLang/python3-xlib',
      license = 'GPLv2',

      author = 'Peter Liljenberg',
      author_email = 'petli@ctrl-c.liu.se',
      maintainer = 'LiuLang',
      maintainer_email = 'gsushzhsosgsu@gmail.com',

      packages = [
          'Xlib',
          'Xlib.ext',
          'Xlib.keysymdef',
          'Xlib.protocol',
          'Xlib.support',
          'Xlib.xobject'
          ],

      long_description = '''\
python3-xlib is python3 version of python-xlib.
'''
      )
