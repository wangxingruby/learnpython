#装饰器

class User(object):
    def __init__(self, name):
        self.name = name



def required_login():
    

@required_login()
def get_msgs(request):
    username = request.user.name
    msgs = query(username=username)
    return msgs

