from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)