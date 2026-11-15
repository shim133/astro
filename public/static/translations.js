/**
 * AstroMatch Pro - Multi-Language Translation Engine
 * Hebrew (RTL) & English (LTR)
 */

export const TRANSLATIONS = {
  he: {
    dir: 'rtl',
    langName: 'עברית',
    flag: '🇮🇱',
    appTitle: 'אסטרו-מאץ׳ פרו',
    engineBadge: 'מנוע נתוני נאס״א מדויק (v2.5.1)',
    heroSubtitle: 'התאמה אסטרולוגית מקצועית ומפות סינסטריה אינטראקטיביות. חישוב אורך אקליפטי מדויק באמצעות Skyfield ומודל NASA DE421.',
    quickSample: '💫 דוגמה מהירה להתאמה',
    viewSaved: '📁 צפה בניתוחים שמורים',
    savedCountSuffix: 'שמורים',
    helpBtn: '❓ מדריך שימוש ואסטרולוגיה',
    helpModalTitle: '📖 מדריך מקצועי למשתמש — אסטרו-מאץ׳ פרו (v2.5.1)',

    // Partner A & B
    partnerA: 'בן/בת זוג א׳',
    partnerB: 'בן/בת זוג ב׳',
    innerWheel: 'גלגל פנימי',
    outerWheel: 'גלגל חיצוני',
    fullName: 'שם מלא או כינוי',
    namePlaceholderP1: 'לדוגמה: אלכס',
    namePlaceholderP2: 'לדוגמה: ירדן',
    dob: 'תאריך לידה',
    exactTime: 'שעת לידה מדויקת',
    cityLabel: 'עיר / יישוב לידה (בארץ ובעולם)',
    checkLocation: '🔍 בדיקת מיקום',
    cityPlaceholder: 'למשל: רמת גן, קרית גת, תל אביב, ירושלים, ניו יורק...',
    cityHelp: 'הזן עיר, יישוב או מושב בארץ ובעולם. נבדק בזמן אמת מול OpenStreetMap ומאגר המקומות המקומי.',
    tzLabel: 'אזור זמן (UTC)',
    tzAuto: 'מתעדכן אוטומטית לפי העיר',
    tzStandardNotice: 'יש להזין שעה באזור הזמן הסטנדרטי (GMT) ללא שעון קיץ (למשל: שעון חורף סטנדרטי)',

    // Actions & Buttons
    calcBtn: '🔮 חשב סינסטריה וצייר מפות אסטרולוגיות',
    calcBtnLoading: '✨ מחשב מיקומי כוכבים ומפות...',
    saveBtn: '💾 שמור לניתוחים שלי',
    formHint: 'מפיק גלגל סינסטריה כפול אינטראקטיבי, מפות בתים וניתוח היבטים מעמיק',
    newCalc: '← חישוב חדש',
    saveToMyAnalyses: '💾 שמור לניתוחים שלי',
    exportSvg: '⬇️ יצוא מפת SVG',
    exportPng: '🖼️ יצוא מפת PNG',

    // Saved Analyses
    savedAnalysesTitle: '📁 ניתוחים ופרופילי זוגות שמורים',
    savedAnalysesSub: 'בחר, טען, ערוך או מחק פרופילי סינסטריה שמורים',
    searchSavedPlaceholder: '🔍 חיפוש שמורים...',
    refreshBtn: '🔄 רענן',
    noSavedYet: 'אין עדיין ניתוחים שמורים.',
    noSavedSub: 'מלא את הטופס למעלה ולחץ על "שמור לניתוחים שלי" כדי לשמור פרופילים.',
    loadIntoForm: '📥 טען לטופס',
    editBtn: '✏️ ערוך',
    deleteBtn: '🗑️ מחק',
    versionBadge: 'גרסה',

    // Modal Edit
    editModalTitle: '✏️ עריכת ניתוח שמור',
    editTitleLabel: 'כותרת / כינוי לניתוח',
    notesLabel: 'הערות / הקשר הזוגי',
    notesPlaceholder: 'הערות אופציונליות...',
    cancelBtn: 'ביטול',
    saveChangesBtn: 'שמור שינויים',

    // Person Profile Management
    chooseSavedPerson: '👤 בחר/י פרופיל שמור...',
    personSavedBadge: '✓ שמור',
    personNotSavedBadge: 'לא שמור',
    personModifiedBadge: 'שונה',
    savePersonBtn: '💾 שמור',
    updatePersonBtn: '💾 עדכן',
    savePersonTooltip: 'שמור פרופיל אישי זה לשימוש חוזר מהיר והשוואות עתידיות',
    savedPeopleTitle: '👥 מאגר פרופילים אישיים',
    savedPeopleSub: 'פרופילי לידה אישיים המוכנים להשוואה מול כל בן/בת זוג',
    searchPeoplePlaceholder: '🔍 חפש פרופיל...',
    noSavedPeopleYet: 'אין עדיין פרופילים אישיים שמורים.',
    noSavedPeopleSub: 'הזינו פרטים בטופס ולחצו "שמור" ליד שם האדם כדי לשמור פרופיל לשימוש חוזר.',
    setAsPartnerA: '👤 הגדר כבן/בת זוג א׳',
    setAsPartnerB: '👤 הגדר כבן/בת זוג ב׳',
    editPersonTitle: '✏️ עריכת פרופיל אישי',
    deletePersonConfirm: 'האם את/ה בטוח/ה שברצונך למחוק את הפרופיל של',
    personSaveSuccess: '✅ הפרופיל האישי נשמר בהצלחה!',

    // Compare & Modify Modal
    editDetailsCompareBtn: '✏️ ערוך פרטים / השווה לבן/בת זוג',
    editCompareModalTitle: '🔮 עריכת פרטי לידה והשוואת בן/בת זוג',
    recalcCompareBtn: '⚡ חשב מחדש והשווה',
    swapPartnersBtn: '🔄 החלף צדדים (א׳ ⇄ ב׳)',

    // Geocoding Badges & Resolution
    checkingLocation: 'בודק מיקום ב-OpenStreetMap ובמאגר...',
    locationNotFound: 'המיקום לא נמצא:',
    couldNotResolve: 'לא ניתן היה לאתר את',
    locationCheckHint: 'בדוק איות או ציין מדינה (למשל: "רמת גן, ישראל").',
    foundViaCurated: '✓ נמצא במאגר המקומי',
    foundViaOsm: '✓ נמצא ב-OpenStreetMap',
    suggestedTZ: 'אזור זמן מוצע:',
    resolvedLabel: 'מיקום שזוהה:',
    coordLabel: 'קואורדינטות',
    curatedDatabaseBadge: 'מאגר מאומת',
    osmBadge: 'חיפוש חי (OpenStreetMap)',

    // Alerts & Confirmations
    fillNamesAlert: 'נא למלא לפחות את שמות בני הזוג לפני השמירה.',
    promptTitle: 'הזן כותרת עבור ניתוח זה:',
    deleteConfirm: 'האם אתה בטוח שברצונך למחוק את',
    saveSuccess: '✅ נשמר בהצלחה בניתוחים!',
    enterCityAlert: 'נא להזין שם עיר או יישוב לבדיקה.',

    // Results Page
    reportSubtitle: 'ניתוח סינסטריה גאוצנטרי ברמת דיוק גבוהה',
    synastryIndex: 'מדד סינסטריה',
    aspectsCount: 'היבטים',
    compatRating: 'דירוג התאמה',
    soulmatePotential: '✨ פוטנציאל לנפשות תאומות',
    harmoniousResonance: '💫 הרמוניה ותהודה הדדית',
    dynamicGrowth: '⚡ זרז צמיחה דינמי',
    romanticChemistry: '🔥 כימיה רומנטית',
    emotionalSafety: '🌊 ביטחון רגשי וחיבור ירחי',
    mentalRapport: '💡 תקשורת והבנה מנטלית',
    stabilityScore: '🏛️ יציבות ארוכת טווח ועוגני שבתאי',

    // Big Three & Planet Labels
    sunSign: 'שמש',
    moonSign: 'ירח',
    ascSign: 'אופק (ASC)',
    planetVenus: 'ונוס (נוגה)',
    planetMars: 'מארס (מאדים)',
    coreIdentity: 'זהות גרעינית וחיוניות',
    subconscious: 'תת-מודע וצרכים רגשיים',
    outerPersona: 'פרסונה וגישה לעולם',

    // Tabs
    tabBiWheel: '🔮 גלגל סינסטריה כפול אינטראקטיבי',
    tabP1Chart: 'מפת לידה - בן/בת זוג א׳',
    tabP2Chart: 'מפת לידה - בן/בת זוג ב׳',
    tabAspects: '📜 קטלוג היבטים מפורט',

    // Chart Controls & Filters
    wheelControls: 'מצב גלגל:',
    coordSystem: 'מערכת קואורדינטות:',
    coordTropical: 'טרופי (Astro.com)',
    coordJ2000: 'J2000 (אסטרומטרי)',
    coordDescTropical: 'אסטרולוגיה מערבית סטנדרטית (נקודת שוויון לתאריך) · תואם Astro.com',
    coordDescJ2000: 'נקודת ייחוס אסטרונומית קבועה J2000.0 (אקליפטיקה אסטרומטרית)',
    planetTableTitle: 'נתוני כוכבים ומעלות',
    aspectGridTitle: 'לוח היבטים (Matrix)',
    aspectFilters: 'סינון היבטים:',
    showAspectLines: 'הצג קווי היבטים',
    equalHouses: 'בתים שווים',
    filterAll: 'הכל',
    filterConjunction: '🟡 צמידות (0°)',
    filterTrine: '🟢 טריין (120°)',
    filterSextile: '🔵 סקסטיל (60°)',
    filterSquare: '🔴 סקוויר (90°)',
    filterOpposition: '🟣 אופוזיציה (180°)',
    filterHarmonious: 'הרמוניים',
    filterChallenging: 'דינמיים / חיכוך',
    harmoniousFlow: '● זרימה הרמונית',
    dynamicCatalyst: '● זרז דינמי',
    chartHint: '💡 העבירו את העכבר מעל סמלי הכוכבים או קווי ההיבטים כדי לצפות במעלות המדויקות, מיקומי הבתים ופרשנויות אסטרולוגיות.',
    aspectSubtitle: 'יחסים זוויתיים גיאומטריים מפורטים בין מפות הלידה',

    // SVG Center Labels
    matchLabel: 'התאמה',
    synastryLabel: 'סינסטריה',
    natalMapLabel: 'מפת לידה',
    biWheelModeLabel: 'גלגל סינסטריה כפול',
    innerLabel: 'פנימי',
    outerLabel: 'חיצוני',
    orbLabel: 'סטייה',
    tightnessLabel: 'דיוק',

    // Zodiac Signs
    zodiac: {
      Aries: 'טלה',
      Taurus: 'שור',
      Gemini: 'תאומים',
      Cancer: 'סרטן',
      Leo: 'אריה',
      Virgo: 'בתולה',
      Libra: 'מאזניים',
      Scorpio: 'עקרב',
      Sagittarius: 'קשת',
      Capricorn: 'גדי',
      Aquarius: 'דלי',
      Pisces: 'דגים'
    },

    // Planets
    planets: {
      Sun: 'שמש',
      Moon: 'ירח',
      Mercury: 'מרקורי (כוכב חמה)',
      Venus: 'ונוס (נוגה)',
      Mars: 'מארס (מאדים)',
      Jupiter: 'יופיטר (צדק)',
      Saturn: 'סטורן (שבתאי)',
      Uranus: 'אורנוס (אורון)',
      Neptune: 'נפטון (רהב)',
      Pluto: 'פלוטו',
      Ascendant: 'אופק עולה (ASC)',
      Midheaven: 'רום שמיים (MC)',
      'North Node': 'ראש הדרקון (☊)'
    },

    // Aspects
    aspectNames: {
      Conjunction: 'צמידות',
      Trine: 'טריין (הרמוניה)',
      Sextile: 'סקסטיל (הזדמנות)',
      Square: 'סקוויר (מתח ואתגר)',
      Opposition: 'אופוזיציה (ניגוד והשלמה)'
    },

    // Elements
    elements: {
      Fire: 'אש',
      Earth: 'אדמה',
      Air: 'אוויר',
      Water: 'מים',
      fire: 'אש',
      earth: 'אדמה',
      air: 'אוויר',
      water: 'מים'
    },

    // Score Verdicts (Synastry & Transits)
    scoreVerdicts: {
      verdict_85: 'זיקה קוסמית יוצאת דופן: הרמוניה מגנטית נדירה עם הבנה הדדית עמוקה וחיבור נשמתי מתמשך.',
      verdict_70: 'תהודה אסטרולוגית גבוהה: כימיה טבעית והיבטים תומכים המאפילים על הבדלים מינוריים.',
      verdict_55: 'קשר דינמי ומשלים: תשוקה משמעותית לצד הזדמנויות צמיחה הדורשות אמפתיה מודעת.',
      verdict_0: 'זרז לצמיחה קארמתית: חיכוך אינטנסיבי ומזגים שונים; טרנספורמציה אישית משמעותית אם מטפחים תקשורת.',
      transit_high_alignment: 'מומנטום קוסמי בשיאו: מעברי כוכבים הרמוניים מפעילים את צירי המפה המרכזיים, ופותחים חלון הזדמנויות נדיר ליוזמה, פריצת דרך, שפע והתרחבות.',
      transit_positive_flow: 'תהודה אסטרולוגית חיובית ויוצרת: רוח גבית פלנטרית תומכת בקידום תוכניות ויוזמות. היבטי הזדמנות גוברים על עומסים זמניים.',
      transit_growth_catalyst: 'מתח בונה וטרנספורמציה: מעברי השמיים מאתגרים אזורי נוחות ומאיצים התפתחות אישית, תוך דרישה לסבלנות, התמדה וגמישות אסטרטגית.',
      transit_recalibration: 'כיול מחדש וחיזוק יסודות: אתגרי מעבר קוראים למשמעת פנימית, התבוננות מעמיקה ושמירה על אנרגיה לקראת השלב הבא.'
    },

    // Single-Entity Transit Resonance & Filtering Keys
    transitResonanceIndex: 'מדד תהודת מעברים קוסמית לתאריך',
    transitAlignmentTitle: 'השפעת מעברי השמיים כיום',
    activeTransitMomentum: 'מומנטום קוסמי פעיל',
    singleReportSubtitle: 'ניתוח מפת לידה אישית ומעברי כוכבים מדויקים לתאריך הנבחר',
    transitWeatherTitle: 'מעברים אסטרולוגיים',
    currentSkyPositions: '🌍 מיקום כוכבי השמיים כיום',
    filterAllAnalyses: 'הכל',
    filterSingleTransits: '👤 אישי ומעברים לתאריך',
    filterCoupleSynastry: '👥 זוגות ושותפויות',
    snapshotBadgeSingle: 'אישי ומעברים',
    snapshotBadgePair: 'סינסטריה זוגית',
    saveTransitSnapshot: '📸 שמור תמונת מצב מעברים',
    activeMomentum: '⚡ מומנטום והיבטי מעבר פעילים',
    mentalClarity: '💡 מיקוד ובהירות מחשבתית',
    emotionalBalance: '🌊 איזון רגשי ורווחה אישית',
    resilienceSaturn: '🏛️ יציבות ועמידות מול אתגרים',
    executiveAmbition: '🚀 עוצמה ביצועית ושאפתנות',
    opportunityFlow: '💎 זרימת הזדמנויות ומשאבים',

    // Detailed Aspect Interpretations
    aspectMeanings: {
      "Sun-Moon-Conjunction": "היבט הנישואין השמיימי. הבנה הדדית אינטואיטיבית ברמת הנשמה, הרמוניה רגשית עמוקה והתאמה טבעית.",
      "Sun-Moon-Trine": "תהודה טבעית וזורמת בין האגו והרגשות. אתם מעניקים ביטחון, חיזוק ונחמה אינסטינקטיביים לעולמות הפנימיים זה של זו.",
      "Sun-Moon-Sextile": "זיקה ידידותית ושיתופית. אתם מתקשרים כוונות בבהירות ותומכים הדדית בצמיחה ובהתפתחות של בן/בת הזוג.",
      "Sun-Moon-Opposition": "קוטביות מגנטית עוצמתית. משיכה עזה המשלבת השקפות עולם שונות; יוצרת צמיחה הדדית באמצעות שונות משלימה.",
      "Sun-Moon-Square": "מתח יצירתי בין כוח הרצון לפגיעות הרגשית. דורש אמפתיה מודעת כדי לגשר על מזגים רגשיים שונים.",

      "Venus-Mars-Conjunction": "משיכה פיזית מחשמלת ומגנטיות רומנטית ראשונית. ניצוץ מיידי עם כימיה חושנית וסוערת.",
      "Venus-Mars-Trine": "זרימה רומנטית מוזהבת. פיתוי, תשוקה וחיבה משתלבים ללא מאמץ, ומייצרים תשוקה מתמשכת נטולת עוינות.",
      "Venus-Mars-Sextile": "כימיה שובבה ומלאת חיים. קלילות פלרטטנית עם הערכה טבעית לסגנון הרומנטי של בן/בת הזוג.",
      "Venus-Mars-Square": "חיכוך מיני בעוצמה גבוהה. תשוקה לוהטת וממכרת הדורשת ערוצי ביטוי בונים כדי למנוע התנגשויות קטנוניות.",
      "Venus-Mars-Opposition": "משיכה מגנטית בלתי ניתנת לעצירה בין קטבים מנוגדים. המרדף מלהיב, אך איזון בין חיבה לאגו דורש סבלנות.",

      "Venus-Venus-Conjunction": "טעמים אסתטיים משותפים, שפות אהבה זהות ומקצבים חברתיים תואמים. אתם חווים הנאה ויופי מאותה נקודת מבט.",
      "Venus-Venus-Trine": "רוך טבעי וחיבה הדדית זורמת. קשר מרגיע ומנחם המרכך מתחים יומיומיים.",
      "Venus-Venus-Square": "סגנונות הבעת אהבה שונים או הרגלי בילוי והוצאות מגוונים. מהנה ומעורר עניין ברגע שמחבקים את ההבדלים.",

      "Moon-Moon-Conjunction": "קרבה רגשית טלפתית. אתם מרגישים כמו 'בית' זה עבור זו ומשקפים ברגישות את הפגיעות ההדדית.",
      "Moon-Moon-Trine": "ביטחון רגשי עמוק, רוך ואמון אינטואיטיבי. אתם מזינים ומטפחים זה את זו באופן טבעי.",
      "Moon-Moon-Square": "הרגלי בית שונים וקצבי עיבוד רגשי נפרדים. דורש הקשבה עדינה ומתן מרחב אישי.",
      "Moon-Moon-Opposition": "נדנדה רגשית המפתחת מודעות עמוקה. אחד משמש כעוגן בעוד השני מבטא רגשות, בחילופים אינסטינקטיביים.",

      "Sun-Sun-Trine": "ערכי ליבה הרמוניים, הערכה הדדית עמוקה וחזון משותף לחיים של משמעות והגשמה.",
      "Sun-Sun-Conjunction": "חיוניות עוצמתית ואור זרקורים משותף. אתם מעצימים זה את זו באנרגיה, אך מרחב לריבונות אישית חיוני.",
      "Sun-Sun-Square": "אתגר דינמי של כוחות רצון. אישיויות חזקות הדוחפות זו את זו לשיאי שאפתנות, כל עוד התחרות נשמרת בריאה.",
      "Sun-Sun-Opposition": "דינמיקת מראה מרתקת. כל בן זוג רואה חלקים לא מבוטאים של עצמו משתקפים בבן/בת הזוג.",

      "Mercury-Mercury-Conjunction": "סנכרון מחשבתי מהיר באותו אורך גל. שעות נעלמות בשיחות קולחות כשאתם משלימים זה את משפטי זו.",
      "Mercury-Mercury-Trine": "קשר אינטלקטואלי מעורר השראה. שיתוף פעולה בפרויקטים יצירתיים, אנליטיים או מעשיים זורם בקלות.",
      "Mercury-Mercury-Square": "דיונים סוערים ומקצבי תקשורת שונים. מגרה ומעורר מחשבה, אך הקשבה פעילה חיונית למניעת אי-הבנות.",

      "Jupiter-Sun-Trine": "שפע של מזל טוב, אופטימיות ועידוד הדדי נדיב. אתם מרחיבים זה לזו את האופקים ומגבירים את המזל.",
      "Jupiter-Moon-Trine": "חום מלבב, הומור ונוחות פסיכולוגית מנחמת. מערכת יחסים המאופיינת בשמחת חיים, קלילות וסלחנות.",
      "Saturn-Sun-Trine": "סלע איתן של מחויבות מתמשכת, נאמנות וכבוד הדדי. קשר שנבנה לעמוד במבחן הזמן ובאתגרי המציאות.",
      "Saturn-Venus-Trine": "נאמנות בלתי מעורערת ואהבה יציבה עם שורשים עמוקים. חיבה המבשילה לאחריות הדדית ומסירות לטווח ארוך.",
      "Saturn-Venus-Square": "שיעורים קארמתיים משמעותיים בנושאי אמון ותזמון. הבעת החיבה עשויה להרגיש זהירה, אך מבשילה עם התמדה ומסירות.",
      "Pluto-Venus-Conjunction": "תשוקה עמוקה ומשנת חיים בעוצמה מהפנטת. אהבה בעלת עומק טרנספורמטיבי שאינה משאירה אף אחד ללא שינוי.",
      "Pluto-Venus-Trine": "עומק רגשי ופיזי רב-עוצמה. תשוקה המרפאה כאבי עבר ומחדשת את כוחות הנפש דרך אמון מוחלט.",
      "Neptune-Venus-Trine": "רומנטיקה פיוטית מהאגדות ומסירות רוחנית או אמנותית ללא תנאי.",
      "Uranus-Venus-Trine": "מתח רומנטי מחשמל ובלתי שגרתי. אפס שעמום, חופש אישי גבוה וכימיה מגנטית מתפרצת."
    },

    // Expert Astrologist v2.5.0 Keys (Hebrew)
    loadElonBtn: '🧪 טען מבחן עיוור: אילון מאסק + SpaceX',
    loadElonTeslaBtn: '⚡ אילון מאסק + טסלה',
    entitySubtitleHint: 'תומך באנשים, חברות, ארגונים ואירועים היסטוריים · ניתן להשאיר את ישות ב׳ ריקה לניתוח מול שמיים נוכחיים בלבד',
    transitBarTitle: '🌍 תאריך ושעת ייחוס למעברים (Current Date Transits)',
    transitBarSub: 'חישוב מיקום הכוכבים בשמיים בתאריך הנבחר והשפעתם על הבתים וכוכבי הלידה',
    transitDateLabel: 'תאריך מעברים (ברירת מחדל: היום)',
    transitTimeLabel: 'שעת מעברים',
    resetTodayBtn: '📅 היום',
    blindModeToggle: '🕵️ מצב עיוור (הסתר שמות וגלה מהמפה בלבד)',
    blindModeActive: '🕵️ מצב עיוור פעיל — מוצג פיענוח מהמפה בלבד!',
    blindEntityA: 'נבדק עיוור א׳',
    blindEntityB: 'נבדק עיוור ב׳',
    powerScore: '⚡ עוצמה ביצועית ודחף הגשמה (Power & Drive)',
    wealthScore: '💎 זרימת הון ומשאבים (Wealth & Resource Flow)',
    mcSign: 'רום שמיים (MC)',
    northNodeSign: 'ראש הדרקון (☊)',
    chartRulerLabel: 'שליט המפה (אופק)',
    mcRulerLabel: 'שליט רום השמיים (MC)',
    tabTransitsP1: '🌍 מעברים להיום - ישות א׳',
    tabTransitsP2: '🌍 מעברים להיום - ישות ב׳',
    expertHubTitle: '🧙‍♂️ תיק אסטרולוג מומחה רב-ממדי (Expert Astrologist Dossier)',
    expertHubSubtitle: 'ניתוח עומק של אופק ושליט המפה, רום שמיים, דיוקן עיוור, מאזן יסודות, כל ההיבטים האישיים, מעברים לתאריך הנוכחי ואינטראקציה בין שתי ישויות',
    expertTabNatalP1: '🌟 מפת עומק ודיוקן עיוור - א׳',
    expertTabNatalP2: '🌟 מפת עומק ודיוקן עיוור - ב׳',
    expertTabTransits: '🌍 מעברים לתאריך הנוכחי (Transits)',
    expertTabInteraction: '🤝 אינטראקציה בין 2 ישויות והשלכות בתים',
    expertTabElonVerify: '🧪 אימות עיוור: אילון מאסק (מפה מול מציאות)',
    blindPortraitHeader: '🕵️ דיוקן עיוור ("מי האדם/הישות מבלי לדעת את שמו?")',
    blindPortraitSub: 'סינתזה הנגזרת אך ורק מתוך הגיאומטריה של אופק, שליט המפה, בתים והיבטים — ללא כל שימוש בשם',
    ascAndMcHeader: '🧭 הצירים הקרדינליים: אופק (Ascendant), שליט המפה ורום שמיים (MC)',
    bigThreeAndBalanceHeader: '⚖️ סינתזת השילוש המרכזי, מאזן יסודות, איכויות והמיספרות',
    patternsHeader: '✨ תבניות גיאומטריות, כוכבים צמודי-ציר וקבלות הדדיות',
    allPlanetsHeader: '🪐 ניתוח מומחה לכל כוכב במזל ובבית (כולל נסיגה Rx וכבוד פלנטרי)',
    allNatalAspectsHeader: '📐 כל ההיבטים הפנימיים במפת הלידה (Natal Aspects)',
    transitsForecastHeader: '🌍 תחזית מעברים אסטרטגית לתאריך',
    transitsHousesHeader: '🏠 מיקום כוכבי השמיים הנוכחיים בבתים האישיים (1–12)',
    transitsAspectsHeader: '⚡ היבטים פעילים בין שמיים נוכחיים למפת הלידה (Transit-to-Natal)',
    interactionSynthesisHeader: '🤝 סינתזת אינטראקציה בין 2 ישויות (אדם + אדם / אדם + חברה / ארגון)',
    overlaysBInAHeader: '🏠 השלכות בתים: היכן כוכבי ישות ב׳ פועלים בתוך בתי החיים של ישות א׳',
    overlaysAInBHeader: '🏠 השלכות בתים: היכן כוכבי ישות א׳ פועלים בתוך בתי החיים של ישות ב׳',
    elonVerifyHeader: '🧪 מבחן אימות עיוור: פיענוח אלגוריתמי של 28.06.1971, 07:30, פרטוריה — מול המציאות המתועדת של אילון מאסק',
    elonColFactor: 'חתימה אסטרולוגית במפה',
    elonColBlind: 'מה האסטרולוג המומחה מסיק בעיוורון מוחלט (ללא ידיעת השם)',
    elonColReality: 'המציאות המתועדת (Elon Musk)',
    retrogradeBadge: 'נסיגה (Rx)',
    directBadge: 'ישיר',

    // Footer
    footerProgram: 'אסטרו-מאץ׳ פרו (AstroMatch Pro) · גרסה {version} · מנוע נתוני נאס״א מדויק · מבוסס Skyfield ו-Python',
    ephemerisFooter: 'מודל נאס״א: NASA DE421 (J2000)'
  },

  en: {
    dir: 'ltr',
    langName: 'English',
    flag: '🇺🇸',
    appTitle: 'AstroMatch Pro',
    engineBadge: 'Pure NASA Ephemeris Engine (v2.5.1)',
    heroSubtitle: 'Professional Astrological Compatibility & Interactive Synastry Wheel Maps. Accurate geocentric ecliptic longitudes via Skyfield & NASA DE421.',
    quickSample: '💫 Quick Sample Match',
    viewSaved: '📁 View Saved Analyses',
    savedCountSuffix: 'Saved',
    helpBtn: '❓ Help & Astrological Guide',
    helpModalTitle: '📖 Professional User & Astrological Guide (v2.5.1)',

    // Partner A & B
    partnerA: 'Partner A',
    partnerB: 'Partner B',
    innerWheel: 'Inner Wheel',
    outerWheel: 'Outer Wheel',
    fullName: 'Full Name or Alias',
    namePlaceholderP1: 'e.g. Alex',
    namePlaceholderP2: 'e.g. Jordan',
    dob: 'Date of Birth',
    exactTime: 'Exact Time',
    cityLabel: 'City / Town of Birth (Worldwide)',
    checkLocation: '🔍 Check Location',
    cityPlaceholder: 'e.g. Ramat Gan, Kiryat Gat, New York, London...',
    cityHelp: 'Enter any city, town, or village worldwide. Checked live against OpenStreetMap and curated coordinates.',
    tzLabel: 'UTC Timezone Offset',
    tzAuto: 'Auto-set from city',
    tzStandardNotice: 'Enter standard time / GMT offset for your location without daylight saving (DST)',

    // Actions & Buttons
    calcBtn: '🔮 Calculate Synastry & Draw Astrological Maps',
    calcBtnLoading: '✨ Computing Celestial Positions...',
    saveBtn: '💾 Save to My Analyses',
    formHint: 'Generates interactive Synastry Bi-Wheel, Natal House Maps, and In-Depth Aspect Interpretations',
    newCalc: '← New Calculation',
    saveToMyAnalyses: '💾 Save to My Analyses',
    exportSvg: '⬇️ Export SVG Map',
    exportPng: '🖼️ Export PNG Map',

    // Saved Analyses
    savedAnalysesTitle: '📁 Saved Analyses & Couple Profiles',
    savedAnalysesSub: 'Select, load, edit, or delete previously saved synastry profiles',
    searchSavedPlaceholder: '🔍 Search saved...',
    refreshBtn: '🔄 Refresh',
    noSavedYet: 'No saved analyses yet.',
    noSavedSub: 'Fill in the form above and click "Save to My Analyses" to store couple profiles.',
    loadIntoForm: '📥 Load into Form',
    editBtn: '✏️ Edit',
    deleteBtn: '🗑️ Delete',
    versionBadge: 'v',

    // Modal Edit
    editModalTitle: '✏️ Edit Saved Analysis',
    editTitleLabel: 'Analysis Title / Label',
    notesLabel: 'Notes / Relationship Context',
    notesPlaceholder: 'Optional notes...',
    cancelBtn: 'Cancel',
    saveChangesBtn: 'Save Changes',

    // Person Profile Management
    chooseSavedPerson: '👤 Choose saved person...',
    personSavedBadge: '✓ Saved',
    personNotSavedBadge: 'Not saved',
    personModifiedBadge: 'Modified',
    savePersonBtn: '💾 Save',
    updatePersonBtn: '💾 Update',
    savePersonTooltip: 'Save this person profile for quick reuse and partner comparisons',
    savedPeopleTitle: '👥 Saved People Profiles',
    savedPeopleSub: 'Individual birth profiles ready to pair and compare against any partner',
    searchPeoplePlaceholder: '🔍 Search people...',
    noSavedPeopleYet: 'No saved people profiles yet.',
    noSavedPeopleSub: 'Enter details in the form above and click "Save" near their name to save for quick reuse.',
    setAsPartnerA: '👤 Set as Partner A',
    setAsPartnerB: '👤 Set as Partner B',
    editPersonTitle: '✏️ Edit Person Profile',
    deletePersonConfirm: 'Are you sure you want to delete profile for',
    personSaveSuccess: '✅ Person profile saved successfully!',

    // Compare & Modify Modal
    editDetailsCompareBtn: '✏️ Edit Details / Compare Partner',
    editCompareModalTitle: '🔮 Modify Birth Details & Compare Partner',
    recalcCompareBtn: '⚡ Recalculate & Compare',
    swapPartnersBtn: '🔄 Swap Partners (A ⇄ B)',

    // Geocoding Badges & Resolution
    checkingLocation: 'Checking location on OpenStreetMap & local database...',
    locationNotFound: 'Location not found:',
    couldNotResolve: 'Could not resolve',
    locationCheckHint: 'Check spelling or specify country/region (e.g. "Ramat Gan, Israel").',
    foundViaCurated: '✓ Found via Curated Database',
    foundViaOsm: '✓ Found via OpenStreetMap',
    suggestedTZ: 'Suggested TZ:',
    resolvedLabel: 'Resolved:',
    coordLabel: 'Coord',
    curatedDatabaseBadge: 'Curated Database',
    osmBadge: 'OpenStreetMap (Live)',

    // Alerts & Confirmations
    fillNamesAlert: 'Please fill in at least Partner A and Partner B names before saving.',
    promptTitle: 'Enter a title for this saved analysis:',
    deleteConfirm: 'Are you sure you want to delete',
    saveSuccess: '✅ Saved to Analyses!',
    enterCityAlert: 'Please enter a city name to verify.',

    // Results Page
    reportSubtitle: 'High-Precision Geocentric Synastry Analysis',
    synastryIndex: 'Synastry Index',
    aspectsCount: 'Aspects',
    compatRating: 'Compatibility Rating',
    soulmatePotential: '✨ Soulmate Potential',
    harmoniousResonance: '💫 Harmonious Resonance',
    dynamicGrowth: '⚡ Dynamic Growth Catalyst',
    romanticChemistry: '🔥 Romantic Chemistry',
    emotionalSafety: '🌊 Emotional Safety & Moon Connection',
    mentalRapport: '💡 Mental Rapport & Communication',
    stabilityScore: '🏛️ Long-term Stability & Saturn Anchors',

    // Big Three & Planet Labels
    sunSign: 'Sun',
    moonSign: 'Moon',
    ascSign: 'ASC Rising',
    planetVenus: 'Venus',
    planetMars: 'Mars',
    coreIdentity: 'Core Identity & Vitality',
    subconscious: 'Subconscious & Instincts',
    outerPersona: 'Outer Persona & Lens',

    // Tabs
    tabBiWheel: '🔮 Interactive Synastry Bi-Wheel',
    tabP1Chart: 'Partner A Natal Chart',
    tabP2Chart: 'Partner B Natal Chart',
    tabAspects: '📜 Detailed Aspect Catalog',

    // Chart Controls & Filters
    wheelControls: 'Wheel Mode:',
    coordSystem: 'Coordinates:',
    coordTropical: 'Tropical (Astro.com)',
    coordJ2000: 'J2000 (Astrometric)',
    coordDescTropical: 'Standard Western Astrology (Apparent Ecliptic of Date) · Matches Astro.com',
    coordDescJ2000: 'IAU Standard Epoch J2000.0 (Astrometric Ecliptic)',
    planetTableTitle: 'Planetary Data',
    aspectGridTitle: 'Aspect Grid',
    aspectFilters: 'Aspect Filters:',
    showAspectLines: 'Show Aspect Lines',
    equalHouses: 'Equal Houses',
    filterAll: 'All',
    filterConjunction: '🟡 Conjunctions (0°)',
    filterTrine: '🟢 Trines (120°)',
    filterSextile: '🔵 Sextiles (60°)',
    filterSquare: '🔴 Squares (90°)',
    filterOpposition: '🟣 Oppositions (180°)',
    filterHarmonious: 'Harmonious',
    filterChallenging: 'Dynamic / Friction',
    harmoniousFlow: '● Harmonious Flow',
    dynamicCatalyst: '● Dynamic Catalyst',
    chartHint: '💡 Hover over any planet glyph or aspect line to view exact degrees, house placements, and astrological interpretations.',
    aspectSubtitle: 'Detailed geometric angular relationships between charts',

    // SVG Center Labels
    matchLabel: 'MATCH',
    synastryLabel: 'SYNASTRY',
    natalMapLabel: 'NATAL MAP',
    biWheelModeLabel: 'Synastry Bi-Wheel',
    innerLabel: 'Inner',
    outerLabel: 'Outer',
    orbLabel: 'Orb',
    tightnessLabel: 'Tightness',

    // Zodiac Signs
    zodiac: {
      Aries: 'Aries',
      Taurus: 'Taurus',
      Gemini: 'Gemini',
      Cancer: 'Cancer',
      Leo: 'Leo',
      Virgo: 'Virgo',
      Libra: 'Libra',
      Scorpio: 'Scorpio',
      Sagittarius: 'Sagittarius',
      Capricorn: 'Capricorn',
      Aquarius: 'Aquarius',
      Pisces: 'Pisces'
    },

    // Planets
    planets: {
      Sun: 'Sun',
      Moon: 'Moon',
      Mercury: 'Mercury',
      Venus: 'Venus',
      Mars: 'Mars',
      Jupiter: 'Jupiter',
      Saturn: 'Saturn',
      Uranus: 'Uranus',
      Neptune: 'Neptune',
      Pluto: 'Pluto',
      Ascendant: 'Ascendant (ASC)',
      Midheaven: 'Midheaven (MC)',
      'North Node': 'North Node (☊)'
    },

    // Aspects
    aspectNames: {
      Conjunction: 'Conjunction',
      Trine: 'Trine',
      Sextile: 'Sextile',
      Square: 'Square',
      Opposition: 'Opposition'
    },

    // Elements
    elements: {
      Fire: 'Fire',
      Earth: 'Earth',
      Air: 'Air',
      Water: 'Water',
      fire: 'Fire',
      earth: 'Earth',
      air: 'Air',
      water: 'Water'
    },

    // Score Verdicts (Synastry & Transits)
    scoreVerdicts: {
      verdict_85: 'Exceptional Cosmic Affinity: Rare magnetic harmony with deep mutual understanding and lasting soul connection.',
      verdict_70: 'High Astrological Resonance: Natural chemistry and supportive aspects outshine minor differences.',
      verdict_55: 'Dynamic & Complementary Bond: Meaningful passion paired with growth opportunities that require conscious empathy.',
      verdict_0: 'Karmic Growth Catalyst: Intense friction and distinct temperaments; great personal transformation if communication is nurtured.',
      transit_high_alignment: 'Peak Cosmic Momentum: Highly supportive transit angles trigger your core natal configuration, creating rare windows for decisive strategic advancement, luck, and recognition.',
      transit_positive_flow: 'Dynamic Astrological Alignment: Solid planetary tailwinds support proactive endeavors. Favorable transit aspects outshine temporary pressures.',
      transit_growth_catalyst: 'Constructive Tension & Transformation: Active transit challenges push you beyond comfort zones, testing endurance and demanding strategic adaptability.',
      transit_recalibration: 'Karmic Consolidation & Focus: Planetary friction calls for inner discipline, reflection, and careful conservation of vital resources before launching major new ventures.'
    },

    // Single-Entity Transit Resonance & Filtering Keys
    transitResonanceIndex: 'Cosmic Transit Resonance Index',
    transitAlignmentTitle: 'Current Sky Transit Alignment',
    activeTransitMomentum: 'Active Transit Momentum',
    singleReportSubtitle: 'High-Precision Geocentric Natal Chart & Current Date Transit Analysis',
    transitWeatherTitle: 'Astrological Transits',
    currentSkyPositions: '🌍 Current Sky Planetary Positions',
    filterAllAnalyses: 'All',
    filterSingleTransits: '👤 Single & Transits',
    filterCoupleSynastry: '👥 Couples & Synastry',
    snapshotBadgeSingle: 'Single & Transits',
    snapshotBadgePair: 'Couple Synastry',
    saveTransitSnapshot: '📸 Save Transit Snapshot',
    activeMomentum: '⚡ Active Transit Momentum',
    mentalClarity: '💡 Mental Focus & Clarity',
    emotionalBalance: '🌊 Emotional Grounding & Balance',
    resilienceSaturn: '🏛️ Resilience & Structural Discipline',
    executiveAmbition: '🚀 Executive Drive & Ambition',
    opportunityFlow: '💎 Resource & Opportunity Flow',

    // Detailed Aspect Interpretations
    aspectMeanings: {
      "Sun-Moon-Conjunction": "The celestial marriage aspect. Effortless soul-level mutual understanding, deep emotional harmony, and instinctive alignment.",
      "Sun-Moon-Trine": "Natural, fluid resonance between ego and emotions. You instinctively validate and comfort each other's inner worlds.",
      "Sun-Moon-Sextile": "Friendly, cooperative affinity. You communicate intentions cleanly and support one another's life growth.",
      "Sun-Moon-Opposition": "Intense magnetic polarity. Profound attraction mixed with distinct worldviews; creates growth through complementary differences.",
      "Sun-Moon-Square": "Creative tension between will and vulnerability. Requires conscious empathy to bridge differing emotional temperaments.",

      "Venus-Mars-Conjunction": "Electric physical attraction and raw romantic magnetism. Immediate spark with powerful sensual chemistry.",
      "Venus-Mars-Trine": "Golden romantic flow. Seduction, desire, and affection align effortlessly, creating sustained passion without hostility.",
      "Venus-Mars-Sextile": "Playful, spirited chemistry. Flirtatious ease with natural appreciation for each other's romantic style.",
      "Venus-Mars-Square": "High-octane sexual friction. Hot, fiery, and intoxicating passion that demands constructive channels to prevent petty clashes.",
      "Venus-Mars-Opposition": "Irresistible magnetic pull across polar opposites. The chase is exhilarating, though balancing affection and ego takes patience.",

      "Venus-Venus-Conjunction": "Shared aesthetic tastes, love languages, and social rhythms. You experience joy and luxury through the same lens.",
      "Venus-Venus-Trine": "Effortless tenderness and reciprocal affection. A deeply soothing bond that softens daily stress.",
      "Venus-Venus-Square": "Contrasting affection styles or differing spending/social habits. Fun and stimulating once you embrace varied tastes.",

      "Moon-Moon-Conjunction": "Telepathic emotional kinship. You feel like 'home' to one another and mirror each other's vulnerabilities.",
      "Moon-Moon-Trine": "Profound emotional safety, tenderness, and intuitive trust. You naturally nurture each other.",
      "Moon-Moon-Square": "Differing domestic habits and emotional processing speeds. Demands gentle listening and spacious boundaries.",
      "Moon-Moon-Opposition": "Emotional seesaw that builds deep awareness. One acts as the anchor while the other expresses, swapping instinctively.",

      "Sun-Sun-Trine": "Harmonious core values, mutual admiration, and shared vision of purposeful living.",
      "Sun-Sun-Conjunction": "Powerful vitality and shared spotlight. You energize one another, though space for individual sovereignty is essential.",
      "Sun-Sun-Square": "Dynamic challenge of wills. Strong personalities push each other toward peak ambition, provided competition is kept healthy.",
      "Sun-Sun-Opposition": "Fascinating mirror dynamic. Each partner sees unexpressed parts of themselves reflected in the other.",

      "Mercury-Mercury-Conjunction": "Rapid mental wavelength synchronization. Hours vanish in conversation as your thought patterns finish each other's sentences.",
      "Mercury-Mercury-Trine": "Stimulating intellectual rapport. Collaboration on creative, analytical, or practical projects flows with ease.",
      "Mercury-Mercury-Square": "Spirited debates and differing communication cadences. Highly stimulating, though active listening is key to avoid misunderstandings.",

      "Jupiter-Sun-Trine": "Abundant good fortune, optimism, and generous mutual encouragement. You expand each other's horizons and luck.",
      "Jupiter-Moon-Trine": "Heartwarming warmth, humor, and psychological comfort. A relationship imbued with good cheer and forgiveness.",
      "Saturn-Sun-Trine": "Bedrock of enduring commitment, loyalty, and mutual respect. Built to withstand time and real-world trials.",
      "Saturn-Venus-Trine": "Unshakable fidelity and grounded love. Affection deepens into lasting mutual loyalty and shared responsibility.",
      "Saturn-Venus-Square": "Heavy karmic lessons regarding trust and timing. Affection may feel cautious, but matures with dedication.",
      "Pluto-Venus-Conjunction": "Profound, transformative passion with obsessive or hypnotic intensity. Love that leaves neither partner unchanged.",
      "Pluto-Venus-Trine": "Deep emotional and physical depth. Passion that renews and heals past heartaches through total trust.",
      "Neptune-Venus-Trine": "Poetic, fairytale romance and unconditional artistic or spiritual devotion.",
      "Uranus-Venus-Trine": "Exciting, unconventional romantic electricity. Zero boredom, high personal freedom, and electric chemistry."
    },

    // Expert Astrologist v2.5.0 Keys (English)
    loadElonBtn: '🧪 Load Blind Test: Elon Musk + SpaceX',
    loadElonTeslaBtn: '⚡ Elon Musk + Tesla',
    entitySubtitleHint: 'Supports People, Companies, Organizations & Historical Events · Leave Entity B blank to analyze against Current Sky Transits',
    transitBarTitle: '🌍 Current / Transit Reference Date & Time',
    transitBarSub: 'Computes real-time sky positions on the selected date and their transits through natal houses & planets',
    transitDateLabel: 'Transit Date (Default: Today)',
    transitTimeLabel: 'Transit Time',
    resetTodayBtn: '📅 Today',
    blindModeToggle: '🕵️ Blind Mode (Hide Names & Deduce Purely from Chart)',
    blindModeActive: '🕵️ Blind Mode Active — Deduced Purely from Chart Math!',
    blindEntityA: 'Blind Subject A',
    blindEntityB: 'Blind Subject B',
    powerScore: '⚡ Executive Power & Drive',
    wealthScore: '💎 Wealth & Resource Flow',
    mcSign: 'Midheaven (MC)',
    northNodeSign: 'North Node (☊)',
    chartRulerLabel: 'Chart Ruler (ASC)',
    mcRulerLabel: 'MC Ruler (10th)',
    tabTransitsP1: '🌍 Current Transits - Entity A',
    tabTransitsP2: '🌍 Current Transits - Entity B',
    expertHubTitle: '🧙‍♂️ Multi-Dimensional Expert Astrologist Dossier',
    expertHubSubtitle: 'Deep analysis of Ascendant & Chart Ruler, Midheaven, Blind Portrait, Elemental Balance, All Natal Aspects, Current Date Transits & 2-Entity House Overlays',
    expertTabNatalP1: '🌟 Deep Natal & Blind Portrait - A',
    expertTabNatalP2: '🌟 Deep Natal & Blind Portrait - B',
    expertTabTransits: '🌍 Current Date Transits & Forecast',
    expertTabInteraction: '🤝 2-Entity Interaction & House Overlays',
    expertTabElonVerify: '🧪 Blind Verification: Elon Musk (Chart vs Reality)',
    blindPortraitHeader: '🕵️ Blind Portrait ("Who Is This Without Knowing Their Name?")',
    blindPortraitSub: 'Synthesized strictly from Ascendant, Chart Ruler, Houses, Dignities, and Aspect Geometry — zero name knowledge used',
    ascAndMcHeader: '🧭 Cardinal Axes: Ascendant (Rising Sign), Chart Ruler & Midheaven (MC)',
    bigThreeAndBalanceHeader: '⚖️ Big Three Synthesis, Elemental, Modal & Hemisphere Balance',
    patternsHeader: '✨ Geometric Patterns, Angular Planets & Mutual Receptions',
    allPlanetsHeader: '🪐 Expert Planet-by-Planet in Sign & House (with Retrograde Rx & Essential Dignities)',
    allNatalAspectsHeader: '📐 Complete Natal Aspects Catalog & Psychological Mechanics',
    transitsForecastHeader: '🌍 Executive Transit Forecast for',
    transitsHousesHeader: '🏠 Current Sky Planets Transiting Natal Houses (1–12)',
    transitsAspectsHeader: '⚡ Active Transit-to-Natal Aspects (Current Sky ⇄ Birth Chart)',
    interactionSynthesisHeader: '🤝 2-Entity Interaction Synthesis (Person + Person / Person + Company / Organization)',
    overlaysBInAHeader: '🏠 House Overlays: Where Entity B’s Planets Activate Entity A’s Houses',
    overlaysAInBHeader: '🏠 House Overlays: Where Entity A’s Planets Activate Entity B’s Houses',
    elonVerifyHeader: '🧪 Blind Verification Case Study: Algorithmic Deduction of 1971-06-28 07:30 Pretoria vs. Documented Reality of Elon Musk',
    elonColFactor: 'Astrological Chart Signature',
    elonColBlind: 'Blind Expert Deduction (Zero Knowledge of Identity)',
    elonColReality: 'Documented Real-World Reality (Elon Musk)',
    retrogradeBadge: 'Retrograde (Rx)',
    directBadge: 'Direct',

    // Footer
    footerProgram: 'AstroMatch Pro · Version {version} · Pure NASA Ephemeris Engine · Built with Skyfield & Python',
    ephemerisFooter: 'Ephemeris: NASA DE421 (J2000)'
  }
};

/**
 * Get current active language key ('en' or 'he')
 */
export function getCurrentLang() {
  const saved = localStorage.getItem('astromatch_lang');
  if (saved && TRANSLATIONS[saved]) return saved;
  return 'en';
}

/**
 * Get string translation helper
 */
export function t(key, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  return dict[key] !== undefined ? dict[key] : (TRANSLATIONS.en[key] !== undefined ? TRANSLATIONS.en[key] : key);
}

/**
 * Get planet translated name
 */
export function tPlanet(planetName, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  return (dict.planets && dict.planets[planetName]) || planetName;
}

/**
 * Get zodiac translated name
 */
export function tZodiac(signName, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  return (dict.zodiac && dict.zodiac[signName]) || signName;
}

/**
 * Get element translated name
 */
export function tElement(elementName, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  return (dict.elements && dict.elements[elementName]) || elementName;
}

/**
 * Get aspect translated name
 */
export function tAspect(aspectName, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  return (dict.aspectNames && dict.aspectNames[aspectName]) || aspectName;
}

/**
 * Get aspect interpretation translated
 */
export function tAspectMeaning(aspectItem, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  
  if (!aspectItem) return '';
  const key = aspectItem.aspect_key;
  if (key && dict.aspectMeanings && dict.aspectMeanings[key]) {
    return dict.aspectMeanings[key];
  }

  // Check reversed pair keys
  const p1 = aspectItem.p1_planet;
  const p2 = aspectItem.p2_planet;
  const asp = aspectItem.aspect;
  const k1 = `${p1}-${p2}-${asp}`;
  const k2 = `${p2}-${p1}-${asp}`;
  if (dict.aspectMeanings && dict.aspectMeanings[k1]) return dict.aspectMeanings[k1];
  if (dict.aspectMeanings && dict.aspectMeanings[k2]) return dict.aspectMeanings[k2];

  // Generic fallback translation
  if (activeLang === 'he') {
    const aspHe = tAspect(asp, 'he');
    const p1He = tPlanet(p1, 'he');
    const p2He = tPlanet(p2, 'he');
    return `חיבור פלנטרי דינמי: היבט ${aspHe} בין ${p1He} ל-${p2He} יוצר תחלופת אנרגיה פעילה והשפעה הדדית משמעותית.`;
  }
  return aspectItem.meaning || `Dynamic planetary link: ${asp} between ${p1} and ${p2} creates active energy exchange.`;
}

/**
 * Get score summary verdict translated
 */
export function tVerdict(verdictKey, defaultVerdict, lang = null) {
  const activeLang = lang || getCurrentLang();
  const dict = TRANSLATIONS[activeLang] || TRANSLATIONS.en;
  if (verdictKey && dict.scoreVerdicts && dict.scoreVerdicts[verdictKey]) {
    return dict.scoreVerdicts[verdictKey];
  }
  return defaultVerdict || '';
}

/**
 * Apply selected language across DOM
 */
export function applyLanguage(lang) {
  if (!TRANSLATIONS[lang]) lang = 'en';
  localStorage.setItem('astromatch_lang', lang);

  const config = TRANSLATIONS[lang];
  document.documentElement.lang = lang;
  document.documentElement.dir = config.dir;

  // 1. Update elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    let text = config[key];
    if (text === undefined && TRANSLATIONS.en[key] !== undefined) {
      text = TRANSLATIONS.en[key];
    }
    if (text !== undefined) {
      const version = el.getAttribute('data-version') || window.APP_VERSION || '2.2.0';
      text = text.replace('{version}', version);
      el.innerHTML = text;
    }
  });

  // 2. Update input placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    const text = config[key] !== undefined ? config[key] : TRANSLATIONS.en[key];
    if (text !== undefined) {
      el.setAttribute('placeholder', text);
    }
  });

  // 3. Update titles
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    const key = el.getAttribute('data-i18n-title');
    const text = config[key] !== undefined ? config[key] : TRANSLATIONS.en[key];
    if (text !== undefined) {
      el.setAttribute('title', text);
    }
  });

  // 4. Update Synastry Score Summary Verdict
  const verdictEl = document.getElementById('synastryVerdictText');
  if (verdictEl) {
    const vKey = verdictEl.getAttribute('data-verdict-key');
    const defV = verdictEl.getAttribute('data-default-verdict');
    verdictEl.textContent = tVerdict(vKey, defV, lang);
  }

  // 5. Update Planet Position strings on Partner Cards
  document.querySelectorAll('.planet-pos').forEach(el => {
    const rawFormatted = el.getAttribute('data-formatted') || '';
    const sign = el.getAttribute('data-sign');
    const symbol = el.getAttribute('data-symbol') || '';
    const deg = el.getAttribute('data-deg');
    const minVal = el.getAttribute('data-min');

    if ((deg === null || deg === undefined || deg === '') && rawFormatted) {
      el.textContent = rawFormatted;
      return;
    }

    const min = (minVal !== null && minVal !== undefined && minVal !== '') ? String(minVal).padStart(2, '0') : '00';
    const signTranslated = tZodiac(sign, lang);
    if (lang === 'he') {
      el.innerHTML = `${signTranslated} <span style="color: inherit;">${symbol}</span> <span dir="ltr" style="display:inline-block;">${deg}° ${min}'</span>`;
    } else {
      el.innerHTML = `<span dir="ltr" style="display:inline-block;">${deg}° ${min}'</span> <span style="color: inherit;">${symbol}</span> ${signTranslated}`;
    }
  });

  // 6. Update Location Source Badges
  document.querySelectorAll('.location-source-badge').forEach(el => {
    const src = el.getAttribute('data-source') || '';
    if (src === 'Curated Database') {
      el.textContent = t('curatedDatabaseBadge', lang);
    } else if (src.includes('Nominatim') || src.includes('OpenStreetMap')) {
      el.textContent = t('osmBadge', lang);
    } else {
      el.textContent = src;
    }
  });

  // 7. Update Natal Map Tab Buttons
  document.querySelectorAll('.tab-natal-btn').forEach(btn => {
    const pName = btn.getAttribute('data-name');
    const partner = btn.getAttribute('data-partner');
    const icon = partner === 'p1' ? '🪐' : '🌙';
    if (lang === 'he') {
      btn.textContent = `${icon} מפת לידה: ${pName}`;
    } else {
      btn.textContent = `${icon} ${pName}'s Natal Map`;
    }
  });

  // 8. Update Aspect Catalog Cards (bottom section)
  document.querySelectorAll('.aspect-pair-header').forEach(el => {
    const p1Name = el.getAttribute('data-p1-name');
    const p1Planet = el.getAttribute('data-p1-planet');
    const p1Sym = el.getAttribute('data-p1-sym') || '';
    const p2Name = el.getAttribute('data-p2-name');
    const p2Planet = el.getAttribute('data-p2-planet');
    const p2Sym = el.getAttribute('data-p2-sym') || '';

    const p1PTranslated = tPlanet(p1Planet, lang);
    const p2PTranslated = tPlanet(p2Planet, lang);

    if (lang === 'he') {
      el.innerHTML = `
        <span class="fw-bold" style="color: var(--p1-color)">${p1Sym} ${p1PTranslated} של ${p1Name}</span>
        <span class="text-secondary">✕</span>
        <span class="fw-bold" style="color: var(--p2-color)">${p2Sym} ${p2PTranslated} של ${p2Name}</span>
      `;
    } else {
      el.innerHTML = `
        <span class="fw-bold" style="color: var(--p1-color)">${p1Name}'s ${p1Sym} ${p1PTranslated}</span>
        <span class="text-secondary">✕</span>
        <span class="fw-bold" style="color: var(--p2-color)">${p2Name}'s ${p2Sym} ${p2PTranslated}</span>
      `;
    }
  });

  document.querySelectorAll('.aspect-badge-name').forEach(el => {
    const asp = el.getAttribute('data-aspect');
    const angle = el.getAttribute('data-angle');
    el.textContent = `${tAspect(asp, lang)} (${angle}°)`;
  });

  document.querySelectorAll('.aspect-meaning-text').forEach(el => {
    const key = el.getAttribute('data-aspect-key');
    const p1Planet = el.getAttribute('data-p1-planet');
    const p2Planet = el.getAttribute('data-p2-planet');
    const asp = el.getAttribute('data-aspect');
    const defMeaning = el.getAttribute('data-default-meaning');
    const item = { aspect_key: key, p1_planet: p1Planet, p2_planet: p2Planet, aspect: asp, meaning: defMeaning };
    el.textContent = tAspectMeaning(item, lang);
  });

  document.querySelectorAll('.aspect-orb-text').forEach(el => {
    const orb = el.getAttribute('data-orb');
    const tightness = el.getAttribute('data-tightness');
    if (lang === 'he') {
      el.innerHTML = `סטייה (Orb): <strong class="text-white">${orb}°</strong> (דיוק: ${tightness}%)`;
    } else {
      el.innerHTML = `Orb: <strong class="text-white">${orb}°</strong> (Tightness: ${tightness}%)`;
    }
  });

  document.querySelectorAll('.aspect-nature-tag').forEach(el => {
    const nature = el.getAttribute('data-nature');
    if (nature === 'harmonious') {
      el.innerHTML = `<span class="text-success">${t('harmoniousFlow', lang)}</span>`;
    } else {
      el.innerHTML = `<span class="text-danger">${t('dynamicCatalyst', lang)}</span>`;
    }
  });

  // 9. Update Footer Ephemeris Badge
  const ephemEl = document.getElementById('footerEphemerisText');
  if (ephemEl) {
    ephemEl.textContent = t('ephemerisFooter', lang);
  }

  // 10. Update Language Toggle Button
  const toggleBtn = document.getElementById('langToggleBtn');
  if (toggleBtn) {
    const nextLang = lang === 'he' ? 'en' : 'he';
    const nextConfig = TRANSLATIONS[nextLang];
    toggleBtn.innerHTML = `🌐 ${nextConfig.langName} (${nextLang.toUpperCase()})`;
    toggleBtn.setAttribute('title', `Switch to ${nextConfig.langName}`);
  }

  // 11. Dispatch custom event for dynamic components (like interactive SVG wheels)
  window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang, config } }));
}

/**
 * Toggle language between English and Hebrew
 */
export function toggleLanguage() {
  const current = getCurrentLang();
  const next = current === 'he' ? 'en' : 'he';
  applyLanguage(next);
}

// Global window exposure for browser compatibility without bundlers
if (typeof window !== 'undefined') {
  window.TRANSLATIONS = TRANSLATIONS;
  window.getCurrentLang = getCurrentLang;
  window.t = t;
  window.tPlanet = tPlanet;
  window.tZodiac = tZodiac;
  window.tElement = tElement;
  window.tAspect = tAspect;
  window.tAspectMeaning = tAspectMeaning;
  window.tVerdict = tVerdict;
  window.applyLanguage = applyLanguage;
  window.toggleLanguage = toggleLanguage;
}
