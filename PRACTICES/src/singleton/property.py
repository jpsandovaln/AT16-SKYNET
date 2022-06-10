from jproperties import Properties


class Property:
    def __init__(self):
        self.configs = Properties()
        with open("singleton/configuration.properties", "rb") as read_prop:
            self.configs.load(read_prop)

    def get_host(self):
        return self.configs.get("DB_HOST").data

    def get_user(self):
        return self.configs.get("DB_USER").data

    def get_pwd(self):
        return self.configs.get("DB_PWD").data
