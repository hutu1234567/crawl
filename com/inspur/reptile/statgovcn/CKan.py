#-*- coding: utf-8 -*-
__author__ = 'xx'
import requests
import json
import pprint
from com.inspur.reptile.statgovcn.Measure import *
CKAN_URL = 'http://10.10.10.59'
#CKAN_URL='http://data.sjtu.edu.cn'
APIkey = 'b6f9241d-09ca-4e77-a5b0-8678802f52c0'
#APIkey='c4dfab38-4762-4734-b689-9afa6bcc0d1a'
OwnerOrg = 'statsgovcn'
PackageName = 'test'
PackageName='inspur'
PackageTitle = 'test'
datasetlocal="D:\\work\\crawl\\statsgovcn\\zb\\"
def create_datasets(datasets):
    for i in range(len(datasets)):
        dataset = datasets[i]
        print(dataset[0])
        print(dataset[3])
        rcode,rtxt = update_package(APIkey,OwnerOrg,dataset[0],dataset[3])
        print(rcode)
        print(rtxt)
def create_package(APIkey, OwnerOrg, PackageName,PackageTitle):
    url = '{ckan}/api/3/action/package_create'.format(
            ckan=CKAN_URL)

    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-CKAN-API-Key'] = APIkey
    headers['Authorization'] = APIkey
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

    dict = {}
    dict['name'] = PackageName.lower()
    dict['title'] = PackageTitle
    dict['owner_org'] = OwnerOrg
    dict['extras']=[{"key":"统计时间跨度","value":"年度"},{"key":"更新频率","value":"每月"}]
    dict = json.dumps(dict).encode('ascii')

    r = requests.post(url, headers=headers, data = dict)
    return r.status_code, r.text
# def upload_resouce(APIkey, OwnerOrg, PackageName,PackageTitle):
#
#     package_id = 'test'
#     resource_name = 'uploadtest'
#     resource_format = 'csv'
#     resource_address = 'A0506.csv'
#
#     file=open(resource_address)
#     r = requests.post(
#         #'{ckan}/api/action/resource_create'.format( ckan=CKAN_URL ),
#         CKAN_URL+'/api/action/resource_create',
#                        data={
#                            "package_id": package_id,
#                            "type": "file.upload",
#                            "url": "10.10.10.59",
#                            "name": resource_name,
#                            "format": resource_format
#                        },
#                        headers={"Authorization": APIkey},
#                        files={'upload': (resource_name, file)} )
#     return r.status_code, r.text
def update_package(APIkey, OwnerOrg, PackageName,PackageTitle):
    url = '{ckan}/api/3/action/package_update'.format(
            ckan=CKAN_URL)

    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-CKAN-API-Key'] = APIkey
    headers['Authorization'] = APIkey
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'

    dict = {}
    dict['name'] = PackageName.lower()
    dict['title'] = PackageTitle
    dict['author']="xiaxue"
    dict['maintainer'] = "xiaxue"
    dict['author_email'] = "xiaxue@inspur.com"
    dict['maintainer_email'] = "xiaxue@inspur.com"
    dict['notes'] = PackageTitle
    dict['extras']=[{"key":"统计时间跨度","value":"年度"},{"key":"更新频率","value":"每月"}]
    dict['tag_string']="国家统计局,年度,"+PackageTitle
    dict = json.dumps(dict).encode('ascii')

    r = requests.post(url, headers=headers, data = dict)
    return r.status_code, r.text

def uploads(datas):
    for i in range(len(datas)):
        retcode,rettxt=upload(datas[i])
def upload(data):
    #file = open("A0506.csv")
    # r=requests.post( 'http://10.10.10.59/api/action/resource_create',
    #                data={"package_id": "test1","name":"xxuploadcsv4","format":"csv"},
    #                headers={"X-CKAN-API-Key": "b6f9241d-09ca-4e77-a5b0-8678802f52c0"},
    #
    #
    #                files=[('upload', open("A0506.csv"))] )
    # return r.status_code, r.text
    dataid=data[0]
    dataname=data[3]
    package_id=data[5].lower()[0:3]
    memo=data[6]
    #memo.replace("\\n\\r","\n\rzzzzzz")
    print(memo)
    file=open(datasetlocal+dataid+".csv")
    #print(file.read())
    print(package_id+":"+dataname+":"+memo)
    r=requests.post( CKAN_URL+'/api/action/resource_create',
                   data={"package_id": package_id,"name":dataname,"format":"csv","description":memo},
                   headers={"X-CKAN-API-Key": APIkey},
                   files=[('upload', file)] )
    if(r.status_code!=200):
        print(dataid+"上传失败！因为："+str(r.status_code)+r.text)
    return r.status_code, r.text
if __name__ == '__main__':
    datas=getAllLeafMeasures();
    uploads(datas)
    #uploads(datas)
    #data=('A0A00', 'zb', 'hgnd', '21全体及分城乡居民收支基本情况(新口径)', '1','A0A01','说明</br>bbbbb')

    #status_code, text = upload_resouce( APIkey, OwnerOrg, PackageName, PackageTitle )
    #pprint.pprint( status_code )
    #pprint.pprint( text )
    # status_code, text =upload()
    # pprint.pprint( status_code )
    # pprint.pprint( text )