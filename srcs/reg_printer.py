# SPDX-License-Identifier: Beerware

from abc import *


class RegisterPrinter(metaclass = ABCMeta):
    def __init__(self, reader):
        self.__reader = reader

    @abstractmethod
    def print(self):
        pass

    def _print_64(self, name):
        reader = self.__reader
        reg_value = reader.read(name)
        print(f' {name:3s}: {reg_value:016x}', end = '')

    def _print_32(self, name):
        reader = self.__reader
        reg_value = reader.read(name)
        print(f' {name:3s}: {reg_value:08x}', end = '')

    def _print_16(self, name):
        reader = self.__reader
        reg_value = reader.read(name)
        print(f' {name:3s}: {reg_value:04x}', end = '')

    def _print_flag(self, name, flag, start, end):
        reader = self.__reader
        reg_value = reader.read(name)
        mask = (1 << (end + 1)) - (1 << start)
        if (end - start) == 0:
            reg_flag = flag if reg_value & mask else flag.lower()
            print(f' {reg_flag:s}', end = '')
        else:
            flag_value = (reg_value & mask) >> start
            print(f' {flag:s}={flag_value:d}', end = '')
