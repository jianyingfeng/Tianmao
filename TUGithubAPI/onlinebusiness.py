from TUGithubAPI.api.user.user import User
import json

class OnlineBusiness():
    def __init__(self,api_root_url,**kwargs):
        self.api_root_url = api_root_url
        self.user = User(self.api_root_url,**kwargs)

if __name__ == '__main__':
    ###登录
    ob = OnlineBusiness('https://127.0.0.1')
    payload = {"phone": 15707494858, "pwd": 123456}
    response = ob.user.login(json=payload)
    assert response.content['result']['phone'] == '15707494858'
    userId = response.content['result']['userId']
    sessionId = response.content['result']['sessionId']
    ###修改昵称
    ob = OnlineBusiness('https://127.0.0.1',userId=userId,sessionId=sessionId)
    payload = {"nickName":"鸡腿"}
    response = ob.user.modifyUserNick(data=json.dumps(payload))
    assert response.content['status'] == '0000'
    ###再次登录验证昵称
    ob = OnlineBusiness('https://127.0.0.1')
    payload = {"phone": 15707494858, "pwd": 123456}
    response = ob.user.login(json=payload)
    assert response.content['result']['nickName'] == '鸡腿'