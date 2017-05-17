#变更记录
#http://www.tianyancha.com/expanse/changeinfo.json?id=2315740&ps=5&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/changeinfo.json?id="
class ChangeInfo(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + "&ps=1000&pn=1"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

if __name__ == '__main__':
    ChangeInfo("2344338651").crawl()