import bean
#用户
class UserService():
    def __init__(self):
        pass

    
    def createUser(self,name,phoneNbr,age,carName,licenseplate):
        newuser = bean.user.User(None,name,phoneNbr,age)
        bean.user.User.insertUser(newuser,newuser)
