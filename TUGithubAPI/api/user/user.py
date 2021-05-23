from TUGithubAPI.core.rest_client import RestClient

class User(RestClient):
    def register(self,**kwargs):
        return self.post('/xxxx/user/v1/register',**kwargs)

    def login(self,**kwargs):
        return self.post('/xxxx/user/v1/login',**kwargs)

    def modifyUserNick(self,**kwargs):
        return self.put('/xxxx/user/verify/v1/modifyUserNick',**kwargs)

    def modifyUserPwd(self,**kwargs):
        return self.put('/xxxx/user/verify/v1/modifyUserPwd',**kwargs)
