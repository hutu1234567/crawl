#公司基本信息
#http://www.tianyancha.com/v2/company/2315740.json
from com.inspur.reptile.skyeyes.common.Token import getToken
from com.inspur.reptile.skyeyes.domain.ComBaseInfoEntity import ComBaseInfoEntity
from com.inspur.reptile.skyeyes.task.Info import Info
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "v2/company/"
class ComBaseInfo(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + ".json"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

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

if __name__ == '__main__':
    comBase=ComBaseInfo("2344338651")
    print(Info.getBaseUrl(comBase))
    session=getToken(Info.getBaseUrl(comBase))
    ret=comBase.crawl(session=session)
    comBaseEntity=ComBaseInfoEntity( ret["data"] )
    comBaseEntity.save()
    print(comBaseEntity)
    #print(ret["data"])