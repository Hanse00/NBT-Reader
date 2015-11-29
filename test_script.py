import struct
import file_reader

data_string = "1231235123123123123513123"

class data(object):
    def __init__(self, content):
        self.content = content
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.content):
            raise StopIteration
        else:
            item = self.content[self.index]
            self.index += 1
            return item

data_container = data(data_string)

#for x in data_container:
#    print(x)

test_file_path = "/Applications/MultiMC.app/Contents/MacOS/instances/SRP Test/minecraft/saves/New World/level.dat"

data =  file_reader.read_gzipped_file(test_file_path)

print(data)

relevant_data = data[23:23 + 8]

relevant_data_string = b''.join(relevant_data)

number = struct.unpack(">q", relevant_data_string)

print(number)
