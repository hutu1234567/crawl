from com.inspur.reptile.statgovcn.HttpTool import request_ajax_data
import csv
import logging
import logging.handlers

LOG_FILE = 'tst.log'
handler = logging.handlers.RotatingFileHandler( LOG_FILE, maxBytes=1024 * 1024, backupCount=5 )  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter( fmt )  # 实例化formatter
handler.setFormatter( formatter )  # 为handler添加formatter

logger = logging.getLogger( 'tst' )  # 获取名为tst的logger
logger.setLevel( logging.DEBUG )
logger.addHandler( handler )  # 为logger添加handler

url = 'http://data.stats.gov.cn/easyquery.htm?'  # url常量，国家统计局的查询基本都通过此url
m="QueryData"
class MeasureData():
    def __init__(self,dbcode,rowcode,colcode,wds,zb,startdate,enddate):
        self.dbcode=dbcode
        self.rowcode=rowcode
        self.colcode=colcode
        self.wds=wds
        self.zb=str(zb)
        self.startdate=startdate
        self.enddate=enddate
        #self.
    def crawl(self):
        logger.debug("start:"+self.zb)
        datas=[]
        for date in range(self.startdate,self.enddate+1):
            print(date)
            dfwds="[{\"wdcode\":\"zb\",\"valuecode\":\""+self.zb+"\"},{\"wdcode\":\"sj\",\"valuecode\":\""+str(date)+"\"}]"
            print(dfwds)
            ajaxRequestBody = {"m": m, "dbcode":self.dbcode , "rowcode":self.rowcode , "colcode":self.colcode , "wds":self.wds ,
                           "dfwds":dfwds}
            logger.debug( "start send request:"+self.zb )
            content=request_ajax_data(url,ajaxRequestBody)
            logger.debug( "end send request:"+self.zb )
            if(content["returncode"]==200):
                wd=content["returndata"]["wdnodes"]
                #print("wd----")
                #print(wd)

                rowh = ("年度",)
                if(date==self.startdate):#只在第一个时间区间拼表头
                    for i in range(0,len(wd)):#取出指标名称作为表头
                        logger.debug( "start make tableheader:" + self.zb )
                        if(wd[i]["wdcode"]=="zb"):#如果该值为zb，则说明本数组为指标说明数组
                            for j in range(0,len(wd[i]["nodes"])):
                                #print(wd[i]["nodes"])
                                rowh+=(wd[i]["nodes"][j]["cname"]+"("+wd[i]["nodes"][j]["unit"]+")",)
                                #h+=","+wd[i]["nodes"][j]["cname"]+"("+wd[i]["nodes"][j]["unit"]+")"
                            #h+="\n"
                            #csv+=h
                            break
                    datas.append( rowh)#将表头写入数组
                    logger.debug( "end make tableheader:" + self.zb )

                #print(datas)

                data=content["returndata"]["datanodes"]
                rowdata = (str( date ) + "年",)#初始化年的一行
                hasData = False#标记本维度是否有数据，如果无数据，则不再拼入表中
                logger.debug( "start make data:" + self.zb + " at " + str(date) )
                for i in range(0,len(data)):#取出指标值

                    if(data[i]["data"]["hasdata"]):
                        hasData=True
                        #v+=","+str(data[i]["data"]["data"])
                        tmp=(str(data[i]["data"]["data"]),)
                        rowdata=rowdata+tmp
                    else:
                        #v+=","
                        tmp=('',)
                        rowdata = rowdata +tmp
                if(hasData):
                    datas.append(rowdata)
                logger.debug( "end make data:" + self.zb + " at " + str(date)  )

                    #csv+=v
        #print("datas====")
        #print(datas)
        logger.debug("end:"+self.zb)

        return datas
        #file_object = open( self.zb+".csv", 'w' )
        #file_object.write( csv )
        #file_object.close()
def saveData(folder,zb,data):
    print( data )
    csvfile = open( folder + zb + ".csv", 'w', newline="" )
    writer = csv.writer( csvfile )
    writer.writerows( data )
    csvfile.close();
if __name__ == '__main__':
    zb="A0101"
    md=MeasureData("hgnd","sj","zb","[]",zb,1960,2017);
    ret=md.crawl()
    saveData("zb/",zb,ret)
    #ajaxRequestBody = {"id":"zb","dbcode":"hgjd","wdcode":"zb","m":"getTree"}
    # ajaxRequestBody = {"m":"QueryData","dbcode":"hgnd","rowcode":"sj","colcode":"zb","wds":"[]","dfwds":"[{\"wdcode\":\"zb\",\"valuecode\":\"A0506\"},{\"wdcode\":\"sj\",\"valuecode\":\"1983\"}]"}
    # print ("[{\"wdcode\":\"zb\",\"valuecode\":\"A0506\"}]")
    # print (ajaxRequestBody)
    # ajaxResponse = request_ajax_data( url, ajaxRequestBody )
    # print (ajaxResponse)
