from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel)
from instr import *

class FinalWin(QWidget):
    ''' вікно, в якому проводиться опитування '''
    def __init__(self):
        super().__init__()
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
        # старт:
        self.show()
    ''' створює графічні елементи '''
    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)
    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)