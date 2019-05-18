from model import model

class Controller:
    def __init__(self, name):
        self.name = name
    

class AccountController(Controller):
    def __init__(self):
        self.accountModel = model.AccountModel()
    
    def get_accounts(self):
        return self.accountModel.getAccounts()


class BulletinController(Controller):
    def __init__(self):
        self.bulletinModel = model.BulletinModel()
    
    def get_bulletins(self):
        #(u1,id),(u2,year),(u3,month),(u4,date),(u5,hour),(u6,minute),(u7,title),(u8,content)
        u1, u2, u3, u4, u5, u6, u7, u8 = str(answer).split(',', 7)

        #(u1,id):去除字串中多餘的符號
        getVals = list([val for val in u1 if val.isnumeric()])
        newU1 = "".join(getVals)
        #(u2,year):去除字串中多餘的符號
        getVals = list([val for val in u2 if val.isnumeric()])
        newU2 = "".join(getVals)
        #(u6,minute):去除字串中多餘的符號
        getVals = list([val for val in u6 if val.isnumeric()])
        newU6 = "".join(getVals)
        #(u7,title),(u8,content):去除空格、引號、右擴號、逗號
        newU7 = u7.replace(' ',"").replace('\'', "")
        newU8 = u8.replace(' ',"").replace('\'',"").replace(')',"").replace(',',"")

        print("第",newU1,"則公告")
        print("日期：",newU2,"年",u3,"月",u4,"號",u5,":",newU6)
        print("標題：",newU7)
        print("內容：",newU8)
        #return self.bulletinModel.getBulletins()


class SearchController(Controller):
    def __init__(self):
        self.CourtModel = model.CourtModel()
    
    def get_court(self):
        return self.CourtModel.get_court()