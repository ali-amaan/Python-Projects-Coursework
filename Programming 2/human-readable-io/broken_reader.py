from io import StringIO


class BrokenReader(StringIO):
    """
    This class is used to artificially create problems. :)

    The class will take a normal Reader object and serve
    all data read from that Reader until a given breaking
    point is reached. At this point the read method will throw
    an OSException.
    """

    def __init__(self, test_data, raise_exception_at):
        """
        Constructs a new BrokenReader from a given data.

        @param test_data: the test data used for initializing the StreamIO.
        @param raise_exception_at: The breaking point position.
        """
        StringIO.__init__(self, test_data)
        self.raise_counter = raise_exception_at


    def close(self):
        """
        If the raise_counter is set high enough, all data can be read.
        In this case closing the stream will throw the OSError instead.
        """
        raise OSError("Simulated I/O problem")


    def close_really(self):
        """
        Closes the file finally.
        """
        StringIO.close(self)


    def read(self, length):
        """
        Works as a normal read-method until the breaking point is reached.
        It then throws a simulated OSException.
        """
        if self.raise_counter <= length:
            raise OSError("Simulated I/O problem")

        self.raise_counter -= length
        read_chars = StringIO.read(self, length)

        return read_chars


    def readline(self):
        """
        Works as a normal readline-method until the breaking point is reached.
        It then throws a simulated OSException.
        """
        read_chars = StringIO.readline(self)
        length = len(read_chars)
        if self.raise_counter <= length:
            raise OSError("Simulated I/O problem")

        self.raise_counter -= length

        return read_chars
