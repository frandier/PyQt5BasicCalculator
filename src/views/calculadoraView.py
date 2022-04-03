from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QGridLayout,
    QPushButton
)

class CalculadoraView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.LayoutGeneral = QVBoxLayout()
        self.setFixedSize(235, 235)
        self._widgetCentral = QWidget(self)
        self.setCentralWidget(self._widgetCentral)
        self._widgetCentral.setLayout(self.LayoutGeneral)
        self._crearPantalla()
        self._crearBotones()

    def _crearPantalla(self):
        self.pantalla = QLineEdit()
        self.pantalla.setFixedHeight(35)
        self.pantalla.setAlignment(Qt.AlignRight)
        self.pantalla.setReadOnly(True)
        self.LayoutGeneral.addWidget(self.pantalla)

    def _crearBotones(self):
        self.botones = {}
        botonesLayout = QGridLayout()
        botones = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), 'C': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '/': (1, 3), 
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '*': (2, 3), 
            '0': (3, 0), '=': (3, 1), '+': (3, 2), '-': (3, 3),
        }

        for btnTexto, pos in botones.items():
            self.botones[btnTexto] = QPushButton(btnTexto)
            self.botones[btnTexto].setFixedSize(40, 40)
            botonesLayout.addWidget(self.botones[btnTexto], pos[0], pos[1])
        
        self.LayoutGeneral.addLayout(botonesLayout)
    
    def setTextoEnPantalla(self, texto):
        self.pantalla.setText(texto)
        self.pantalla.setFocus()

    def getTextoEnPantalla(self):
        return self.pantalla.text()

    def limpiarPantalla(self):
        self.setTextoEnPantalla('')