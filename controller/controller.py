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
        return self.bulletinModel.getBulletins()

        
class MaintainController(Controller):
    def __init__(self):
        self.maintainModel = model.MaintainModel()

    def get_maintains(self):
        return self.maintainModel.getMaintain()
        

class SearchController(Controller):
    def __init__(self):
        self.CourtModel = model.CourtModel()
        self.InquireMode = model.InquireModel()
    
    def get_court(self):
        return self.CourtModel.get_court()
    
    def get_day(self, day):
        return self.InquireMode.get_day()
        
    