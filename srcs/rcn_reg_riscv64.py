# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.lldb.reg_reader import RcnRegReaderLLDB
from rcn.riscv64.reg_printer import RcnRegPrinterRiscV64


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ' + __name__
                           + '.command ' + 'rcn_reg')


def command(debugger, command, exe_ctx, result, internal_dict):
    aliases = {
        'dummy': 'unused'
    }
    reader = RcnRegReaderLLDB(exe_ctx, aliases)
    printer = RcnRegPrinterRiscV64(reader)
    printer.print()
