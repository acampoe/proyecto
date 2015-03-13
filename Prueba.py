from Cliente import Cliente
from ListaClientes import ListaClientes

__author__ = 'xgarlics'

lista_clientes = ListaClientes()

c1 = Cliente(22425, "Andres Ochoa", "ACTIVO")

lista_clientes.agregar_cliente(c1)
lista_clientes.consultar_clientes()