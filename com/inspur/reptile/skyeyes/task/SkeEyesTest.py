from selenium import webdriver
import selenium
import time
import re
from bs4 import BeautifulSoup
import urllib
#获取企业基本信息数据
def get_enterprise_data(ename):
    #搜索页面链接地址
    keyword = urllib.parse.quote(ename)
    url = 'http://www.tianyancha.com/search/'+keyword
    #获得搜索结果页面
    driver = webdriver.PhantomJS(executable_path='D:/tools/phantomjs-2.1.1-windows/bin/phantomjs')
    driver.maximize_window()
    driver.get(url)
    time.sleep(20000)
    #从搜索结果中点击第一个结果
    driver.find_element_by_class_name('query_name').click()
    time.sleep(20000)
    #抓取第一个结果的网页，匹配出需要的字段
    soup = BeautifulSoup(driver.page_source,"html.parser")
    basic_info_list = soup.find_all('p',class_="ng-binding ng-scope")
    data = []
    print(driver.__doc__)
    print(driver.title)
    qiyemingcheng = driver.title.split('】')[1].split('信息查询')[0]
    data.append(qiyemingcheng)
    for i in basic_info_list:
        data.append(i.get_text().strip())

    return data

if __name__ == '__main__':

    print(get_enterprise_data('科润智能'))
