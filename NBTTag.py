import struct
from enum import Enum

import ByteContainer

class TagType(Enum):
    End = 0
    Byte = 1
    Short = 2
    Int = 3
    Long = 4
    Float = 5
    Double = 6
    Byte_Array = 7
    String = 8
    List = 9
    Compund = 10
    Int_Array = 11

class NBTTag(object):
    def __init__(self, tag_type, tag_name = None, tag_data = None):
        self.tag_type = tag_type
        self.tag_name = tag_name
        self.tag_data = tag_data

    def __repr__(self):
        return "<NBTTag type:{}, name:{}, data:{}>".format(self.tag_type,
            self.tag_name, self.tag_data)

    @classmethod
    def _get_short_from_bytes(cls, byte_values):
        byte_string = b''.join(byte_values)
        short = struct.unpack(">h", byte_string)[0]
        return short

    @classmethod
    def _get_long_from_bytes(cls, byte_values):
        byte_string = b''.join(byte_values)
        long_value = struct.unpack(">q", byte_string)[0]
        return long_value

    @classmethod
    def _get_string_from_bytes(cls, byte_values):
        byte_string = b''.join(byte_values)
        string = byte_string.decode("utf-8")
        return string

    @classmethod
    def _get_type_from_byte(cls, byte):
        byte_value = ord(byte)
        tag_type = TagType(byte_value)
        return tag_type

    @classmethod
    def _get_name_from_bytecontainer(cls, bytecontainer):
        length_bytes = bytecontainer.get(2)
        name_length = cls._get_short_from_bytes(length_bytes)

        name_bytes = bytecontainer.get(name_length)
        name = cls._get_string_from_bytes(name_bytes)
        return name

    @classmethod
    def get_tag_from_byte_container(cls, bytecontainer):
        #TODO: Check if this is a valid tag type
        tag_type = cls._get_type_from_byte(bytecontainer.get(1))
        if tag_type == TagType.End:
            return cls(tag_type)

        #TODO: Name of length 0 is possible, code does not allow it
        tag_name = cls._get_name_from_bytecontainer(bytecontainer)

        #TODO: Read in the various data types
        tag_data = cls._get_long_from_bytes(bytecontainer.get(8))
        return cls(tag_type, tag_name, tag_data)


testing_data = [b'\x04', b'\x00', b'\n', b'R', b'a', b'n', b'd', b'o', b'm', b'S', b'e', b'e', b'd', b'P', b'\xd9', b'\xb8', b'\xd8', b'\xd5', b'\t', b'>', b'\x04']
container = ByteContainer.ByteContainer(testing_data)
tag = NBTTag.get_tag_from_byte_container(container)
print(tag)
