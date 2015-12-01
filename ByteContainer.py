class ByteContainer(object):
    def __init__(self, data):
        self.data = data

    # Check that n is a valid number of bytes to request
    def _validate_number(self, n):
        # Check if n is an int
        if not type(n) is int:
            error = "Number must be type 'int', is type '{}'".format(
                type(n).__name__)
            raise ValueError(error)

        # Check if 0 < n <= len(data)
        if not n > 0 or not n <= len(self.data):
            error = "Number out of range. Value: {}, range: 1, {}".format(
                n, len(self.data))
            raise ValueError(error)

        return True

    def _retrieve_n_bytes(self, n):
        return self.data[0:n]

    def _remove_n_bytes(self, n):
        del self.data[0:n]

    def __len__(self):
        return len(self.data)

    # Get the next n bytes, removing them from the object data
    def get(self, n):
        self._validate_number(n)
        data = self._retrieve_n_bytes(n)
        self._remove_n_bytes(n)

        # If data has length 1, return the value itself rather than
        # a list of length 1
        if n == 1:
            data = data[0]
        return data
