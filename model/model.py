import json
import pymysql
from config import config
import time


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
        cursor.execute('INSERT INTO `account` (`student_id`, `line_id`) VALUES (%s, %s)', [
                       student_id, uid])

        self.connection.commit()
        answer = cursor.lastrowid
        self.close()

        return answer

    def find(self, uid):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM `account` WHERE `line_id` = %s", uid)
        answer = cursor.fetchall()

        self.close()
        answer = json.dumps(answer)
        return answer

    def account2id(self, user_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM account WHERE student_id=%s', user_id)
        answer = cursor.fetchone()
        return answer[0]


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

    def court2id(self, court):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM court WHERE name=%s', court)
        answer = cursor.fetchone()
        return answer[0]


class MaintainModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "maintain"

    def getMaintainList(self):
        self.connect()

        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT `name` FROM `maintain` LEFT JOIN `court` ON `maintain`.`court_id` = `court`.`id`")
        answer = cursor.fetchall()

        self.close()
        return answer

    def postMaintain(self, court, uid, time):
        self.connect()
        cursor = self.connection.cursor()

        cursor.execute('INSERT INTO maintain (line_id,court_id,create_time) VALUES (%s,%s,%s)',
                       (uid, court, time))

        self.connection.commit()
        self.close()


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


class HobbyModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "hobby"

    def store(self, uid, time_range, court):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO `hobby` (`line_id`, `time_range_id`, `court_id`) VALUES (%(uid)s, %(time_range)s, %(court)s) ON DUPLICATE KEY UPDATE `time_range_id` = %(time_range)s , `court_id` = %(court)s',
                       {
                           'uid': uid,
                           'time_range': time_range,
                           'court': court
                       })

        self.connection.commit()
        answer = cursor.lastrowid
        self.close()

        return answer

    def find(self, uid):
        self.connect()

        cursor = self.connection.cursor()
        cursor.execute("SELECT `day_of_week`,`zone`, `name` FROM `hobby` \
                        LEFT JOIN `time_range` ON `hobby`.`time_range_id` = `time_range`.`id` \
                        LEFT JOIN `court` ON `hobby`.`court_id` = `court`.`id` \
                        WHERE `line_id` = %s", uid)
        answer = cursor.fetchone()

        self.close()

        return answer


    def find_ver2(self, uid):
        self.connect()

        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM `hobby` \
                        LEFT JOIN `time_range` ON `hobby`.`time_range_id` = `time_range`.`id` \
                        LEFT JOIN `court` ON `hobby`.`court_id` = `court`.`id` \
                        WHERE `line_id` = %s", uid)
        answer = cursor.fetchone()

        self.close()

        return answer

class BookingModel(Model):
    def __init__(self, ):
        super().__init__()
        self.table = "booking"

    def find(self, time, court):
        self.connect()

        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT count(*) as amount FROM `booking` WHERE `time_range_id` = %s and `court_id` = %s", (time, court))
        answer = cursor.fetchone()

        self.close()

        return answer

    def store(self, uid, time, court):
        self.connect()

        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "INSERT INTO `booking` (`line_id`, `time_range_id`, `court_id`) VALUES (%s, %s, %s)", (uid, time, court))

        self.connection.commit()
        answer = cursor.lastrowid
        self.close()

        return answer