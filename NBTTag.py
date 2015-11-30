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
    def _get_type_from_byte(cls, byte):
        byte_value = ord(byte)
        tag_type = TagType(byte_value)
        return tag_type

    @classmethod
    def get_tag_from_byte_container(cls, bytecontainer):
        tag_type = cls._get_type_from_byte(bytecontainer.get(1))
        return cls(tag_type)

testing_data = [b'\x04', b'\x00', b'\n', b'R', b'a', b'n', b'd', b'o', b'm', b'S', b'e', b'e', b'd', b'P', b'\xd9', b'\xb8', b'\xd8', b'\xd5', b'\t', b'>', b'\x04']
container = ByteContainer.ByteContainer(testing_data)
tag = NBTTag.get_tag_from_byte_container(container)
print(tag)
