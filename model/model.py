import json
import pymysql
from config import config


class Model():
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

    def store(self, student_id, uid):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO `account` (`student_id`, `line_token`) VALUES (%s, %s)', [
                       student_id, uid])

        self.connection.commit()
        answer = cursor.lastrowid
        self.close()

        return answer

    def find(self, id):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM `account` WHERE `id` = %s", id)
        answer = cursor.fetchall()

        self.close()
        answer = json.dumps(answer)
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


class CourtModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "court"

    def get_court(self):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM `court`')
        answer = cursor.fetchall()

        self.close()
        return answer


class MaintainModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "maintain"

    def getMaintain(self):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM `maintain`')
        answer = cursor.fetchall()

        self.close()
        return answer


class InquireModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "time_slot"

    def get_day(self, day):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('SELECT ' + day + ' FROM `time_slot`')
        answer = cursor.fetchall()

        self.close()
        return answer


class StatusModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "user_status"

    def store(self, uid, status):
        self.connect()

        cursor = self.connection.cursor()
        insert_str = 'INSERT INTO `{table}` (`line_uid`, `status`) VALUES ({uid}, {status})'.format(
            table=self.table,
            uid=uid,
            status=status
        )

        cursor.execute(insert_str)
        self.connection.commit()
        answer = cursor.lastrowid
        self.close()

        return answer
