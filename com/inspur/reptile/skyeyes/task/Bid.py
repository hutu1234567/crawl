# 招投标
# http://www.tianyancha.com/expanse/bid.json?id=6923813&pn=1&ps=10
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.BidEntity import BidEntity

contentUrl= "expanse/bid.json?id="

class Bid(Info):
    def __init__(self,comId):
        url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=100"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)

if __name__ == '__main__':
    comid="6923813"
    ret=Bid(comid).crawl()
    print(ret)
    for data in (ret["data"]["items"]):
        data["comid"]=comid
        BidEntity(data).save()
