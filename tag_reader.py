data = "30430436189156"

class Tag(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "Tag - '{}'".format(self.data)

    def __repr__(self):
        return "Tag - '{}'".format(self.data)

    @classmethod
    def get_tag_from_data(cls, data):
        tag = Tag(data[0])
        remainder = data[1:]

        return tag, remainder

def read_tags(data):
    tag_list = []

    while len(data) > 0:
        tag, data = Tag.get_tag_from_data(data)

        if tag.data == "0":
            print "compound"
            new_tags, data = read_tags(data)
            tag_list.append(Tag(new_tags))
        elif tag.data == "1":
            print "end"
            return tag_list, data
        else:
            print tag
            tag_list.append(tag)

    return tag_list

print read_tags(data)
