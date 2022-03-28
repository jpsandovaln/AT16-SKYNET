import psycopg2
class Connection:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def get_host(self):
        return self.host

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_database(self):
        return self.database

    def get_port(self):
        return self.port

    def tryconnection(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            return "se conecto correctamente"
        except Exception as ex:
            return ex

    def setingconnection(self):
        connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        #print("host=" + self.host + "user=" + self.user + "password=" + self.password + "dabase=" + self.database + "port=" + self.port)
        return connection