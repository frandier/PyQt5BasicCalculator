ERROR_MSG = "ERROR"

class CalculadoraModel:
    def __init__(self):
        self.expresion = ""

    def evaluarExpresion(self, expresion):
        try:
            resultado = str(eval(expresion))
        except:
            resultado = ERROR_MSG
        return resultado