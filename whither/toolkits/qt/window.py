#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# window.py
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

""" Wrapper for QMainWindow """

# Standard Lib

# 3rd-Party Libs
from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    qApp,
    QWidget,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# This Library
from whither.base.objects import Window

WINDOW_STATES = {
    'NORMAL': Qt.WindowNoState,
    'MINIMIZED': Qt.WindowMinimized,
    'MAXIMIZED': Qt.WindowMaximized,
    'FULLSCREEN': Qt.WindowFullScreen,
}


class QtWindow(Window):

    def __init__(self, name: str = '_window', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.states = WINDOW_STATES  # type: dict
        self.widget = None           # type: QWidget

        self._initialize()

    def _initialize(self) -> None:
        config = self._config.window
        toolbar_config = self._config.toolbar
        initial_state = config.initial_state.upper()

        if not self._app.windows:
            self.widget = QMainWindow()
        else:
            self.widget = QWidget()

        self._app.windows.append(self.widget)

        self.widget.setAttribute(Qt.WA_DeleteOnClose)

        if config.title:
            self.widget.setWindowTitle(config.title)

        if config.icon:
            self.widget.setWindowIcon(QIcon(config.icon))

        if config.width and config.height:
            self.widget.setFixedSize(config.width, config.height)

        if config.decorated and toolbar_config.enabled:
            self.init_menu_bar()

        elif not config.decorated:
            self.widget.setWindowFlags(self.widget.windowFlags() | Qt.FramelessWindowHint)

        if config.stays_on_top:
            self.widget.setWindowFlags(
                self.widget.windowFlags() | Qt.WindowStaysOnTopHint
            )

        self.widget.setWindowFlags(
            self.widget.windowFlags() | Qt.MaximizeUsingFullscreenGeometryHint
        )

        self.set_state(self.states[initial_state])

    def init_menu_bar(self) -> None:
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.widget.menuBar()

        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        edit_menu = menu_bar.addMenu('&Edit')
        edit_menu.addAction(exit_action)

        view_menu = menu_bar.addMenu('&View')
        view_menu.addAction(exit_action)

        about_menu = menu_bar.addMenu('&About')
        about_menu.addAction(exit_action)

    def show(self) -> None:
        self.widget.show()

    def show_fullscreen(self) -> None:
        try:
            self.widget.windowHandle().showFullScreen()
        except Exception:
            self.widget.showFullScreen()

    def show_maximized(self) -> None:
        try:
            self.widget.windowHandle().showMaximized()
        except Exception:
            self.widget.showMaximized()

    def show_minimized(self) -> None:
        try:
            self.widget.windowHandle().showMinimized()
        except Exception:
            self.widget.showMinimized()

    def set_state(self, state: int) -> None:
        if state != self.state:
            self.widget.setWindowState(state)
            self.state = state
