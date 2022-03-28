import unittest
from src.reporting.connection import Connection


class ConnectionTestSuit(unittest.TestCase):

#tests getters
    def test_gethost(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.get_host()
        self.assertEqual("localhost", result)


    def test_getuser(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.get_user()
        self.assertEqual("postgres", result)


    def test_getpassword(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.get_password()
        self.assertEqual("intiinti", result)


    def test_getdatabase(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.get_database()
        self.assertEqual("PEDIDOS", result)


    def test_getport(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.get_port()
        self.assertEqual("5433", result)

#test setingconnection
    def test_setingconnection(self):
        inst = Connection('localhost', 'postgres', 'intiinti', 'PEDIDOS', '5433')
        result = inst.tryconnection()
        self.assertEqual("se conecto correctamente", result)

