from model import model

class Controller:
    def __init__(self, name):
        self.name = name
    

class AccountController(Controller):
    def __init__(self):
        self.accountModel = model.AccountModel()
    
    def get_accounts(self):
        return self.accountModel.getAccounts()