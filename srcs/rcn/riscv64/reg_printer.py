# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.reg_printer import RcnRegPrinter


class RcnRegPrinterRiscV64(RcnRegPrinter):
    def __init__(self, reader):
        super().__init__(reader)
        self.__reader = reader
        self.__reg2abi = {
            'x1': 'ra',
            'x2': 'sp',
            'x3': 'gp',
            'x4': 'tp',
            'x5': 't0',
            'x6': 't1',
            'x7': 't2',
            'x8': 'fp',
            'x9': 's1',
            'x10': 'a0',
            'x11': 'a1',
            'x12': 'a2',
            'x13': 'a3',
            'x14': 'a4',
            'x15': 'a5',
            'x16': 'a6',
            'x17': 'a7',
            'x18': 's2',
            'x19': 's3',
            'x20': 's4',
            'x21': 's5',
            'x22': 's6',
            'x23': 's7',
            'x24': 's8',
            'x25': 's9',
            'x26': 's10',
            'x27': 's11',
            'x28': 't3',
            'x29': 't4',
            'x30': 't5',
            'x31': 't6'
        }

    def print(self):
        self.__print_print_reg(1, 6)
        self.__print_print_reg(6, 11)
        self.__print_print_reg(11, 16)
        self.__print_print_reg(16, 21)
        self.__print_print_reg(21, 26)
        self.__print_print_reg(26, 31)
        self.__print_pc()

    def __print_print_reg(self, start, end):
        reg2abi = self.__reg2abi
        for idx in range(start, end):
            reg = 'x' + str(idx)
            super()._print_64(reg2abi[reg])
        print()

    def __print_pc(self):
        super()._print_64('pc')
        print()

    def __print_cpsr(self):
        pass
