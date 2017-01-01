#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# web_container.py
#
# Copyright © 2016-2017 Antergos
#
# This file is part of whither.
#
# whither is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# whither is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# The following additional terms are in effect as per Section 7 of the license:
#
# The preservation of all legal notices and author attributions in
# the material or in the Appropriate Legal Notices displayed
# by works containing it is required.
#
# You should have received a copy of the GNU General Public License
# along with whither; If not, see <http://www.gnu.org/licenses/>.

# Standard Lib
from typing import Optional, Union, Tuple

# This Library
from whither.base.object import BaseObject

# Typing Helpers
BridgeObjects = Optional[Tuple['BridgeObjectBase']]


class WebContainer(BaseObject):

    def __init__(self, bridge_objects: BridgeObjects = None) -> None:
        super().__init__(name='web_container')

        self.bridge_objects = bridge_objects or ()  # type: tuple

    def _init_bridge_channel(self) -> None:
        raise NotImplementedError()
