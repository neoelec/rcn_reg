# SPDX-License-Identifier: Beerware

from abc import *


class RegisterReader(metaclass = ABCMeta):
    @abstractmethod
    def read(self, name):
        pass
