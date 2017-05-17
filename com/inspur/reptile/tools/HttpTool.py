import urllib.request
import json

def request_ajax_data(url,session=None,data=None,**headers):
    print(url)
    ret =request(url,session=session,data=data,**headers)
    #jsonText = response.read()
    return json.loads(ret)

def request(url,session=None,data=None,**headers):
    req = urllib.request.Request( url )
    print("data========",data)

    for name,value in(headers.items()):
        req.add_header(name, value )
    print(req.headers)
    req.add_header( 'User-Agent',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' )

    #print(req.headers)
    if headers:
        for k in headers.keys():
            req.add_header( k, headers[k] )
    print ("session======",session)
    if(session!=None):
        r= session.request("Get",url)
        return r.content
    if(data==None):
        response = urllib.request.urlopen( req )
    else:
        params = urllib.parse.urlencode( data ).encode( 'utf-8' )
        print( params )
        response = urllib.request.urlopen( req, params )
    return  response.read()

if __name__ == '__main__':

    url='http://www.tianyancha.com/annualreport/newReport.json?id=2344338651&year=2015'

    #ajaxRequestBody = {"id":"zb","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    #ajaxRequestBody = {"m":"QueryData","dbcode":"hgnd","rowcode":"zb","valuecode":"A0506"}

    #ajaxRequestBody = {"id":"A01","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    #ajaxRequestBody={"dbcode":"hgnd","dbcode":"zb","m":"getTree"}
    #b="bb"
    #ajaxResponse = request_ajax_data(url)
    req=urllib.request.Request(url)
    req.add_header( 'User-Agent',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' )

    ajaxResponse=urllib.request.urlopen(req)
    print(ajaxResponse.read())
