#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":[
# {"webSite":["www.inspur.com"],"examineDate":"2017-04-17","companyType":"企业","webName":"浪潮集团企业网站","ym":"inspur.com.cn",
# "companyName":"浪潮集团有限公司","liscense":"鲁ICP备05019369号"},
# {"webSite":["www.inspur.com"],"examineDate":"2017-04-17","companyType":"企业","webName":"浪潮集团企业网站","ym":"langchao.com","companyName":"浪潮集团有限公司","liscense":"鲁ICP备05019369号"},{"webSite":["www.inspur.com"],"examineDate":"2017-04-17","companyType":"企业","webName":"浪潮集团企业网站","ym":"langchao.com.cn","companyName":"浪潮集团有限公司","liscense":"鲁ICP备05019369号"},{"webSite":["www.inspur.com"],"examineDate":"2017-04-17","companyType":"企业","webName":"浪潮集团企业网站","ym":"inspur.com","companyName":"浪潮集团有限公司","liscense":"鲁ICP备05019369号"},{"webSite":["218.57.146.229"],"examineDate":"2017-04-17","companyType":"企业","webName":"浪潮信息","ym":"218.57.146.229","companyName":"浪潮集团有限公司","liscense":"鲁ICP备05019369号"}]}

# <table id="CWL_SITE_RECORD" name="网站备案">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="APPROVE_DATE"  type="varchar(8)"  name="审核日期" />
#     <column id="SITE_NAME"  type="varchar(128)" name="网站名称"/>
#     <column id="SITE_HOME" type="varchar(32)" name="网站首页" />
#     <column id="DOMAIN" type="varchar(32)" name="域名" />
#     <column id="RECORD_CODE" type="varchar(32)" name="备案号" />
#     <column id="STATUS" type="varchar(32)" name="状态" /> json未返回该值
#     <column id="ORGAN_TYPE" type="varchar(32)" name="单位性质" />
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql

class SiteRecordEntity(Entity):
    tableName="CWL_SITE_RECORD"
    map={"ID":'uuid',
         "APPROVE_DATE":'examineDate',
         "SITE_NAME":'webName',
         "SITE_HOME":'webSite',
         "DOMAIN":'ym',
         "RECORD_CODE":'liscense',
         "ORGAN_TYPE":'companyType',
         "COM_ID": 'comid',
         }
    def __init__(self,dataStr={},source=None):
        dataStr["uuid"]=Entity.createUUID()
        if(dataStr['examineDate'] is None):
            dataStr['examineDate']=""
        else:
            dataStr['examineDate'] = str(dataStr['examineDate']).replace("-","")

        dataStr["webSite"] = pymysql.escape_string( str(dataStr["webSite"] ))

        self.dataStr=dataStr
        super().__init__(source)