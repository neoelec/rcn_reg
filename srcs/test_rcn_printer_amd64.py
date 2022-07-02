#!/usr/bin/python

# SPDX-License-Identifier: Beerware

from mock_reg_reader_amd64 import RegisterReaderMockAMD64
from reg_printer_amd64 import RegisterPrinterAMD64

reader = RegisterReaderMockAMD64()
printer = RegisterPrinterAMD64(reader)
printer.print()
