from enum import Enum
import file_reader

test_file_path = "/Applications/MultiMC.app/Contents/MacOS/instances/SRP Test/minecraft/saves/New World/level.dat"
test_date = file_reader.read_gzipped_file(test_file_path)

print(test_date)

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
        tag = Tag(data[0])
        remainder = data[1:]

        return tag, remainder

def read_tags(data):
    tag_list = []

    while len(data) > 0:
        tag, data = Tag.get_tag_from_data(data)

        if tag.data == str(TagType.TAG_Compund.value):
            print("compound")
            new_tags, data = read_tags(data)
            tag_list.append(Tag(new_tags))
        elif tag.data == str(TagType.TAG_End.value):
            print("end")
            return tag_list, data
        else:
            print(tag)
            tag_list.append(tag)

    return tag_list

print(read_tags(data))
