import struct
import file_reader

data_list = [1,2,3,4,5]

class RawData(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def _is_valid_index(self, index):
        if not type(index) is int:
            error = "Index must be an integer"
            raise ValueError(error)

        # Check that it's within the valid range 0 < index < (length of data)
        if not (index >= 0) or not (index < len(self.data)):
            error = "Index out of range. Index: {}, Valid range: 0, {}".format(
                index, len(self.data) - 1)
            raise ValueError(error)

        return True

    def get(self, start_index, end_index=None):
        self._is_valid_index(start_index)
        if end_index:
            self._is_valid_index(end_index)

        return "Indexes are valid!"

data_object = RawData(data_list)
print(data_object)
print(data_object.get(0))
print(data_object)
print(data_object.get(0,3))




#for x in data_container:
#    print(x)

#test_file_path = "/Applications/MultiMC.app/Contents/MacOS/instances/SRP Test/minecraft/saves/New World/level.dat"

#data =  file_reader.read_gzipped_file(test_file_path)

#print(data)

#relevant_data = data[23:23 + 8]

#relevant_data_string = b''.join(relevant_data)

#number = struct.unpack(">q", relevant_data_string)

#print(number)
