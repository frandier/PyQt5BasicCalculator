from functools import partial

ERROR_MSG = "ERROR"

class CalculadoraController:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        # conecta los signals de los botones con sus slots
        self._conectarSignals()

    def _calcularResultado(self):
        resultado = self._evaluate.evaluarExpresion(self._view.getTextoEnPantalla())
        self._view.setTextoEnPantalla(resultado)

    def _construirExpresion(self, sub_exp):
        if self._view.getTextoEnPantalla() == ERROR_MSG:
            self._view.limpiarPantalla()

        expresion = self._view.getTextoEnPantalla() + sub_exp
        self._view.setTextoEnPantalla(expresion)

    def _conectarSignals(self):
        for btnTexto, btn in self._view.botones.items():
            if btnTexto not in {'=', 'C'}:
                btn.clicked.connect(partial(self._construirExpresion, btnTexto))

        self._view.botones['='].clicked.connect(self._calcularResultado)
        self._view.pantalla.returnPressed.connect(self._calcularResultado)
        self._view.botones['C'].clicked.connect(self._view.limpiarPantalla)