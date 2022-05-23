import os
def __get_last_line(self, filename):
    """
    get last line of a file
    :param filename: file name
    :return: last line or None for empty file
    """
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, 'rb') as fp: # to use seek from end, must use mode 'rb'
                offset = -8                 # initialize offset
                while -offset < filesize:   # offset cannot exceed file size
                    fp.seek(offset, 2) #read#offset chars from eof(represent by number'2')
                    lines = fp.readlines()  # read from fp to eof
                    if len(lines) >= 2:     # if contains at least 2 lines
                        return lines[-1]    # then last line is totally included
                    else:
                        offset *= 2         # enlarge offset
                fp.seek(0)
                lines = fp.readlines()
                return lines[-1]
    except FileNotFoundError:
        print(filename + ' not found!')
        return None