""" Utility functions
"""
import random
import time
from . import constants
import codecs
import os
import struct

try:
    unicode = str;
except:
    pass

guid_rng = random.Random()   # Uses urandom seed


def collector_url_from_hostport(host, port):
    """
    Create an appropriate collector URL given the parameters.
    """
    return ''.join(['http://', host, ':', str(port), '/api/v1/spans'])


def id_to_hex(id):
    if id is None:
        return None
    return '{0:x}'.format(id)


def coerce_str(str_or_unicode):
    if isinstance(str_or_unicode, str):
        return str_or_unicode
    elif isinstance(str_or_unicode, unicode):
        return str_or_unicode.encode('utf-8', 'replace')
    else:
        try:
            return str(str_or_unicode)
        except Exception:
            # Never let these errors bubble up
            return '(encoding error)'


def unsigned_hex_to_signed_int(hex_string):
    """Converts a 64-bit hex string to a signed int value.
    This is due to the fact that Apache Thrift only has signed values.
    Examples:
        '17133d482ba4f605' => 1662740067609015813
        'b6dbb1c2b362bf51' => -5270423489115668655
    :param hex_string: the string representation of a zipkin ID
    :returns: signed int representation
    """
    return struct.unpack('q', struct.pack('Q', int(hex_string, 16)))[0]
