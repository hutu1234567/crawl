#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"total":8,"items":[
# {"title":"浪潮集团有限公司与华盖创意（北京）图像技术有限公司侵害作品信息网络传播权纠纷二审民事裁定书","submittime":"1486656000000","court":"北京知识产权法院",
# "casetype":"民事案件","uuid":"1e22ca81df8b4f83a198fd83d9c001df","doctype":"民事裁定书",
# "url":"http://wenshu.court.gov.cn/content/content?DocID=e6770fe3-7ae7-42e0-bad4-a740000e14fa","caseno":"（2016）京73民辖终1156号"},
# {"title":"青岛新天物业发展有限责任公司与山东茗筑世家置业有限公司物业服务合同纠纷一审民事判决书","submittime":"1474300800000","court":"山东省济南市中级人民法院","casetype":"民事案件","uuid":"0b293eecfe5a4f78826e58ae9a7fcf5c","doctype":"民事判决书","url":"http://wenshu.court.gov.cn/content/content?DocID=bd6181b6-50e0-4f8f-a447-c80f1045f826","caseno":"（2015）济民一初字第21号"},{"title":"赵光顺与浪潮集团有限公司建设工程施工合同纠纷一审民事判决书","submittime":"1456675200000","court":"济南高新技术产业开发区人民法院","casetype":"民事案件","uuid":"8030b1f5c7c044da9f1d32927ccd1b26","doctype":"民事判决书","url":"http://wenshu.court.gov.cn/content/content?DocID=487443d9-984d-4333-98d1-e708a5959cf9","caseno":"（2015）高民初字第413号"}],"pagesize":3}}
#
# <table id="CWL_LEGAL_CASE" name="法律诉讼">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="DATE"  type="varchar(8)"  name="日期" />
#     <column id="TITLE"  type="varchar(256)" name="裁判文书"/>
#     <column id="CONTEXT" type="TEXT" name="裁判文书内容" />
#     <column id="TYPE" type="varchar(32)" name="案件类型" />
#     <column id="CODE" type="varchar(32)" name="案件号" />
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>


import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class LawCaseEntity(Entity):
    tableName="CWL_LEGAL_CASE"
    map={"ID":'uuid',
         "DATE":'submittime',
         "TITLE":'title',
         "CONTEXT":'url',
         "TYPE":'casetype',
         "CODE":'caseno',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        if("submittime" in dataStr.keys()):
            dataStr['submittime'] = DateTool.transDataFormat(dataStr['submittime'],"%Y%m%d")
        self.dataStr=dataStr
        super().__init__(source)