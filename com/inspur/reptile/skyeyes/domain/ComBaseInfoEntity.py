# <column	id="COM_ID"  primaryKey="true" required="true" type="varchar(30)"  name="企业ID"/>
# <column id="DAS_COM_ID" required="true" type="VARCHAR(30)" name="企业编号" note="DAS_IND_COM_INFO表主键"/>
# <column id="COM_NAME" required="true" type="VARCHAR(128)"  name="企业名称" />
# <column id="LEGAL_REPRESENT" type="varchar(128)"  name="法人代表"  />
# <column id="REGIST_CAPITAL" type="varchar(32)"  name="注册资本"  />
# <column id="REGIST_DATE" type="varchar(8)"  name="注册时间"  note='yyyyMMdd'/>
# <column id="STATUS" type="varchar(32)"  name="经营状态"  />
# <column id="REGIST_CODE" type="varchar(32)"  name="工商注册号"  />
# <column id="ORGAN_CODE" type="varchar(32)"  name="组织机构代码"  />
# <column id="CREDIT_CODE" type="varchar(64)"  name="统一信用代码"  />
# <column id="COM_TYPE" type="varchar(64)"  name="企业类型"  />
# <column id="IND_TYPE" type="varchar(64)"  name="行业"  />
# <column id="BUSIN_PERIOD" type="varchar(32)"  name="营业期限"  />
# <column id="APPROVED_DATE" type="varchar(8)"  name="核准日期"  />
# <column id="REGIST_ORGAN" type="varchar(32)"  name="登记机关"  />
# <column id="ADDR" type="varchar(256)"  name="注册地址"  />
# <column id="BUSINESS_SCOPE" type="TEXT"  name="经营范围"  />

#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"updatetime":1494395270512,"fromTime":1145462400000,"bondName":"伊莱特",
# "categoryScore":9597,"type":1,"id":2344338651,"usedBondName":"","percentileScore":7954,"regNumber":"370000400004164","phoneNumber":"0531-83806707",
# "regCapital":"25850万人民币","regInstitute":"济南市工商行政管理局","name":"山东伊莱特重工股份有限公司","regLocation":"济南市章丘市官庄镇济王路9001号",
# "approvedTime":1453046400000,"industry":"专用设备制造业","logo":"http://static.tianyancha.com/logo/lll/c4cda54aa33cfacdc9c055157e1b78de.png",
# "businessScope":"从事热锻件配件、热锻环件、锻轴件、高合金钢锻件、有色金属锻件、管件的研发和生产制造；销售本公司生产的产品。（依法须经批准的项目，经相关部门批准后方可开展经营活动，有效期限以许可证为准）。",
# "orgNumber":"787407639","regStatus":"在营","estiblishTime":1145462400000,"bondType":"新三板","legalPersonName":"牛余刚","legalPersonId":2061601839,
# "sourceFlag":"http://qyxy.baic.gov.cn/","actualCapital":"","websiteList":"www.iraetaforging.cn","flag":1,"email":"sdyltcw@163.com","correctCompanyId":"",
# "companyOrgType":"股份有限公司(中外合资、未上市)","base":"sd","updateTimes":1494395272000,"companyType":0,"creditCode":"913701007874076393",
# "companyId":65233949,"historyNames":"山东伊莱特重工有限公司\t","bondNum":"837192"}}
# 在本类中定义数据集与数据库的对应，并完成对特定属性的处理

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
import com.inspur.reptile.tools.MySQLTool as mysql
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class ComBaseInfoEntity(Entity):
    tableName="CWL_COM_BASE"
    map={"COM_ID":'id',"DAS_COM_ID":'regNumber',"COM_NAME":'name',"LEGAL_REPRESENT":'legalPersonName',"REGIST_CAPITAL":'actualCapital',
         "REGIST_DATE":'estiblishTime',"STATUS":'regStatus',"REGIST_CODE":'regNumber',"ORGAN_CODE":'orgNumber',"CREDIT_CODE":'creditCode',
         "COM_TYPE":'companyOrgType',"IND_TYPE":'industry',"BUSINESS_BEGIN":'fromTime',"BUSINESS_END":'toTime',"APPROVED_DATE":'approvedTime',
         "REGIST_ORGAN":'regInstitute',"ADDR":'regLocation',"BUSINESS_SCOPE":'businessScope'}
    def __init__(self,dataStr={}):
        DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        DateTool.transDataFormat(dataStr,"toTime","%Y%m%d")
        self.dataStr=dataStr

if __name__ == '__main__':
        #dt = datetime.fromtimestamp( 2867155200000 /1000)
        #lll = dt.strftime("%Y%m%d")
        #lll=datetime.strptime(dt.st,"%Y%m%d")
        # a=lll.time()
        #print (lll)
        #combase=ComBaseInfoBean(a=1)
        #print(combase.a)
        datastr={"fromTime":2867155200000,"toTime":1867155200000,"id":"2344338651"}
        com = ComBaseInfoEntity( datastr )

        print(com.map)