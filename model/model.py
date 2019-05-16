import pymysql
from config import config

class Model():
    # def __init__(self, dbhost, dbname, account, password, port):
    def __init__(self):
        configData = config.Config()
        self.dbhost = configData.dbhost
        self.dbname = configData.dbname
        self.account = configData.account
        self.password = configData.password
        self.port = configData.dbport

    def connect(self):
        self.connection = pymysql.connect(host=self.dbhost,
                                          port=self.port,
                                          user=self.account,
                                          password=self.password,
                                          db=self.dbname,
                                          charset='utf8')

    def close(self):
        self.connection.close()


class AccountModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "account"

    def getAccounts(self):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM `account`')
        answer = cursor.fetchall()

        self.close()
        return answer


class BulletinModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "bulletin"

    def getBulletins(self):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM `bulletin`')
        answer = cursor.fetchall()

        self.close()
        return answer
