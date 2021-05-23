import requests
class Response():
    pass

def process(raw_response):
    response = Response()
    response.raw = raw_response
    response.status_code = raw_response.status_code
    try:
        response.content = raw_response.json()
    except:
        response.content = raw_response.content
    return response

class RestClient():
    def __init__(self,api_root_url,userId=None,sessionId=None):
        self.api_root_url = api_root_url
        self.session = requests.session()
        if userId and sessionId:
            self.session.headers['userId'] = userId
            self.session.headers['sessionId'] = sessionId

    def get(self,url,**kwargs):
        return self.request(url,'get',**kwargs)     ###process也可以写在这一层，都是调用底层返回，所以在任意层级进行处理都是可以的

    def post(self,url,data=None,json=None,**kwargs):
        return self.request(url,'post',data,json,**kwargs)    ###process也可以写在这一层

    def patch(self,url,data=None,**kwargs):
        return self.request(url,'patch',data,**kwargs)     ###process也可以写在这一层

    def request(self,url,method,data=None,json=None,**kwargs):
        url = self.api_root_url+url
        if method == 'get':
            return process(self.session.get(url,**kwargs))
        if method == 'post':
            return process(self.session.post(url,data,json,**kwargs))
        if method == 'patch':
            # if json:
            #     data = json_pr.dumps(json)
            return process(self.session.patch(url,data,**kwargs))