#竞品
# http://www.tianyancha.com/expanse/findJingpin.json?name=%E6%B5%AA%E6%BD%AE%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&ps=10&pn=1
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.CompetingGoodsEntity import CompetingGoodsEntity

ps = 1000
class CompetingGoods(Info):
    def __init__(self, comid,comName, pn=1):
        self.comid=comid
        self.comName = comName
        self.pn=pn
        comNameDecode = urllib.parse.quote( comName )

        url = "%sexpanse/findJingpin.json?name=%s&pn=%s&ps=%s"%(super().getBaseUrl(), comNameDecode, pn, ps)
        super().__init__(url)
    def run(self):
        ret =self.crawl()
        for data in (ret["data"]["page"]["rows"]):
            data["comid"]=self.comid
            CompetingGoodsEntity( data,self.taskid )
        if (int( ret["data"]["page"]["total"] ) > self.pn * ps):
            CompetingGoods(self.comid, self.comName,self.pn+1 )
if __name__ == '__main__':
    comid="1499023"
    CompetingGoods(comid, "中国石油化工股份有限公司" )