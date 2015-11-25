data = "00101001"

tag_list = []

def read_tag(data):
    tag = data[0]
    remainder = data[1:]

    return tag, remainder

while len(data) > 0:
    tag, data = read_tag(data)
    tag_list.append(tag)

print tag_list
