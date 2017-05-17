from com.inspur.reptile.tools.HttpTool import request as requestWithoutJson
from com.inspur.reptile.tools.HttpTool import request_ajax_data as request

urlDemo="http://www.tianyancha.com/expanse/patent.json?id=2344338651&pn=1&ps=1000"
baseUrl="http://www.tianyancha.com/"

class Info():
    def __init__(self,url,params=None,):
        self.params=params
        self.url=url
    def getParams(self):
        return self.params
    def getUrl(self):
        return self.url
    def getBaseUrl(self):
        return baseUrl

    def crawl(self,isJson=True,session=None):
        print("url=======",self.getUrl())
        if(isJson):
            ret = request(self.getUrl(),session=session,data=self.getParams())
        else:
            ret = requestWithoutJson(self.getUrl(),data=self.getParams(),session=session)
        return ret

if __name__ == '__main__':
    Info("2344338651").crawl()