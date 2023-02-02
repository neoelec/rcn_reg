# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

import gdb
from rcn.gdb.reg_reader import RcnRegReaderGDB
from rcn.riscv64.reg_printer import RcnRegPrinterRiscV64


class GDBRCNRegisterRiscV64(gdb.Command):
    def __init__(self):
        super(GDBRCNRegisterRiscV64, self).__init__(
            'rcn_reg', gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        modifier = GDBModifierRiscV64()
        reader = RcnRegReaderGDB(modifier)
        printer = RcnRegPrinterRiscV64(reader)
        printer.print()


class GDBModifierRiscV64:
    def modify(self, name, reg_raw):
        reg_val = int(reg_raw.split()[0], 0)
        reg_val &= 0xFFFFFFFFFFFFFFFF
        return reg_val


GDBRCNRegisterRiscV64()
