# _*_ coding:utf-8 _*_
#xiaohei.python.seo.call.me:)
#win+python2.7.x
import csv

csvfile = open('csvtest.csv','w')
writer = csv.writer(csvfile)
writer.writerow(['id', 'url', 'keywords'])
data = [
  ('1', 'http://www.xiaoheiseo.com/', '小黑'),
  ('2', 'http://www.baidu.com/', '百度'),
  ('3', 'http://www.jd.com/', '京东')
]

data=[('年度', '全社会住宅投资(亿元)', '城镇住宅投资(亿元)', '房地产住宅投资(亿元)'), ('1983年', '416.1', '193.8', '')]

writer.writerows(data)
csvfile.close()