class Persona():
    def __init__(self):
        self._perso = {}
        self.__listaPersonas = []
    
    def agregar persona(self, cedula, nombre, apellidos, direccion, telefono):
        self._perso = {
            'cedula': cedula,
            'nombre': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
        }
        self.__listaPersonas.append(self._perso)

class Empleado(Persona):
    def __init__(self):
        super().__init__
        self.__devengado = {}
        self.__deducciones = {}
        self.__listaEmpleados = []
    
    def agregarEmpleados(self):
        cedula = input("Digite su cedula: ")
        nombre = input("Digite su nombre: ")
        apellidos = input("Digite su apellidos ")
        direccion = input("Digite su direccion: ")
        telefono = input("Digite su telefono: ")
        salario = float("Digite su salario: ")

        per = {
             'cedula': cedula,
             'nombre': nombre,
             'apellidos': apellidos,
             'direccion': direccion,
             'telefono': telefono,
        }

        self.__devengado = {
            'salario' : salario,
            'alimentacion': 0,
            'transporte': 0
        }

        self.__deducciones = {
            'salario': salario,
            'alimentacion': 0 
        }
        super().agregarPersona(cedula, nombre, apellidos, direccion, telefono)
        self.__listaEmpleados.append([{"persona": per}, {"devengado": self.__devengado}, {"deducciones": self.__deducciones}])

def menuPrincipal():
    "MENU PRINCIPAL",
    "1. Adicionar Empleado",
    "2. Mostrar Empleado",
    "3. Eliminar Empleado",
    "S. Salir"

def main():
    




if __name__ == "__main__":
    main()