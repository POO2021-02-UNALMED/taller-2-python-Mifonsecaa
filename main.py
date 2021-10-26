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
        numero = 0
        for i in self.asientos:
            if i == None:
                pass
            else:
                numero += 1
        return numero      
        

    def verificarIntegridad(self):
        lista =[]
        for i in self.asientos:
            if i == None:
                pass
            else:
                lista.append(i)
        nuevo = lista[0]
        nuevo1 = lista[1]
        if (self.registro == self.motor.registro and self.registro == nuevo.registro and self.registro == nuevo1.registro):
            print("Auto Original")
        else:
            print("Las piezas no son originales")
        

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

