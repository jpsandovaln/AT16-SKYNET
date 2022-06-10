from src.singleton.property import Property


class SingletonProperty(object):
    _instance = None
    property = Property()

    def __new__(cls):
        if cls._instance is None:
            print("Creating instance")
            cls._instance = super(SingletonProperty, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_property(cls):
        return cls.property
