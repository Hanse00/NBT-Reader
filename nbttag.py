import bytereader
from bytecontainer import ByteContainer
from tagtype import TagType

class NBTTag(object):
    def __init__(self, tag_type, tag_name = None, tag_data = None):
        self.tag_type = tag_type
        self.tag_name = tag_name
        self.tag_data = tag_data

    def __repr__(self):
        return "<NBTTag type:{}, name:{}, data:{}>".format(self.tag_type,
            self.tag_name, self.tag_data)

    @classmethod
    def _get_name_from_bytecontainer(cls, bytecontainer):
        length_bytes = bytecontainer.get(2)
        name_length = bytereader.get_short_from_bytes(length_bytes)

        if name_length == 0:
            return None

        name_bytes = bytecontainer.get(name_length)
        name = bytereader.get_string_from_bytes(name_bytes)
        return name

    @classmethod
    def get_tag_from_byte_container(cls, bytecontainer):
        type_byte = bytecontainer.get(1)
        if not TagType.is_valid_type(type_byte):
            error = "Start byte for tag not valid. Byte:'{}'".format(type_byte)
            raise ValueError(error)

        tag_type = TagType.get_from_byte(type_byte)
        if tag_type == TagType.type_end:
            return cls(tag_type)

        tag_name = cls._get_name_from_bytecontainer(bytecontainer)

        #TODO: Read in the various data types
        tag_data = bytereader.get_long_from_bytes(bytecontainer.get(8))
        return cls(tag_type, tag_name, tag_data)


testing_data = [b'\x04', b'\x00', b'\n', b'R', b'a', b'n', b'd', b'o', b'm', b'S', b'e', b'e', b'd', b'P', b'\xd9', b'\xb8', b'\xd8', b'\xd5', b'\t', b'>', b'\x04', b'\x00']
container = ByteContainer(testing_data)

tags = []
while len(container) > 0:
 tags.append(NBTTag.get_tag_from_byte_container(container))

print(tags)
