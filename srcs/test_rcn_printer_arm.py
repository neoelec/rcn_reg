#!/usr/bin/python

# SPDX-License-Identifier: Beerware

from mock_reg_reader_arm import RegisterReaderMockArm
from reg_printer_arm import RegisterPrinterArm

reader = RegisterReaderMockArm()
printer = RegisterPrinterArm(reader)
printer.print()
