# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

import lldb
from rcn.reg_reader import RcnRegReader


class RcnRegReaderLLDB(RcnRegReader):
    def __init__(self, exe_ctx, aliases):
        self.__register = exe_ctx.frame.register
        self.__aliases = aliases

    def read(self, name):
        register = self.__register
        aliases = self.__aliases
        reg_name = name if name not in aliases else aliases[name]
        return int(register[reg_name].value, 16)
