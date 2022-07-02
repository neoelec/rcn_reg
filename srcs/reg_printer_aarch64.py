# SPDX-License-Identifier: Beerware

from reg_printer import RegisterPrinter


class RegisterPrinterAArch64(RegisterPrinter):
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
        self.__print_last_line()

    def __print_print_reg(cls, start, end):
        for idx in range(start, end):
            reg = 'x' + str(idx)
            super()._print_64(reg)
        print()

    def __print_last_line(cls):
        name_list = ['lr', 'sp', 'pc']
        for name in name_list:
            super()._print_64(name)
        flag_list = [
            (0x80000000, 'N'), (0x40000000, 'Z'), (0x20000000, 'C'),
            (0x10000000, 'V'), (0x08000000, 'Q'), (0x01000000, 'J')
            ]
        for (mask, flag) in flag_list:
            super()._print_flag('cpsr', mask, flag)
        cls.__print_cpsr_ge()
        cls.__print_cpsr_it()
        flag_list = [
            (0x00000200, 'E'), (0x00000100, 'A'), (0x00000080, 'I'),
            (0x00000040, 'F'), (0x00000020, 'T')
            ]
        for (mask, flag) in flag_list:
            super()._print_flag('cpsr', mask, flag)
        cls.__print_cpsr_m()
        print()

    def __print_cpsr_ge(cls):
        reader = cls.__reader
        cpsr = reader.read('cpsr')
        cpsr_ge = (cpsr >> 16) & 0xF
        print(f' GE[{cpsr_ge:02x}]', end = '')

    def __print_cpsr_it(cls):
        reader = cls.__reader
        cpsr = reader.read('cpsr')
        cpsr_it = (cpsr >> 10) & 0x3F
        cpsr_it = (cpsr_it << 2) | ((cpsr >> 25) & 0x3)
        print(f' IT[{cpsr_it:02x}]', end = '')

    def __print_cpsr_m(cls):
        reader = cls.__reader
        cpsr = reader.read('cpsr')
        cpsr_m = cpsr & 0x1F
        mode_list = {
            0x10: 'Usr',
            0x11: 'Fiq',
            0x12: 'Irq',
            0x13: 'Svc',
            0x16: 'Abt',
            0x1A: 'Hyp',
            0x1B: 'Und',
            0x1F: 'Sys',
            0x00: 'EL0t',
            0x04: 'EL1t',
            0x05: 'EL1h',
            0x08: 'EL2t',
            0x09: 'EL2h',
            0x0C: 'EL3t',
            0x0D: 'EL3h'
            }
        mode = mode_list[cpsr_m] if cpsr_m in mode_list else 'Unkn'
        print(f' {mode:4s}', end = '')
