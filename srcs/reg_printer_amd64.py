# SPDX-License-Identifier: Beerware

from reg_printer import RegisterPrinter


class RegisterPrinterAMD64(RegisterPrinter):
    def __init__(self, reader):
        super().__init__(reader)

    def print(self):
        self.__print_1st_line()
        self.__print_2nd_line()
        self.__print_3rd_line()
        self.__print_4th_line()
        self.__print_5th_line()

    def __print_1st_line(cls):
        name_list = ['rax', 'rbx', 'rcx', 'rdx']
        for name in name_list:
            super()._print_64(name)
        flag_list = [
            (0x0800, 'O'), (0x0400, 'D'), (0x0200, 'I'), (0x0100, 'T'),
            (0x0080, 'S'), (0x0040, 'Z'), (0x0010, 'A'),
            (0x0004, 'P'), (0x0001, 'C')
            ]
        for (mask, flag) in flag_list:
            super()._print_flag('eflags', mask, flag)
        print()

    def __print_2nd_line(cls):
        name_list = ['rsi', 'rdi', 'rbp', 'rsp', 'rip']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_3rd_line(cls):
        name_list = ['r8', 'r9', 'r10', 'r11', 'r12']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_4th_line(cls):
        name_list = ['r13', 'r14', 'r15']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_5th_line(cls):
        name_list = ['cs', 'ds', 'es', 'fs', 'gs', 'ss']
        for name in name_list:
            super()._print_16(name)
        print()
