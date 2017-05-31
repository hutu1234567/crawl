#该类为所有数据抓取类的抽象基类，公共的代码抽取出来放到这个类中实现
from com.inspur.reptile.base.HttpTool import request as requestWithoutJson
from com.inspur.reptile.base.HttpTool import request_ajax_data as request
from com.inspur.reptile.base.BaseTask import BaseTask
urlDemo="http://www.tianyancha.com/expanse/patent.json?id=2344338651&pn=1&ps=1000"
baseUrl="http://www.tianyancha.com/"
class Info( BaseTask ):
    def __init__(self,url,params=None):
        #params为http请求所可能需要的报头参数
        self.params=params
        self.url=url
        self.action="crawl"
        self.seelptime = 10  # 抓取任务设置延时，避免被屏蔽
        self.task_flag=self.__class__.__name__
        super().__init__(url)
    def getParams(self):
        return self.params
    def getUrl(self):
        return self.url
    def getBaseUrl(self):
        return baseUrl

    def crawl(self,isJson=True,session=None,headers=None):
        #print("url=======",self.getUrl())
        if(isJson):
            ret = request(self.getUrl(),session=session,data=self.getParams(),headers=headers)
        else:
            ret = requestWithoutJson(self.getUrl(),data=self.getParams(),session=session,headers=headers)
        self.content=ret#设置爬取到的内容是什么
        #print(ret)
        #print("bbbbbbb"*8,hasattr(ret,"state"))
        if (ret["state"] != "ok"):#如果状态码不是ok，则表示未查询到数据
            self.content = str( ret )
            raise Exception("未查询到数据")
        return ret

if __name__ == '__main__':
    Info("2344338651").crawl()