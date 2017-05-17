#法律案件，诉讼
#http://www.tianyancha.com/v2/getlawsuit/%E6%B5%AA%E6%BD%AE%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8.json?page=1&ps=10
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info


class LawCase(Info):
    def __init__(self,comName):
        comName = urllib.parse.quote( comName )
        url = "%sv2/getlawsuit/%s.json?page=1&ps=1000"%(super().getBaseUrl(),comName)
        super().__init__(url)

if __name__ == '__main__':
    LawCase("浪潮集团有限公司").crawl()