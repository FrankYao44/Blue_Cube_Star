#!/usr/bin python3
# -*- coding: utf-8 -*-

# https://blog.csdn.net/m0_37329910/article/details/86557942
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
    QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class AppClass(QWidget):
    def __init__(self):
        super().__init__()

    def _height_and_weight(self, i, j):
        if 0 <= i <= 1 and 0 <= j <= 1:
            return self._desktop.width()*i, self._desktop.height()*j
        else:
            print('Warning')
            return self._desktop.width()*0.2, self._desktop.height()*0.2

    def init_frame(self, title, picture, text):
        # frame include size, title, icon, tip,
        self.setGeometry(*self._height_and_weight(0, 0), *self._height_and_weight(1, 1))
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(picture))
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip(text)

    def init_button(self, name, height, weight, fn=None, parent=None):
        if parent is None:
            parent = self
        btn = QPushButton(name, parent)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(fn)
        btn.resize(btn.sizeHint())
        btn.move(*self._height_and_weight(height, weight))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Base(QMainWindow, AppClass):
    def __init__(self):
        super().__init__()
        self._desktop = QApplication.desktop()
        self.init_frame('a', 'a', 'a')
        self.init_button('aa', 0.01, 0.01, self.closeEvent)
        self.statusBar().showMessage('Ready')
        self.init_main_windows()
        self.show()

    def init_main_windows(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAction = QAction(QIcon('t2.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

def main():
    app = QApplication(sys.argv)
    a = Base()
    sys.exit(app.exec_())


main()
