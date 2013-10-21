#!/usr/bin/env python3

# examples/threadtest.py
#
#    Copyright (C) 2013 LiuLang <gsushzhsosgsu@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import os
import sys
try:
    # Python 3
    import _thread as thread
except ImportError:
    # Python 2
    import thread
import time

# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Xlib import display, X, threaded

def redraw(win, gc):
    # win.clear_area()
    win.fill_rectangle(gc, 20, 20, 60, 60)

def blink(display, win, gc, cols):
    while True:
        time.sleep(2)
        print('Changing color %i' % cols[0])
        gc.change(foreground = cols[0])
        cols = (cols[1], cols[0])
        redraw(win, gc)
        display.flush()

def main():
    d = display.Display()
    root = d.screen().root

    colormap = d.screen().default_colormap

    red = colormap.alloc_named_color("red").pixel
    blue = colormap.alloc_named_color("blue").pixel
    background = colormap.alloc_named_color("white").pixel

    window = root.create_window(100, 100, 100, 100, 1,
                                X.CopyFromParent, X.InputOutput,
                                X.CopyFromParent,
                                background_pixel = background,
                                event_mask = X.StructureNotifyMask |
                                X.ExposureMask)
    window.map()

    gc = window.create_gc(foreground = red)

    thread.start_new_thread(blink, (d, window, gc, (blue, red)))

    while True:
        event = d.next_event()
        if event.type == X.Expose:
            if event.count == 0:
                redraw(window, gc)
        elif event.type == X.DestroyNotify:
            sys.exit(0)

if __name__ == "__main__":
    main()
