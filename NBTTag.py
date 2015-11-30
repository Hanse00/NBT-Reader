from enum import Enum

testing_data = [b'\x04', b'\x00', b'\n', b'R', b'a', b'n', b'd', b'o', b'm', b'S', b'e', b'e', b'd', b'P', b'\xd9', b'\xb8', b'\xd8', b'\xd5', b'\t', b'>', b'\x04']

print(testing_data)

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
    pass
