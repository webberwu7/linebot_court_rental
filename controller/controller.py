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


class SearchController(Controller):
    def __init__(self):
        self.CourtModel = model.CourtModel()
    
    def get_court(self):
        return self.CourtModel.get_court()