class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def setuser (self, user):
        self.user = user

    
    def setpassword (self, password):
        self.password = password
        

    @classmethod
    def creat_with_auth (cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password 
        return connection       

connection = Connection()
connection.setuser("Karllos")
connection.setpassword(1234)

print(connection.user, connection.password)

connection2 = Connection.creat_with_auth('Eduardo', 4321)

print(connection2.user, connection2.password)