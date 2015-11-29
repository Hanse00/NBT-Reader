import gzip

def read_gzipped_file(file_path):
    byte_list = []

    with gzip.open(file_path, "rb") as f:
        byte = f.read(1)

        while byte != b'':
            byte_list.append(ord(byte))
            byte = f.read(1)

    return byte_list
