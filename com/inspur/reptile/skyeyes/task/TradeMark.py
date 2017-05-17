#商标
# http://www.tianyancha.com/tm/getTmList.json?id=2315740&pageNum=1&ps=1000
from com.inspur.reptile.skyeyes.task.Info import Info
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "tm/getTmList.json?id="
class TradeMark(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + "&pageNum=1&ps=1000"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

if __name__ == '__main__':
    TradeMark("2344338651").crawl()