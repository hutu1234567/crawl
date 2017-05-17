#对外投资
#http://www.tianyancha.com/expanse/inverst.json?id=2315740&ps=20&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/inverst.json?id="
class Invest(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + "&ps=1000&pn=1"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

if __name__ == '__main__':
    Invest("2344338651").crawl()