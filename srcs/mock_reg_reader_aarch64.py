# SPDX-License-Identifier: Beerware

from reg_reader import RegisterReader


class RegisterReaderMockAArch64(RegisterReader):
    def __init__(self):
        self.__register = {
            'x0': 0x1,
            'x1': 0xfffffffff4d8,
            'x2': 0xfffffffff4e8,
            'x3': 0xaaaaaaaa0774,
            'x4': 0x0,
            'x5': 0xfa114e0947ca4c1e,
            'x6': 0xfffff7fc8788,
            'x7': 0x10001004000000,
            'x8': 0xffffffffffffffff,
            'x9': 0x3,
            'x10': 0x0,
            'x11': 0x0,
            'x12': 0xfffff7e5d228,
            'x13': 0x0,
            'x14': 0x0,
            'x15': 0x6fffff47,
            'x16': 0x0,
            'x17': 0x0,
            'x18': 0xffffffffdf50,
            'x19': 0xaaaaaaaa07a0,
            'x20': 0x0,
            'x21': 0xaaaaaaaa0660,
            'x22': 0x0,
            'x23': 0x0,
            'x24': 0x0,
            'x25': 0x0,
            'x26': 0x0,
            'x27': 0x0,
            'x28': 0x0,
            'x29': 0xfffffffff360,
            'lr': 0xfffff7e7a218,
            'sp': 0xfffffffff360,
            'pc': 0xaaaaaaaa0784,
            'cpsr': 0x60000000
            }

    def read(self, name):
        register = self.__register
        return register[name]
