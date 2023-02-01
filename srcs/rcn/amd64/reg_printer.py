# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.reg_printer import RcnRegPrinter


class RcnRegPrinterAMD64(RcnRegPrinter):
    def __init__(self, reader):
        super().__init__(reader)

    def print(self):
        self.__print_1st_line()
        self.__print_2nd_line()
        self.__print_3rd_line()
        self.__print_4th_line()
        self.__print_5th_line()
        self.__print_6th_line()

    def __print_1st_line(self):
        name_list = ['rax', 'rbx', 'rcx', 'rdx', 'rsi']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_2nd_line(self):
        name_list = ['rdi', 'r8', 'r9', 'r10', 'r11']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_3rd_line(self):
        name_list = ['r12', 'r13', 'r14', 'r15']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_4th_line(self):
        name_list = ['cs', 'ds', 'es', 'fs', 'gs', 'ss']
        for name in name_list:
            super()._print_16(name)
        print()

    def __print_5th_line(self):
        name_list = ['rbp', 'rsp', 'rip']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_6th_line(self):
        flag_list = [
            ('CF', 0, 0),
            ('PF', 2, 2),
            ('AF', 4, 4),
            ('ZF', 6, 6),
            ('SF', 7, 7),
            ('TF', 8, 8),
            ('IF', 9, 9),
            ('DF', 10, 10),
            ('OF', 11, 11),
            ('NT', 14, 14),
            ('RF', 16, 16),
            ('VM', 17, 17),
            ('AC', 18, 18),
            ('VIF', 19, 19),
            ('VIP', 20, 20),
            ('ID', 21, 21)
        ]
        print(' [', end='')
        for (flag, start, end) in flag_list:
            super()._print_flag('eflags', flag, start, end)
        print(' ]')
