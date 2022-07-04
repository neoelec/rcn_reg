# SPDX-License-Identifier: Beerware

from reg_reader_lldb import RegisterReaderLLDB
from reg_printer_arm import RegisterPrinterArm

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ' + __name__
        + '.command ' + 'rcn_reg')

def command(debugger, command, exe_ctx, result, internal_dict):
    aliases = {
        'dummy': 'unused'
        }
    reader = RegisterReaderLLDB(exe_ctx, aliases)
    printer = RegisterPrinterArm(reader)
    printer.print()
