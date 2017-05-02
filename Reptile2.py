import urllib.request
import pymysql
import json

#url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22110000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A1404%22%7D%5D&k1=1492396109462'  #目标网址
url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A1404%22%7D%5D&k1=1492396964665'
request=urllib.request.Request(url=url)  #请求服务器
response=urllib.request.urlopen(request)  #服务器应答
content=response.read().decode('utf-8')   #以一定的编码方式查看源码

s=json.loads(content)
l = []
try:
    conn = pymysql.connect(host='localhost', user='root', passwd='inspur', db='sys', port=3306)
    cur = conn.cursor()

    for i in range(len(s['returndata']['datanodes'])):
        o = s['returndata']['datanodes'][i-1]
        v = '%d' %o['data']['data']
        #print("指标：" + o['wds'][0]['valuecode'] + ";时间区间：" + o['wds'][1]['valuecode'] + ";值：" + v)
        p = {'zb': o['wds'][0]['valuecode'],'sj':o['wds'][1]['valuecode'],'data':o['data']['data']}
        #l.append(p)
        effect_row = cur.executemany("INSERT INTO sys.ns_data(ID, INDI_ID, TIME_ID, VALUE, AREA_ID) VALUES(%s,%s,%s,%s,%s)",[(i,o['wds'][0]['valuecode'],o['wds'][1]['valuecode'],o['data']['data'],"ALL")])
        conn.commit()
#    s2=json.dumps(l)
#    print(s2)
    cur.close()
    conn.close()
except pymysql.Error as e:
    print
    "Mysql Error %d: %s" % (e.args[0], e.args[1])