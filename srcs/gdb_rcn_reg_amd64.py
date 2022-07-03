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
        else:
            reg_val = self.__eflags(reg_raw)
        return reg_val

    def __eflags(cls, reg_raw):
        mask = {
            'CF': 0x0001,
            'PF': 0x0004,
            'AF': 0x0010,
            'ZF': 0x0040,
            'SF': 0x0080,
            'TF': 0x0100,
            'IF': 0x0200,
            'DF': 0x0400,
            'OF': 0x0800
            }
        reg_val = 0x0
        for bit in reg_raw.split():
            reg_val |= 0x0 if bit not in mask else mask[bit]
        return reg_val


GDBRCNRegisterAMD64()
