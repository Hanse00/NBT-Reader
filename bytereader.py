import struct

from tagtype import TagType

STRUCT_FORMATS = {TagType.type_byte: ">b",
                  TagType.type_short: ">h",
                  TagType.type_int: ">i",
                  TagType.type_long: ">q",
                  TagType.type_float: ">f",
                  TagType.type_double: ">d"
}

def get_number_from_bytes(data_bytes, number_type):
    byte_string = b''.join(data_bytes)
    number = struct.unpack(STRUCT_FORMATS[number_type], byte_string)[0]
    return number

def get_byte_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_byte)

def get_short_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_short)

def get_int_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_int)

def get_long_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_long)

def get_float_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_float)

def get_double_from_bytes(data_bytes):
    return _get_number_from_bytes(data_bytes, TagType.type_double)

def get_string_from_bytes(data_bytes):
    byte_string = b''.join(data_bytes)
    string = byte_string.decode("utf-8")
    return string
