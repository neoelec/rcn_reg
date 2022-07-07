# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

import gdb
import os
from rcn.gdb.reg_reader import RcnRegReaderGDB
from rcn.arm.reg_printer import RcnRegPrinterArm


class GDBRCNRegisterArm(gdb.Command):
    def __init__(self):
        super(GDBRCNRegisterArm, self).__init__('rcn_reg', gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        modifier = GDBModifierArm()
        reader = RcnRegReaderGDB(modifier)
        printer = RcnRegPrinterArm(reader)
        printer.print()


class GDBModifierArm:
    def modify(self, name, reg_raw):
        reg_val = int(reg_raw.split()[0], 0)
        reg_val &= 0xFFFFFFFF
        return reg_val


GDBRCNRegisterArm()
