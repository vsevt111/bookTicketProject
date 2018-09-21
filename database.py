class database():
    moneyDictionary = {}
    clientDictionary = {}
    loginList = []
    def __init__(self):
        loginList=[]
        clientDictionary = {}
        moneyDictionary = {}

    def signup(self, name, password):
        if self.clientDictionary.get(name, '0') == '0':
            self.clientDictionary[name] = password
            self.moneyDictionary[name] = 0
            return "700 sign up complete"
        else:
            return "750 fail to sign up because this username already exist."

