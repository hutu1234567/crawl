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
from com.inspur.reptile.base.MySQLTool import *
import traceback
def runTasksByComName(searStr):
    searStr = searStr.strip( "\n" )


    print( searStr )
    ret = HumanSearch( searStr )
    if (hasattr( ret, "data" )):
        datas = ret.data
    else:
        datas = None
    if (datas != None):
        data = datas[0]
    id = str( data["id"] )
    comName = str( data["name"] ).replace( "</em>", "" ).replace( "<em>", "" )
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
def runTasksWithExcel(fileName):
    # searStr="章丘东汉铁艺有限公司"
    fileName="D:/work/PycharmProjects/untitled/com/inspur/reptile/fixtures/company.txt"
    print( "D:/work/PycharmProjects/untitled/com/inspur/reptile/fixtures/company.txt" )
    txt = open( "D:/work/PycharmProjects/untitled/com/inspur/reptile/fixtures/companys.txt", encoding="utf-8" )
    list_of_all_the_lines = txt.readlines()
    # print(list_of_all_the_lines)
    # list_of_all_the_lines = ["济南天马泰山石材有限公司"]
    for searStr in list_of_all_the_lines:
        try:
            runTasksByComName( searStr )
        except:
            print( searStr )
            traceback.print_exc()
def runWithInvest():
    sql= "select distinct com_name from cwl_invest where id not in (select com_id from cwl_com_base)"
    query()
if __name__ == '__main__':
