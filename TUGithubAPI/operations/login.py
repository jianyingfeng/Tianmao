from TUGithubAPI.api.user.user import User
from TUGithubAPI.onlinebusiness import OnlineBusiness
from TUGithubAPI.core.base import CommonItem

def login_success(onlinebusiness,phone,pwd):
    result = CommonItem()
    payload = {"phone": phone, 'pwd': pwd}
    result.success = False
    response = onlinebusiness.user.login(json = payload)
    result.response = response
    if response.content['status'] == '0000':
        result.success = True
    else:
        result.error = '登录失败'
    userId = response.content['result']['userId']
    sessionId = response.content['result']['sessionId']
    ob = OnlineBusiness(onlinebusiness.api_root_url,userId=userId,sessionId=sessionId)
    result.ob = ob
    return result