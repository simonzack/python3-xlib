About
=====
python3-xlib is python3 version of [python-xlib](http://sourceforge.net/p/python-xlib "python-xlib")

Original python3 patch for python-xlib is written by @thomasklausner. Patch 
can be found [here](http://sourceforge.net/p/python-xlib/patches/5/ "patch")

I needed a keybinding tool in my [project](https://github.com/LiuLang/kwplayer "kwplayer"),
but no python3 version exists. So I spent some days porting python-xlib to
python3, I searched and found a patch written by @thomasklausner. That patch
was merged to python-xlib-0.14 and all source files were revised by now, and
that is python3-xlib-0.14.

This library is used in [another project](https://github.com/LiuLang/python3-keybinder "python3-keybinder").

I'm not sure whether I'll have enough time to maintain this library,
including improving its performance. Any help will be welcome.

It has been 4 yeras since the latest version of python-xlib was released.


Introduction(from python-xlib)
=============================
The Python X Library is intended to be a fully functional X client
library for Python programs.  It is written entirely in Python, in
contrast to earlier X libraries for Python (the ancient X extension
and the newer plxlib) which were interfaces to the C Xlib.

This is possible to do since X client programs communicate with the X
server via the X protocol.  The communication takes place over TCP/IP,
Unix sockets, DECnet or any other streaming network protocol.  The C
Xlib is merely an interface to this protocol, providing functions
suitable for a C environment.

There are three advantages of implementing a pure Python library:

 * Integration:  The library can make use of the wonderful object
   system in Python, providing an easy-to-use class hierarchy.

 * Portability: The library will be usable on (almost) any computer
   which have Python installed.  A C interface could be problematic to
   port to non-Unix systems, such as MS Windows or OpenVMS.

 * Maintainability:  It is much easier to develop and debug native
   Python modules than modules written in C.

Install
=======
In Debian like system, python2 is default python interpreter, so use `pip3`
to install python3 modules:

`# pip3 install python3-xlib`

In Arch Linux:

`# pip install python3-xlib`


COPYRIGHT
=========
The main part of the code is `Copyright (C) 2000-2002  Peter Liljenberg <petli@ctrl-c.liu.se>`

python3-xlib is maintained by `Copyright (C) 2013 LiuLang <gsushzhsosgsu@gmail.com>`
