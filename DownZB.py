import urllib.request
import json
from urllib.parse import quote_plus,unquote_plus,urlencode
#url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22110000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A1404%22%7D%5D&k1=1492396109462'  #目标网址
#url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A1404%22%7D%5D&k1=1492396964665'
#url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"valuecode":"A0102","wdcode": "zb"},{"valuecode": "2014","wdcode": "sj"}]&k1=1463383802505'
url='http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj'
k1='&k1=1492396109462'
#print(unquote_plus(url))
wds_key='&wds='
wds_value='[{"wdcode":"reg","valuecode":"120000"}]'#修改valuecode即可爬取其他地区数据，比如12000为天津
dfwds_key='&dfwds='
dfwds_value='[{"wdcode":"zb","valuecode":"A1405"}]'#修改valuecode即可爬取其他指标数据，比如A1405为办公楼施工、竣工面积

#postdata={'cn':'c01','zb':'A010503','sj':'2013'}
#postdata={'m':'QueryData','dbcode':'fsyd','rowcode':'zb','colcode':'sj','wds':'[{"wdcode":"reg","valuecode":"110000"}]','dfwds':'[{"wdcode":"zb","valuecode":"A1404"}]','k1':'1492396109462'}
#s1=quote_plus(json.dumps(postdata))
url=url+wds_key+quote_plus(wds_value)+dfwds_key+quote_plus(dfwds_value)+k1
print(url)
request=urllib.request.Request(url)  #请求服务器
#response=urllib.request.urlopen('http://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A010503&sj=2013')  #服务器应答
response=urllib.request.urlopen(request)  #服务器应答
content=response.read().decode('utf-8')   #以一定的编码方式查看源码
print("origin content="+content)
s=json.loads(content)
l = []
for i in range(len(s['returndata']['datanodes'])):
    o = s['returndata']['datanodes'][i-1]
    v = '%d' %o['data']['data']
    #print("指标：" + o['wds'][0]['valuecode'] + ";时间区间：" + o['wds'][1]['valuecode'] + ";值：" + v)
    p = {'zb': o['wds'][0]['valuecode'],'sj':o['wds'][1]['valuecode'],'data':o['data']['data']}
    l.append(p)

s2=json.dumps(l)
print("formated content="+s2)