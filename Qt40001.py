# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:52:21 2021

@author: Zikantika
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("PyQT Tuts!")

window.show()