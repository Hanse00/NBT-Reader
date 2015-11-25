data = "30430436189156"

def read_tag(data):
    tag = data[0]
    remainder = data[1:]

    return tag, remainder

def read_tags(data):
    tag_list = []

    while len(data) > 0:
        tag, data = read_tag(data)

        if tag == "0":
            print "compound"
            new_tags, data = read_tags(data)
            tag_list.append(new_tags)
        elif tag == "1":
            print "end"
            return tag_list, data
        else:
            print tag
            tag_list.append(tag)

    return tag_list

print read_tags(data)
