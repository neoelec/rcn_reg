#!/usr/bin/python

# SPDX-License-Identifier: Beerware

from mock_reg_reader_aarch64 import RegisterReaderMockAArch64
from reg_printer_aarch64 import RegisterPrinterAArch64

reader = RegisterReaderMockAArch64()
printer = RegisterPrinterAArch64(reader)
printer.print()
