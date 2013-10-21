#!/usr/bin/env python3

import array
import os
import struct
import sys
import unittest

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Xlib.protocol import request, rq, event
import Xlib.protocol.event

class CmpArray:
    def __init__(self, *args, **kws):
        self.array = array.array(*args, **kws)

    def __len__(self):
        return len(self.array)

    def __getslice__(self, x, y):
        return list(self.array[x:y])

    def __getattr__(self, attr):
        return getattr(self.array, attr)

    def __eq__(self, other):
        return self.array.tolist() == other

    def __ne__(self, other):
        return self.array.tolist() != other

rq.array = CmpArray

def tohex(bin):
    bin = ''.join(map(lambda c: '\\x%02x' % c, bin))

    bins = []
    for i in range(0, len(bin), 16):
        bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
        try:
            bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
        except IndexError:
            bins2.append("'%s'" % bins[i])

    return ' \\\n            '.join(bins2)

class DummyDisplay:
    def get_resource_class(self, x):
        return None

    event_classes = Xlib.protocol.event.event_class
dummy_display = DummyDisplay()


def check_endian():
    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 1:
        sys.stderr.write('Big-endian tests, skipping on this system.\n')
        sys.exit(0)


class TestKeymapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'type': 154,
            'data': [160, 192, 133, 223, 245, 128, 133, 188, 208, 142, 202, 142, 218, 238, 145, 150, 211, 150, 165, 230, 149, 162, 139, 159, 135, 255, 246, 202, 232, 185, 164],
            }
        self.evt_bin_0 = b'\x9a\xa0\xc0\x85' b'\xdf\xf5\x80\x85' \
            b'\xbc\xd0\x8e\xca' b'\x8e\xda\xee\x91' \
            b'\x96\xd3\x96\xa5' b'\xe6\x95\xa2\x8b' \
            b'\x9f\x87\xff\xf6' b'\xca\xe8\xb9\xa4'


    def testPack0(self):
        bin = event.KeymapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.KeymapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'height': 22214,
            'sequence_number': 56268,
            'type': 254,
            'x': 16974,
            'y': 19752,
            'window': 1381709156,
            'width': 26369,
            'count': 60118,
            }
        self.evt_bin_0 = b'\xfe\x00\xdb\xcc' b'\x52\x5b\x35\x64' \
            b'\x42\x4e\x4d\x28' b'\x67\x01\x56\xc6' \
            b'\xea\xd6\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.Expose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.Expose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGraphicsExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'height': 352,
            'sequence_number': 6380,
            'type': 242,
            'drawable': 820411264,
            'x': 57593,
            'y': 41762,
            'major_event': 216,
            'count': 63321,
            'width': 58556,
            'minor_event': 22632,
            }
        self.evt_bin_0 = b'\xf2\x00\x18\xec' b'\x30\xe6\x7b\x80' \
            b'\xe0\xf9\xa3\x22' b'\xe4\xbc\x01\x60' \
            b'\x58\x68\xf7\x59' b'\xd8\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GraphicsExpose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.GraphicsExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestNoExpose(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 46171,
            'major_event': 242,
            'type': 187,
            'window': 1319843810,
            'minor_event': 45687,
            }
        self.evt_bin_0 = b'\xbb\x00\xb4\x5b' b'\x4e\xab\x37\xe2' \
            b'\xb2\x77\xf2\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.NoExpose._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.NoExpose._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestVisibilityNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'state': 238,
            'sequence_number': 52805,
            'type': 242,
            'window': 1543431298,
            }
        self.evt_bin_0 = b'\xf2\x00\xce\x45' b'\x5b\xfe\xe4\x82' \
            b'\xee\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.VisibilityNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.VisibilityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'height': 15506,
            'sequence_number': 8253,
            'type': 255,
            'border_width': 53414,
            'x': -31204,
            'y': -23908,
            'override': 1,
            'parent': 654326356,
            'window': 8505372,
            'width': 8871,
            }
        self.evt_bin_0 = b'\xff\x00\x20\x3d' b'\x27\x00\x3a\x54' \
            b'\x00\x81\xc8\x1c' b'\x86\x1c\xa2\x9c' \
            b'\x22\xa7\x3c\x92' b'\xd0\xa6\x01\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.CreateNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.CreateNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestDestroyNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 49137,
            'event': 408289937,
            'type': 223,
            'window': 1716558237,
            }
        self.evt_bin_0 = b'\xdf\x00\xbf\xf1' b'\x18\x56\x02\x91' \
            b'\x66\x50\x99\x9d' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.DestroyNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.DestroyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUnmapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'from_configure': 0,
            'sequence_number': 4412,
            'event': 1122103072,
            'type': 217,
            'window': 1455493798,
            }
        self.evt_bin_0 = b'\xd9\x00\x11\x3c' b'\x42\xe1\xef\x20' \
            b'\x56\xc1\x12\xa6' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.UnmapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.UnmapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 65096,
            'event': 328610268,
            'type': 228,
            'window': 1882369959,
            'override': 0,
            }
        self.evt_bin_0 = b'\xe4\x00\xfe\x48' b'\x13\x96\x31\xdc' \
            b'\x70\x32\xaf\xa7' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'parent': 1664235152,
            'sequence_number': 51552,
            'type': 171,
            'window': 488763730,
            }
        self.evt_bin_0 = b'\xab\x00\xc9\x60' b'\x63\x32\x36\x90' \
            b'\x1d\x21\xf1\x52' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MapRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MapRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestReparentNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 9256,
            'event': 2000272853,
            'type': 229,
            'override': 1,
            'x': -28587,
            'y': -11597,
            'parent': 912114770,
            'window': 1142506827,
            }
        self.evt_bin_0 = b'\xe5\x00\x24\x28' b'\x77\x39\xbd\xd5' \
            b'\x44\x19\x45\x4b' b'\x36\x5d\xc4\x52' \
            b'\x90\x55\xd2\xb3' b'\x01\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ReparentNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ReparentNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConfigureNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'height': 16243,
            'sequence_number': 62364,
            'event': 1373455462,
            'type': 191,
            'border_width': 7244,
            'x': -12771,
            'y': -15228,
            'override': 1,
            'above_sibling': 1099666850,
            'window': 2046157981,
            'width': 8604,
            }
        self.evt_bin_0 = b'\xbf\x00\xf3\x9c' b'\x51\xdd\x44\x66' \
            b'\x79\xf5\xe4\x9d' b'\x41\x8b\x95\xa2' \
            b'\xce\x1d\xc4\x84' b'\x21\x9c\x3f\x73' \
            b'\x1c\x4c\x01\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ConfigureNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConfigureRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 31377,
            'value_mask': 19345,
            'type': 156,
            'border_width': 54779,
            'x': -18191,
            'y': -17663,
            'window': 1231046739,
            'width': 51620,
            'height': 47094,
            'sibling': 1154714518,
            'stack_mode': 199,
            'parent': 176713389,
            }
        self.evt_bin_0 = b'\x9c\xc7\x7a\x91' b'\x0a\x88\x6e\xad' \
            b'\x49\x60\x48\x53' b'\x44\xd3\x8b\x96' \
            b'\xb8\xf1\xbb\x01' b'\xc9\xa4\xb7\xf6' \
            b'\xd5\xfb\x4b\x91' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ConfigureRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ConfigureRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGravityNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 43376,
            'event': 641536677,
            'type': 192,
            'window': 51697690,
            'x': -21924,
            'y': -4866,
            }
        self.evt_bin_0 = b'\xc0\x00\xa9\x70' b'\x26\x3d\x12\xa5' \
            b'\x03\x14\xd8\x1a' b'\xaa\x5c\xec\xfe' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.GravityNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.GravityNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestResizeRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'height': 59752,
            'sequence_number': 21348,
            'type': 149,
            'window': 1698104652,
            'width': 41494,
            }
        self.evt_bin_0 = b'\x95\x00\x53\x64' b'\x65\x37\x05\x4c' \
            b'\xa2\x16\xe9\x68' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ResizeRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ResizeRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPropertyNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'atom': 762586168,
            'sequence_number': 29670,
            'time': 1791118117,
            'type': 188,
            'state': 181,
            'window': 334365400,
            }
        self.evt_bin_0 = b'\xbc\x00\x73\xe6' b'\x13\xee\x02\xd8' \
            b'\x2d\x74\x24\x38' b'\x6a\xc2\x4b\x25' \
            b'\xb5\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.PropertyNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.PropertyNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionClear(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'time': 578079299,
            'sequence_number': 13691,
            'atom': 1385452659,
            'type': 170,
            'window': 355039782,
            }
        self.evt_bin_0 = b'\xaa\x00\x35\x7b' b'\x22\x74\xca\x43' \
            b'\x15\x29\x7a\x26' b'\x52\x94\x54\x73' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionClear._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionClear._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionRequest(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 13254,
            'type': 162,
            'property': 397160681,
            'owner': 2075837783,
            'time': 1154635674,
            'target': 1312534659,
            'selection': 1972323175,
            'requestor': 178195168,
            }
        self.evt_bin_0 = b'\xa2\x00\x33\xc6' b'\x44\xd2\x57\x9a' \
            b'\x7b\xba\xc5\x57' b'\x0a\x9f\x0a\xe0' \
            b'\x75\x8f\x43\x67' b'\x4e\x3b\xb0\x83' \
            b'\x17\xac\x30\xe9' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionRequest._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionRequest._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSelectionNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 39736,
            'type': 199,
            'property': 302372755,
            'time': 882192222,
            'target': 2131462701,
            'selection': 781895626,
            'requestor': 1242076588,
            }
        self.evt_bin_0 = b'\xc7\x00\x9b\x38' b'\x34\x95\x2f\x5e' \
            b'\x4a\x08\x95\xac' b'\x2e\x9a\xc7\xca' \
            b'\x7f\x0b\x8a\x2d' b'\x12\x05\xd7\x93' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.SelectionNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.SelectionNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestColormapNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'state': 209,
            'sequence_number': 62902,
            'colormap': 300799750,
            'type': 233,
            'window': 1591667531,
            'new': 1,
            }
        self.evt_bin_0 = b'\xe9\x00\xf5\xb6' b'\x5e\xde\xeb\x4b' \
            b'\x11\xed\xd7\x06' b'\x01\xd1\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.ColormapNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ColormapNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


class TestClientMessage(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 48712,
            'data': (8, '01234567890123456789'),
            'type': 245,
            'client_type': 1340394836,
            'window': 1256861040,
            }
        self.evt_bin_0 = b'\xf5\x08\xbe\x48' b'\x4a\xea\x2d\x70' \
            b'\x4f\xe4\xcd\x54' b'\x30\x31\x32\x33' \
            b'\x34\x35\x36\x37' b'\x38\x39\x30\x31' \
            b'\x32\x33\x34\x35' b'\x36\x37\x38\x39'

        self.evt_args_1 = {
            'sequence_number': 62804,
            'data': (16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'type': 250,
            'client_type': 214585025,
            'window': 151327338,
            }
        self.evt_bin_1 = b'\xfa\x10\xf5\x54' b'\x09\x05\x12\x6a' \
            b'\x0c\xca\x4e\xc1' b'\x00\x01\x00\x02' \
            b'\x00\x03\x00\x04' b'\x00\x05\x00\x06' \
            b'\x00\x07\x00\x08' b'\x00\x09\x00\x0a'

        self.evt_args_2 = {
            'sequence_number': 3122,
            'data': (32, [1, 2, 3, 4, 5]),
            'type': 243,
            'client_type': 698151018,
            'window': 725159371,
            }
        self.evt_bin_2 = b'\xf3\x20\x0c\x32' b'\x2b\x39\x0d\xcb' \
            b'\x29\x9c\xf0\x6a' b'\x00\x00\x00\x01' \
            b'\x00\x00\x00\x02' b'\x00\x00\x00\x03' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x05'


    def testPack0(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPack1(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_1)
        try:
            assert bin == self.evt_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack1(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_1
        except AssertionError:
            raise AssertionError(args)

    def testPack2(self):
        bin = event.ClientMessage._fields.to_binary(*(), **self.evt_args_2)
        try:
            assert bin == self.evt_bin_2
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack2(self):
        args, remain = event.ClientMessage._fields.parse_binary(self.evt_bin_2, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_2
        except AssertionError:
            raise AssertionError(args)


class TestMappingNotify(unittest.TestCase):
    def setUp(self):
        self.evt_args_0 = {
            'sequence_number': 53541,
            'count': 151,
            'request': 141,
            'type': 252,
            'first_keycode': 218,
            }
        self.evt_bin_0 = b'\xfc\x00\xd1\x25' b'\x8d\xda\x97\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPack0(self):
        bin = event.MappingNotify._fields.to_binary(*(), **self.evt_args_0)
        try:
            assert bin == self.evt_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpack0(self):
        args, remain = event.MappingNotify._fields.parse_binary(self.evt_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.evt_args_0
        except AssertionError:
            raise AssertionError(args)


if __name__ == "__main__":
    check_endian()
    unittest.main()
