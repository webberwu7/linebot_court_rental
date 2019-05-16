import os

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self):
        self.dbhost = os.environ.get('dbhost')
        self.dbname = os.environ.get('dbname')
        self.account = os.environ.get('account')
        self.password = os.environ.get('password')
        self.dbport = int(os.environ.get('dbport'))
