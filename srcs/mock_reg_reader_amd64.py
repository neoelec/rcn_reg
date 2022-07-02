# SPDX-License-Identifier: Beerware

from reg_reader import RegisterReader


class RegisterReaderMockAMD64(RegisterReader):
    def __init__(self):
        self.__register = {
            'rax': 0x555555555135,
            'rbx': 0x0,
            'rcx': 0x7ffff7fa4718,
            'rdx': 0x7fffffffe168,
            'rsi': 0x7fffffffe158,
            'rdi': 0x1,
            'rbp': 0x7fffffffe060,
            'rsp': 0x7fffffffe050,
            'r8': 0x0,
            'r9': 0x7ffff7fe21b0,
            'r10': 0x7,
            'r11': 0x2,
            'r12': 0x555555555050,
            'r13': 0x0,
            'r14': 0x0,
            'r15': 0x0,
            'rip': 0x555555555144,
            'eflags': 0x206,
            'cs': 0x33 ,
            'ss': 0x2b,
            'ds': 0x0,
            'es': 0x0,
            'fs': 0x0,
            'gs': 0x0
            }

    def read(self, name):
        register = self.__register
        return register[name]
