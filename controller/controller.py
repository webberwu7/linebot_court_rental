# coding=utf-8
from model import model
from view import view
import time


class Controller:
    def __init__(self, name):
        self.name = name


class AccountController(Controller):
    def __init__(self):
        self.accountModel = model.AccountModel()
        self.statusModel = model.StatusModel()
        self.hobbyModel = model.HobbyModel()
        self.bookingModel = model.BookingModel()

    def ask_register(self, uid):
        status_row = self.statusModel.store(uid, 1)
        return status_row

    def store(self, uid, student_id):
        answer = self.accountModel.store(student_id, uid)
        answer = self.accountModel.find(uid)
        outputStr = "you register new account : \nLine_id: {line_id}\nstudent_id: {student_id}".format(
            line_id=answer['line_id'],
            student_id=answer['student_id']
        )

        return view.TextView(outputStr)

    def get_accounts(self):
        return self.accountModel.getAccounts()

    def set_hobby(self, uid, time, court):
        self.hobbyModel.store(uid, time, court)
        return "新增喜好成功"

    def get_hobby(self, uid):
        answer = self.hobbyModel.find(uid)
        return "my hobby : " + str(answer)

    def hobby_search(self, uid):
        hobby = self.hobbyModel.find_ver2(uid)
        time = hobby['time_range_id']
        court = hobby['court_id']
        booking = self.bookingModel.find(time, court)
        print(str(booking))
        if booking['amount'] != 0:
            return view.TextView("{time} 的 {court} 已經被借走了".format(time=hobby['day_of_week']+hobby['zone'], court=hobby['name']))

        return view.TextView("{time} 的 {court} 可以被租借".format(time=hobby['day_of_week']+hobby['zone'], court=hobby['name']))

    def hobby_booking(self, uid):
        hobby = self.hobbyModel.find_ver2(uid)
        time = hobby['time_range_id']
        court = hobby['court_id']
        booking = self.bookingModel.find(time, court)
        if booking['amount'] == 0:
            text = "確認預約 {time} 的 {court} ?".format(
                time=hobby['day_of_week']+hobby['zone'], court=hobby['name'])

            return view.BookingConfirmView(text, time, court)

        return view.TextView("{time} 的 {court} 已經被借走了".format(time=hobby['day_of_week']+hobby['zone'], court=hobby['name']))

    def get_booking(self, uid):
        bookings = self.bookingModel.find_by_uid(uid)
        answer = "\n你預約的時間有:\n"
        for booking in bookings:
            answer += "id= {id}, {time} 的 {court}\n".format(
                id=str(booking['id']),
                time=str(booking['day_of_week']+str(booking['zone'])),
                court=str(booking['name']))

        return view.TextView(answer)


class BulletinController(Controller):
    def __init__(self):
        self.bulletinModel = model.BulletinModel()

    def get_bulletins(self):
        bulletins = self.bulletinModel.getBulletins()
        # (u1,id),(u2,year),(u3,month),(u4,date),(u5,hour),(u6,minute),(u7,title),(u8,content)
        u1, u2, u3, u4, u5, u6, u7, u8 = str(bulletins).split(',', 7)

        # (u1,id):去除字串中多餘的符號
        getVals = list([val for val in u1 if val.isnumeric()])
        newU1 = "".join(getVals)

        # (u2,year):去除字串中多餘的符號
        getVals = list([val for val in u2 if val.isnumeric()])
        newU2 = "".join(getVals)

        # (u6,minute):去除字串中多餘的符號
        getVals = list([val for val in u6 if val.isnumeric()])
        newU6 = "".join(getVals)

        # (u7,title),(u8,content):去除空格、引號、右擴號、逗號
        newU7 = u7.replace(' ', "").replace('\'', "")
        newU8 = u8.replace(' ', "").replace(
            '\'', "").replace(')', "").replace(',', "")

        output = ""
        output += "第 {newU1} 則公告\n".format(newU1=newU1)
        output += "日期：{newU2}年{u3}月{u4}號{u5}:{newU6}\n".format(
            newU2=newU2, u3=u3, u4=u4, u5=u5, newU6=newU6)
        output += "標題：{newU7}\n".format(newU7=newU7)
        output += "內容：{newU8}".format(newU8=newU8)
        return output


class MaintainController(Controller):
    def __init__(self):
        self.maintainModel = model.MaintainModel()

    def get_maintains(self):
        maintains = self.maintainModel.getMaintainList()
        answer = "\n"
        for maintain in maintains:
            answer += "報修通報: " + maintain['name'] + " 場地已被通報維修\n"

        return answer

    def post_maintain(self, court, uid):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        return self.maintainModel.postMaintain(court, uid, now)


class SearchController(Controller):
    def __init__(self):
        self.bookingModel = model.BookingModel()

    def find(self, time, court):
        answer = self.bookingModel.find(time, court)
        if answer['amount'] != 0:
            return view.TextView("這時間的球場有人預約囉")

        return view.BookingConfirmView("此時段為空 請問要預約嗎？", time, court)


class BookingController(Controller):
    def __init__(self):
        self.bookingModel = model.BookingModel()

    def store(self, uid, time, court):
        self.bookingModel.store(uid, time, court)
        return view.TextView("預約完成")

    def delete(self, uid, id):
        self.bookingModel.delete(uid, id)
        return view.TextView("刪除完成")


class CourtController(Controller):
    def __init__(self):
        self.courtModel = model.CourtModel()

    def index(self):
        courts = self.courtModel.get_courts()
        answer = "\n目前開放的球場:\n"
        for court in courts:
            answer += "{name} 位置在 {loc} 數量有 {amount} 敘述 {desc}\n".format(
                name=court['name'],
                loc=court['location'],
                amount=court['amount'],
                desc=court['description']
            )

        return view.TextView(answer)
