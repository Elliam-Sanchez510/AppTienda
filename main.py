from TiendaApp import TiendaApp
from Aplicaciones import Aplicacion

if __name__ == '__main__':
    ejecutar = True
    
    while(ejecutar):
        print("....Tienda de App....")
        opcion = int(input("1-Crear Tienda:\n2-Agregar aplicacion:\n3-Ver informacion:\n4-Salir:\n"))
        
        if opcion == 1:
            nombre = input("Nombre de la tienda: ")
            tienda = TiendaApp(nombre)
            
            print("Se creo la tienda: {}".format(tienda.consultar_nombre_tienda(nombre)))
            
        elif opcion == 2:
            nombre = input("Nombre de la Aplicacion: ")
            desarrollador = input("Nombre del Creador: ")
            fecha_de_lanzamiento = input("Año: ")
            seguridad = input("seguridad: ")
            funcion = input("funcion: ")
            
            aplicacion = Aplicacion(nombre, desarrollador, fecha_de_lanzamiento, seguridad, funcion)
            tienda.agregar_aplicacion(aplicacion)
            
        elif opcion == 3:
            print("Informacion de aplicaciones de Aplicaciones")
            for i in tienda.consultar_aplicacion():
                print(i)
                
        elif opcion == 4:
            ejecutar = False