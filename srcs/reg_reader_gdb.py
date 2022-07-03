# SPDX-License-Identifier: Beerware

import gdb
from reg_reader import RegisterReader


class RegisterReaderGDB(RegisterReader):
    def __init__(self, modifier):
        self.__frame = gdb.selected_frame()
        self.__modifier = modifier

    def read(self, name):
        frame = self.__frame
        m = self.__modifier
        reg_raw = str(frame.read_register(name))
        reg_val = m.modiry(name, reg_raw)
        return reg_val
