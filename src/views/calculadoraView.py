from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QLineEdit,
    QGridLayout, QPushButton,
    QMenu, QToolBar,
    QAction
)

class CalculadoraView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.LayoutGeneral = QVBoxLayout()
        self.setFixedSize(260, 260)
        self._widgetCentral = QWidget(self)
        self.setCentralWidget(self._widgetCentral)
        self._widgetCentral.setLayout(self.LayoutGeneral)

        self._crearPantalla()
        self._crearBotones()
        self._createActions()
        self._crearMenuBar()
        self._crearToolBars()

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

    def _crearMenuBar(self):
        menuBar = self.menuBar()

        menuArchivo = QMenu("&Archivo", self)
        menuArchivo.addAction(self.accionNuevo)
        menuArchivo.addAction(self.accionAbrir)
        menuArchivo.addAction(self.accionGuardar)
        menuArchivo.addAction(self.accionSalir)

        menuBar.addMenu(menuArchivo)
        menuEditar = menuBar.addMenu("&Editar")
        menuEditar.addAction(self.accionCopiar)
        menuEditar.addAction(self.accionPegar)
        menuEditar.addAction(self.accionCortar)

        menuAyuda = menuBar.addMenu("&Ayuda")
        menuAyuda.addAction(self.accionContenido)
        menuAyuda.addAction(self.accionSobre)

    def _crearToolBars(self):
        self.addToolBar("Archivo")
        editarToolBar = QToolBar("Editar", self)
        self.addToolBar(editarToolBar)
        ayudaToolBar = QToolBar("Ayuda", self)
        self.addToolBar(Qt.LeftToolBarArea, ayudaToolBar)

    def _createActions(self):
        self.accionNuevo = QAction(self)
        self.accionNuevo.setText("&Nuevo")
        self.accionAbrir = QAction("&Abrir...", self)
        self.accionGuardar = QAction("&Guardar", self)
        self.accionSalir = QAction("&Salir", self)
        self.accionCopiar = QAction("&Copiar", self)
        self.accionPegar = QAction("&Pegar", self)
        self.accionCortar = QAction("&Cortar", self)
        self.accionContenido = QAction("&Contenido", self)
        self.accionSobre = QAction("&Sobre", self)
    
    def setTextoEnPantalla(self, texto):
        self.pantalla.setText(texto)
        self.pantalla.setFocus()

    def getTextoEnPantalla(self):
        return self.pantalla.text()

    def limpiarPantalla(self):
        self.setTextoEnPantalla('')