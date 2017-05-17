# 网站备案
# http://www.tianyancha.com/v2/IcpList/6923813.json
from com.inspur.reptile.skyeyes.task.Info import Info
contentUrl= "v2/IcpList/"

class SitRecord(Info):
    def __init__(self,comId):
        url=super().getBaseUrl()+contentUrl+comId+".json"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)

if __name__ == '__main__':
    SitRecord("6923813").crawl()