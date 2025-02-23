from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None: 
        super().__init__(parent, *args, **kwargs)

        #Configrando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)   
        self.setCentralWidget(self.cw)

        #Título da janela
        self.setWindowTitle('CALCULADORA')

    def adjustFixedSize(self):
        #Última coisa a fazer
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)