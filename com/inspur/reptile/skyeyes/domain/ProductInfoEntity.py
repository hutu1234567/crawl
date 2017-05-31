#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"count":69,"items":[
# {"classes":"生活","filterName":"爱城市网探索版","icon":"http://a1.mzstatic.com/us/r30/Purple111/v4/cc/cb/ee/cccbee6c-c323-9fd4-11e0-f84a19fa9d7b/CRV_AP_600x360.jpeg","
# type":"应用","brief":"在“互联网+”的大趋势下，爱城市网探索版整合各个政务单位分散的服务资源和服务渠道，提供统一的“城市便民服务”入口，为百姓提供办事指南查询，以及各类政务办事服务；在社保、住房、公积金、教育、医疗、交通等方面提供查询、验证、预约、推送等服务；公共事业方面，提供水、电、燃气费查询缴费服务和多种渠道支付方式，同时接入各类第三方智慧应用，让更多市民便捷地享受到智慧城市建设成果。",
# "name":"爱城市网探索版"},
# {"classes":"商务","filterName":"浪潮云+","icon":"http://a4.mzstatic.com/us/r30/Purple122/v4/7e/07/86/7e0786d9-5d1c-6d9e-d04b-c16c73c251d1/CRV_AP_600x360.jpeg","type":"应用","brief":"浪潮云+，将浪潮GS管理软件后台业务以移动场景重新梳理，并赋予移动化、智能化、协同化的能力，为企业提供最佳的移动应用体验。<br/><br/>浪潮云+融合最新技术，基于云部署，申请即用；融合移动设备管理云，安全可靠；支持开放标准协议，可作为统一移动入口集成第三方轻应用，是智能化的企业移动应用平台。<br/><br/>围绕工作沟通：在聊天中内置智能对象，可围绕审批、报告等各种业务对象进行沟通，以同步信息、共享知识、激发创意。<br/><br/>事项一目了然：集成会议、企业日历、待办事项、智能通知功能，将眼前与近期事项聚合，让工作井然有序。<br/><br/>信息一手掌握：汇聚分析报告、知识文档、企业资讯等信息资源，融合全文搜索，智能推荐等大数据技术，让智慧释于指尖。<br/><br/>一切皆可链接：内置集成审批、差旅报销等浪潮GS企业管理软件业务，通过云连接器、OAuth安全开放协议，可集成第三方轻应用、数据流、消息流，统一入口，尽享极致体验。","name":"浪潮云+  -智能化的企业移动应用平台"}]}}
#
# <table id="CWL_PRODUCT" name="产品信息">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="ICON"  type="varchar(512)"  name="图标链接" />
#     <column id="NAME"  type="varchar(256)" required="true" name="产品名称"/>
#     <column id="SHORT" type="varchar(256)" name="产品简称" />
#     <column id="TYPE" type="varchar(32)" name="产品分类" />
#     <column id="DOMAIN" type="varchar(32)" name="产品领域" />
#     <column id="PRODUCT_URL" type="varchar(512)" name="产品详情链接"/>#前端动态拼接的信息，在所有字段中已经包括
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>


import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql

class ProductInfoEntity(Entity):
    tableName="CWL_PRODUCT"
    map={"ID":'uuid',
         "ICON":'icon',
         "NAME":'name',
         "SHORT":'filterName',
         "TYPE":'type',
         "DOMAIN":'classes',
         "BRIEF":'brief',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        dataStr["uuid"]=Entity.createUUID()
        dataStr["detail"] = pymysql.escape_string( str( dataStr ) )

        if("createTime" in dataStr.keys()):
            dataStr['createTime'] = DateTool.transDataFormat(dataStr['createTime'],"%Y%m%d")
        self.dataStr=dataStr

        super().__init__(source)