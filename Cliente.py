__author__ = 'xgarlics'


class Cliente:

    def __init__(self, cedula, nombre, estado):
        self.cedula = cedula
        self.nombre = nombre
        self.estado = estado
        self.inicio_contactos = None
        self.inicio_ventas = None
        self.final_contactos = None
        self.final_ventas = None
        self.siguiente = None

    def agregar_contacto(self, contacto):
        if self.lista_contactos_vacia():
            self.inicio_contactos = contacto
        else:
            self.final_contactos.siguiente = contacto

        self.final_contactos = contacto

    def agregar_venta(self, venta):
        if self.lista_ventas_vacia():
            self.inicio_ventas = venta
        else:
            self.final_ventas.siguiente = venta

        self.final_ventas = venta

    def lista_contactos_vacia(self):
        return self.inicio_contactos is None and self.final_contactos is None

    def lista_ventas_vacia(self):
        return self.inicio_ventas is None and self.final_ventas is None

    def consultar_contactos(self):
        contacto = self.inicio_contactos
        while contacto is not None:
            print(contacto)
            contacto = contacto.siguiente

    def consultar_ventas(self):
        venta = self.inicio_ventas
        while venta is not None:
            print(venta)
            venta = venta.siguiente

    def __str__(self):
        return \
            "cedula: " + str(self.cedula) + ", " + \
            "nombre: " + self.nombre + ", " + \
            "estado: " + self.estado
