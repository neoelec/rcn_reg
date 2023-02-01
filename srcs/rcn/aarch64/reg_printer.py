# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.reg_printer import RcnRegPrinter


class RcnRegPrinterAArch64(RcnRegPrinter):
    def __init__(self, reader):
        super().__init__(reader)
        self.__reader = reader

    def print(self):
        self.__print_print_reg(0, 5)
        self.__print_print_reg(5, 10)
        self.__print_print_reg(10, 15)
        self.__print_print_reg(15, 20)
        self.__print_print_reg(20, 25)
        self.__print_print_reg(25, 30)
        self.__print_lr_sp_pc()
        self.__print_cpsr()

    def __print_print_reg(self, start, end):
        for idx in range(start, end):
            reg = 'x' + str(idx)
            super()._print_64(reg)
        print()

    def __print_lr_sp_pc(self):
        name_list = ['lr', 'sp', 'pc']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_cpsr(self):
        flag_list = [
            ('SP', 0, 0),
            ('EL', 2, 3),
            ('nRW', 4, 4),
            ('F', 6, 6),
            ('I', 7, 7),
            ('A', 8, 8),
            ('D', 9, 9),
            ('BTYPE', 10, 11),
            ('SSBS', 12, 12),
            ('IL', 20, 20),
            ('SS', 21, 21),
            ('PAN', 22, 22),
            ('UAO', 23, 23),
            ('DIT', 24, 24),
            ('TCO', 25, 25),
            ('V', 28, 28),
            ('C', 29, 29),
            ('Z', 30, 30),
            ('N', 31, 31)
        ]
        print(' [', end='')
        for (flag, start, end) in flag_list:
            super()._print_flag('cpsr', flag, start, end)
        print(' ]')
