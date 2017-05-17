#竞品
# http://www.tianyancha.com/expanse/findJingpin.json?name=%E6%B5%AA%E6%BD%AE%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&ps=10&pn=1
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info


class CompetingGoods(Info):
    def __init__(self,comName):
        comName = urllib.parse.quote( comName )
        url = "%sexpanse/findJingpin.json?name=%s&ps=1000&pn=1"%(super().getBaseUrl(),comName)
        super().__init__(url)

if __name__ == '__main__':
    CompetingGoods("浪潮集团有限公司").crawl()