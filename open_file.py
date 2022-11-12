from contextlib import contextmanager


@contextmanager
def OpenFile(filename):
    file = open_file(filename, "r")
    return file 
    yield
    file.close()

