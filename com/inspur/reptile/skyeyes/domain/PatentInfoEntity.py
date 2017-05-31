#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"viewtotal":"61","items":[
# {"mainCatNum":"C21D9/30(2006.01)I","createTime":"1484288389000","updateTime":"0","applicationPublishNum":"CN106319186A","pid":"ff562bd7b42346aead84a7bd25ca5f10",
# "inventor":"尚贺军;赵丽美;","applicationPublishTime":"2017.01.11","patentNum":"CN201610851456.8",
# "imgUrl":"http://pic.cnipr.com:8080/XmlData/FM/20170111/201610851456.8/201610851456.gif","allCatNum":"C21D9/30(2006.01)I;C21D1/18(2006.01)I;",
# "patentName":"一种45钢滚轮轴高温短时淬火回火工艺",
# "abstracts":"本发明涉及一种45钢滚轮轴高温短时淬火回火工艺，将粗车后的45钢滚轮轴装入炉温≤300℃的炉内，升温至800±10℃，保温0.5h后，快速升温至900±10℃短时保温，淬水；将45钢滚轮轴入炉，在300±10℃下保温0.5h，升温至520±10℃，保温1.0h后，空冷降温。经过本发明高温短时淬火回火处理的滚轮轴，其本体表面硬度240‑250HB，同炉处理的滚轮轴回火后表面颜色均匀一致，没有发现因淬火冷却不均匀而产生的白斑等现象，本体硬度偏差控制在30HB之内。",
# "address":"250207 山东省济南市章丘济王路9001号","applicationTime":"2016.09.27","uuid":"ff562bd7b42346aead84a7bd25ca5f10","patentType":"发明专利",
# "applicantName":"山东伊莱特重工股份有限公司;"},

# <table id="CWL_PATENT" name="专利">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="APPLY_DATE"  type="varchar(8)"  name="申请日期" />
#     <column id="NAME"  type="varchar(256)" name="专利名称"/>
#     <column id="APPLY_CODE" type="varchar(32)" name="申请号" />
#     <column id="RELEASE_CODE" type="varchar(32)" name="申请公布号" />
#     <column id="DETAIL_URL" type="varchar(512)" name="详情" />
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>


import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql

class PatentInfoEntity(Entity):
    tableName="CWL_PATENT"
    map={"ID":'uuid',
         "APPLY_DATE":'createTime',
         "NAME":'patentName',
         "APPLY_CODE":'patentNum',
         "RELEASE_CODE":'applicationPublishNum',
         "DETAIL":'detail',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        dataStr["detail"] = pymysql.escape_string( str( dataStr ) )

        if("createTime" in dataStr.keys()):
            dataStr['createTime'] = DateTool.transDataFormat(dataStr['createTime'],"%Y%m%d")
        self.dataStr=dataStr
        super().__init__(source)