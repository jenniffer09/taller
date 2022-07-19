from datetime import date
import os
class Usuario: 
    def __init__(self,nombre,cedula,direccion,telefono,correo):
        self.nombre=nombre
        self.cedula=cedula
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
class Empleado1(Usuario):  
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class Administrador(Usuario):   
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
from abc import ABC, abstractclassmethod
class Rol(ABC):  
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    @abstractclassmethod
    def mostrarRol(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class Usuario:  
    def __init__(self,nombre,cedula,direccion,telefono,correo):
        self.nombre=nombre
        self.cedula=cedula
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
class Estudiante(Usuario): 
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class Docente(Usuario):
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class OpcionesSistemas:  
    _registro=0
    def __init__(self,codigo,descripcion,record,nomb,rol,emp,ruc):
        self.codigo=codigo
        self.descripcion=descripcion
        self.consulta=record
        OpcionesSistemas._registro+=1
        self._registro="#0"+str(OpcionesSistemas._registro)
        self.date=date.today()
        self.nomb=nomb
        self.rol=rol
        self.emp=emp
        self.ruc=ruc
    def mostrarOpcSistemaPersona(self):
        print(f"Consulta: {self._registro:14} Empresa: {self.emp:14} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:16} Ruc: {self.ruc:18} Rol: {self.rol}")
        print("*"*29,"Record crediticio","*"*29)
        print("Cédula              Estado        Record crediticio")
        print(f"{self.codigo:14} {self.descripcion:25} {self.consulta}")
    def mostrarOpcSistemaAdministrador(self):
        print()
        print(f"Consulta: {self._registro:20} Empresa: {self.emp:24} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:22} Ruc: {self.ruc:29}Rol: {self.rol}")
        print("*"*45,"Record crediticio","*"*45)
        print("Código        Nombre       Récord crediticio   Incrementar/disminuir récord crediticio   Última actualización")
        print("{:7} {:22} {:30} +{}-                  {} " .format(self.codigo,self.descripcion,self.consulta,OpcionesSistemas._registro, self.date))
while True:
    
    print()
    print(" "*20,"Menú"," "*20)
    print("1.-Persona natural/jurídica")
    print("2.-Administrador")
    print("3.-Salir")
    opc= int(input("Elegir una opción [1...3]: "))
    if opc ==1:
        os.system("cls")
        print(" "*20,"Opciones del sistema"," "*20)
        print("1.- Consultar:")
        print("2.- Volver al menú principal")
        print("3.- Presione cualquier tecla para salir")
        opc2=input("Elegir una opcion [1...3]: ")
        if opc2 == '1':
            os.system("cls")
            notas = OpcionesSistemas("0923704332","Central de riesgo","90","Jenniffer Freire","Persona natural","EMPRESAS SA","0923704332001")
            notas.mostrarOpcSistemaPersona()
            opc3=input("Presione cualquier tecla para regresar al menú principal: ")
            if opc3 ==opc3:
                os.system("cls")
            else:
                os.system("cls")
                print("Opción incorrecta")
        elif opc2 =='2':
            os.system("cls")
        elif opc2==opc2:
            os.system("cls")
            print("Gracias por preferirnos")
            break
        else:
            os.system("cls")
            print("Opción incorrecta")
    elif opc ==2:
        os.system("cls")
        print(" "*20,"Opciones del sistema"," "*20)
        print("1.- Consultar:")
        print("2.- Volver al menú principal")
        print("3.- Presione cualquier tecla para salir")
        opc4=input("Eligir una opcion [1...3]: ")
        if opc4 == '1':
            os.system("cls")
            notas2= OpcionesSistemas("0923704332","Jenniffer Freire","90","Lissette","Gerente","EMPRESAS SA","0923704332001")
            notas2.mostrarOpcSistemaAdministrador()
            print()
            opc5=input("Presione cualquier tecla para regresar al menú principal: ")
            if opc5 ==opc5:
                os.system("cls")
            else:
                os.system("cls")
                print("Opción incorrecta")
        elif opc4 =='2':
            os.system("cls")
        elif opc4==opc4:
            os.system("cls")
            print("Gracias por preferirnos")
            break
        else:
            os.system("cls")
            print("Opción incorrecta")
    elif opc ==3:
        os.system("cls")
        print("Gracias por preferirnos")
        break
    else:
        os.system("cls")
        print("Opción incorrecta")