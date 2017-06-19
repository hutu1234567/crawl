from __future__ import division  # fruture

import csv
import logging.handlers

from com.inspur.reptile.statgovcn.Measure import saveMemo
from com.inspur.reptile.base.HttpTool import request_ajax_data

#该类负责抓取具体指标数据
LOG_FILE = 'tst.log'
handler = logging.handlers.RotatingFileHandler( LOG_FILE, maxBytes=1024 * 1024*1024, backupCount=5 )  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter( fmt )  # 实例化formatter
handler.setFormatter( formatter )  # 为handler添加formatter

logger = logging.getLogger( 'tst' )  # 获取名为tst的logger
logger.setLevel( logging.DEBUG )
logger.addHandler( handler )  # 为logger添加handler

url = 'http://data.stats.gov.cn/easyquery.htm?'  # url常量，国家统计局的查询基本都通过此url
m="QueryData"


class MeasureData():
    def __init__(self,dbcode,rowcode,colcode,wds,zb,startdate,enddate=0):
        self.dbcode=dbcode
        self.rowcode=rowcode
        self.colcode=colcode
        self.wds=wds
        self.zb=str(zb)
        self.startdate = startdate
        self.enddate = enddate
        self.dates=[]

        if(enddate==0):
            self.dates=[startdate]
        else:
            startyear = int( str( startdate )[0:4] )#取前4位为年
            endyear = int( str( enddate )[0:4] )#取前4位为年
            if(dbcode=="hgyd"):#如果是按月度查询，则构建月度跨度list
                startmonth = int( str( startdate )[4:6] )#取5，6位为月
                endmonth = int( str( enddate )[4:6] )#取5，6位为月
                print( startmonth )
                for year in range( startyear, endyear + 1 ):
                    for month in range( 1, 12 + 1 ):
                        if (year == startyear and month < startmonth):
                            continue
                        if (year == endyear and month > endmonth):
                            continue
                        self.dates.append( str( year ) + (str( month ) if month >= 10 else "0" + str( month )) )
                print(self.dates)
            elif(dbcode=="hgnd"):#如果按年度查询，则构建年度跨度list
                for year in range( startyear, endyear + 1 ):
                    self.dates.append( str( year ))
                print(self.dates)
            elif(dbcode=="hgjd"):#如果按季度查询，则构建年度跨度list
                print("暂未实现")
    def crawl(self):

        logger.debug("start:"+self.zb)
        datas=[]
        doneHead=False
        doneMemo = False  # 标记是否已经解析保存过Memo了，memo只需要处理一次，完成一次之后，就置为true。
        for date in  (self.dates):
            print(date)
            dfwds="[{\"wdcode\":\"zb\",\"valuecode\":\""+self.zb+"\"},{\"wdcode\":\"sj\",\"valuecode\":\""+str(date)+"\"}]"
            print(dfwds)
            ajaxRequestBody = {"m": m, "dbcode":self.dbcode , "rowcode":self.rowcode , "colcode":self.colcode , "wds":self.wds ,
                           "dfwds":dfwds}
            logger.debug( "start send request:"+self.zb )
            content=request_ajax_data(url,data=ajaxRequestBody)
            logger.debug( "end send request:"+self.zb )
            if(content["returncode"]==200):
                #先解析出memo并保存
                memostr = parseMemo( content )
                dbdata = (memostr, self.zb)
                saveMemo( dbdata )
                #再解析出数据
                datas=paserDatas(content)
                print("datas======"+str(datas))

        return datas
        #file_object = open( self.zb+".csv", 'w' )
        #file_object.write( csv )
        #file_object.close()
def paserDatas(content):
    wd = content["returndata"]["wdnodes"]
    datanodes = content["returndata"]["datanodes"]
    datas=[]
    rowh = ("时间",)#表头
    dateCols=[]#时间列数组，保存共有多少时间有数据
    # 先拼表头
    for i in range( 0, len( wd ) ):  # 取出指标名称作为表头
        if (wd[i]["wdcode"] == "zb"):  # 如果该值为zb，则说明本数组为指标说明数组
            for j in range( 0, len( wd[i]["nodes"] ) ):
                #print("unit::::::::::::::::::"+str(wd[i]["nodes"][j]))
                unitname="(" + wd[i]["nodes"][j]["unit"] + ")" if  wd[i]["nodes"][j]["unit"] !="" else ""
                cname=wd[i]["nodes"][j]["cname"] + unitname
                print("cname======"+cname)
                rowh += (cname,)
                # h+=","+wd[i]["nodes"][j]["cname"]+"("+wd[i]["nodes"][j]["unit"]+")"
            # h+="\n"
            # csv+=h
        elif(wd[i]["wdcode"] == "sj"):  # 如果该值为zb，则说明本数组为指标说明数组
            for j in range( 0, len( wd[i]["nodes"] ) ):
                # print(wd[i]["nodes"])
                dateCols.append(wd[i]["nodes"][j]["cname"])
                # h+=","+wd[i]["nodes"][j]["cname"]+"("+wd[i]["nodes"][j]["unit"]+")"
            # h+="\n"
            # csv+=h
    datas.append( rowh )  # 将表头写入数组

    zbcounts=len(datanodes)//len(dateCols)
    i=0
    zbdatas=[]
    for zbindex in range (zbcounts):
        zbdata=[]
        for dateindex in range (len(dateCols)):
            data=datanodes[i]["data"]
            zbdata.append(str(data["data"] if data["hasdata"] else ""))
            i+=1
        zbdatas.append(zbdata)
    print("zbdatas"+str(zbdatas))
    for dateindex in range(len(dateCols)):
        rowdata=[dateCols[dateindex]]
        hasvalue=False
        for zbindex in range( zbcounts ):
            value=zbdatas[zbindex][dateindex]
            rowdata.append(value)
            if(zbdatas[zbindex][dateindex]!=""):
                hasvalue=True
        if(hasvalue):
            datas.append(rowdata)

    print(len(datanodes))
    print(zbcounts)

    return datas
def parseMemo(content):
    dictionarys = content["returndata"]["wdnodes"][0]["nodes"]
    #dictionarys = [('年度', '粮食人均占有量(公斤)', '棉花人均占有量(公斤)', '油料人均占有量(公斤)', '糖料人均占有量(公斤)', '茶叶人均产量(公斤)', '水果人均占有量(公斤)', '猪牛羊肉人均占有量(公斤)', '水产品人均占有量(公斤)', '人均原煤产量(吨)', '人均原油产量(公斤)', '人均纱产量(公斤)', '人均布产量(米)', '人均机制纸及纸板产量(公斤)', '人均水泥产量(公斤)', '人均粗钢产量(公斤)', '人均发电量(千瓦小时)'), ('1988', '357.725370587221', '3.76594355636647', '11.9846963136443', '56.1664453582419', '0.49', '15.12', '', '9.63', '0.89', '124.41', '4.23', '17.06', '11.53', '190.75', '53.95', '494.9')]
    print("dictionarys======="+str(dictionarys))
    memos=[]
    for dict in dictionarys:
        memo=dict["memo"]
        items = memo.split( "||" )
        for item in items:
            if item in memos or memo == "":
                print( "memo重复或为空" )
            else:
                memos.append(item)
    i=1
    memostr=""
    for memo in memos:
        items=memo.split("||")#把memo分隔开，然后再去重，因为有子memo重复情况
        for item in items:
            memostr+=str(i)+"."+item+" "
            print(memostr)
            i+=1
        memostr=memostr.rstrip()
    print ("memostr====="+memostr)
    return memostr

def saveData(folder,zb,data):

    print( data )
    csvfile = open( folder + zb + ".csv", 'w',newline="",encoding='utf_8_sig' )
    #f = codecs.open(csvfile,'w', 'utf_8_sig')
    writer = csv.writer( csvfile )
    writer.writerows( data )
    csvfile.close();
if __name__ == '__main__':

    zb="A010101"
    md=MeasureData("hgyd","sj","zb",[],zb,"1900-");
    ret=md.crawl()
    #saveData("D:\\work\\icrawl\\statsgovcn\\zb\\test\\",zb,ret)
    #ajaxRequestBody = {"id":"zb","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    # ajaxRequestBody = {"m":"QueryData","dbcode":"hgnd","rowcode":"sj","colcode":"zb","wds":"[]","dfwds":"[{\"wdcode\":\"zb\",\"valuecode\":\"A0506\"},{\"wdcode\":\"sj\",\"valuecode\":\"1983\"}]"}
    # print ("[{\"wdcode\":\"zb\",\"valuecode\":\"A0506\"}]")
    # print (ajaxRequestBody)
    # ajaxResponse = request_ajax_data( url, ajaxRequestBody )
    # print (ajaxResponse)
