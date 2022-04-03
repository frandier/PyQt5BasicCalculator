import sys
from PyQt5.QtWidgets import QApplication
from src.views import calculadoraView
from src.controllers import calculadoraController
from src.models import calculadoraModel

def main():
    # Crea una instancia de QApplication
    app = QApplication(sys.argv)

    # Muestra la ventana (Interfaz de la calculadora)
    view = calculadoraView.CalculadoraView()
    view.show()

    # Crea instancias de los controladores y modelos
    model = calculadoraModel.CalculadoraModel()
    calculadoraController.CalculadoraController(model=model, view=view)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()