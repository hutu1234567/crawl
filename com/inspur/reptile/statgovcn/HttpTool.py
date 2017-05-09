import urllib.request
import json

def request_ajax_data(url,data,referer=None,**headers):

    response =request(url,data)
    jsonText = response.read()
    return json.loads(jsonText)

def request(url,data,referer=None,**headers):
    req = urllib.request.Request( url )
    req.add_header( 'Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8' )
    req.add_header( 'X-Requested-With', 'XMLHttpRequest' )
    req.add_header( 'User-Agent',
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116' )
    if referer:
        req.add_header( 'Referer', referer )
    if headers:
        for k in headers.keys():
            req.add_header( k, headers[k] )
    params = urllib.parse.urlencode( data ).encode( 'utf-8' )
    print( params )
    response = urllib.request.urlopen( req, params )
    return  response

if __name__ == '__main__':

    url='http://data.stats.gov.cn/easyquery.htm?cn=B01'
    ajaxRequestBody = {"id":"zb","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    #ajaxRequestBody = {"m":"QueryData","dbcode":"hgnd","rowcode":"zb","valuecode":"A0506"}

    #ajaxRequestBody = {"id":"A01","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    #ajaxRequestBody={"dbcode":"hgnd","dbcode":"zb","m":"getTree"}

    ajaxResponse = request_ajax_data(url,ajaxRequestBody)

    print(ajaxResponse)
