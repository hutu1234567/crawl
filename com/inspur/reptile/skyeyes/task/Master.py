from com.inspur.reptile.skyeyes.task.AnnualReport import AnualReport
from com.inspur.reptile.skyeyes.task.ComBaseInfo import ComBaseInfo
from com.inspur.reptile.skyeyes.task.Bid import Bid
from com.inspur.reptile.skyeyes.task.ChangeInfo import ChangeInfo
from com.inspur.reptile.skyeyes.task.CompetingGoods import CompetingGoods
from com.inspur.reptile.skyeyes.task.CopyRight import CopyRight
from com.inspur.reptile.skyeyes.task.Holder import Holder
from com.inspur.reptile.skyeyes.task.Invest import Invest
from com.inspur.reptile.skyeyes.task.LawCase import LawCase
from com.inspur.reptile.skyeyes.task.PatentInfo import PatentInfo
from com.inspur.reptile.skyeyes.task.ProductInfo import ProductInfo
from com.inspur.reptile.skyeyes.task.RecruitmentInfo import RecuitmentInfo
from com.inspur.reptile.skyeyes.task.SiteRecord import SitRecord
from com.inspur.reptile.skyeyes.task.Staff import Staff
from com.inspur.reptile.skyeyes.task.TradeMark import TradeMark
from com.inspur.reptile.skyeyes.task.TaxRatingInfo import TaxRatingInfo
from com.inspur.reptile.skyeyes.task.HumanSearch import HumanSearch
import com.inspur.reptile.base.MySQLTool as mysql
import traceback
def runTasksByComName(searStr,comList=[]):
    if(len(comList)==0):
        comList = getAllComs()
    searStr = searStr.strip( "\n" )
    #print( searStr )
    ret = HumanSearch( searStr )
    if (hasattr( ret, "data" )):
        datas = ret.data
        #print( datas )
    else:
        return
    if(datas != None):
        data = datas[0]
    else:
        return
    id = str( data["id"] )
    comName = str( data["name"] ).replace( "</em>", "" ).replace( "<em>", "" )
    # if(comName!=searStr):
    #     if (hasattr( datas, "matchField" )):
    #         his_name=datas["matchField"][0]["content"].replace( "</em>", "" ).replace( "<em>", "" )
    #         if(his_name!=searStr):
    #             return
    if(id in comList):
        #print(id,"已经存在了,不再抓取")
        return
    else:
        print(id,searStr, comName,"不存在，需要抓取")
    ComBaseInfo( id )
    AnualReport( id )
    Bid( id )
    ChangeInfo( id )
    CompetingGoods( id, comName )
    CopyRight( id )
    Holder( id )
    Invest( id )
    LawCase( id, comName )
    PatentInfo( id )
    ProductInfo( id )
    RecuitmentInfo( id, comName )
    SitRecord( id )
    Staff( id )
    TradeMark( id )
    TaxRatingInfo( id )
def runTasksWithExcel():
    # searStr="章丘东汉铁艺有限公司"
    fileName="D:/work/PycharmProjects/untitled/com/inspur/reptile/fixtures/companys.txt"
    txt = open( fileName, encoding="utf-8" )
    list_of_all_the_lines = txt.readlines()
    expect_com_list=getAllComs()
    # print(list_of_all_the_lines)
    # list_of_all_the_lines = ["济南天马泰山石材有限公司"]
    for searStr in list_of_all_the_lines:
        try:
            runTasksByComName( searStr,expect_com_list )
        except:
            #print( searStr )
            traceback.print_exc()
def runWithInvest():
    queryInvestComSql= "select distinct com_name from cwl_invest where com_name  not in (select com_name from cwl_com_base )"
    ret_com_names = mysql.query(getcon(),queryInvestComSql)
    runWithComNames(ret_com_names,getAllComs())
def runWithHolder():
    queryInvestComSql= "select name from cwl_holder where name  not in (select com_name from cwl_com_base ) and length(name)>6"
    ret_com_names = mysql.query(getcon(),queryInvestComSql)
    runWithComNames(ret_com_names,getAllComs())

def runWithComNames(com_names, except_com_names=[]):
    for comName in com_names:
        try:
            print( comName[0] )
            comid=runTasksByComName( comName[0], except_com_names )
            except_com_names.append(comid)
        except:
            print( comName[0] )
            traceback.print_exc()
def getcon():
    return mysql.getcon( "10.110.1.245", "root", "v6root", "v6db", 3306 )
def getAllComs():
    queryAllComSql = "select com_id from cwl_com_base"
    retComList = mysql.query( getcon(), queryAllComSql )
    except_com_list = []  # 抓取过的公司不再抓取
    for comid in retComList:
        except_com_list.append(comid[0])
    return except_com_list
if __name__ == '__main__':
   # runWithInvest()
   # runTasksWithExcel()
   #runTasksWithExcel()
   runTasksByComName("山东亿同新纸业有限公司")
   #  ids=['a','bb']
   #  if('a' in ids):
   #      print ("asdfadsfas")
   #      ids.append('cc')
   #      print(ids)