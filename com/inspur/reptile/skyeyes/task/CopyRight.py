# 著作权
from com.inspur.reptile.skyeyes.task.Info import Info
#http://www.tianyancha.com/expanse/copyReg.json?id=2315740&pn=1&ps=5
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/copyReg.json?id="
class CopyRight(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + "&pn=1&ps=1000"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

if __name__ == '__main__':
    CopyRight("2315740").crawl()