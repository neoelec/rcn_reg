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
        self.__print_lr_sp_pc()
        self.__print_cpsr()

    def __print_print_reg(cls, start, end):
        for idx in range(start, end):
            reg = 'x' + str(idx)
            super()._print_64(reg)
        print()

    def __print_lr_sp_pc(cls):
        name_list = ['lr', 'sp', 'pc']
        for name in name_list:
            super()._print_64(name)
        print()

    def __print_cpsr(cls):
        flag_list = [
            (0x80000000, 'N'), (0x40000000, 'Z'), (0x20000000, 'C'),
            (0x10000000, 'V'), (0x08000000, 'Q'), (0x01000000, 'J'),
            (0x02000000, 'TCO'), (0x01000000, 'DIT'), (0x00800000, 'UAO'),
            (0x00400000, 'PAN'), (0x00200000, 'SS'), (0x00100000, 'IL'),
            (0x00001000, 'SSBS')
            ]
        for (mask, flag) in flag_list:
            super()._print_flag('cpsr', mask, flag)
        cls.__print_cpsr_BYTE()
        flag_list = [
            (0x00000200, 'E'), (0x00000100, 'A'), (0x00000080, 'I'),
            (0x00000040, 'F'), (0x00000020, 'T')
            ]
        for (mask, flag) in flag_list:
            super()._print_flag('cpsr', mask, flag)
        cls.__print_cpsr_m()
        print()

    def __print_cpsr_BYTE(cls):
        reader = cls.__reader
        cpsr = reader.read('cpsr')
        cpsr_byte = (cpsr >> 10) & 0x3
        if cpsr_byte == 1:
            print(' BTI_c ', end = '')
        elif cpsr_byte == 2:
            print(' BTIj_ ', end = '')
        elif cpsr_byte == 3:
            print(' BTIjc', end = '')
        else:
            print(' bti__', end = '')

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
