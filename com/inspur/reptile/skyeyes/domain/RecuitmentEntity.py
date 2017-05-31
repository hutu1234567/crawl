#{"state":"ok","message":"","data":{"companyEmploymentList":[
# {"id":193252150,"title":"平面美工","city":"济南","district":"济南","companyName":"山东伊莱特重工股份有限公司","oriSalary":"4000-4999",
# "urlPath":"http://job.01hr.com/j/b-11597868.html","startdate":1492531200000,"enddate":1494172800000,"source":"数字英才网","education":"大专","employerNumber":"",
# "experience":"不限","createTime":1492722010000,"updateTime":1492982829000,
# "description":"岗位职责： 1、负责淘宝店铺、网站、样册的美工设计，图片处理，要求对户外用品有一定敏感度。 2、熟悉网页焦点理论，对网页布局有丰富经验;对色彩敏感，能处理各种视觉冲突，有良好的审美观; 3、负责图片的设计和美化，包括拍照及图片修改和制作、动态广告条等的设计，商品展示模板设计，日常产品维护、调整、美化; 4、淘宝店铺的主页美化，制作促销、描述模板，根据公司产品的上架情况和促销信息自主制作促销广告位，对拍摄后的产品图进行校色、美化处理; 5、站在用户角度去思考，提高网站的可用性，优化设计，能够挖掘消费者的浏览习惯和点击需求。 任职要求： 1、优秀的视觉设计能力，认真细致，善于创新，以人为本的设计理念; 2、熟练使用Photoshop、Dreamweaver、Fireworks、Flash等软件; 3、良好的沟通能力，善于对设计的表达，具有良好的团队协作精神; 4、有美工工作经验者优先，专科以上学历，美术相关专业优先。"}
# ,{"id":184935748,"title":"数控机床装配技工（钳工、电工）(大型设备/机电设备/重工业)",
# "city":"济南","district":"济南","companyName":"山东伊莱特重工股份有限公司","oriSalary":"4000-8000元/月",
# "urlPath":"http://www.kanzhun.com/job/1710220987.html?sid=aladinglz","startdate":1489248000000,"enddate":1491840000000,"source":"看准网","education":"大专",
# "employerNumber":"36人","experience":"不限","createTime":1489284614000,"updateTime":1490199708000,"description":"岗位职责：\n1、掌握常用设备的名称、型号、规格、性能、结构、传动、润滑系统、使用规则及保养方法。 \n2、掌握常用刀具的种类、牌号、用途、规格、性能和维护保养方法，刀具的几何形状、角度对切削性能的影响；\n3、掌握常用金属材料的种类、牌号、用途、切削性能和力学性能及热胀冷缩性能。\n4、执行作业计划，优质、高效、低耗地完成或超额完成生产任务。\n5、按设计图样、工艺文件、技术标准进行生产，在加工过程中进行自检和互检。\n贯彻执行工艺规程（产品工艺路线表、专业工种工艺、典型工艺过程等）。\n6、遵守安全操作规程，执行定置管理标准，遵守国家环境保护有关规定。\n7、维护保养设备、工装、量具，使其保持良好。\n8、对修理质量，恢复原有的精度负责。 对技术改进、技术创新、简单修理工艺的制定负责。 对工作中的问题及时报告，协调负责。\n9、对所使用的工具的维护保养负责。 对所分管的经济指标负责。对分管的现场负责  对设备大修、项修、设备改造负责。\n\n任职要求：\n1、机械、电气专业大专及以上学历，3年及以上装配经验。\n2、有高级装配证书和加工中心实际装配经验者优先考虑。\n3、有团队合作意识，责任心强，吃苦耐劳。\n工作地址：\n\n                            济南章丘市济王路9001号 朱家裕风景区对面，技师学院东1000米"}]
# ,"totalRows":29}}

# <table id="CWL_RECRUIT" name="招聘">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="CDATE"  type="varchar(8)"  name="发布时间" />
#     <column id="POSITION"  type="varchar(128)" name="招聘职位"/>
#     <column id="SALARY" type="varchar(32)" name="薪资" />
#     <column id="EXP" type="varchar(32)" name="工作经验" />
#     <column id="NUM" type="varchar(32)" name="招聘人数" />
#     <column id="CITY" type="varchar(32)" name="工作城市" />
#     <column id="DISTRICT"  type="varchar(32)" name="所在区"/>
#     <column id="SOURCE" type="varchar(32)" name="来源" />
#     <column id="START_DATE" type="varchar(8)" name="招聘开始日期" />
#     <column	id="END_DATE"   type="varchar(8)"  name="招聘截止日期"/>
#     <column	id="EDU"    type="varchar(32)"  name="教育"/>
#     <column	id="DESC"   type="TEXT"  name="职位描述"/>
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql

class RecuitmentEntity(Entity):
    tableName="CWL_RECRUIT"
    map={"ID":'id',
         "CDATE":'createTime',
         "POSITION":'title',
         "SALARY":'oriSalary',
         "EXP":'experience',
         "NUM":'employerNumber',
         "CITY":'city',
         "DISTRICT": 'district',
         "SOURCE": 'source',
         "START_DATE": 'startdate',
         "END_DATE": 'enddate',
         "EDU": 'education',
         "NOTE": 'description',
         "COM_ID": 'comid',
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        dataStr["description"] = pymysql.escape_string( dataStr["description"] )

        if("createTime" in dataStr.keys()):
            dataStr['createTime'] = DateTool.transDataFormat(dataStr['createTime'],"%Y%m%d")
        if ("startdate" in dataStr.keys()):
            dataStr['startdate'] = DateTool.transDataFormat( dataStr['startdate'], "%Y%m%d" )
        if ("enddate" in dataStr.keys()):
            dataStr['enddate'] = DateTool.transDataFormat( dataStr['enddate'], "%Y%m%d" )
        self.dataStr=dataStr
        super().__init__(source)