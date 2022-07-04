# SPDX-License-Identifier: Beerware

from reg_reader import RegisterReader


class RegisterReaderMockArm(RegisterReader):
    def __init__(self):
        self.__register = {
            'r0': 0x00000001,
            'r1': 0xbefff644,
            'r2': 0xbefff64c,
            'r3': 0x0040050d,
            'r4': 0xbefff4f8,
            'r5': 0x00000000,
            'r6': 0x004003fd,
            'r7': 0xbefff4d8,
            'r8': 0x00000000,
            'r9': 0x00000000,
            'r10': 0x00411000,
            'r11': 0x00000000,
            'r12': 0xbefff560,
            'sp': 0xbefff4d8,
            'lr': 0xb6ef0a21,
            'pc': 0x00400516,
            'cpsr': 0x400e0030,
            }

    def read(self, name):
        register = self.__register
        return register[name]
