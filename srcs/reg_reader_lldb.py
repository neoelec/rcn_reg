# SPDX-License-Identifier: Beerware

import lldb
from reg_reader import RegisterReader


class RegisterReaderLLDB(RegisterReader):
    def __init__(self, exe_ctx):
        self.__register = exe_ctx.frame.register

    def read(self, name):
        register = self.__register
        aliases = {
            'eflags': 'rflags',
            'x30': 'fp'
            }
        reg_name = name if name not in aliases else aliases[name]
        return int(register[reg_name].value, 16)
