import pandas as pd
from src.reporting.connection import Connection

class Chargepandas:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def charge_postgress(self):
        conn = Connection(self.host, self.user, self.password, self.database, self.port)
        tryquery = "SELECT * FROM clientes"
        df = pd.read_sql(tryquery, conn.setingconnection())
        print(df)


