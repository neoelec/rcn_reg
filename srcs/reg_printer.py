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

    def _print_flag(self, name, mask, flag):
        reader = self.__reader
        reg_value = reader.read(name)
        reg_flag = flag if reg_value & mask else flag.lower()
        print(f' {reg_flag:1s}', end = '')
