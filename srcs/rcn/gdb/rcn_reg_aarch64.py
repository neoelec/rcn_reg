# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

import gdb
from rcn.gdb.reg_reader import RcnRegReaderGDB
from rcn.aarch64.reg_printer import RcnRegPrinterAArch64


class GDBRCNRegisterAArch64(gdb.Command):
    def __init__(self):
        super(GDBRCNRegisterAArch64, self).__init__('rcn_reg', gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        modifier = GDBModifierAArch64()
        reader = RcnRegReaderGDB(modifier)
        printer = RcnRegPrinterAArch64(reader)
        printer.print()


class GDBModifierAArch64:
    def modify(self, name, reg_raw):
        if name != 'cpsr':
            reg_val = int(reg_raw.split()[0], 0)
            reg_val &= 0xFFFFFFFFFFFFFFFF
        else:
            reg_val = self.__cpsr(reg_raw)
        return reg_val

    def __cpsr(cls, reg_raw):
        mask = {
            'SP': 1 << 0,
            'EL=1': 1 << 2,
            'EL=2': 2 << 2,
            'EL=3': 3 << 2,
            'nRW': 1 << 4,
            'F': 1 << 6,
            'I': 1 << 7,
            'A': 1 << 8,
            'D': 1 << 9,
            'BTYPE=1': 1 << 10,
            'BTYPE=2': 2 << 10,
            'BTYPE=3': 3 << 10,
            'SSBS': 1 << 12,
            'IL': 1 << 20,
            'SS': 1 << 21,
            'PAN': 1 << 22,
            'UAO': 1 << 23,
            'DIT': 1 << 24,
            'TCO': 1 << 25,
            'V': 1 << 28,
            'C': 1 << 29,
            'Z': 1 << 30,
            'N': 1 << 31
            }
        reg_val = 0x0
        for bit in reg_raw.split():
            reg_val |= 0x0 if bit not in mask else mask[bit]
        return reg_val


GDBRCNRegisterAArch64()
