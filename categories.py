#! python
# -*- coding: utf-8 -*-
from enum import Enum, auto

class Categories(Enum):
    SUPER = auto()
    ELECTRICITY = auto()
    INTERNET_AND_PHONES = auto()
    OTHER_FOOD = auto()
    RESTAURANTS_AND_HOTELS = auto()
    WATER = auto()
    ARNONA = auto()
    CAR_INSURANCE = auto()
    CAR_EXPENSES = auto()
    HEALTH_INSURANCE = auto()
    OTHER_INSURANCE = auto()
    GAS = auto()
    FUEL = auto()
    INCOME_TAX = auto()
    HEALTH_AND_MACABI = auto()
    SCHOOLS = auto()
    STARTUP = auto()
    HUGIM = auto()
    INVESTMENTS = auto()
    CASPOMAT = auto()
    CLOTHING = auto()
    PRESENTS = auto()
    INTERNET_SERVICES_AND_SHOPPING = auto()
    ABROAD_EXPENSES = auto()
    VISA = auto()
    CHECKS = auto()
    BANK_AMLOT = auto()
    HOME_RELATED = auto()
    FUN_AND_MOVIES = auto()
    MISC = auto()
    UNKNOWN = auto()

# Categorizations - list of tuples, each tuple contains a category and a list of strings that are the names of the expenses that belong to this category
Categorizations = [
            (Categories.BANK_AMLOT, ['11 שי ץורע.למע','טנרטניא תויושר','טנרטניא תויושר','31 שי ץורע.למע','טנרטניא-הינק','טנרטניא-הרמה','41 שי ץורע.למע','91 שי ץורע.למע','546ורש אובי.מע','9 שי ץורע.למע','007יגיד הרבעה','01 שי ץורע.למע','007טניא .עה','7 שי ץורע.למע','טנרטניא הרמה','546 ח"טמ תרבעה',"007טנרטניא .עה", "696הדקפה/הרבעה","21 שי ץורע.למע",'ע"ינ לוהינ ימד', '546טמ תרבעה.מע' ]),
            (Categories.VISA,['מקס'] ),


            (Categories.WATER,['מיה','שטראוס','מים'] ),           
            (Categories.SUPER[ 'סופר זול', 'מתחם 22','יוחננוף', 'אושר עד', 'שופרסל',  'עדיקה', 'מינימרקט ', 'חצי חינם','AM PM','AM:PM' ,'PM:AM', 'טיב טעם'],),
            (Categories.SCHOOLS,['א.מ.ש.', 'LEAPLEARNER ', ' CBT', 'מכללת בית ברל'] ),
            (Categories.RESTAURANTS_AND_HOTELS,['אונמי','שירותי בר בארועים', 'פורטונה פיצה', 'ארקפה ', 'פיצה ביס', 'נונומימי'
                                                , 'מאפיית טלר', 'עידנס', 'בר אירי', 'חומוס ', 'ארומה ', 'בית רמות'
                                                , 'שיפודי הנכדים', 'טופולופומפו', 'מייזון קייזר', 'קפה מתתיהו', 'קומבה'
                                                , "ג'ירף ", 'שרון פיצה', 'זורבה', 'ארקפה ', ' לנדוור', 'דנון', 'מלון ים סוף'
                                                , 'קפה זוריק', 'גרקו', 'גלידות השרון', 'רמותה קפה אוכל ', 'בורגר ראנץ '
                                                , 'רימון דוכני ', 'אמפנדו במחנה', 'LEO BLOOMS  ', 'ארקפה  ', 'KFC ', 'מימי ', 'נקודה בלב  '
                                                , 'שגב ניהון', ' לב הפארק', 'נומי',  "ג'ונז פיצה ", 'חנדלה', 'לנדוור ', 'ברביץ', 'מיצי בשוק '
                                                , "מקדונלד'ס", 'זוזוברה', 'שושנה', 'OMAM', 'אננדה']),
            (Categories.PRESENTS,['AMZN MKTP ', 'צעצועון ', 'פאזלבוקס', 'PAYBOX', 'BUYME', ' CHICKIES'
                                  , ' BIT', 'צומת ספרים', 'אייבורי ', 'PAYBOX', ' STEAM'
                                  , 'כפר השעשועים', ' SMT', 'אימפריית הצעצועים'] ),
            (Categories.OTHER_INSURANCE,['שירביט'])
            (Categories.CHECKS, ["שיק"]),
            (Categories.OTHER_FOOD,['שוק','התמרים','יובל','ROLADIN ', 'מרכז הזמנו', ' סוליקה', 'WOLT', 'בוטיק סטנרל  ', 'בבקה ', 'עולם הממתקים', 'מאפית טלר'
                                    , 'גולדה ', 'לה פרומזרי ', 'מעדני שמיל ומקסים  ', 'גבינות המשק', 'חומוס כספי', 'קלית הכיכר', 'מעל המצופה'
                                    , 'מיסטר פיש', 'קפה ', 'ארטיזנל', 'רוזנר', 'לחם תושייה', 'בייקר', 'הפרטוי', "בולנז'רי ", 'אלי דלאל  ', 'בר המשקאות'
                                    , ' מטבח', 'סוליקה  ', 'מאפית', 'שמו', 'יין בעיר', 'בלילה', 'חלאתי  ', 'פפה ', 'בוטיק סנטרל כפר סבא', 'גלידוש']),
            (Categories.INTERNET_AND_PHONES, ['HOT', 'SPIGEN', 'פרטנר', 'סלקום ', 'פלאפון']),
            (Categories.INVESTMENTS, ['מנורה מבטחים-חיים/בריאות']),
            (Categories.ELECTRICITY, ["חשמל"]),
            (Categories.MISC, ['פאנקי ', 'לוקר אמבין ', "יהושע בפארק ", 'קורט צבי הולנדר ', 'צורי ובניו', 'קפלה'
                               , 'סקארה', 'השואה', ' המכס', 'סיגר קלאב ', 'רשות הדואר-רכישת מוצר דאר', 'צחי ובנצי עיצוב שיער'] ),
            (Categories.ARNONA, ['עיריית הוד השרון', 'עירית הוד השרון']),
            (Categories.CAR_INSURANCE, ['כלמוביל', 'AIG', 'חובה', ' ביטוח ', 'הפניקס']),
            (Categories.CAR_EXPENSES, ['חניונים', 'חניה', 'רכבת', 'טעינת', 'פנגו', 'חניון ', 'GETT', 'איתוראן', 'חניו', 'כביש 6', 'קאר', 'חניוני', 'הרכב','אי.וי.']),
            (Categories.HEALTH_INSURANCE, [ 'הפניקס ביטוח', 'מגדל חיים', ' בריאות' ]),
            (Categories.OTHER_INSURANCE, ["פסגות", "מנורה ביטוח דירה"]),
            (Categories.GAS, ["סופרגז"]),
            (Categories.FUEL,['מכמורת', 'סונול', 'פז', 'דלק']),
            (Categories.INCOME_TAX, ['מס הכנסה']),
            (Categories.HEALTH_AND_MACABI, ['מכבידנט  ', ' מכבי', 'רפואי', 'דראגסטורס', 'מדיקל ', 'סופר פארם','רביע']),
            (Categories.STARTUP,['GOOGLE HEX', 'GOOGLE STORAGE', 'CHATGPT', ' MEDIUM ', 'GOOGLE DEVSISTERS ', 'TOME.APP', 'CLOUD ', 'GITHUB', 'OPENAI '
                                 , "גאדג'ט טים", 'CLOUD', 'MIDJOURNEY ', 'OPENAI', 'MICROSOFT*STORE ', 'CHATGPT', 'MICROSOFT*PC'])
            (Categories.HUGIM, ['קאנטרי', 'מחול', 'אולדרימס', 'שבט איתן', ' ספורט ', 'אנרגים', 'סטודיו']),
            
            (Categories.CASPOMAT, ["כספומט"]),
           
            (Categories.CLOTHING,['מרגלית ילדים', 'דרים ספורט', 'קרולינה למקה ', 'S WEAR', 'דלתא', 'רנואר', 'WE SHOSE',
                                'שופרא', 'תינוקי', 'פוקס', 'אירית הראל', 'קסטרו', 'הודיס ', 'ETSY ', 'גולף', 'מקס',
                                  'מיידלה', 'זארה', 'גלי', 'אורבניקה', 'סימפוני' , 'מיננה'  ,'דקטלון']),
            
            (Categories.HOME_RELATED,['ללין ', 'RING ', 'א.א חומרי בנין', 'אור לבית', 'אייס כפר סבא', 'אלומה', 'מעבדת השרון'
                                      , 'קיי. אס.פי', 'פרחי שרונים', 'KSP', 'המרכז לבניין',  'מ.נ.מ   ', 'בריכות ', '  פרחים '
                                      , 'המשתלה  ', 'איקאה ', ' ELEGANT RADIATORS', 'איקאה', 'וולקום  ', 'סנט- הייר','קיי אס פי'] ),

            (Categories.INTERNET_SERVICES_AND_SHOPPING, ["KINDLE","MARKETPLACE",'PAYPAL', 'WWW.ALIEXPRES','ALIEXPRESS',"WWW.ALIEXPRESS.COM","AMAZON", "AMZN", "GOOGLE", "amzn","SPOTIFYIL","NETFLIX.COM"]),

            (Categories.FUN_AND_MOVIES, ['מקס ', 'ארץ ערבה', 'סטימצקי  ', 'קופת כרטיסים', ' סינמה' , ' צלילה', ' פינוקים ', 'מוזיאון ישראל', 'היכל התרבות', 'PUZZLEBOX', 'מלון השרון'])
            (Categories.ABROAD_EXPENSES,  ['AIRBNB', 'HERCULES GREEK', 'SEA LIFE', 'TIN BUILDING', 'HULK CART', 
                                           'CHILL-N', 'BREAD ALONE', 'CICCOLATITALIAN', 'AVIS', ' SUPERCENTER ',
                                           'MIGROSS', 'PRASINI', 'ITALMARK', 'RESTAURANT ALPTRIDA', 'GEMMA PIZZERIA', 'PIGASOS', '3505 PESCHIERA',
                                           "YUKI'S BAKERY", 'DUNKIN', 'VITAEGUSTO', 'ERGON HOUSE', 'LIM*RIDE', 'UBER', 'ELDORADO', 'AMERIKA GAS STATION',
                                           'WOW', 'AVIS', 'MULBERRY', 'VANDERBILT', 'CAPTAIN CANDY', 'FYF*FROMYOUFLOWERS', 'TARGET', 'GRUPPO',
                                           'HM', 'UBER ', 'CAFE  GRAMSCI ', 'ALIEXPRESS', 'SPORT & MODE T', "ZARO'S", 'BONEYARD',
                                           'NIKEPOS_US', 'מגדל ב. כללי נסיעות לחו"ל', 'TIGER HELLAS', 'CIRCLE K ', ' IPMATIC', 'ROADHOUSE',
                                           '1ST COFFEEBIZ', 'GALLO STREET', 'O D A P ','CONAD','OLIVE GARDEN', ' HOSPITALITY', 'MTA', 'TROPICALNEWSST2527',
                                           'SENILRIA', 'SP HONEY BUG', 'TANKSTELLE', 'PASTICCERIA', 'FARMACIA DOTT', 'TST* HAMILTON PORK ',
                                           'BALTHAZAR', 'WIZZ AIR', 'PARK AUTOSILO', 'AIRALO', 'FRESHTOWN#604', 'STUBHUB', 'ERGON ', 'SHAKE SHACK',
                                           'CREMERIA ', 'TAXIS', 'BSPDV', 'KAYAK ', 'AUTOSTRADA ', 'CARIBBEAN KING', 'AGGELMAR EPE',
                                           'IPER', 'FLOCAFE ', 'קניה יזומה לארנק מט"ח', 'SCRIB HUNTER', 'DUFRITAL', 'HARD ROCK',
                                           'THGIL JS', '*YANKEE DOODLE', 'VERONA', 'IDALPE', 'BORGO MONDRAGON', 'ERGON HOUSE', 'FINGEMI',
                                           'MENCHIE 00107029   ', 'IL TORCHIO', 'ROSETTA BAKERY', 'SHAWON', 'BOX LUNCH ', "L'ARTE DEL", 'SPORTS & EMOTIONS',
                                           'LOEWS ROYAL', 'TARGET', '4035 MARKET', 'TST* MAMAN ', 'EL AL', 'CHICK-FIL-A', 'INTERSPAR',
                                           'BENACUS DI BACCOLO ', 'EATALY', 'PATATA', 'YARD HOUSE', 'רשות האוכלוסין וההגירה  ת', 'ERGON',
                                           'PRIMARK ', 'WB STUDIO', 'SQ *MY BUSINESS', 'ERGON', 'WHOLEFDS', 'DISTRIBUTORE AGIP',
                                           'זיכוי מיתרת ארנק מט"ח', 'UBER S', 'SUPERMERCATO', 'MISCUSI', 'BILLA', 'ASPIT DIREZ.', 'BOUGATSADIKO',
                                           'ALFIERI BARDOLINO', 'DUTY FREE', 'SUNRISE ', 'MEAT THE GREEK ', 'ארומה נתבג טרמינל 3',
                                           "ג'יי.אר.-היינמן טרמינל 3", 'SQ *BLANK STREET', 'THE UNDERDOG ', 'MARGATE ', 'HM IT0322',
                                           'ישראייר תעופה בע"מ-צמרת', 'COMUNE ', 'WENDYS ', 'רכישת מט"ח', 'MY STRALI',
                                             'LIDL', 'ZARA HELLAS', 'PINOTSI', 'CELIO 6332', 'WORLD8.CO.IL'])
        ]

unknown_companies = []

def get_category(company: str) -> Categories:
    """
    Determines the category of a given company based on predefined categorizations.

    Args:
    - company (str): The name of the company to categorize.

    Returns:
    - Categories: The category the company belongs to. Returns Categories.OTHERS if no match is found.
    """
    if company is None:
        return Categories.UNKNOWN
    
    for category, matches in Categorizations:
        if any(match in company for match in matches):
            return category
    
    #save the company name a list of unique unknown companies
    if company not in unknown_companies:
        unknown_companies.append(company)
        with open(".unknown_companies.txt", "a") as f:
            f.write(company + "\n")
            print(f"Unknown category for company {company}")

    return Categories.UNKNOWN


