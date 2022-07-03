# SPDX-License-Identifier: Beerware

import gdb
import os
import sys
sys.path.append(os.path.dirname(os.path.expanduser(__file__)))
from reg_reader_gdb import RegisterReaderGDB
from reg_printer_amd64 import RegisterPrinterAMD64


class GDBRCNRegisterAMD64(gdb.Command):
    def __init__(self):
        super(GDBRCNRegisterAMD64, self).__init__('rcn_reg', gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        modifier = GDBModifierAMD64()
        reader = RegisterReaderGDB(modifier)
        printer = RegisterPrinterAMD64(reader)
        printer.print()


class GDBModifierAMD64:
    def modiry(self, name, reg_raw):
        if name != 'eflags':
            reg_val = int(reg_raw.split()[0], 0)
            reg_val &= 0xFFFFFFFFFFFFFFFF
        else:
            reg_val = self.__eflags(reg_raw)
        return reg_val

    def __eflags(cls, reg_raw):
        mask = {
            'CF': 1 << 0,
            'PF': 1 << 2,
            'AF': 1 << 4,
            'ZF': 1 << 6,
            'SF': 1 << 7,
            'TF': 1 << 8,
            'IF': 1 << 9,
            'DF': 1 << 10,
            'OF': 1 << 11,
            'NT': 1 << 14,
            'RF': 1 << 16,
            'VM': 1 << 17,
            'AC': 1 << 18,
            'VIF': 1 << 19,
            'VIP': 1 << 20,
            'ID': 1 << 21
            }
        reg_val = 0x0
        for bit in reg_raw.split():
            reg_val |= 0x0 if bit not in mask else mask[bit]
        return reg_val


GDBRCNRegisterAMD64()
