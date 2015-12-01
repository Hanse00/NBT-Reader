from enum import Enum

class TagType(Enum):
    type_end = 0
    type_byte = 1
    type_short = 2
    type_int = 3
    type_long = 4
    type_float = 5
    type_double = 6
    type_byte_array = 7
    type_string = 8
    type_list = 9
    type_compound = 10
    type_int_array = 11

    @classmethod
    def get_from_byte(cls, data_byte):
        byte_value = ord(data_byte)
        tag_type = cls(byte_value)
        return tag_type

    # Check if the byte given is a valid member of the possible tag types
    @classmethod
    def is_valid_type(cls, data_byte):
        return ord(data_byte) in [member.value for member in cls]
