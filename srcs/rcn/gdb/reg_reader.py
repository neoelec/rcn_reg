# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

import gdb
from rcn.reg_reader import RcnRegReader


class RcnRegReaderGDB(RcnRegReader):
    def __init__(self, modifier):
        self.__frame = gdb.selected_frame()
        self.__modifier = modifier

    def read(self, name):
        frame = self.__frame
        m = self.__modifier
        reg_raw = str(frame.read_register(name))
        reg_val = m.modify(name, reg_raw)
        return reg_val
