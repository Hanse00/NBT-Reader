import gzip

def read_gzipped_file(file_path):
    with gzip.open(file_path, "rb") as f:
        byte_list = []

        byte = f.read(1)

        while byte != b'':
            byte_list.append(byte)
            byte = f.read(1)

        return byte_list
