#!/usr/bin/env python3

# Distutils script for python3-xlib

from distutils.core import setup

import Xlib

setup(name = 'python3-xlib',
      version = Xlib.__version_string__,

      description = "Python X Library",
      url = 'http://python-xlib.sourceforge.net/',

      author = 'Peter Liljenberg',
      author_email = 'petli@ctrl-c.liu.se',

      packages = [
          'Xlib',
          'Xlib.ext',
          'Xlib.keysymdef',
          'Xlib.protocol',
          'Xlib.support',
          'Xlib.xobject'
          ],
      )
