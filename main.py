class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        if ( nuevoColor == "amarillo" or nuevoColor == "verde" or nuevoColor == "negro" or nuevoColor == "rojo"):
            self.color = nuevoColor
        else:
            self.color = self.color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro 
        
    
    def cantidadAsientos(self):
        for i in self.asientos:
            clase = (str(type(i))[17:24])
            if clase == "Asiento":
                self.asientos += 1
                return self.asientos
                
        

    def verificarIntegridad(self):
        pass
        

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numero):
        self.registro = numero

    def asignarTipo(self, valor):
        if (valor == "electrico" or valor == "gasolina"):
            self.tipo = valor 
        else:
            self.tipo = self.tipo
if __name__ == "__main__":
    main()

