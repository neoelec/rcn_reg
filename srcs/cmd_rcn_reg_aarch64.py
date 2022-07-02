# SPDX-License-Identifier: Beerware

from reg_reader_lldb import RegisterReaderLLDB
from reg_printer_aarch64 import RegisterPrinterAArch64

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ' + __name__
        + '.command ' + 'rcn_reg')

def command(debugger, command, exe_ctx, result, internal_dict):
    reader = RegisterReaderLLDB(exe_ctx)
    printer = RegisterPrinterAArch64(reader)
    printer.print()
