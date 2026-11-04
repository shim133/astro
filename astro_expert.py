"""
AstroMatch Pro - Expert Astrologist Synthesis, Natal Dossier, Transits & Entity Interaction Engine
Pure-Python astrological interpretation engine supporting Bilingual (English & Hebrew) output.
"""

SIGN_RULERS = {
    "Aries": {"traditional": "Mars", "modern": "Mars"},
    "Taurus": {"traditional": "Venus", "modern": "Venus"},
    "Gemini": {"traditional": "Mercury", "modern": "Mercury"},
    "Cancer": {"traditional": "Moon", "modern": "Moon"},
    "Leo": {"traditional": "Sun", "modern": "Sun"},
    "Virgo": {"traditional": "Mercury", "modern": "Mercury"},
    "Libra": {"traditional": "Venus", "modern": "Venus"},
    "Scorpio": {"traditional": "Mars", "modern": "Pluto"},
    "Sagittarius": {"traditional": "Jupiter", "modern": "Jupiter"},
    "Capricorn": {"traditional": "Saturn", "modern": "Saturn"},
    "Aquarius": {"traditional": "Saturn", "modern": "Uranus"},
    "Pisces": {"traditional": "Jupiter", "modern": "Neptune"},
}

SIGN_META = {
    "Aries": {"element": "Fire", "quality": "Cardinal", "he": "טלה", "element_he": "אש", "quality_he": "יוזם (קרדינלי)"},
    "Taurus": {"element": "Earth", "quality": "Fixed", "he": "שור", "element_he": "אדמה", "quality_he": "קבוע"},
    "Gemini": {"element": "Air", "quality": "Mutable", "he": "תאומים", "element_he": "אוויר", "quality_he": "משתנה"},
    "Cancer": {"element": "Water", "quality": "Cardinal", "he": "סרטן", "element_he": "מים", "quality_he": "יוזם (קרדינלי)"},
    "Leo": {"element": "Fire", "quality": "Fixed", "he": "אריה", "element_he": "אש", "quality_he": "קבוע"},
    "Virgo": {"element": "Earth", "quality": "Mutable", "he": "בתולה", "element_he": "אדמה", "quality_he": "משתנה"},
    "Libra": {"element": "Air", "quality": "Cardinal", "he": "מאזניים", "element_he": "אוויר", "quality_he": "יוזם (קרדינלי)"},
    "Scorpio": {"element": "Water", "quality": "Fixed", "he": "עקרב", "element_he": "מים", "quality_he": "קבוע"},
    "Sagittarius": {"element": "Fire", "quality": "Mutable", "he": "קשת", "element_he": "אש", "quality_he": "משתנה"},
    "Capricorn": {"element": "Earth", "quality": "Cardinal", "he": "גדי", "element_he": "אדמה", "quality_he": "יוזם (קרדינלי)"},
    "Aquarius": {"element": "Air", "quality": "Fixed", "he": "דלי", "element_he": "אוויר", "quality_he": "קבוע"},
    "Pisces": {"element": "Water", "quality": "Mutable", "he": "דגים", "element_he": "מים", "quality_he": "משתנה"},
}

PLANET_HE = {
    "Sun": "שמש",
    "Moon": "ירח",
    "Mercury": "מרקורי (כוכב חמה)",
    "Venus": "ונוס (נוגה)",
    "Mars": "מארס (מאדים)",
    "Jupiter": "יופיטר (צדק)",
    "Saturn": "סטורן (שבתאי)",
    "Uranus": "אורנוס",
    "Neptune": "נפטון",
    "Pluto": "פלוטו",
    "North Node": "ראש הדרקון (North Node)",
    "Ascendant": "אופק (ASC)",
    "Midheaven": "רום שמיים (MC)",
}

ESSENTIAL_DIGNITIES = {
    "Sun": {"domicile": ["Leo"], "exaltation": ["Aries"], "detriment": ["Aquarius"], "fall": ["Libra"]},
    "Moon": {"domicile": ["Cancer"], "exaltation": ["Taurus"], "detriment": ["Capricorn"], "fall": ["Scorpio"]},
    "Mercury": {"domicile": ["Gemini", "Virgo"], "exaltation": ["Virgo"], "detriment": ["Sagittarius", "Pisces"], "fall": ["Pisces"]},
    "Venus": {"domicile": ["Taurus", "Libra"], "exaltation": ["Pisces"], "detriment": ["Scorpio", "Aries"], "fall": ["Virgo"]},
    "Mars": {"domicile": ["Aries", "Scorpio"], "exaltation": ["Capricorn"], "detriment": ["Libra", "Taurus"], "fall": ["Cancer"]},
    "Jupiter": {"domicile": ["Sagittarius", "Pisces"], "exaltation": ["Cancer"], "detriment": ["Gemini", "Virgo"], "fall": ["Capricorn"]},
    "Saturn": {"domicile": ["Capricorn", "Aquarius"], "exaltation": ["Libra"], "detriment": ["Cancer", "Leo"], "fall": ["Aries"]},
    "Uranus": {"domicile": ["Aquarius"], "exaltation": ["Scorpio"], "detriment": ["Leo"], "fall": ["Taurus"]},
    "Neptune": {"domicile": ["Pisces"], "exaltation": ["Cancer"], "detriment": ["Virgo"], "fall": ["Capricorn"]},
    "Pluto": {"domicile": ["Scorpio"], "exaltation": ["Aries", "Leo"], "detriment": ["Taurus"], "fall": ["Libra"]},
}

ASCENDANT_INTERPRETATIONS = {
    "Aries": {
        "en": "Aries Rising projects raw pioneering courage, directness, and an unmistakable warrior presence. Life is approached as a series of conquests and first-principles challenges requiring immediate action and fearlessness.",
        "he": "אופק טלה מקרין אומץ חלוצי, ישירות בלתי מתפשרת ונוכחות לוחמנית בולטת. הגישה לחיים היא כאל רצף של אתגרים ופריצות דרך הדורשים יוזמה מיידית, מהירות והיעדר פחד."
    },
    "Taurus": {
        "en": "Taurus Rising radiates grounded stability, material endurance, and calm sensory authority. This entity moves deliberately, building unshakable physical and financial foundations that outlast competitors.",
        "he": "אופק שור מקרין יציבות מעשית, כוח התמדה חומרי וסמכות שקטה. תנועה מחושבת הבונה יסודות פיזיים וכלכליים איתנים העומדים במבחן הזמן."
    },
    "Gemini": {
        "en": "Gemini Rising interfaces with the world through curiosity, rapid intellectual synthesis, and verbal agility. Versatile and multi-threaded, this persona thrives on information networks and constant mental stimulation.",
        "he": "אופק תאומים פוגש את העולם דרך סקרנות אינטלקטואלית, סינתזה מהירה של מידע וגמישות תקשורתית. אישיות רב-תחומית המשגשגת ברשתות מידע ובגירוי מנטלי מתמיד."
    },
    "Cancer": {
        "en": "Cancer Rising combines a protective, self-contained outer shell with fierce cardinal initiative around security, tribe, or existential preservation. While appearing guarded or deeply intuitive on the surface, when a core mission is adopted, Cancer Rising defends and nurtures its 'ark' or vision with tenacious, maternal/paternal ferocity.",
        "he": "אופק סרטן משלב שריון חיצוני מגונן ומופנם עם יוזמה קרדינלית עזה סביב ביטחון, בית או שימור קיומי. למרות חזות אינטואיטיבית או שמורה, כאשר מאומצת משימת-על, אופק סרטן מגן ומטפח את החזון או ה'תיבה' שלו בנחישות טוטאלית."
    },
    "Leo": {
        "en": "Leo Rising commands the stage with solar magnetism, dramatic flair, and natural royal authority. Built to lead visibly, inspire loyalty, and leave an unmistakable personal signature on everything touched.",
        "he": "אופק אריה תופס את מרכז הבמה במגנטיות שמשית, נוכחות כריזמטית וסמכות מלכותית טבעית. בנוי להנהיג בגלוי, לעורר השראה ולהטביע חותם אישי עוצמתי."
    },
    "Virgo": {
        "en": "Virgo Rising approaches reality through precision engineering, sharp discernment, and relentless optimization. Nothing escapes notice; flaws in systems are spotted immediately and systematically refined.",
        "he": "אופק בתולה ניגש למציאות דרך דיוק הנדסי, הבחנה חדה ואופטימיזציה בלתי פוסקת. שום פרט אינו חומק מהעין; כשלים במערכות מזוהים מיד ומשופרים בשיטתיות."
    },
    "Libra": {
        "en": "Libra Rising projects diplomatic grace, aesthetic sophistication, and strategic partnership orientation. Skilled at reading social dynamics, negotiating alliances, and shaping harmonious architectures.",
        "he": "אופק מאזניים מקרין תחכום אסתטי, דיפלומטיה ואוריינטציה אסטרטגית לשותפויות. מיומן בקריאת המפה החברתית, יצירת בריתות ועיצוב מערכות מאוזנות."
    },
    "Scorpio": {
        "en": "Scorpio Rising possesses X-ray psychological intensity, strategic secrecy, and formidable willpower. Immune to superficiality, this persona commands respect and thrives in high-stakes crises or total transformation.",
        "he": "אופק עקרב ניחן בעוצמה פסיכולוגית חודרת, חשאיות אסטרטגית וכוח רצון אדיר. חסין לשטחיות, מעורר יראת כבוד ומשגשג במשברים ובמצבי קצה הדורשים טרנספורמציה."
    },
    "Sagittarius": {
        "en": "Sagittarius Rising radiates boundless exploration, philosophical boldness, and grand-scale optimism. Driven by a quest for distant horizons, global expansion, and audacious future possibilities.",
        "he": "אופק קשת מקרין רוח מחקר חסרת גבולות, תעוזה פילוסופית ואופטימיות רחבת-היקף. מונע מדחף לכיבוש אופקים רחוקים, התרחבות גלובלית וחזון נועז."
    },
    "Capricorn": {
        "en": "Capricorn Rising projects executive gravitas, stoic discipline, and master-builder ambition. Early challenges forge an iron spine capable of climbing the steepest institutional or industrial mountains.",
        "he": "אופק גדי מקרין כובד ראש ניהולי, משמעת עצמית ושאפתנות של בונה-אימפריות. אתגרים מוקדמים מחשלים עמוד שדרה מפלדה המסוגל להעפיל לפסגות הגבוהות ביותר."
    },
    "Aquarius": {
        "en": "Aquarius Rising operates as an iconoclastic futurist, standing slightly outside convention to re-architect the collective future. Original, egalitarian yet fiercely independent, and wired for innovation.",
        "he": "אופק דלי פועל כעתידן שובר-מוסכמות, העומד מחוץ לעדר כדי לתכנן מחדש את פני העתיד. מקורי, עצמאי לחלוטין ומחווט לחדשנות טכנולוגית וחברתית."
    },
    "Pisces": {
        "en": "Pisces Rising moves with chameleon-like adaptability, visionary imagination, and deep empathic permeability. Capable of channeling collective dreams, artistic currents, and transcendent ideals.",
        "he": "אופק דגים נע בגמישות על-חושית, דמיון חזוני ורגישות אמפתית עמוקה. מסוגל לתעל חלומות קולקטיביים, זרמים תת-הכרתיים ואידיאלים נשגבים."
    },
}

MC_INTERPRETATIONS = {
    "Aries": {
        "en": "Midheaven in Aries (10th House Cusp): Public destiny and career demand fearless pioneering, being 'first' into uncharted territory, and autonomous leadership. Rather than following established corporate ladders, this entity is wired to launch bold, combative, first-principles crusades.",
        "he": "רום שמיים (MC) בטלה: הייעוד הציבורי והקריירה דורשים חלוציות חסרת פחד, הובלה כ'ראשון' בטריטוריות לא ממופות ומנהיגות עצמאית. במקום לטפס בסולם קיים, הישות בנויה להוביל מסעות כיבוש ופריצות דרך מאפס."
    },
    "Taurus": {
        "en": "Midheaven in Taurus: Vocation centers on building tangible, enduring economic value, real assets, infrastructure, or luxury craftsmanship with unshakable financial permanence.",
        "he": "רום שמיים בשור: הייעוד המקצועי מתמקד בבניית ערך כלכלי מוחשי ומתמשך, נכסים ריאליים, תשתיות ויציבות פיננסית בלתי מתפשרת."
    },
    "Gemini": {
        "en": "Midheaven in Gemini: Public reputation is built on communication, media, software/information networks, commerce, and intellectual versatility.",
        "he": "רום שמיים בתאומים: המוניטין והקריירה נבנים סביב תקשורת, מדיה, רשתות מידע, מסחר ורב-תחומיות אינטלקטואלית."
    },
    "Cancer": {
        "en": "Midheaven in Cancer: Public mission connects deeply with foundational human needs, housing, homeland security, nourishment, or creating a protective umbrella for the public.",
        "he": "רום שמיים בסרטן: השליחות הציבורית מתחברת לצרכים קיומיים בסיסיים, הגנה, בית, ביטחון או יצירת מעטפת מגוננת לקולקטיב."
    },
    "Leo": {
        "en": "Midheaven in Leo: Destiny calls for iconic leadership, executive command, creative showmanship, and standing unmistakably in the global spotlight.",
        "he": "רום שמיים באריה: הייעוד קורא למנהיגות אייקונית, פיקוד פרונטלי, יצירתיות בולטת ועמידה טבעית באור הזרקורים."
    },
    "Virgo": {
        "en": "Midheaven in Virgo: Professional authority stems from technical mastery, scientific/engineering precision, data analytics, health, and systemic optimization.",
        "he": "רום שמיים בבתולה: הסמכות המקצועית נובעת ממומחיות טכנית, דיוק מדעי והנדסי, ניתוח מערכות וייעול מתמיד."
    },
    "Libra": {
        "en": "Midheaven in Libra: Career excels through high-level diplomacy, law, design, strategic alliances, and shaping cultural or interpersonal harmony.",
        "he": "רום שמיים במאזניים: הקריירה מצטיינת בדיפלומטיה, משפט, עיצוב, יצירת בריתות אסטרטגיות וגישור."
    },
    "Scorpio": {
        "en": "Midheaven in Scorpio: Vocation involves deep research, high-stakes finance/capital, crisis transformation, intelligence, and uncovering hidden power.",
        "he": "רום שמיים בעקרב: הייעוד כרוך במחקר עומק, הון ופיננסים בסיכון גבוה, ניהול משברים, מודיעין וטרנספורמציה שורשית."
    },
    "Sagittarius": {
        "en": "Midheaven in Sagittarius: Public path expands across international borders, higher truth, publishing, aerospace/exploration, and visionary ideology.",
        "he": "רום שמיים בקשת: הנתיב הציבורי מתרחב מעבר לגבולות גיאוגרפיים, אקדמיה, חקר מרחבים חדשים וחזון פילוסופי רחב."
    },
    "Capricorn": {
        "en": "Midheaven in Capricorn: The classic signature of supreme institutional authority, long-range statecraft, industrial scale, and enduring historical legacy.",
        "he": "רום שמיים בגדי: החתימה הקלאסית של סמכות ממסדית עליונה, אסטרטגיה ארוכת-טווח, קנה מידה תעשייתי ומורשת היסטורית."
    },
    "Aquarius": {
        "en": "Midheaven in Aquarius: Public destiny is tied to futuristic technology, disruptive innovation, aerospace, collective networks, and reshaping humanity's trajectory.",
        "he": "רום שמיים בדלי: הייעוד הציבורי קשור לטכנולוגיה עתידנית, חדשנות משבשת, חלל, רשתות קולקטיביות ועיצוב עתיד האנושות."
    },
    "Pisces": {
        "en": "Midheaven in Pisces: Vocation channels visionary imagination, cinema/art, healing, spiritual inspiration, or dissolving old boundaries into a unified whole.",
        "he": "רום שמיים בדגים: הייעוד מתעל דמיון חזוני, יצירה, ריפוי, השראה רוחנית והמסת גבולות ישנים."
    },
}

HOUSE_MEANINGS = {
    1: {
        "title_en": "1st House (Identity, Persona & Frontline Action)",
        "title_he": "בית 1 (אופק, זהות עצמית, נוכחות ודחף ראשוני)",
        "en": "governing direct personal agency, physical vitality, frontline execution, and how this entity projects its power immediately into the environment",
        "he": "השולט על יוזמה אישית ישירה, נוכחות פרונטלית, חיוניות והאופן שבו הישות מקרינה עוצמה מיידית אל הסביבה"
    },
    2: {
        "title_en": "2nd House (Wealth, Material Resources & Core Valuation)",
        "title_he": "בית 2 (כספים, נכסים, משאבים חומריים וערך עצמי)",
        "en": "governing tangible wealth accumulation, engineering/material assets, revenue streams, and uncompromising practical value",
        "he": "השולט על צבירת הון ונכסים מוחשיים, משאבים חומריים והנדסיים, תזרים הכנסות ויצירת ערך כלכלי מעשי"
    },
    3: {
        "title_en": "3rd House (Intellect, Communication, Media & Transportation/Vehicles)",
        "title_he": "בית 3 (חשיבה, תקשורת, מדיה, רשתות ותחבורה/רכבים)",
        "en": "governing the analytical mind, information networks, media/speech, short-range transit, vehicles, and technological connectivity",
        "he": "השולט על החשיבה האנליטית, תקשורת ומדיה, רשתות מידע, תחבורה וכלי רכב, וחיבוריות טכנולוגית"
    },
    4: {
        "title_en": "4th House (Foundations, Roots, Real Estate & Inner Sanctuary)",
        "title_he": "בית 4 (שורשים, בית, נדל״ן, תשתית עמוקה וביטחון פנימי)",
        "en": "governing foundational roots, homeland, physical infrastructure/land, private life, and the psychological anchor",
        "he": "השולט על שורשים, מולדת, קרקע ותשתיות פיזיות, החיים הפרטיים והעוגן הפסיכולוגי העמוק"
    },
    5: {
        "title_en": "5th House (Bold Creation, Speculative Risk, Passion & Offspring)",
        "title_he": "בית 5 (יצירה מקורית, לקיחת סיכונים/הימורים נועזים, תשוקה וילדים/מיזמים)",
        "en": "governing audacious creative brainchildren, high-stakes speculative ventures, willpower expression, romance, and legacy through creation",
        "he": "השולט על יצירה מקורית נועזת, מיזמים ספקולטיביים בסיכון גבוה, ביטוי עצמי, רומנטיקה ודור ההמשך"
    },
    6: {
        "title_en": "6th House (Systems Engineering, Work Ethic, Operations & Precision)",
        "title_he": "בית 6 (הנדסת מערכות, מוסר עבודה, תפעול יומיומי ודיוק)",
        "en": "governing relentless daily work, operational efficiency, technical problem-solving, workforce management, and health",
        "he": "השולט על עבודה מאומצת, יעילות תפעולית, פתרון בעיות טכניות, ניהול צוותים ובריאות"
    },
    7: {
        "title_en": "7th House (Partnerships, Contracts, Marriages & Open Rivals)",
        "title_he": "בית 7 (זוגיות, שותפויות אסטרטגיות, חוזים ויריבים גלויים)",
        "en": "governing one-on-one committed alliances, marriage, legal contracts, public negotiations, and open competitors",
        "he": "השולט על זוגיות ומערכות יחסים מחייבות, שותפויות עסקיות, חוזים משפטיים ויריבים גלויים"
    },
    8: {
        "title_en": "8th House (High-Stakes Capital, Leverage, Crisis Transformation & Deep Power)",
        "title_he": "בית 8 (הון סיכון, מינוף פיננסי, משברים, טרנספורמציה ועוצמה נסתרת)",
        "en": "governing other people's money (venture capital, debt, equity, mergers), existential survival under pressure, deep psychological intensity, and radical rebirth",
        "he": "השולט על הון משותף ומימון חיצוני (הון סיכון, מינוף, מיזוגים והשקעות ענק), הישרדות במצבי קצה, עומק פסיכולוגי ולידה מחדש"
    },
    9: {
        "title_en": "9th House (Distant Horizons, Aerospace/Global Reach, Science & Philosophy)",
        "title_he": "בית 9 (אופקים רחוקים, התרחבות גלובלית/חלל, מדע, חזון ופילוסופיה)",
        "en": "governing long-distance exploration, global/interplanetary horizons, higher science, publishing, and overarching worldview",
        "he": "השולט על חקר מרחבים רחוקים, פריצה גלובלית, מדע גבוה, אידיאולוגיה ותפיסת עולם רחבה"
    },
    10: {
        "title_en": "10th House (Public Destiny, Executive Authority, Reputation & Legacy)",
        "title_he": "בית 10 (קריירה, רום שמיים, סמכות ציבורית, מוניטין עולמי ומורשת)",
        "en": "governing supreme career achievement, global visibility, leadership authority, and historical impact",
        "he": "השולט על פסגת הקריירה, נראות ציבורית עולמית, סמכות מנהיגותית והשפעה היסטורית"
    },
    11: {
        "title_en": "11th House (Future of Humanity, Technology Networks, Alliances & Collective Vision)",
        "title_he": "בית 11 (עתיד האנושות, טכנולוגיה עילית, רשתות, קהילות וחזון קולקטיבי)",
        "en": "governing long-range futuristic goals, technological revolutions, collective networks, and alliances that reshape society",
        "he": "השולט על יעדים עתידניים ארוכי-טווח, מהפכות טכנולוגיות, רשתות חברתיות וחזון למען הקולקטיב"
    },
    12: {
        "title_en": "12th House (The Unconscious, Hidden Incubation, Existential Mission & Solitude)",
        "title_he": "בית 12 (תת-מודע, הבשלה מאחורי הקלעים, שליחות קיומית ועולם פנימי נסתר)",
        "en": "governing vast behind-the-scenes incubation, tapped collective unconscious, existential/karmic mission, private solitude, and visionary imagination",
        "he": "השולט על תהליכי עומק מאחורי הקלעים, תת-מודע קולקטיבי, דמיון חזוני ושליחות קיומית רחבה"
    },
}

PLANET_CORE_ROLES = {
    "Sun": {
        "en": "Core Identity, Conscious Will, Vitality & Supreme Purpose",
        "he": "זהות גרעינית, כוח רצון מודע, חיוניות וייעוד מרכזי"
    },
    "Moon": {
        "en": "Emotional Core, Instinctual Needs, Subconscious Habits & Adaptive Security",
        "he": "עולם רגשי, צרכים אינסטינקטיביים, תגובות אוטומטיות וביטחון פנימי"
    },
    "Mercury": {
        "en": "Cognitive Architecture, Analytical Processing, Speech & Strategic Logic",
        "he": "מבנה החשיבה, עיבוד מידע אנליטי, תקשורת ולוגיקה אסטרטגית"
    },
    "Venus": {
        "en": "Values, Attraction, Relational Style, Aesthetics & Wealth Affinity",
        "he": "סולם ערכים, אהבה ומשיכה, אסתטיקה, הרמוניה וזיקה לשפע"
    },
    "Mars": {
        "en": "Drive, Combativeness, Execution Speed, Courage & Raw Ambition",
        "he": "דחף פעולה, יוזמה, לוחמנות, ביצוע מהיר, אומץ ותשוקה"
    },
    "Jupiter": {
        "en": "Expansion, Grand Vision, Risk Appetite, Fortune & Scale",
        "he": "התרחבות, שפע, חזון גדול, תיאבון לסיכון, אופטימיות וקנה מידה"
    },
    "Saturn": {
        "en": "Structure, Discipline, Physics/Reality Constraints, Mastery & Endurance",
        "he": "מבנה, משמעת, חוקי המציאות והפיזיקה, התמדה, ביקורת עצמית ובנייה לטווח ארוך"
    },
    "Uranus": {
        "en": "Disruption, Technological Genius, Rebellion, Lightning Breakthroughs & Independence",
        "he": "חדשנות משבשת, גאונות טכנולוגית, מרדנות במוסכמות, הברקות פתאומיות ועצמאות"
    },
    "Neptune": {
        "en": "Mythic Vision, Boundless Imagination, Idealism, Intuition & Dissolution of Limits",
        "he": "חזון מיתי, דמיון חסר גבולות, אידיאליזם, השראה והמסת מגבלות"
    },
    "Pluto": {
        "en": "Obsessive Intensity, Total Transformation, Power Dynamics, Crisis Mastery & Regeneration",
        "he": "אינטנסיביות טוטאלית, טרנספורמציה עמוקה, מוקדי כוח ושליטה, וצמיחה מתוך משבר"
    },
    "North Node": {
        "en": "Evolutionary Destiny, Karmic North Star & Future Growth Edge",
        "he": "ייעוד אבולוציוני (ראש הדרקון), כיוון הצמיחה הגורלי והייעוד העתידי"
    },
}

SIGN_TRAITS = {
    "Aries": {"en": "pioneering, combative, first-principles, fearless, and urgently self-starting", "he": "חלוצי, לוחמני, ישיר, חסר פחד ובעל יוזמה מתפרצת"},
    "Taurus": {"en": "grounded, materially enduring, resourceful, stubborn, and value-focused", "he": "יציב, מעשי, עקשן, ממוקד בבניית ערך מוחשי ובעל אורך רוח"},
    "Gemini": {"en": "hyper-curious, mentally agile, communicative, multi-tasking, and information-driven", "he": "סקרן, מהיר-תפיסה, תקשורתי, ורסטילי ומונע ממידע ורעיונות"},
    "Cancer": {"en": "tenaciously protective, deeply intuitive, mission-driven around existential security and tribe", "he": "מגונן בנחישות, אינטואיטיבי, רגיש ומונע מתחושת שליחות ושימור קיומי"},
    "Leo": {"en": "commanding, charismatic, fiercely proud, creative, and built for central leadership", "he": "כריזמטי, מלכותי, גאה, יצירתי ובנוי להובלה במרכז הבמה"},
    "Virgo": {"en": "hyper-analytical, engineering-minded, perfectionistic, critical, and relentlessly optimizing", "he": "אנליטי להפליא, בעל חשיבה הנדסית מדויקת, פרפקציוניסט וביקורתי המשפר מערכות ללא הרף"},
    "Libra": {"en": "strategic, relational, harmonizing, intellectually balanced, and aesthetically refined", "he": "אסטרטגי, דיפלומטי, שואף לאיזון, שיתופי ומעודן"},
    "Scorpio": {"en": "all-or-nothing, psychologically penetrating, secretive, relentless, and crisis-hardened", "he": "טוטאלי ('הכל או כלום'), חודר לעומק, אסטרטגי, נחוש ועוצמתי במצבי קצה"},
    "Sagittarius": {"en": "visionary, boundary-breaking, philosophical, globally expansive, and audacious", "he": "חזוני, פורץ גבולות, פילוסופי, שואף למרחבים רחוקים ונועז"},
    "Capricorn": {"en": "disciplined, pragmatic, structurally ambitious, stoic, and focused on monumental mastery", "he": "ממושמע, פרגמטי, שאפתן, מחושב וממוקד בבניית הישגים מונומנטליים"},
    "Aquarius": {"en": "futuristic, iconoclastic, scientific/technological, contrarian, and focused on humanity's future", "he": "עתידני, שובר מוסכמות, מדעי-טכנולוגי, מקורי וממוקד בעתיד האנושות"},
    "Pisces": {"en": "imaginative, boundless, intuitive, transcendent, and attuned to collective dreams", "he": "בעל דמיון אינסופי, אינטואיטיבי, רגיש ומחובר לחלומות ותת-מודע קולקטיבי"},
}


def get_dignity(planet_name, sign_name):
    """Return essential dignity status ('domicile', 'exaltation', 'detriment', 'fall', or 'peregrine')."""
    cfg = ESSENTIAL_DIGNITIES.get(planet_name, {})
    if sign_name in cfg.get("domicile", []):
        return {
            "status": "domicile",
            "label_en": "Domicile (Rulership)",
            "label_he": "שליט ביתו (עוצמה מלאה)",
            "color": "#10b981"
        }
    if sign_name in cfg.get("exaltation", []):
        return {
            "status": "exaltation",
            "label_en": "Exalted",
            "label_he": "נעלה (התעלות)",
            "color": "#38bdf8"
        }
    if sign_name in cfg.get("detriment", []):
        return {
            "status": "detriment",
            "label_en": "Detriment (Unconventional)",
            "label_he": "ירוד (ביטוי מאתגר/לא שגרתי)",
            "color": "#f59e0b"
        }
    if sign_name in cfg.get("fall", []):
        return {
            "status": "fall",
            "label_en": "Fall (Karmic Friction)",
            "label_he": "נפילה (רגישות/מאמץ מוגבר)",
            "color": "#ef4444"
        }
    return {
        "status": "peregrine",
        "label_en": "Peregrine",
        "label_he": "ניטרלי",
        "color": "#94a3b8"
    }


def find_mutual_receptions(planets_dict):
    """Detect planets in mutual reception by traditional or modern rulership."""
    receptions = []
    planet_names = [p for p in ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"] if p in planets_dict]
    for i in range(len(planet_names)):
        for j in range(i + 1, len(planet_names)):
            p1 = planet_names[i]
            p2 = planet_names[j]
            s1 = planets_dict[p1]["sign"]
            s2 = planets_dict[p2]["sign"]
            r1_trad = SIGN_RULERS[s1]["traditional"]
            r1_mod = SIGN_RULERS[s1]["modern"]
            r2_trad = SIGN_RULERS[s2]["traditional"]
            r2_mod = SIGN_RULERS[s2]["modern"]

            if (p2 in (r1_trad, r1_mod)) and (p1 in (r2_trad, r2_mod)):
                s1_he = SIGN_META[s1]["he"]
                s2_he = SIGN_META[s2]["he"]
                p1_he = PLANET_HE[p1]
                p2_he = PLANET_HE[p2]
                receptions.append({
                    "p1": p1,
                    "p2": p2,
                    "s1": s1,
                    "s2": s2,
                    "en": f"Mutual Reception between {p1} (in {s1}) and {p2} (in {s2}): Both planets sit in each other's signs of rulership, creating a high-speed feedback loop that fuses {p1}'s function with {p2}'s domain.",
                    "he": f"קבלה הדדית (Mutual Reception) בין {p1_he} (ב{s1_he}) לבין {p2_he} (ב{s2_he}): כל כוכב מתארח במזל הנשלט על ידי השני, מה שיוצר סינרגיה ושיתוף פעולה פנימי עוצמתי במיוחד בין שני הכוחות."
                })
    return receptions


def interpret_planet_placement(p_entry):
    """Generate rich expert interpretation for a planet in its Sign and House."""
    name = p_entry["name"]
    sign = p_entry["sign"]
    house = p_entry.get("house", 1)
    is_rx = p_entry.get("retrograde", False)
    dignity = p_entry.get("dignity", {})

    role = PLANET_CORE_ROLES.get(name, {"en": name, "he": PLANET_HE.get(name, name)})
    trait = SIGN_TRAITS.get(sign, {"en": sign, "he": SIGN_META.get(sign, {}).get("he", sign)})
    h_info = HOUSE_MEANINGS.get(house, HOUSE_MEANINGS[1])
    sign_he = SIGN_META.get(sign, {}).get("he", sign)
    p_he = PLANET_HE.get(name, name)

    rx_en = " Because this body is **Retrograde (Rx)**, its energy operates inward and independently of social consensus, developing an unconventional, deeply internalized mastery." if is_rx else ""
    rx_he = " מכיוון שהכוכב נמצא **בנסיגה (Rx)**, האנרגיה שלו פועלת באופן עצמאי, פנימי ולא קונבנציונלי, מחוץ לתבניות המוכרות של הסביבה." if is_rx else ""

    dig_en = ""
    dig_he = ""
    if dignity.get("status") == "domicile":
        dig_en = f" Positioned in its own domicile ({sign}), {name} operates at peak sovereign strength."
        dig_he = f" מיקום זה במזל שליטתו ({sign_he}) מעניק ל{p_he} עוצמה מקסימלית וביטוי טבעי וישיר."
    elif dignity.get("status") == "exaltation":
        dig_en = f" Exalted in {sign}, {name} expresses its highest, most elevated potential."
        dig_he = f" כוכב זה נמצא בהתעלות (Exalted) ב{sign_he}, מה שמעצים את איכויותיו לרמה הגבוהה ביותר."

    text_en = (
        f"**{name} in {sign} (House {house})** — *{role['en']}*: "
        f"Expresses in a {trait['en']} manner, channeled directly into the **{h_info['title_en']}** ({h_info['en']})."
        f"{dig_en}{rx_en}"
    )
    text_he = (
        f"**{p_he} ב{sign_he} (בית {house})** — *{role['he']}*: "
        f"מתבטא באופן {trait['he']}, ומתועל ישירות אל **{h_info['title_he']}** ({h_info['he']})."
        f"{dig_he}{rx_he}"
    )
    return {"en": text_en, "he": text_he}


def interpret_natal_aspect(asp):
    """Generate expert interpretation for a natal aspect between p1 and p2."""
    p1 = asp["p1"]
    p2 = asp["p2"]
    aspect = asp["aspect"]
    orb = asp["orb"]
    pair = {p1, p2}

    p1_he = PLANET_HE.get(p1, p1)
    p2_he = PLANET_HE.get(p2, p2)
    asp_he_map = {
        "Conjunction": "צמידות (0°)",
        "Opposition": "אופוזיציה / מולות (180°)",
        "Trine": "טריין / משולש הרמוני (120°)",
        "Square": "סקוויר / ריבוע מאתגר (90°)",
        "Sextile": "סקסטיל / משושה תומך (60°)",
    }
    asp_he = asp_he_map.get(aspect, aspect)

    # Specific high-profile natal aspect archetypes
    if pair == {"Mercury", "Ascendant"} and aspect == "Conjunction":
        return {
            "en": f"Exact Mercury Conjunct Ascendant (orb {orb}°): A hallmark of a hyper-intellectual frontline persona. The mind, analytical speech, and rapid problem-solving sit directly on the Rising degree—thinking, calculating, and communicating ARE the identity.",
            "he": f"צמידות מדויקת בין מרקורי לאופק (סטייה {orb}°): חתימה מובהקת של אישיות שבה השכל, החשיבה האנליטית והתקשורת יושבים ישירות על האופק. האינטלקט נמצא בחזית ומנווט כל צעד."
        }
    if pair == {"Sun", "Uranus"} and aspect in ("Square", "Conjunction", "Opposition"):
        return {
            "en": f"Sun {aspect} Uranus (orb {orb}°): The Rebel-Visionary & Disruptor signature. Refuses to accept status-quo limitations, thrives on high-voltage breakthroughs, challenges established industries, and exhibits sudden, unpredictable shifts.",
            "he": f"היבט {asp_he} בין השמש לאורנוס (סטייה {orb}°): חתימת המהפכן והמחדש הטכנולוגי. סירוב מוחלט לקבל מוסכמות או מגבלות קיימות, דחף לפריצות דרך מדעיות/חברתיות, עצמאות קיצונית וקצב פעולה בלתי צפוי."
        }
    if pair == {"Mercury", "Uranus"} and aspect in ("Square", "Conjunction", "Opposition", "Trine", "Sextile"):
        return {
            "en": f"Mercury {aspect} Uranus (orb {orb}°): Lightning-fast, non-linear engineering & futuristic intellect. Connects disparate concepts at high speed, gravitates toward advanced technology, physics, and unconventional communication, though prone to bluntness and mental restlessness.",
            "he": f"היבט {asp_he} בין מרקורי לאורנוס (סטייה {orb}°): חשיבה מבריקה, מהירה כברק ולא-ליניארית. יכולת נדירה לתפוס מערכות מורכבות, טכנולוגיה עתידנית ופיזיקה, לצד חוסר סבלנות לחשיבה איטית וביטוי ישיר וחד."
        }
    if pair == {"Uranus", "Ascendant"} and aspect in ("Square", "Conjunction", "Opposition"):
        return {
            "en": f"Uranus {aspect} Ascendant (orb {orb}°): Electric, contrarian personal magnetism. Projects an unmistakable Maverick aura that disrupts every room or market entered; wired for radical autonomy.",
            "he": f"היבט {asp_he} בין אורנוס לאופק (סטייה {orb}°): נוכחות מחשמלת, עצמאית ושוברת מוסכמות. מקרין הילה של חלוץ שאינו מתיישר עם הנורמה ומחולל טלטלה ושינוי בכל זירה שבה הוא פועל."
        }
    if pair == {"Sun", "Moon"}:
        if aspect in ("Sextile", "Trine", "Conjunction"):
            return {
                "en": f"Sun {aspect} Moon (orb {orb}°): Internal integration between conscious willpower (Sun) and instinctual/emotional stamina (Moon), enabling sustained focus under pressure.",
                "he": f"היבט {asp_he} בין השמש לירח (סטייה {orb}°): שיתוף פעולה הרמוני בין כוח הרצון המודע (שמש) לבין הצרכים האינסטינקטיביים והחוסן הרגשי (ירח)."
            }
        else:
            return {
                "en": f"Sun {aspect} Moon (orb {orb}°): Dynamic inner tension between conscious ambition and emotional needs, fueling relentless drive to prove oneself through action.",
                "he": f"היבט {asp_he} בין השמש לירח (סטייה {orb}°): מתח פנימי מניע בין השאיפות המודעות לבין העולם הרגשי, המייצר דחף מתמיד להישגיות."
            }
    if pair == {"Venus", "Mars"}:
        return {
            "en": f"Venus {aspect} Mars (orb {orb}°): Strong creative and passionate synergy uniting magnetism, desire, and assertive execution.",
            "he": f"היבט {asp_he} בין ונוס למארס (סטייה {orb}°): חיבור עוצמתי בין תשוקה, כריזמה, משיכה ויכולת ביצוע נחושה."
        }
    if pair == {"Jupiter", "Saturn"}:
        return {
            "en": f"Jupiter {aspect} Saturn (orb {orb}°): The Master Architect polarity—balancing boundless visionary expansion (Jupiter) against hard physical/structural reality and discipline (Saturn). Drives monumental enterprise building.",
            "he": f"היבט {asp_he} בין יופיטר לשבתאי (סטייה {orb}°): ציר 'האדריכל הגדול' — מפגש בין חזון התרחבות אדיר (יופיטר) לבין חוקי המציאות, המשמעת והמבנה ההנדסי (שבתאי). מנוע לבניית מיזמים בקנה מידה היסטורי."
        }
    if pair == {"Jupiter", "Pluto"}:
        return {
            "en": f"Jupiter {aspect} Pluto (orb {orb}°): Extreme wealth-building and Plutonian scale signature. Amplifies ambition to transform entire industries and command massive financial/strategic resources.",
            "he": f"היבט {asp_he} בין יופיטר לפלוטו (סטייה {orb}°): חתימת עוצמה של קנה מידה אדיר, שאפתנות על-אנושית ויכולת לגייס ולשנע משאבי ענק לשינוי פני המציאות."
        }
    if pair == {"Saturn", "Pluto"}:
        return {
            "en": f"Saturn {aspect} Pluto (orb {orb}°): Iron endurance and survival through extreme crisis. Gives the grit to endure brutal pressure, rebuild foundations, and exercise unyielding authority.",
            "he": f"היבט {asp_he} בין שבתאי לפלוטו (סטייה {orb}°): כוח עמידות מפלדה ויכולת הישרדות בלחצים קיצוניים. נחישות בלתי מתפשרת לבנות מחדש מתוך משבר."
        }
    if pair == {"Jupiter", "Neptune"}:
        return {
            "en": f"Jupiter {aspect} Neptune (orb {orb}°): Boundless mythic imagination and sci-fi/idealistic vision—dreaming on a cosmic or interplanetary scale beyond what others deem possible.",
            "he": f"היבט {asp_he} בין יופיטר לנפטון (סטייה {orb}°): דמיון חזוני חסר גבולות ושאיפה להגשים חלומות בקנה מידה קוסמי שנראים לאחרים כמדע בדיוני."
        }
    if pair == {"Saturn", "Neptune"}:
        return {
            "en": f"Saturn {aspect} Neptune (orb {orb}°): Turning impossible dreams (Neptune) into concrete physical engineering and hard structure (Saturn).",
            "he": f"היבט {asp_he} בין שבתאי לנפטון (סטייה {orb}°): היכולת לתרגם חלומות מופשטים וחזון דמיוני (נפטון) למציאות פיזית, הנדסית ומבנית מוצקה (שבתאי)."
        }
    if pair == {"Mars", "North Node"}:
        return {
            "en": f"Mars {aspect} North Node (orb {orb}°): Destiny requires bold, combative action and pioneering leadership aligned with the evolutionary path.",
            "he": f"היבט {asp_he} בין מארס לראש הדרקון (סטייה {orb}°): הייעוד הגורלי דורש פעולה אמיצה, חלוצית ולוחמנית בחזית הקדמה."
        }

    # Generic fallback with high astrological precision
    r1 = PLANET_CORE_ROLES.get(p1, {"en": p1, "he": p1_he})
    r2 = PLANET_CORE_ROLES.get(p2, {"en": p2, "he": p2_he})
    if aspect == "Conjunction":
        return {
            "en": f"{p1} Conjunct {p2} (orb {orb}°): Direct fusion of {p1} ({r1['en']}) and {p2} ({r2['en']}) into a single concentrated focal point.",
            "he": f"צמידות בין {p1_he} לבין {p2_he} (סטייה {orb}°): מיזוג ישיר ועוצמתי בין {p1_he} ({r1['he']}) לבין {p2_he} ({r2['he']})."
        }
    elif aspect in ("Trine", "Sextile"):
        return {
            "en": f"{p1} {aspect} {p2} (orb {orb}°): Harmonious structural channel linking {p1} and {p2}, allowing natural talent and effortless execution between their domains.",
            "he": f"היבט {asp_he} הרמוני בין {p1_he} לבין {p2_he} (סטייה {orb}°): זרימה טבעית ושיתוף פעולה פורה בין שני הכוחות."
        }
    else:
        return {
            "en": f"{p1} {aspect} {p2} (orb {orb}°): High-voltage developmental friction between {p1} and {p2} that compels relentless action, mastery, and breakthrough results.",
            "he": f"היבט {asp_he} דינמי ומאתגר בין {p1_he} לבין {p2_he} (סטייה {orb}°): מתח פנימי מניע הדוחף לפעולה בלתי פוסקת, התגברות על מכשולים ופריצת גבולות."
        }


def compute_element_modality_balance(chart_sys):
    """Calculate weighted Elemental, Modal, and Hemisphere balance."""
    weights = {
        "Sun": 2.0, "Moon": 2.0, "Ascendant": 2.0, "Midheaven": 1.5,
        "Mercury": 1.5, "Venus": 1.2, "Mars": 1.2,
        "Jupiter": 1.0, "Saturn": 1.0,
        "Uranus": 0.7, "Neptune": 0.7, "Pluto": 0.7
    }
    elements = {"Fire": 0.0, "Earth": 0.0, "Air": 0.0, "Water": 0.0}
    modalities = {"Cardinal": 0.0, "Fixed": 0.0, "Mutable": 0.0}
    hemispheres = {"upper_public": 0, "lower_private": 0, "eastern_self": 0, "western_other": 0}

    all_pts = chart_sys["planets"] + [chart_sys["asc_point"], chart_sys["mc_point"]]
    total_w = 0.0
    for pt in all_pts:
        w = weights.get(pt["name"], 1.0)
        s_meta = SIGN_META.get(pt["sign"], {"element": "Fire", "quality": "Cardinal"})
        elements[s_meta["element"]] += w
        modalities[s_meta["quality"]] += w
        total_w += w

        if pt["name"] not in ("Ascendant", "Midheaven"):
            h = pt.get("house", 1)
            if 7 <= h <= 12:
                hemispheres["upper_public"] += 1
            else:
                hemispheres["lower_private"] += 1
            if h in (10, 11, 12, 1, 2, 3):
                hemispheres["eastern_self"] += 1
            else:
                hemispheres["western_other"] += 1

    elem_pct = {k: int(round((v / total_w) * 100)) for k, v in elements.items()}
    mod_pct = {k: int(round((v / total_w) * 100)) for k, v in modalities.items()}

    dom_element = max(elements.items(), key=lambda x: x[1])[0]
    def_element = min(elements.items(), key=lambda x: x[1])[0]
    dom_modality = max(modalities.items(), key=lambda x: x[1])[0]

    elem_desc = {
        "Fire": {
            "en": "Fire dominance fuels visionary inspiration, combative courage, and relentless pioneering momentum.",
            "he": "דומיננטיות של יסוד האש מעניקה להט חלוצי, אומץ לב, חזון מתפרץ ודחף להוביל."
        },
        "Earth": {
            "en": "Earth dominance anchors everything in tangible engineering, material execution, and practical economics.",
            "he": "דומיננטיות של יסוד האדמה מעגנת הכל בביצוע מעשי, הנדסי, חומרי וכלכלי מוחשי."
        },
        "Air": {
            "en": "Air dominance elevates abstract systems thinking, technological/social networks, and rapid intellect.",
            "he": "דומיננטיות של יסוד האוויר מדגישה חשיבה מערכתית, קונספטים, טכנולוגיה ותקשורת מהירה."
        },
        "Water": {
            "en": "Water dominance provides deep instinctual radar, emotional intensity, and protective existential commitment.",
            "he": "דומיננטיות של יסוד המים מעניקה אינטואיציה עמוקה, עוצמה רגשית ומחויבות קיומית טוטאלית."
        },
    }

    mod_desc = {
        "Cardinal": {
            "en": "Cardinal dominance marks an initiator and prime mover who launches bold new enterprises and refuses stagnation.",
            "he": "דומיננטיות של איכות יוזמת (Cardinal) מסמנת אדם/ישות היוזמים מהלכים חדשים, פורצים קדימה ומניעים מערכות."
        },
        "Fixed": {
            "en": "Fixed dominance bestows unyielding persistence, monumental staying power, and refusal to back down.",
            "he": "דומיננטיות של איכות קבועה (Fixed) מעניקה כוח התמדה אדיר, נחישות בלתי מתפשרת ויכולת לעמוד בלחצים."
        },
        "Mutable": {
            "en": "Mutable dominance grants high adaptability, multi-disciplinary synthesis, and rapid pivoting in complex environments.",
            "he": "דומיננטיות של איכות משתנה (Mutable) מעניקה גמישות מחשבתית, יכולת הסתגלות מהירה וסינתזה רב-תחומית."
        },
    }

    return {
        "elements_pct": elem_pct,
        "modalities_pct": mod_pct,
        "dominant_element": dom_element,
        "deficient_element": def_element,
        "dominant_modality": dom_modality,
        "hemispheres": hemispheres,
        "summary_en": f"{elem_desc[dom_element]['en']} {mod_desc[dom_modality]['en']}",
        "summary_he": f"{elem_desc[dom_element]['he']} {mod_desc[dom_modality]['he']}",
    }


def detect_chart_patterns(chart_sys):
    """Detect major geometric and structural patterns in the natal chart."""
    patterns = []
    p_dict = chart_sys["planets_dict"]
    asc_lon = chart_sys["asc"]
    mc_lon = chart_sys["mc"]

    # 1. Angular Planets (within 6.5 deg of ASC, MC, DSC, IC)
    angles_check = [
        ("Ascendant (ASC)", "אופק (ASC)", asc_lon),
        ("Midheaven (MC)", "רום שמיים (MC)", mc_lon),
        ("Descendant (DSC)", "שוקע (DSC)", chart_sys["dsc"]),
        ("Imum Coeli (IC)", "חצות שמיים (IC)", chart_sys["ic"]),
    ]
    for p in chart_sys["planets"]:
        for ang_en, ang_he, ang_lon in angles_check:
            diff = abs(p["lon"] - ang_lon)
            diff = min(diff, 360.0 - diff)
            if diff <= 6.5:
                p_he = PLANET_HE.get(p["name"], p["name"])
                patterns.append({
                    "type": "Angular Planet",
                    "badge_en": "Angular Powerhouse",
                    "badge_he": "כוכב צמוד-ציר (Angular)",
                    "title_en": f"{p['symbol']} {p['name']} Conjunct {ang_en} (orb {diff:.1f}°)",
                    "title_he": f"{p['symbol']} {p_he} בצמידות ל{ang_he} (סטייה {diff:.1f}°)",
                    "desc_en": f"In expert astrology, a planet within {diff:.1f}° of {ang_en} acts as a dominant megaphone for the entire chart—making {p['name']}'s qualities ({PLANET_CORE_ROLES.get(p['name'], {}).get('en', '')}) immediately visible and central to destiny.",
                    "desc_he": f"באסטרולוגיה מקצועית, כוכב הנמצא במרחק {diff:.1f}° בלבד מ{ang_he} פועל כ'מגפון' ראשי של המפה כולה — והופך את איכויות {p_he} ({PLANET_CORE_ROLES.get(p['name'], {}).get('he', '')}) לבולטות ומכריעות בגורל."
                })

    # 2. Mutual Receptions
    for rec in find_mutual_receptions(p_dict):
        patterns.append({
            "type": "Mutual Reception",
            "badge_en": "Mutual Reception",
            "badge_he": "קבלה הדדית",
            "title_en": f"Mutual Reception: {rec['p1']} ({rec['s1']}) ⇄ {rec['p2']} ({rec['s2']})",
            "title_he": f"קבלה הדדית: {PLANET_HE[rec['p1']]} ({SIGN_META[rec['s1']]['he']}) ⇄ {PLANET_HE[rec['p2']]} ({SIGN_META[rec['s2']]['he']})",
            "desc_en": rec["en"],
            "desc_he": rec["he"],
        })

    # 3. Stelliums (3+ bodies in same Sign or same House)
    sign_groups = {}
    house_groups = {}
    for p in chart_sys["planets"]:
        sign_groups.setdefault(p["sign"], []).append(p["name"])
        house_groups.setdefault(p["house"], []).append(p["name"])

    for s_name, p_list in sign_groups.items():
        if len(p_list) >= 3:
            s_he = SIGN_META[s_name]["he"]
            p_he_list = ", ".join(PLANET_HE.get(x, x) for x in p_list)
            patterns.append({
                "type": "Sign Stellium",
                "badge_en": "Stellium",
                "badge_he": "סטליום (ריכוז כוכבים)",
                "title_en": f"{s_name} Stellium ({', '.join(p_list)})",
                "title_he": f"סטליום במזל {s_he} ({p_he_list})",
                "desc_en": f"High concentration of {len(p_list)} planets in {s_name} creates laser-like intensity and unmistakable {s_name} traits.",
                "desc_he": f"ריכוז עוצמתי של {len(p_list)} כוכבים במזל {s_he} הממקד חלק אדיר מהאנרגיה האישית בתכונות מזל זה."
            })

    for h_num, p_list in house_groups.items():
        if len(p_list) >= 3:
            h_info = HOUSE_MEANINGS.get(h_num, HOUSE_MEANINGS[1])
            p_he_list = ", ".join(PLANET_HE.get(x, x) for x in p_list)
            patterns.append({
                "type": "House Stellium",
                "badge_en": "House Stellium",
                "badge_he": "סטליום בבית",
                "title_en": f"House {h_num} Stellium ({', '.join(p_list)})",
                "title_he": f"ריכוז כוכבים בבית {h_num} ({p_he_list})",
                "desc_en": f"Massive life focus in the {h_info['title_en']}: {', '.join(p_list)} all operate in this arena.",
                "desc_he": f"מיקוד גורלי ב{h_info['title_he']}: הכוכבים {p_he_list} פועלים יחד בזירה זו."
            })

    # 4. High-Voltage Focal Squares (e.g. Planet squaring 2+ core points like Sun/Moon/Mercury/ASC)
    asps = chart_sys["natal_aspects"]
    square_map = {}
    for a in asps:
        if a["aspect"] == "Square":
            square_map.setdefault(a["p1"], []).append(a["p2"])
            square_map.setdefault(a["p2"], []).append(a["p1"])

    for focal_p, targets in square_map.items():
        core_targets = [t for t in targets if t in ("Sun", "Moon", "Mercury", "Ascendant", "Midheaven", "Mars")]
        if len(core_targets) >= 2:
            f_he = PLANET_HE.get(focal_p, focal_p)
            t_he = ", ".join(PLANET_HE.get(x, x) for x in core_targets)
            patterns.append({
                "type": "Focal Square Apex",
                "badge_en": "Breakthrough Tension",
                "badge_he": "מוקד מתח ופריצת דרך",
                "title_en": f"{focal_p} Squaring {', '.join(core_targets)}",
                "title_he": f"{f_he} בריבוע (90°) מול {t_he}",
                "desc_en": f"{focal_p} forms a high-tension square to {', '.join(core_targets)}, acting as a relentless dynamo that refuses comfort zones and drives radical innovation.",
                "desc_he": f"{f_he} יוצר זווית מתח (ריבוע 90°) מול {t_he}, מה שפועל כמנוע פנימי חסר מנוחה הדוחף לפריצת גבולות וחדשנות רדיקלית."
            })

    # 5. Opposition Wedge / Mystic Funnel (Opposition where a 3rd planet trines one and sextiles the other)
    oppositions = [(a["p1"], a["p2"]) for a in asps if a["aspect"] == "Opposition"]
    trines = {(a["p1"], a["p2"]) for a in asps if a["aspect"] == "Trine"} | {(a["p2"], a["p1"]) for a in asps if a["aspect"] == "Trine"}
    sextiles = {(a["p1"], a["p2"]) for a in asps if a["aspect"] == "Sextile"} | {(a["p2"], a["p1"]) for a in asps if a["aspect"] == "Sextile"}

    all_names = list(p_dict.keys())
    for op1, op2 in oppositions:
        for apex in all_names:
            if apex in (op1, op2):
                continue
            if ((op1, apex) in trines and (op2, apex) in sextiles) or ((op2, apex) in trines and (op1, apex) in sextiles):
                patterns.append({
                    "type": "Mystic Wedge",
                    "badge_en": "Focal Wedge Pattern",
                    "badge_he": "מבנה יתד (תיעול אנרגטי)",
                    "title_en": f"{op1}–{op2} Opposition Channeled via {apex}",
                    "title_he": f"מולות {PLANET_HE.get(op1, op1)}–{PLANET_HE.get(op2, op2)} המתועלת דרך {PLANET_HE.get(apex, apex)}",
                    "desc_en": f"The polarity between {op1} and {op2} finds its constructive release valve through {apex} (in {p_dict[apex]['sign']}, House {p_dict[apex]['house']}), turning massive tension into laser-focused execution.",
                    "desc_he": f"הקוטביות בין {PLANET_HE.get(op1, op1)} לבין {PLANET_HE.get(op2, op2)} מתועלת בצורה בונה וממוקדת דרך {PLANET_HE.get(apex, apex)} (ב{SIGN_META[p_dict[apex]['sign']]['he']}, בית {p_dict[apex]['house']}), מה שהופך מתח אדיר לכוח ביצוע מעשי."
                })

    return patterns


def build_expert_natal_dossier(chart_sys, entity_type="person"):
    """
    Generate a complete Expert Astrologist Natal Dossier in both English and Hebrew,
    including Ascendant (אופק), Chart Ruler, Midheaven (MC), Big Three Synthesis,
    Planetary Dignities & Retrogrades, Natal Aspects, and a 'Blind Portrait' deduction.
    """
    p_dict = chart_sys["planets_dict"]
    asc_pt = chart_sys["asc_point"]
    mc_pt = chart_sys["mc_point"]
    nn_pt = chart_sys.get("north_node")

    asc_sign = asc_pt["sign"]
    mc_sign = mc_pt["sign"]
    sun = p_dict["Sun"]
    moon = p_dict["Moon"]
    mercury = p_dict["Mercury"]
    venus = p_dict["Venus"]
    mars = p_dict["Mars"]
    jupiter = p_dict["Jupiter"]
    saturn = p_dict["Saturn"]
    uranus = p_dict["Uranus"]
    neptune = p_dict["Neptune"]
    pluto = p_dict["Pluto"]

    # 1. Chart Ruler (Ruler of Ascendant)
    asc_ruler_trad = SIGN_RULERS[asc_sign]["traditional"]
    asc_ruler_mod = SIGN_RULERS[asc_sign]["modern"]
    ruler_planet = p_dict.get(asc_ruler_mod, p_dict.get(asc_ruler_trad, sun))
    ruler_h_info = HOUSE_MEANINGS.get(ruler_planet["house"], HOUSE_MEANINGS[1])

    # 2. MC Ruler (Ruler of Midheaven / 10th House)
    mc_ruler_name = SIGN_RULERS[mc_sign]["traditional"]
    mc_ruler_mod = SIGN_RULERS[mc_sign]["modern"]
    mc_ruler_planet = p_dict.get(mc_ruler_mod, p_dict.get(mc_ruler_name, mars))
    mc_ruler_h_info = HOUSE_MEANINGS.get(mc_ruler_planet["house"], HOUSE_MEANINGS[10])

    # Ascendant Expert Section
    asc_base = ASCENDANT_INTERPRETATIONS.get(asc_sign, {"en": "", "he": ""})
    asc_sign_he = SIGN_META[asc_sign]["he"]
    ruler_name_he = PLANET_HE.get(ruler_planet["name"], ruler_planet["name"])
    ruler_sign_he = SIGN_META[ruler_planet["sign"]]["he"]

    asc_section = {
        "sign": asc_sign,
        "sign_he": asc_sign_he,
        "formatted": asc_pt["formatted"],
        "chart_ruler": ruler_planet["name"],
        "chart_ruler_he": ruler_name_he,
        "chart_ruler_sign": ruler_planet["sign"],
        "chart_ruler_sign_he": ruler_sign_he,
        "chart_ruler_house": ruler_planet["house"],
        "en": (
            f"**Ascendant (Rising Sign) at {asc_pt['deg']}° {asc_pt['min']:02d}' {asc_sign}**: {asc_base['en']} "
            f"Crucially, the **Chart Ruler (steersman of the chart) is {ruler_planet['name']}**, which is placed in **{ruler_planet['sign']} in House {ruler_planet['house']}**. "
            f"This directs the entire life trajectory toward the **{ruler_h_info['title_en']}**—{ruler_h_info['en']}, expressed with {SIGN_TRAITS[ruler_planet['sign']]['en']} precision."
        ),
        "he": (
            f"**אופק עולה (Ascendant) ב-{asc_pt['deg']}° {asc_pt['min']:02d}' במזל {asc_sign_he}**: {asc_base['he']} "
            f"נתון מפתח באסטרולוגיה מקצועית הוא **שליט המפה (שליט האופק) — {ruler_name_he}**, הממוקם ב**מזל {ruler_sign_he} בבית {ruler_planet['house']}**. "
            f"מיקום זה מנתב את מסלול החיים כולו אל **{ruler_h_info['title_he']}** ({ruler_h_info['he']}), תוך פעולה בסגנון {SIGN_TRAITS[ruler_planet['sign']]['he']}."
        )
    }

    # Midheaven & Vocation Expert Section
    mc_base = MC_INTERPRETATIONS.get(mc_sign, {"en": "", "he": ""})
    mc_sign_he = SIGN_META[mc_sign]["he"]
    mc_ruler_he = PLANET_HE.get(mc_ruler_planet["name"], mc_ruler_planet["name"])
    mc_ruler_sign_he = SIGN_META[mc_ruler_planet["sign"]]["he"]

    mc_section = {
        "sign": mc_sign,
        "sign_he": mc_sign_he,
        "formatted": mc_pt["formatted"],
        "mc_ruler": mc_ruler_planet["name"],
        "mc_ruler_he": mc_ruler_he,
        "mc_ruler_sign": mc_ruler_planet["sign"],
        "mc_ruler_house": mc_ruler_planet["house"],
        "en": (
            f"**Midheaven (MC / Public Destiny) at {mc_pt['deg']}° {mc_pt['min']:02d}' {mc_sign}**: {mc_base['en']} "
            f"The ruler of the Midheaven is **{mc_ruler_planet['name']}**, positioned in **{mc_ruler_planet['sign']} in House {mc_ruler_planet['house']}**. "
            f"Consequently, public authority and career breakthroughs are achieved through {SIGN_TRAITS[mc_ruler_planet['sign']]['en']} action inside the **{mc_ruler_h_info['title_en']}** ({mc_ruler_h_info['en']})."
        ),
        "he": (
            f"**רום שמיים (MC / ייעוד ציבורי וקריירה) ב-{mc_pt['deg']}° {mc_pt['min']:02d}' במזל {mc_sign_he}**: {mc_base['he']} "
            f"**שליט רום השמיים הוא {mc_ruler_he}**, הממוקם ב**מזל {mc_ruler_sign_he} בבית {mc_ruler_planet['house']}**. "
            f"לכן, השגת מעמד עולמי, סמכות והצלחה מקצועית מתרחשת באופן {SIGN_TRAITS[mc_ruler_planet['sign']]['he']} דרך זירת **{mc_ruler_h_info['title_he']}** ({mc_ruler_h_info['he']})."
        )
    }

    # Big Three Synthesis
    sun_h_info = HOUSE_MEANINGS.get(sun["house"], HOUSE_MEANINGS[1])
    moon_h_info = HOUSE_MEANINGS.get(moon["house"], HOUSE_MEANINGS[1])
    sun_sign_he = SIGN_META[sun["sign"]]["he"]
    moon_sign_he = SIGN_META[moon["sign"]]["he"]

    big_three_section = {
        "en": (
            f"**The Big Three Synthesis (☉ {sun['sign']} in House {sun['house']} · ☽ {moon['sign']} in House {moon['house']} · ASC {asc_sign})**: "
            f"At the core sits a **{sun['sign']} Sun in the {sun_h_info['title_en']}**, driven by a {SIGN_TRAITS[sun['sign']]['en']} sense of mission. "
            f"Beneath this operates a **{moon['sign']} Moon in the {moon_h_info['title_en']}**, which processes emotions and instincts in a {SIGN_TRAITS[moon['sign']]['en']} way ({moon_h_info['en']}). "
            f"Presented through the **{asc_sign} Ascendant**, this creates a rare combination where inner vision ({sun['sign']}), practical/instinctual rigor ({moon['sign']}), and frontline presence ({asc_sign}) reinforce one another."
        ),
        "he": (
            f"**סינתזת השילוש המרכזי (☉ שמש ב{sun_sign_he} בבית {sun['house']} · ☽ ירח ב{moon_sign_he} בבית {moon['house']} · אופק ב{asc_sign_he})**: "
            f"בליבת האישיות פועלת **שמש ב{sun_sign_he} ב{sun_h_info['title_he']}**, המונעת מתחושת שליחות באופי {SIGN_TRAITS[sun['sign']]['he']}. "
            f"מתחת לפני השטח פועל **ירח ב{moon_sign_he} ב{moon_h_info['title_he']}**, המעבד רגשות ואינסטינקטים באופן {SIGN_TRAITS[moon['sign']]['he']} ({moon_h_info['he']}). "
            f"דרך עדשת **אופק {asc_sign_he}**, נוצר שילוב רב-עוצמה שבו החזון הפנימי ({sun_sign_he}), המנוע האינסטינקטיבי-מעשי ({moon_sign_he}) והנוכחות החיצונית ({asc_sign_he}) מזינים זה את זה."
        )
    }

    # Balance & Patterns
    balance = compute_element_modality_balance(chart_sys)
    patterns = detect_chart_patterns(chart_sys)

    # Planet placements interpreted
    planets_interpreted = []
    all_bodies = chart_sys["planets"] + ([nn_pt] if nn_pt else [])
    for p in all_bodies:
        interp = interpret_planet_placement(p)
        planets_interpreted.append({
            "name": p["name"],
            "name_he": PLANET_HE.get(p["name"], p["name"]),
            "symbol": p["symbol"],
            "color": p["color"],
            "formatted": p["formatted"],
            "sign": p["sign"],
            "sign_he": SIGN_META.get(p["sign"], {}).get("he", p["sign"]),
            "house": p["house"],
            "retrograde": p.get("retrograde", False),
            "speed": p.get("speed", 0.0),
            "dignity": p.get("dignity", {}),
            "en": interp["en"],
            "he": interp["he"],
        })

    # Natal aspects interpreted
    natal_aspects_interpreted = []
    sorted_natal_asps = sorted(chart_sys["natal_aspects"], key=lambda x: x["orb"])
    for a in sorted_natal_asps:
        interp = interpret_natal_aspect(a)
        natal_aspects_interpreted.append({
            **a,
            "en": interp["en"],
            "he": interp["he"],
        })

    # Blind Portrait Synthesis ("Who is this person/entity without knowing their name?")
    pattern_highlights_en = "; ".join(p["title_en"] for p in patterns[:4]) if patterns else "Balanced planetary distribution"
    pattern_highlights_he = "; ".join(p["title_he"] for p in patterns[:4]) if patterns else "פיזור פלנטרי מאוזן"

    nn_text_en = ""
    nn_text_he = ""
    if nn_pt:
        nn_h_info = HOUSE_MEANINGS.get(nn_pt["house"], HOUSE_MEANINGS[1])
        nn_sign_he = SIGN_META[nn_pt["sign"]]["he"]
        nn_text_en = (
            f"The **Lunar North Node (Karmic Destiny) in {nn_pt['sign']} in House {nn_pt['house']}** points unmistakably toward a life path of {SIGN_TRAITS[nn_pt['sign']]['en']} evolution within the {nn_h_info['title_en']}."
        )
        nn_text_he = (
            f"**ראש הדרקון (הייעוד האבולוציוני והגורלי) במזל {nn_sign_he} בבית {nn_pt['house']}** מצביע בבירור על נתיב גורל {SIGN_TRAITS[nn_pt['sign']]['he']} בזירת {nn_h_info['title_he']}."
        )

    blind_portrait = {
        "archetype_title_en": f"The {asc_sign}-Rising / {mc_sign}-MC Visionary Architect ({sun['sign']} Sun · {moon['sign']} Moon)",
        "archetype_title_he": f"ארכיטיפ {asc_sign_he} באופק עם ייעוד {mc_sign_he} (שמש ב{sun_sign_he} · ירח ב{moon_sign_he})",
        "paragraphs_en": [
            f"1. **Frontline Persona & Operating System (Ascendant & Chart Ruler)**: Without knowing who this chart belongs to, an expert astrologist immediately sees an individual with **{asc_sign} Rising ({asc_pt['deg']}°)** steered by **{ruler_planet['name']} in {ruler_planet['sign']} (House {ruler_planet['house']})**. {asc_section['en']}",
            f"2. **Mental Architecture & Communication (Mercury & 3rd House)**: With **Mercury in {mercury['sign']} (House {mercury['house']})** and **Uranus in {uranus['sign']} (House {uranus['house']})**, this mind operates with {SIGN_TRAITS[mercury['sign']]['en']} intensity and {SIGN_TRAITS[uranus['sign']]['en']} originality. Key structural signatures detected: **{pattern_highlights_en}**.",
            f"3. **Emotional & Material Engine (Moon & 2nd/6th Houses)**: The **Moon in {moon['sign']} in House {moon['house']}** reveals that inner security is not found in passive comfort, but in {SIGN_TRAITS[moon['sign']]['en']} mastery over the {moon_h_info['title_en']}.",
            f"4. **Vocation, Power & Global Scale (MC, Mars, Jupiter, Saturn & Pluto)**: With **Midheaven in {mc_sign}** ruled by **{mc_ruler_planet['name']} in {mc_ruler_planet['sign']} (House {mc_ruler_planet['house']})**, **Jupiter in {jupiter['sign']} (House {jupiter['house']})**, **Saturn in {saturn['sign']} (House {saturn['house']})**, and **Pluto in {pluto['sign']} (House {pluto['house']})**, this chart is wired for high-stakes risk, monumental structural engineering, and reshaping future horizons ({nn_text_en})."
        ],
        "paragraphs_he": [
            f"1. **זהות פרונטלית ומערכת הפעלה (אופק ושליט המפה)**: מבלי לדעת למי שייכת המפה, אסטרולוג מומחה מזהה מיד אדם/ישות עם **אופק {asc_sign_he} ({asc_pt['deg']}°)** המנווט על ידי **{ruler_name_he} במזל {ruler_sign_he} (בית {ruler_planet['house']})**. {asc_section['he']}",
            f"2. **מבנה החשיבה, תקשורת וחדשנות (מרקורי ואורנוס)**: עם **מרקורי ב{SIGN_META[mercury['sign']]['he']} (בית {mercury['house']})** ו**אורנוס ב{SIGN_META[uranus['sign']]['he']} (בית {uranus['house']})**, המוח פועל בעוצמה {SIGN_TRAITS[mercury['sign']]['he']} ובמקוריות {SIGN_TRAITS[uranus['sign']]['he']}. חתימות מבניות בולטות במפה: **{pattern_highlights_he}**.",
            f"3. **המנוע הרגשי והחומרי (ירח ומשאבים)**: **הירח במזל {moon_sign_he} בבית {moon['house']}** חושף שהביטחון הפנימי אינו מושג דרך מנוחה פסיבית, אלא דרך שליטה {SIGN_TRAITS[moon['sign']]['he']} בזירת {moon_h_info['title_he']}.",
            f"4. **ייעוד, קריירה, הון וקנה מידה עולמי (רום שמיים, מארס, יופיטר, שבתאי ופלוטו)**: עם **רום שמיים ב{mc_sign_he}** הנשלט על ידי **{mc_ruler_he} ב{mc_ruler_sign_he} (בית {mc_ruler_planet['house']})**, לצד **יופיטר ב{SIGN_META[jupiter['sign']]['he']} (בית {jupiter['house']})**, **שבתאי ב{SIGN_META[saturn['sign']]['he']} (בית {saturn['house']})** ו**פלוטו ב{SIGN_META[pluto['sign']]['he']} (בית {pluto['house']})**, המפה בנויה ללקיחת סיכונים אדירים, בניית מערכות בקנה מידה היסטורי ועיצוב העתיד ({nn_text_he})."
        ]
    }

    return {
        "ascendant_section": asc_section,
        "mc_section": mc_section,
        "big_three_section": big_three_section,
        "balance": balance,
        "patterns": patterns,
        "planets_interpreted": planets_interpreted,
        "natal_aspects_interpreted": natal_aspects_interpreted,
        "blind_portrait": blind_portrait,
    }


def compute_transits_report(natal_sys, transit_sys, transit_date_str, get_house_fn):
    """
    Compare current sky transits (transit_sys) against a natal chart (natal_sys).
    Returns house transits, transit-to-natal aspects, and an executive forecast in EN & HE.
    """
    natal_cusps = [h["cusp"] for h in natal_sys["houses"]]
    natal_points = natal_sys["planets"] + [natal_sys["asc_point"], natal_sys["mc_point"]]
    if natal_sys.get("north_node"):
        natal_points.append(natal_sys["north_node"])

    transit_bodies = transit_sys["planets"] + ([transit_sys["north_node"]] if transit_sys.get("north_node") else [])

    # 1. Which Natal House each transiting planet occupies
    house_transits = []
    for tp in transit_bodies:
        n_house = get_house_fn(tp["lon"], natal_cusps)
        h_info = HOUSE_MEANINGS.get(n_house, HOUSE_MEANINGS[1])
        tp_he = PLANET_HE.get(tp["name"], tp["name"])
        sign_he = SIGN_META.get(tp["sign"], {}).get("he", tp["sign"])
        rx_badge = " (Rx)" if tp.get("retrograde") else ""
        house_transits.append({
            "planet": tp["name"],
            "planet_he": tp_he,
            "symbol": tp["symbol"],
            "color": tp["color"],
            "formatted": tp["formatted"] + rx_badge,
            "sign": tp["sign"],
            "sign_he": sign_he,
            "retrograde": tp.get("retrograde", False),
            "natal_house": n_house,
            "en": f"**Transit {tp['symbol']} {tp['name']}{rx_badge} in {tp['sign']}** is transiting **Natal House {n_house}** ({h_info['title_en']}), activating {PLANET_CORE_ROLES.get(tp['name'], {}).get('en', '').lower()} in this life sector.",
            "he": f"**מעבר {tp['symbol']} {tp_he}{rx_badge} במזל {sign_he}** נע כעת ב**בית {n_house} במפת הלידה** ({h_info['title_he']}), ומפעיל אנרגיה של {PLANET_CORE_ROLES.get(tp['name'], {}).get('he', '')} בגזרה זו."
        })

    # 2. Transit-to-Natal Aspects
    transit_aspect_cfgs = [
        ("Conjunction", 0, 4.5, "#fbbf24", "harmonious", "צמידות (0°)"),
        ("Opposition", 180, 4.0, "#f43f5e", "challenging", "מולות (180°)"),
        ("Trine", 120, 4.0, "#10b981", "harmonious", "טריין (120°)"),
        ("Square", 90, 4.0, "#ef4444", "challenging", "סקוויר (90°)"),
        ("Sextile", 60, 3.0, "#06b6d4", "harmonious", "סקסטיל (60°)"),
    ]

    planet_priority = {
        "Pluto": 10, "Neptune": 9, "Uranus": 9, "Saturn": 8, "Jupiter": 8,
        "North Node": 7, "Mars": 6, "Sun": 5, "Venus": 4, "Mercury": 4, "Moon": 3
    }

    transit_aspects = []
    for tp in transit_bodies:
        for np_pt in natal_points:
            diff = abs(tp["lon"] - np_pt["lon"])
            diff = min(diff, 360.0 - diff)
            for asp_name, angle, max_orb, color, nature, asp_he in transit_aspect_cfgs:
                orb = abs(diff - angle)
                if orb <= max_orb:
                    tp_he = PLANET_HE.get(tp["name"], tp["name"])
                    np_he = PLANET_HE.get(np_pt["name"], np_pt["name"])
                    t_role = PLANET_CORE_ROLES.get(tp["name"], {"en": tp["name"], "he": tp_he})
                    n_role = PLANET_CORE_ROLES.get(np_pt["name"], {"en": np_pt["name"], "he": np_he})
                    importance = planet_priority.get(tp["name"], 5) * (1.5 if np_pt["name"] in ("Sun", "Moon", "Ascendant", "Midheaven", "Mercury", "Mars") else 1.0) * (1.0 - orb / (max_orb + 1.0))

                    if nature == "harmonious":
                        desc_en = f"Transit {tp['name']} ({tp['sign']}) forms a {asp_name} (orb {orb:.1f}°) to Natal {np_pt['name']} ({np_pt['sign']}), opening a powerful window of expansion, alignment, and momentum for {n_role['en'].lower()}."
                        desc_he = f"מעבר {tp_he} (ב{SIGN_META.get(tp['sign'], {}).get('he', tp['sign'])}) יוצר {asp_he} (סטייה {orb:.1f}°) אל {np_he} במפת הלידה, ופותח חלון הזדמנויות, תנופה וחיזוק סביב {n_role['he']}."
                    else:
                        desc_en = f"Transit {tp['name']} ({tp['sign']}) forms a high-pressure {asp_name} (orb {orb:.1f}°) to Natal {np_pt['name']} ({np_pt['sign']}), demanding structural adaptation, decisive leadership, and resilience around {n_role['en'].lower()}."
                        desc_he = f"מעבר {tp_he} (ב{SIGN_META.get(tp['sign'], {}).get('he', tp['sign'])}) יוצר {asp_he} מאתגר (סטייה {orb:.1f}°) אל {np_he} במפת הלידה, הדורש הסתגלות אסטרטגית, קבלת החלטות נחושה ועמידות סביב {n_role['he']}."

                    transit_aspects.append({
                        "t_planet": tp["name"],
                        "t_planet_he": tp_he,
                        "t_symbol": tp["symbol"],
                        "t_lon": tp["lon"],
                        "t_sign": tp["sign"],
                        "n_planet": np_pt["name"],
                        "n_planet_he": np_he,
                        "n_symbol": np_pt["symbol"],
                        "n_lon": np_pt["lon"],
                        "n_sign": np_pt["sign"],
                        "aspect": asp_name,
                        "aspect_he": asp_he,
                        "angle": angle,
                        "orb": round(orb, 1),
                        "color": color,
                        "nature": nature,
                        "importance": round(importance, 2),
                        "en": desc_en,
                        "he": desc_he,
                    })
                    break

    transit_aspects.sort(key=lambda x: (-x["importance"], x["orb"]))

    # Build Executive Forecast Summary
    outer_map = {h["planet"]: h for h in house_transits}
    pluto_h = outer_map.get("Pluto", {}).get("natal_house", 1)
    saturn_h = outer_map.get("Saturn", {}).get("natal_house", 1)
    jupiter_h = outer_map.get("Jupiter", {}).get("natal_house", 1)
    uranus_h = outer_map.get("Uranus", {}).get("natal_house", 1)

    top_hits_en = "; ".join(f"Transit {a['t_planet']} {a['aspect']} Natal {a['n_planet']} ({a['orb']}°)" for a in transit_aspects[:3]) or "Steady orbital progression across natal houses"
    top_hits_he = "; ".join(f"מעבר {a['t_planet_he']} ב{a['aspect_he']} אל {a['n_planet_he']} ({a['orb']}°)" for a in transit_aspects[:3]) or "תנועה פלנטרית יציבה בבתים"

    forecast_en = (
        f"**Current Sky Synthesis ({transit_date_str})**: "
        f"Jupiter is expanding **Natal House {jupiter_h}** ({HOUSE_MEANINGS[jupiter_h]['title_en']}), "
        f"while Saturn tests and structures **Natal House {saturn_h}** ({HOUSE_MEANINGS[saturn_h]['title_en']}). "
        f"Uranus is electrifying **House {uranus_h}**, and Pluto is driving deep long-term transformation in **House {pluto_h}**. "
        f"Major active transit hits right now: **{top_hits_en}**."
    )
    forecast_he = (
        f"**סינתזת מעברים לתאריך ({transit_date_str})**: "
        f"יופיטר (צדק) מרחיב ומעצים כעת את **בית {jupiter_h}** ({HOUSE_MEANINGS[jupiter_h]['title_he']}), "
        f"בעוד שבתאי בונה ומאתגר את **בית {saturn_h}** ({HOUSE_MEANINGS[saturn_h]['title_he']}). "
        f"אורנוס מחולל שינויים וחדשנות ב**בית {uranus_h}**, ופלוטו מוביל טרנספורמציה עמוקה ב**בית {pluto_h}**. "
        f"היבטי המעבר החזקים ביותר כעת: **{top_hits_he}**."
    )

    return {
        "date": transit_date_str,
        "house_transits": house_transits,
        "transit_aspects": transit_aspects[:18],
        "forecast_en": forecast_en,
        "forecast_he": forecast_he,
    }


def build_interaction_dossier(c1_sys, c2_sys, synastry_sys, name1, name2, get_house_fn):
    """
    Build expert 2-Entity Interaction analysis (for 2 People, Person + Company, or 2 Companies),
    including House Overlays (Entity A's planets in Entity B's Houses and vice versa)
    and 6-Dimensional Synergy Synthesis.
    """
    cusps1 = [h["cusp"] for h in c1_sys["houses"]]
    cusps2 = [h["cusp"] for h in c2_sys["houses"]]

    key_bodies = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Pluto"]
    p1_dict = {**c1_sys["planets_dict"], "Ascendant": c1_sys["asc_point"], "Midheaven": c1_sys["mc_point"]}
    p2_dict = {**c2_sys["planets_dict"], "Ascendant": c2_sys["asc_point"], "Midheaven": c2_sys["mc_point"]}

    overlays_2_in_1 = []
    overlays_1_in_2 = []

    for b_name in key_bodies + ["Ascendant", "Midheaven"]:
        pt2 = p2_dict.get(b_name)
        if pt2:
            h_in_1 = get_house_fn(pt2["lon"], cusps1)
            h_info = HOUSE_MEANINGS.get(h_in_1, HOUSE_MEANINGS[1])
            b_he = PLANET_HE.get(b_name, b_name)
            overlays_2_in_1.append({
                "planet": b_name,
                "planet_he": b_he,
                "symbol": pt2["symbol"],
                "sign": pt2["sign"],
                "sign_he": SIGN_META.get(pt2["sign"], {}).get("he", pt2["sign"]),
                "target_house": h_in_1,
                "en": f"**{name2}'s {pt2['symbol']} {b_name}** falls in **{name1}'s House {h_in_1}** ({h_info['title_en']}), directly energizing {name1}'s {h_info['en']}.",
                "he": f"**{pt2['symbol']} {b_he} של {name2}** נופל ב**בית {h_in_1} של {name1}** ({h_info['title_he']}), ומפעיל בעוצמה את תחום זה אצל {name1}."
            })

        pt1 = p1_dict.get(b_name)
        if pt1:
            h_in_2 = get_house_fn(pt1["lon"], cusps2)
            h_info = HOUSE_MEANINGS.get(h_in_2, HOUSE_MEANINGS[1])
            b_he = PLANET_HE.get(b_name, b_name)
            overlays_1_in_2.append({
                "planet": b_name,
                "planet_he": b_he,
                "symbol": pt1["symbol"],
                "sign": pt1["sign"],
                "sign_he": SIGN_META.get(pt1["sign"], {}).get("he", pt1["sign"]),
                "target_house": h_in_2,
                "en": f"**{name1}'s {pt1['symbol']} {b_name}** falls in **{name2}'s House {h_in_2}** ({h_info['title_en']}), imprinting {name1}'s {b_name} authority onto {name2}'s {h_info['en']}.",
                "he": f"**{pt1['symbol']} {b_he} של {name1}** נופל ב**בית {h_in_2} של {name2}** ({h_info['title_he']}), ומטביע את חותם {b_he} של {name1} על גזרה זו של {name2}."
            })

    # Compute executive & wealth scores from synastry aspects + house overlays
    power_raw = 55.0
    wealth_raw = 55.0
    for asp in synastry_sys["aspects"]:
        pair = {asp["p1_planet"], asp["p2_planet"]}
        pts = asp["points"]
        if pair & {"Mars", "Pluto", "Sun", "Midheaven", "Saturn"}:
            power_raw += abs(pts) * 0.85 if asp["nature"] == "harmonious" else abs(pts) * 0.35
        if pair & {"Jupiter", "Venus", "Pluto", "Sun", "Moon"}:
            wealth_raw += pts * 1.1 if asp["nature"] == "harmonious" else pts * 0.4

    # Boost if key planets fall in Houses 2, 8, 10, 11
    for ov in overlays_2_in_1 + overlays_1_in_2:
        if ov["target_house"] in (10, 1, 11) and ov["planet"] in ("Sun", "Mars", "Jupiter", "Pluto", "Midheaven"):
            power_raw += 3.5
        if ov["target_house"] in (2, 8, 5, 11) and ov["planet"] in ("Sun", "Venus", "Jupiter", "Pluto", "Moon"):
            wealth_raw += 3.5

    power_score = int(max(30, min(99, round(power_raw))))
    wealth_score = int(max(30, min(99, round(wealth_raw))))

    top_asps = synastry_sys["aspects"][:4]
    top_asps_en = "; ".join(f"{name1}'s {a['p1_planet']} {a['aspect']} {name2}'s {a['p2_planet']} ({a['orb']}°)" for a in top_asps)
    top_asps_he = "; ".join(f"{PLANET_HE.get(a['p1_planet'], a['p1_planet'])} של {name1} ב{a['aspect']} מול {PLANET_HE.get(a['p2_planet'], a['p2_planet'])} של {name2} ({a['orb']}°)" for a in top_asps)

    synthesis_en = (
        f"**Expert Interaction Synthesis ({name1} ⇄ {name2})**: "
        f"Across both personal and organizational/strategic dimensions, {name1} ({c1_sys['sun_sign']} Sun, {c1_sys['asc_sign']} ASC) and {name2} ({c2_sys['sun_sign']} Sun, {c2_sys['asc_sign']} ASC) form **{len(synastry_sys['aspects'])} inter-chart aspects**. "
        f"Tightest geometric locks: **{top_asps_en}**. "
        f"Executive Power & Mission Synergy reaches **{power_score}%**, while Resource/Wealth Flow reaches **{wealth_score}%**."
    )
    synthesis_he = (
        f"**סינתזת אינטראקציה מקצועית ({name1} ⇄ {name2})**: "
        f"הן ברמה האישית והן ברמה הארגונית/אסטרטגית, {name1} (שמש ב{SIGN_META[c1_sys['sun_sign']]['he']}, אופק {SIGN_META[c1_sys['asc_sign']]['he']}) ו-{name2} (שמש ב{SIGN_META[c2_sys['sun_sign']]['he']}, אופק {SIGN_META[c2_sys['asc_sign']]['he']}) יוצרים **{len(synastry_sys['aspects'])} היבטים בין-מפתים**. "
        f"הנעילות הגיאומטריות המדויקות ביותר: **{top_asps_he}**. "
        f"מדד העוצמה והגשמת היעדים המשותף עומד על **{power_score}%**, ומדד זרימת המשאבים וההון עומד על **{wealth_score}%**."
    )

    return {
        "overlays_2_in_1": overlays_2_in_1,
        "overlays_1_in_2": overlays_1_in_2,
        "power_score": power_score,
        "wealth_score": wealth_score,
        "synthesis_en": synthesis_en,
        "synthesis_he": synthesis_he,
    }


ELON_MUSK_CASE_STUDY = {
    "subject_blind_label_en": "Blind Chart Subject #1971-0628 (Born 1971-06-28, 07:30 SAST, Pretoria)",
    "subject_blind_label_he": "נבדק עיוור #1971-0628 (נולד ב-28.06.1971, שעה 07:30, פרטוריה)",
    "real_identity_en": "Elon Musk (CEO of SpaceX, Tesla, xAI, Neuralink; Owner of X)",
    "real_identity_he": "אילון מאסק (מייסד ומנכ״ל SpaceX, טסלה, Neuralink, xAI ובעלי X)",
    "comparisons": [
        {
            "factor_en": "Ascendant 13°31' Cancer + Mercury 14°04' Cancer Conjunct ASC (0.5° orb)",
            "factor_he": "אופק 13°31' בסרטן + מרקורי ב-14°04' סרטן בצמידות מדויקת לאופק (סטייה 0.5°!)",
            "blind_deduction_en": "Purely from the chart: An individual whose raw intellect, voice, and rapid mental calculations sit directly on the frontline persona (0.5° from the horizon). Coupled with Cancer Rising and Sun in Cancer (House 12), their life obsession is framed around existential preservation ('saving the ark/species'), yet delivered with blunt, hyper-analytical intensity.",
            "blind_deduction_he": "מהמפה בלבד (ללא ידיעת השם): אדם שהשכל, התקשורת והחישוב האנליטי שלו יושבים בדיוק של חצי מעלה על האופק. בשילוב אופק סרטן ושמש בסרטן (בית 12), האובססיה הקיומית שלו ממוקדת ב'הצלת התיבה/המין האנושי' ושימור קיומי, אך מבוטאת בחזית אינטלקטואלית חדה וישירה.",
            "reality_match_en": "Elon Musk's entire public identity is driven by existential preservation of consciousness (making life multi-planetary, sustainable energy, AI safety) combined with relentless first-principles engineering calculations and constant direct communication.",
            "reality_match_he": "כל זהותו הציבורית של מאסק מונעת מחרדה קיומית לעתיד האנושות (הפיכת האנושות לבין-פלנטרית, אנרגיה בת-קיימא) בשילוב חשיבה מבוססת עקרונות-ראשוניים (First Principles) ותקשורת ישירה בלתי פוסקת."
        },
        {
            "factor_en": "Sun & Mercury-ASC Square Uranus (9°29' Libra) in the 3rd House (Vehicles, Transit & Media)",
            "factor_he": "שמש, מרקורי ואופק בריבוע (90°) לאורנוס (9°29' מאזניים) בבית 3 (תחבורה, רכבים, תקשורת ומדיה)",
            "blind_deduction_en": "Purely from the chart: A textbook triple-Uranian disruptor. Uranus in the 3rd House squaring Sun, Mercury, and Ascendant predicts someone who shocks the world by revolutionizing 3rd-House domains: automobiles/transportation, telecommunications/satellites, neural-computer interfaces, and digital media platforms—while exhibiting erratic, rebellious, lightning-bolt behavior.",
            "blind_deduction_he": "מהמפה בלבד: חתימה קלאסית של מהפכן אוראני משולש. אורנוס בבית 3 (בית הרכבים, התחבורה, התקשורת והמדיה) היוצר ריבוע לשמש, למרקורי ולאופק מנבא אדם שישבש לחלוטין את תחומי בית 3: מכוניות ותחבורה, לוויינים ותקשורת, ממשקי מוח-מחשב ופלטפורמות מדיה — תוך התנהלות מרדנית, בלתי צפויה ושוברת מוסכמות.",
            "reality_match_en": "Disrupted the automotive industry (Tesla electric vehicles), global telecommunications (Starlink), brain-machine interfaces (Neuralink), and social media/speech (X/Twitter)—all classic 3rd-House arenas.",
            "reality_match_he": "חולל מהפכה בתעשיית הרכב והתחבורה (טסלה, היפרלופ), תקשורת לוויינית (Starlink), ממשק מוח-מחשב (Neuralink) ורשתות תקשורת (X/טוויטר) — כולם תחומי הליבה המדויקים של בית 3 באסטרולוגיה!"
        },
        {
            "factor_en": "Midheaven (MC) 28°22' Aries Ruled by Mars in Aquarius (House 8) + North Node in Aquarius",
            "factor_he": "רום שמיים (MC) ב-28°22' טלה הנשלט ע״י מארס בדלי (בית 8) + ראש הדרקון בדלי",
            "blind_deduction_en": "Purely from the chart: Career destiny (MC in Aries) demands pioneering conquest, and its ruler (Mars) sits in futuristic Aquarius (aerospace, electricity, AI, sci-fi technology) in the 8th House (high-stakes venture capital, leveraging billions, flirting with bankruptcy/survival) conjunct the Karmic North Node in Aquarius.",
            "blind_deduction_he": "מהמפה בלבד: ייעוד הקריירה (MC בטלה) דורש כיבוש חלוצי, ושליט הקריירה (מארס) יושב במזל דלי העתידני (חלל, חשמל, טכנולוגיה עילית) בתוך בית 8 (הון סיכון, מינוף פיננסי אדיר, הליכה על חבל דק מול פשיטת רגל והישרדות) בצמידות לראש הדרקון בדלי.",
            "reality_match_en": "Pioneered private rocketry (SpaceX) and EVs by repeatedly betting his entire net worth in high-stakes 8th-House financial crunches (2008 SpaceX/Tesla near-bankruptcy, leveraged acquisitions) to build an Aquarian sci-fi future.",
            "reality_match_he": "הוביל את מהפכת החלל הפרטית (SpaceX) והרכב החשמלי תוך הימור חוזר ונשנה על כל הונו במשברי קצה פיננסיים (בית 8 — כמעט פשיטת רגל ב-2008, מינופי ענק) למען הגשמת חזון עתידני של מזל דלי."
        },
        {
            "factor_en": "Moon in Virgo (House 2) in Mutual Reception with Mercury in Cancer (House 1)",
            "factor_he": "ירח בבתולה (בית 2) בקבלה הדדית עם מרקורי בסרטן (בית 1)",
            "blind_deduction_en": "Purely from the chart: Emotional safety (Moon) is locked into Virgo in the 2nd House of wealth and material production—indicating an obsessive workaholic who micromanages manufacturing tolerances, sleeps on factory floors, and builds massive material valuation.",
            "blind_deduction_he": "מהמפה בלבד: הצורך הרגשי (ירח) נעול במזל בתולה ההנדסי והפרפקציוניסטי בתוך בית 2 (הון, ייצור וערך חומרי) — מעיד על וורקוהוליק קיצוני היורד לפרטי-פרטים הנדסיים בפס הייצור ובונה שווי כלכלי עצום.",
            "reality_match_en": "Famous for sleeping on the Tesla factory floor during 'production hell', obsessing over micron-level manufacturing tolerances, and becoming the world's wealthiest individual (House 2).",
            "reality_match_he": "מפורסם בכך שישן על רצפת המפעל של טסלה בתקופות 'גיהינום הייצור', יורד לרמת המיקרון ההנדסי, והפך לאדם העשיר בעולם (בית 2)."
        },
        {
            "factor_en": "Saturn in Gemini (House 11) Opposite Jupiter-Neptune (House 5) Channeled into Pluto in Virgo (0.6° orb)",
            "factor_he": "שבתאי בתאומים (בית 11) מול צמידות יופיטר-נפטון (בית 5) המתועלים לפלוטו בבתולה (סטייה 0.6°!)",
            "blind_deduction_en": "Purely from the chart: The 'Impossible Dream Made Physical' wedge. Jupiter-Neptune in House 5 dreams of mythic, interplanetary gambles, opposed by Saturn's hard laws of physics in House 11, with Pluto in Virgo (0.6° sextile to Jupiter!) forcing those dreams into industrial hardware.",
            "blind_deduction_he": "מהמפה בלבד: מבנה 'החלום הבלתי-אפשרי ההופך לחומרה'. צמידות יופיטר-נפטון בבית 5 חולמת על הימורים בקנה מידה מיתי, מול חוקי הפיזיקה הנוקשים של שבתאי בבית 11, כשפלוטו בבתולה (בדיוק של 0.6°!) כופה על החלום להפוך להנדסה תעשייתית.",
            "reality_match_en": "Landing orbital rocket boosters vertically and mass-producing reusable spacecraft—turning impossible sci-fi visions into rigorous physics-constrained engineering.",
            "reality_match_he": "הנחתת טילי שיגור אנכית וייצור המוני של חלליות רב-פעמיות — הפיכת מדע בדיוני להנדסה פיזיקלית תעשייתית."
        }
    ]
}

