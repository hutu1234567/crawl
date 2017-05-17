from com.inspur.reptile.skyeyes import ComBaseInfo,IntellectualPropertyInfo, LegalCase
from com.inspur.reptile.skyeyes.task import RecruitmentInfo, PatentInfo, TaxRatingInfo

#import com.inspur.reptile.skyeyes.ComBaseInfo as ComBaseInfo

if __name__ == '__main__':
    id="2344338651"
    ComBaseInfo.ComBaseInfo(id).crawl()
    IntellectualPropertyInfo.IntellectualPropertyInfo(id).crawl()
    PatentInfo.PatentInfo( id ).crawl()
    RecruitmentInfo.RecuitmentInfo( "山东伊莱特重工股份有限公司" ).crawl()
    TaxRatingInfo.TaxRatingInfo( id ).crawl()
    LegalCase.LegalCase("山东伊莱特重工股份有限公司").crawl()