# SPDX-License-Identifier: Beerware

import gdb
import os
import sys
sys.path.append(os.path.dirname(os.path.expanduser(__file__)))
from reg_reader_gdb import RegisterReaderGDB
from reg_printer_arm import RegisterPrinterArm


class GDBRCNRegisterArm(gdb.Command):
    def __init__(self):
        super(GDBRCNRegisterArm, self).__init__('rcn_reg', gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        modifier = GDBModifierArm()
        reader = RegisterReaderGDB(modifier)
        printer = RegisterPrinterArm(reader)
        printer.print()


class GDBModifierArm:
    def modiry(self, name, reg_raw):
        reg_val = int(reg_raw.split()[0], 0)
        reg_val &= 0xFFFFFFFF
        return reg_val


GDBRCNRegisterArm()
