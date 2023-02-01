# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.reg_printer import RcnRegPrinter


class RcnRegPrinterArm(RcnRegPrinter):
    def __init__(self, reader):
        super().__init__(reader)
        self.__reader = reader

    def print(self):
        self.__print_print_reg(0, 7)
        self.__print_print_reg(7, 13)
        self.__print_lr_sp_pc()
        self.__print_cpsr()

    def __print_print_reg(self, start, end):
        for idx in range(start, end):
            reg = 'r' + str(idx)
            super()._print_32(reg)
        print()

    def __print_lr_sp_pc(self):
        name_list = ['sp', 'lr', 'pc']
        for name in name_list:
            super()._print_32(name)
        print()

    def __print_cpsr(self):
        reader = self.__reader
        flag_list = [
            ('M', 0, 4),
            ('T', 5, 5),
            ('F', 6, 6),
            ('I', 7, 7),
            ('A', 8, 8),
            ('E', 9, 9),
        ]
        print(' [', end='')
        for (flag, start, end) in flag_list:
            super()._print_flag('cpsr', flag, start, end)
        cpsr = reader.read('cpsr')
        it = (cpsr >> 10) & 0x3F
        it = (it << 2) | ((cpsr >> 25) & 0x3)
        print(f' IT={it:d}', end='')
        ge = (cpsr >> 16) & 0xF
        print(f' GE={ge:d}', end='')
        flag_list = [
            ('J', 24, 24),
            ('V', 28, 28),
            ('C', 29, 29),
            ('Z', 30, 30),
            ('N', 31, 31)
        ]
        for (flag, start, end) in flag_list:
            super()._print_flag('cpsr', flag, start, end)
        print(' ]')
