# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from rcn.lldb.reg_reader import RcnRegReaderLLDB
from rcn.aarch64.reg_printer import RcnRegPrinterAArch64

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ' + __name__
        + '.command ' + 'rcn_reg')

def command(debugger, command, exe_ctx, result, internal_dict):
    aliases = {
        'x29': 'fp'
        }
    reader = RcnRegReaderLLDB(exe_ctx, aliases)
    printer = RcnRegPrinterAArch64(reader)
    printer.print()
