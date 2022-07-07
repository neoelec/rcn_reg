# SPDX-License-Identifier: Beerware
# Copyright 2022 YOUNGJIN JOO <neoelec@gmail.com>

from abc import *


class RcnRegReader(metaclass = ABCMeta):
    @abstractmethod
    def read(self, name):
        pass
