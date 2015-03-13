__author__ = 'xgarlics'


class ListaClientes:

    def __init__(self):
        self.inicio_cliente = None
        self.final_cliente = None

    def agregar_cliente(self, cliente):
        if self.clientes_vacios():
            self.inicio_cliente = cliente
        else:
            if self.existe_cliente(cliente):
                exec "Ya existe el cliente"
            self.final_cliente.siguiente = cliente

        self.final_cliente = cliente

    def agregar_venta(self, cedula_cliente, venta):
        cliente = self.inicio_cliente
        while cliente is not None:
            if cliente.cedula == cedula_cliente:
                cliente.agregar_venta(venta)
                break
            cliente = cliente.siguiente

    def agregar_contacto(self, cedula_cliente, contacto):
        cliente = self.inicio_cliente
        while cliente is not None:
            if cliente.cedula == cedula_cliente:
                cliente.agregar_contacto(contacto)
                break
            cliente = cliente.siguiente

    def clientes_vacios(self):
        return self.final_cliente is None and self.final_cliente is None

    def existe_cliente(self, cliente1):
        cliente2 = self.inicio_cliente
        while cliente2 is not None:
            if cliente2.cedula == cliente1.cedula:
                return True
        return False

    def consultar_clientes(self):
        cliente = self.inicio_cliente
        while cliente is not None:
            print(cliente)
            cliente = cliente.siguiente