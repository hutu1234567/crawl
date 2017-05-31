# 产品信息
# http://www.tianyancha.com/expanse/appbkinfo.json?id=6923813&ps=5&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.ProductInfoEntity import ProductInfoEntity

contentUrl= "expanse/appbkinfo.json?id="
ps = 1000


class ProductInfo(Info):
    def __init__(self,comId, pn=1):
        self.comid=comId
        self.pn=pn
        # url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    def run(self):
        ret=self.crawl()
        for data in (ret["data"]["items"]):
            data["comid"]=self.comid
            ProductInfoEntity(data)
        if (int( ret["data"]["count"] ) > self.pn * ps):
            ProductInfo(self.comid,self.pn+1)
if __name__ == '__main__':
    comid="6923813"
    ProductInfo(comid)
