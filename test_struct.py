# -*- coding: utf-8 -*-

import struct


LENGHT_HEADER = '!I'

HEADER_LENGTH = struct.calcsize(LENGHT_HEADER)
print HEADER_LENGTH

