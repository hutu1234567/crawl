#招聘
#http://www.tianyancha.com/extend/getEmploymentList.json?companyName=山东伊莱特重工股份有限公司8&pn=1&ps=10
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info


class RecuitmentInfo(Info):
    def __init__(self,comName):
        print(comName)
        comName = urllib.parse.quote( comName )
        super().__init__(url="%s/extend/getEmploymentList.json?companyName=%s&pn=1&ps=1000"%(super().getBaseUrl(),comName))
if __name__ == '__main__':
    RecuitmentInfo("山东伊莱特重工股份有限公司").crawl()