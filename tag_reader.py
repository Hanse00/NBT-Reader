from enum import Enum
import file_reader

test_file_path = "/Applications/MultiMC.app/Contents/MacOS/instances/SRP Test/minecraft/saves/New World/level.dat"

class TagType(Enum):
    TAG_End = 0
    TAG_Byte = 1
    TAG_Short = 2
    TAG_Int = 3
    TAG_Long = 4
    TAG_Float = 5
    TAG_Double = 6
    TAG_Byte_Array = 7
    TAG_String = 8
    TAG_List = 9
    TAG_Compund = 10
    TAG_Int_Array = 11

class Tag(object):
    def __init__(self, tag_type, name = None, data = None):
        self.type = tag_type
        self.name = name
        self.data = data

    def __str__(self):
        return "Tag - type: '{}', name: '{}', data: '{}'".format(
            self.type, self.name, self.data)

    def __repr__(self):
        return "Tag - '{}' '{}' '{}'".format(
            self.type, self.name, self.data)

    @classmethod
    def get_tag_from_data(cls, data):
        tag_type = TagType(data[0])

        if tag_type == TagType.TAG_End:
            tag = Tag(TagType.TAG_End)
            remainder = data[1:]
            return tag, remainder

        name_len_1 = data[1]
        name_len_2 = data[2]
        name_length = (name_len_1 << 8) + name_len_2


        remainder = data[1:]
        return tag, remainder

def read_tags(data_stream):
    tag_list = []

    while len(data_stream) > 0:
        tag, data_stream = Tag.get_tag_from_data(data_stream)

        if tag.type == TagType.TAG_Compund:
            nested_tags, data_stream = read_tags(data_stream)
            tag.data = nested_tags
            tag_list.append(tag)
        elif tag.type == TagType.TAG_End:
            return tag_list, data_stream
        else:
            tag_list.append(tag)

    return tag_list

test_data = file_reader.read_gzipped_file(test_file_path)
tags = read_tags(test_data)
