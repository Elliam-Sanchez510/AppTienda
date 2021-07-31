class TiendaApp:
    def __init__(self, nombre):
        self.nombre = nombre
        self._aplicacion = []
        #Defino un atributo privado llamado libros
    def consultar_nombre_tienda(self, nombre):
        return self.nombre

    def agregar_aplicacion(self, aplicacion):
        self._aplicacion.append({
            #crear una lista con los siguientes valores
            aplicacion.nombre,
            aplicacion.desarrollador,
            aplicacion.fecha_de_lanzamiento,
            aplicacion.seguridad,
            aplicacion.funcion
        })

    def consultar_aplicacion(self):
        return self._aplicacion
