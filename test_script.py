import struct
import file_reader

data_list = [1,2,3,4,5]

class RawData(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def get_single(self, index):
        return self.data.pop(index)

    def get_range(self, start_index, end_index):
        return_data = self.data[start_index:end_index]
        del self.data[start_index:end_index]
        return return_data

data_object = RawData(data_list)
print(data_object)
print(data_object.get_single(0))
print(data_object)
print(data_object.get_range(1,3))
print(data_object)



#for x in data_container:
#    print(x)

#test_file_path = "/Applications/MultiMC.app/Contents/MacOS/instances/SRP Test/minecraft/saves/New World/level.dat"

#data =  file_reader.read_gzipped_file(test_file_path)

#print(data)

#relevant_data = data[23:23 + 8]

#relevant_data_string = b''.join(relevant_data)

#number = struct.unpack(">q", relevant_data_string)

#print(number)
