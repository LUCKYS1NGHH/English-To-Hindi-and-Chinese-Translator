print(''''##:::::::'##::::'##::'######::'##:::'##:'##:::'##::'######:::::'##:::'##::: ##::'######:::'##::::'##:'##::::'##:
 ##::::::: ##:::: ##:'##... ##: ##::'##::. ##:'##::'##... ##::'####::: ###:: ##:'##... ##:: ##:::: ##: ##:::: ##:
 ##::::::: ##:::: ##: ##:::..:: ##:'##::::. ####::: ##:::..:::.. ##::: ####: ##: ##:::..::: ##:::: ##: ##:::: ##:
 ##::::::: ##:::: ##: ##::::::: #####::::::. ##::::. ######::::: ##::: ## ## ##: ##::'####: #########: #########:
 ##::::::: ##:::: ##: ##::::::: ##. ##:::::: ##:::::..... ##:::: ##::: ##. ####: ##::: ##:: ##.... ##: ##.... ##:
 ##::::::: ##:::: ##: ##::: ##: ##:. ##::::: ##::::'##::: ##:::: ##::: ##:. ###: ##::: ##:: ##:::: ##: ##:::: ##:
 ########:. #######::. ######:: ##::. ##:::: ##::::. ######:::'######: ##::. ##:. ######::: ##:::: ##: ##:::: ##:
........:::.......::::......:::..::::..:::::..::::::......::::......::..::::..:::......::::..:::::..::..:::::..::''')

# Dictionary for translations
translations_dict = {
    "hello": {
        "Chinese (Simplified)": "你好 (nǐ hǎo)",
        "Hindi": "नमस्ते (namaste)"
    },
    "food": {
        "Chinese (Simplified)": "食物 (shí wù)",
        "Hindi": "खाना (khaana)"
    },
    "bat": {
        "Chinese (Simplified)": "蝙蝠 (biān fú)",
        "Hindi": "चमगादड़ (Chamgādaṛ)"
    },
    "language": {
        "Chinese (Simplified)": "语言 (yǔ yán)",
        "Hindi": "भाषा (bhāṣā)"
    },
    "apple": {
        "Chinese (Simplified)": "苹果 (píng guǒ)",
        "Hindi": "सेब (seb)"
    },
    "banana": {
        "Chinese (Simplified)": "香蕉 (xiāng jiāo)",
        "Hindi": "केला (kelā)"
    },
    "orange": {
        "Chinese (Simplified)": "橙子 (chéng zi)",
        "Hindi": "संतरा (santrā)"
    },
    "grape": {
        "Chinese (Simplified)": "葡萄 (pú táo)",
        "Hindi": "अंगूर (angūr)"
    },
    "mango": {
        "Chinese (Simplified)": "芒果 (máng guǒ)",
        "Hindi": "आम (ām)"
    },
    "pineapple": {
        "Chinese (Simplified)": "菠萝 (bō luó)",
        "Hindi": "अनानास (anānās)"
    },
    "watermelon": {
        "Chinese (Simplified)": "西瓜 (xī guā)",
        "Hindi": "तरबूज (tarbūz)"
    },
    "peach": {
        "Chinese (Simplified)": "桃子 (táo zi)",
        "Hindi": "आड़ू (āḍū)"
    },
    "strawberry": {
        "Chinese (Simplified)": "草莓 (cǎo méi)",
        "Hindi": "स्ट्रॉबेरी (strawberry)"
    },
    "kiwi": {
        "Chinese (Simplified)": "奇异果 (qí yì guǒ)",
        "Hindi": "कीवी (kīvī)"
    },
    "cherry": {
        "Chinese (Simplified)": "樱桃 (yīng táo)",
        "Hindi": "चेरी (cherī)"
    },
    "pear": {
        "Chinese (Simplified)": "梨 (lí)",
        "Hindi": "नाशपाती (nāśpātī)"
    },
    "apricot": {
        "Chinese (Simplified)": "杏子 (xìng zi)",
        "Hindi": "खुबानी (khubānī)"
    },
    "pomegranate": {
        "Chinese (Simplified)": "石榴 (shí liú)",
        "Hindi": "अनार (anār)"
    },
    "plum": {
        "Chinese (Simplified)": "李子 (lǐ zi)",
        "Hindi": "आलूबुखारा (ālūbukhārā)"
    },
    "lemon": {
        "Chinese (Simplified)": "柠檬 (níng méng)",
        "Hindi": "नींबू (nīmbū)"
    },
    "coconut": {
        "Chinese (Simplified)": "椰子 (yē zi)",
        "Hindi": "नारियल (nāriyāl)"
    },
    "papaya": {
        "Chinese (Simplified)": "木瓜 (mù guā)",
        "Hindi": "पपीता (papītā)"
    },
    "fig": {
        "Chinese (Simplified)": "无花果 (wú huā guǒ)",
        "Hindi": "अंजीर (anjīr)"
    },
    "dragon fruit": {
        "Chinese (Simplified)": "火龙果 (huǒ lóng guǒ)",
        "Hindi": "ट्रेगन फ्रूट (ṭrēgan frūṭ)"
    },
    "melon": {
        "Chinese (Simplified)": "甜瓜 (tián guā)",
        "Hindi": "खरबूजा (kharbūjā)"
    },
    "guava": {
        "Chinese (Simplified)": "番石榴 (fān shí liú)",
        "Hindi": "अमरूद (amrūd)"
    },
    "red": {
        "Chinese (Simplified)": "红色 (hóng sè)",
        "Hindi": "लाल (lāl)"
    },
    "blue": {
        "Chinese (Simplified)": "蓝色 (lán sè)",
        "Hindi": "नीला (nīlā)"
    },
    "green": {
        "Chinese (Simplified)": "绿色 (lǜ sè)",
        "Hindi": "हरा (harā)"
    },
    "yellow": {
        "Chinese (Simplified)": "黄色 (huáng sè)",
        "Hindi": "पीला (pīlā)"
    },
    "black": {
        "Chinese (Simplified)": "黑色 (hēi sè)",
        "Hindi": "काला (kālā)"
    },
    "white": {
        "Chinese (Simplified)": "白色 (bái sè)",
        "Hindi": "सफेद (safed)"
    },
    "orange": {
        "Chinese (Simplified)": "橙色 (chéng sè)",
        "Hindi": "नारंगी (nāraṅgī)"
    },
    "purple": {
        "Chinese (Simplified)": "紫色 (zǐ sè)",
        "Hindi": "बैंगनी (bainganī)"
    },
    "pink": {
        "Chinese (Simplified)": "粉红色 (fěn hóng sè)",
        "Hindi": "गुलाबी (gulābī)"
    },
    "brown": {
        "Chinese (Simplified)": "棕色 (zōng sè)",
        "Hindi": "भूरा (bhūrā)"
    },
    "gray": {
        "Chinese (Simplified)": "灰色 (huī sè)",
        "Hindi": "धूसर (dhūsar)"
    },
    "violet": {
        "Chinese (Simplified)": "紫罗兰色 (zǐ luó lán sè)",
        "Hindi": "बैंगनी (bainganī)"
    },
    "cyan": {
        "Chinese (Simplified)": "青色 (qīng sè)",
        "Hindi": "नस्ली (naslī)"
    },
    "indigo": {
        "Chinese (Simplified)": "靛蓝色 (diàn lán sè)",
        "Hindi": "इंडिगो (indigo)"
    },
    "beige": {
        "Chinese (Simplified)": "米色 (mǐ sè)",
        "Hindi": "बेज (bej)"
    },
    "turquoise": {
        "Chinese (Simplified)": "绿松石色 (lǜ sōng shí sè)",
        "Hindi": "फिरोजी (fīrojī)"
    },
    "teal": {
        "Chinese (Simplified)": "青绿色 (qīng lǜ sè)",
        "Hindi": "नीलापन (nīlāpan)"
    },
    "magenta": {
        "Chinese (Simplified)": "洋红色 (yáng hóng sè)",
        "Hindi": "मैजेंटा (majenṭā)"
    },
    "lavender": {
        "Chinese (Simplified)": "薰衣草色 (xūn yī cǎo sè)",
        "Hindi": "लैवेंडर (laivendar)"
    },
    "gold": {
        "Chinese (Simplified)": "金色 (jīn sè)",
        "Hindi": "सोना (sonā)"
    },
    "silver": {
        "Chinese (Simplified)": "银色 (yín sè)",
        "Hindi": "चाँदी (chāndī)"
    },
    "platinum": {
        "Chinese (Simplified)": "铂金色 (bó jīn sè)",
        "Hindi": "प्लैटिनम (platinum)"
    },
    "water": {
        "Chinese (Simplified)": "水 (shuǐ)",
        "Hindi": "पानी (paani)"
    },
    "how are you": {
        "Chinese (Simplified)": "你好吗 (nǐ hǎo ma)",
        "Hindi": "कैसे हो? (kaise ho?)"
    },
    "good night": {
        "Chinese (Simplified)": "晚安 (wǎn ān)",
        "Hindi": "शुभ रात्रि (shubh raatri)"
    },
    "carrot": {
        "Chinese (Simplified)": "胡萝卜 (hú luó bo)",
        "Hindi": "गाजर (gājar)"
    },
    "potato": {
        "Chinese (Simplified)": "土豆 (tǔ dòu)",
        "Hindi": "आलू (ālū)"
    },
    "onion": {
        "Chinese (Simplified)": "洋葱 (yáng cōng)",
        "Hindi": "प्याज (pyāj)"
    },
    "tomato": {
        "Chinese (Simplified)": "番茄 (fān qié)",
        "Hindi": "टमाटर (ṭamāṭar)"
    },
    "spinach": {
        "Chinese (Simplified)": "菠菜 (bō cài)",
        "Hindi": "पालक (pālak)"
    },
    "cucumber": {
        "Chinese (Simplified)": "黄瓜 (huáng guā)",
        "Hindi": "खीरा (khīrā)"
    },
    "cauliflower": {
        "Chinese (Simplified)": "菜花 (cài huā)",
        "Hindi": "गोभी (gōbhī)"
    },
    "broccoli": {
        "Chinese (Simplified)": "西兰花 (xī lán huā)",
        "Hindi": "ब्रोकोली (brokōlī)"
    },
    "beans": {
        "Chinese (Simplified)": "豆类 (dòu lèi)",
        "Hindi": "फली (phalī)"
    },
    "peas": {
        "Chinese (Simplified)": "豌豆 (wān dòu)",
        "Hindi": "मटर (maṭar)"
    },
    "pumpkin": {
        "Chinese (Simplified)": "南瓜 (nán guā)",
        "Hindi": "कद्दू (kaḍdū)"
    },
    "eggplant": {
        "Chinese (Simplified)": "茄子 (qié zi)",
        "Hindi": "बैंगन (baingan)"
    },
    "sweet potato": {
        "Chinese (Simplified)": "甘薯 (gān shǔ)",
        "Hindi": "शकरकंदी (śakarakandī)"
    },
    "lettuce": {
        "Chinese (Simplified)": "生菜 (shēng cài)",
        "Hindi": "सलाद पत्ता (salād pattā)"
    },
    "radish": {
        "Chinese (Simplified)": "萝卜 (luó bo)",
        "Hindi": "मूली (mūlī)"
    },
    "bell pepper": {
        "Chinese (Simplified)": "甜椒 (tián jiāo)",
        "Hindi": "शिमला मिर्च (shimlā mirch)"
    },
    "zucchini": {
        "Chinese (Simplified)": "西葫芦 (xī hú lú)",
        "Hindi": "लौकी (lauki)"
    },
    "asparagus": {
        "Chinese (Simplified)": "芦笋 (lú sǔn)",
        "Hindi": "शतावरी (śatāvarī)"
    },
    "mushroom": {
        "Chinese (Simplified)": "蘑菇 (mó gū)",
        "Hindi": "कढ़ी (kaṛhī)"
    },
    "cabbage": {
        "Chinese (Simplified)": "卷心菜 (juǎn xīn cài)",
        "Hindi": "पत्तागोभी (pattāgōbhī)"
    },
    "leek": {
        "Chinese (Simplified)": "韭菜 (jiǔ cài)",
        "Hindi": "हिरा प्याज (hirā pyāj)"
    },
    "artichoke": {
        "Chinese (Simplified)": "朝鲜蓟 (zhāo xiǎn jì)",
        "Hindi": "अर्थी (arthī)"
    },
    "celery": {
        "Chinese (Simplified)": "芹菜 (qín cài)",
        "Hindi": "शलरी (shalrī)"
    },
    "corn": {
        "Chinese (Simplified)": "玉米 (yù mǐ)",
        "Hindi": "मकई (makai)"
    },
    "chili": {
        "Chinese (Simplified)": "辣椒 (là jiāo)",
        "Hindi": "मिर्च (mirch)"
    },
    "ginger": {
        "Chinese (Simplified)": "姜 (jiāng)",
        "Hindi": "अदरक (adarak)"
    },
    "life": {
        "Hindi": "जीवन (jīvan)",
        "Chinese (Simplified)": "生命 (shēngmìng)"
    },
    "affect": {
        "Hindi": "प्रभावित करना (prabhāvit karnā)",
        "Chinese (Simplified)": "影响 (yǐngxiǎng)"
    },
    "effect": {
        "Hindi": "प्रभाव (prabhāv)",
        "Chinese (Simplified)": "效果 (xiàoguǒ)"
    },
    "peek": {
        "Hindi": "झाँकना (jhāṅknā)",
        "Chinese (Simplified)": "偷看 (tōukàn)"
    },
    "seen": {
        "Hindi": "देखा (dekha)",
        "Chinese (Simplified)": "看到 (kàndào)"
    },
    "pick": {
        "Hindi": "चुनना (cunnā)",
        "Chinese (Simplified)": "挑选 (tiāoxuǎn)"
    },
    "shave": {
        "Hindi": "दाढ़ी बनाना (dāṛhī banānā)",
        "Chinese (Simplified)": "刮胡子 (guāhúzi)"
    },
    "global": {
        "Hindi": "वैश्विक (vaišvik)",
        "Chinese (Simplified)": "全球的 (quánqiú de)"
    },
    "illegal": {
        "Hindi": "अवैध (avaidh)",
        "Chinese (Simplified)": "非法的 (fēifǎ de)"
    },
    "legal": {
        "Hindi": "कानूनी (kānūnī)",
        "Chinese (Simplified)": "合法的 (héfǎ de)"
    },
    "myths": {
        "Hindi": "मिथक (mithak)",
        "Chinese (Simplified)": "神话 (shénhuà)"
    },
    "myth": {
        "Hindi": "मिथक (mithak)",
        "Chinese (Simplified)": "神话 (shénhuà)"
    },
    "stereotypes": {
        "Hindi": "रूढ़ियाँ (rūṛhiyāṅ)",
        "Chinese (Simplified)": "刻板印象 (kèbǎn yìnxiàng)"
    },
    "message": {
        "Hindi": "संदेश (sandēś)",
        "Chinese (Simplified)": "消息 (xiāoxi)"
    },
    "about": {
        "Hindi": "के बारे में (ke bāre meṃ)",
        "Chinese (Simplified)": "关于 (guānyú)"
    },
    "expect": {
        "Hindi": "उम्मीद करना (ummīd karnā)",
        "Chinese (Simplified)": "期待 (qīdài)"
    },
    "past": {
        "Hindi": "बीता हुआ (bītā huā)",
        "Chinese (Simplified)": "过去的 (guòqù de)"
    },
    "present": {
        "Hindi": "वर्तमान (vartman)",
        "Chinese (Simplified)": "现在 (xiànzài)"
    },
    "future": {
        "Hindi": "भविष्य (bhaviṣya)",
        "Chinese (Simplified)": "未来 (wèilái)"
    },
    "rise": {
        "Hindi": "उदय (uday)",
        "Chinese (Simplified)": "上升 (shàngshēng)"
    },
    "fall": {
        "Hindi": "गिरना (girnā)",
        "Chinese (Simplified)": "下降 (xiàjiàng)"
    },
    "strategy": {
        "Hindi": "रणनीति (raṇanīti)",
        "Chinese (Simplified)": "战略 (zhànlüè)"
    },
    "proof": {
        "Hindi": "प्रमाण (pramāṇa)",
        "Chinese (Simplified)": "证据 (zhèngjù)"
    },
    "respect": {
        "Hindi": "सम्मान (sammān)",
        "Chinese (Simplified)": "尊重 (zūnjìng)"
    },
    "call": {
        "Hindi": "कॉल करना (kāl karnā)",
        "Chinese (Simplified)": "打电话 (dǎ diànhuà)"
    },
    "available": {
        "Hindi": "उपलब्ध (upalabdh)",
        "Chinese (Simplified)": "可用的 (kěyòng de)"
    },
    "banner": {
        "Hindi": "बैनर (bainar)",
        "Chinese (Simplified)": "横幅 (héngfú)"
    },
    "morning": {
        "Chinese (Simplified)": "早晨 (zǎo chén)",
        "Hindi": "सुबह (subah)"
    },
    "evening": {
        "Chinese (Simplified)": "晚上 (wǎn shàng)",
        "Hindi": "शाम (shaam)"
    },
    "love you": {
        "Chinese (Simplified)": "我爱你 (wǒ ài nǐ)",
        "Hindi": "मैं तुमसे प्यार करता हूँ (main tumse pyaar karta hoon)"
    },
    "where": {
        "Chinese (Simplified)": "哪里 (nǎ lǐ)",
        "Hindi": "कहाँ (kahaan)"
    },
    "good": {
        "Chinese (Simplified)": "好 (hǎo)",
        "Hindi": "अच्छा (accha)"
    },
    "bad": {
        "Chinese (Simplified)": "坏 (huài)",
        "Hindi": "बुरा (bura)"
    },
    "time": {
        "Chinese (Simplified)": "时间 (shí jiān)",
        "Hindi": "समय (samay)"
    },
    "day": {
        "Chinese (Simplified)": "天 (tiān)",
        "Hindi": "दिन (din)"
    },
    "night": {
        "Chinese (Simplified)": "夜晚 (yè wǎn)",
        "Hindi": "रात (raat)"
    },
    "happy": {
        "Chinese (Simplified)": "快乐 (kuài lè)",
        "Hindi": "खुश (khush)"
    },
    "sad": {
        "Chinese (Simplified)": "悲伤 (bēi shāng)",
        "Hindi": "उदास (udaas)"
    },
    "help": {
        "Chinese (Simplified)": "帮助 (bāng zhù)",
        "Hindi": "मदद (madad)"
    },
    "goodbye": {
        "Chinese (Simplified)": "再见 (zài jiàn)",
        "Hindi": "अलविदा (alvida)"
    },
    "father": {
        "Chinese (Simplified)": "父亲 (fù qīn)",
        "Hindi": "पिता (pita)"
    },
    "mother": {
        "Chinese (Simplified)": "母亲 (mǔ qīn)",
        "Hindi": "माँ (maa)"
    },
    "brother": {
        "Chinese (Simplified)": "兄弟 (xiōng dì)",
        "Hindi": "भाई (bhai)"
    },
    "sister": {
        "Chinese (Simplified)": "姐妹 (jiě mèi)",
        "Hindi": "बहन (behen)"
    },
    "son": {
        "Chinese (Simplified)": "儿子 (ér zi)",
        "Hindi": "पुत्र/बेटा (putra)"
    },
    "daughter": {
        "Chinese (Simplified)": "女儿 (nǚ ér)",
        "Hindi": "बेटी (beti)"
    },
    "friend": {
        "Chinese (Simplified)": "朋友 (péng yǒu)",
        "Hindi": "मित्र/दोस्त (dost)"
    },
    "house": {
        "Chinese (Simplified)": "房子 (fáng zi)",
        "Hindi": "घर (ghar)"
    },
    "school": {
        "Chinese (Simplified)": "学校 (xué xiào)",
        "Hindi": "स्कूल (school)"
    },
    "book": {
        "Chinese (Simplified)": "书 (shū)",
        "Hindi": "किताब (kitaab)"
    },
    "pen": {
        "Chinese (Simplified)": "钢笔 (gāng bǐ)",
        "Hindi": "कलम (kalam)"
    },
    "phone": {
        "Chinese (Simplified)": "电话 (diàn huà)",
        "Hindi": "फोन (phone)"
    },
    "computer": {
        "Chinese (Simplified)": "电脑 (diànnǎo)",
        "Hindi": "कंप्यूटर (kampyūṭar)"
    },
    "internet": {
        "Chinese (Simplified)": "互联网 (hùliánwǎng)",
        "Hindi": "इंटरनेट (intarnet)"
    },
    "keyboard": {
        "Chinese (Simplified)": "键盘 (jiànpán)",
        "Hindi": "कीबोर्ड (kībōrḍ)"
    },
    "monitor": {
        "Chinese (Simplified)": "显示器 (xiǎnshìqì)",
        "Hindi": "मॉनिटर (mōniṭar)"
    },
    "mouse": {
        "Chinese (Simplified)": "鼠标 (shǔbiāo)",
        "Hindi": "माउस (māus)"
    },
    "software": {
        "Chinese (Simplified)": "软件 (ruǎnjiàn)",
        "Hindi": "सॉफ़्टवेयर (sāfṭaveyar)"
    },
    "hardware": {
        "Chinese (Simplified)": "硬件 (yìngjiàn)",
        "Hindi": "हार्डवेयर (hārdaveyar)"
    },
    "processor": {
        "Chinese (Simplified)": "处理器 (chǔlǐqì)",
        "Hindi": "प्रोसेसर (prosesar)"
    },
    "database": {
        "Chinese (Simplified)": "数据库 (shùjùkù)",
        "Hindi": "डेटाबेस (ḍeṭābes)"
    },
    "network": {
        "Chinese (Simplified)": "网络 (wǎngluò)",
        "Hindi": "नेटवर्क (neṭavark)"
    },
    "file": {
        "Chinese (Simplified)": "文件 (wénjiàn)",
        "Hindi": "फाइल (phāil)"
    },
    "application": {
        "Chinese (Simplified)": "应用 (yìngyòng)",
        "Hindi": "एप्लिकेशन (epalikēśan)"
    },
    "program": {
        "Chinese (Simplified)": "程序 (chéngxù)",
        "Hindi": "प्रोग्राम (prōgrām)"
    },
    "code": {
        "Chinese (Simplified)": "代码 (dàimǎ)",
        "Hindi": "कोड (koḍ)"
    },
    "password": {
        "Chinese (Simplified)": "密码 (mìmǎ)",
        "Hindi": "पासवर्ड (pāsvard)"
    },
    "server": {
        "Chinese (Simplified)": "服务器 (fúwùqì)",
        "Hindi": "सर्वर (sarvar)"
    },
    "cloud": {
        "Chinese (Simplified)": "云 (yún)",
        "Hindi": "क्लाउड (klāuḍ)"
    },
    "virtual": {
        "Chinese (Simplified)": "虚拟 (xūnǐ)",
        "Hindi": "वर्चुअल (varchuval)"
    },
    "router": {
        "Chinese (Simplified)": "路由器 (lùyóuqì)",
        "Hindi": "राउटर (rāuṭar)"
    },
    "firewall": {
        "Chinese (Simplified)": "防火墙 (fánghuǒqiáng)",
        "Hindi": "फ़ायरवॉल (phāyarvāl)"
    },
    "encryption": {
        "Chinese (Simplified)": "加密 (jiāmì)",
        "Hindi": "एन्क्रिप्शन (enkripeśan)"
    },
    "algorithm": {
        "Chinese (Simplified)": "算法 (suànfǎ)",
        "Hindi": "एल्गोरिदम (elgōridam)"
    },
    "data": {
        "Chinese (Simplified)": "数据 (shùjù)",
        "Hindi": "डेटा (ḍeṭā)"
    },
    "binary": {
        "Chinese (Simplified)": "二进制 (èrjìnzhì)",
        "Hindi": "बाइनरी (bāinari)"
    },
    "compile": {
        "Chinese (Simplified)": "编译 (biānyì)",
        "Hindi": "कम्पाइल (kampāil)"
    },
    "debug": {
        "Chinese (Simplified)": "调试 (tiáoshì)",
        "Hindi": "डीबग (ḍībaga)"
    },
    "syntax": {
        "Chinese (Simplified)": "语法 (yǔfǎ)",
        "Hindi": "सिंटैक्स (siṇṭaiks)"
    },
    "framework": {
        "Chinese (Simplified)": "框架 (kuàngjià)",
        "Hindi": "फ्रेमवर्क (phremavark)"
    },
    "rain": {
        "Chinese (Simplified)": "雨 (yǔ)",
        "Hindi": "बारिश (baarish)"
    },
    "sun": {
        "Chinese (Simplified)": "太阳 (tài yáng)",
        "Hindi": "सूरज (sooraj)"
    },
    "moon": {
        "Chinese (Simplified)": "月亮 (yuè liàng)",
        "Hindi": "चाँद (chaand)"
    },
    "hot": {
        "Chinese (Simplified)": "热 (rè)",
        "Hindi": "गर्म (garm)"
    },
    "cold": {
        "Chinese (Simplified)": "冷 (lěng)",
        "Hindi": "ठंडा (thanda)"
    },
    "big": {
        "Chinese (Simplified)": "大 (dà)",
        "Hindi": "बड़ा (bada)"
    },
    "work": {
        "Chinese (Simplified)": "工作 (gōng zuò)",
        "Hindi": "काम (kaam)"
    },
    "world": {
        "Chinese (Simplified)": "世界 (shì jiè)" ,
        "Hindi": "दुनिया (duniya)"
    },
    "thank you": {
        "Chinese (Simplified)": "谢谢 (xiè xiè)" ,
        "Hindi": "धन्यवाद (dhanyavaad)"
    },
    "good morning": {
        "Chinese (Simplified)": "早上好 (zǎo shang hǎo)" ,
        "Hindi": "सुप्रभात (shubh prabhat) "
    },
    "today": {
        "Chinese (Simplified)": "今天 (jīn tiān)",
        "Hindi": "आज (aaj)"
    },
    "yes": {
        "Chinese (Simplified)": "是的 (shì de)" ,
        "Hindi": "हाँ (haan)"
    },
    "no": {
        "Chinese (Simplified)": "不是 (bù)",
        "Hindi": "नहीं (nahin)"
    },
    "please": {
        "Chinese (Simplified)": "请 (qing)",
        "Hindi": "कृपया (kripya)"
    },
    "sorry": {
        "Chinese (Simplified)": "对不起 (duì bu qǐ)",
        "Hindi": "माफ़ कीजिए (maaf kijiye)"
    },
    "friend": {
        "Chinese (Simplified)": "朋友 (péng yǒu)",
        "Hindi": "दोस्त (dost)"
    },
    "love": {
        "Chinese (Simplified)": "爱 (ài)",
        "Hindi": "प्यार (pyar)"
    },
    "goodbye": {
        "Chinese (Simplified)": "再见 (zài jiàn)",
        "Hindi": "अलविदा (alvida)"
    },
    "please": {
        "Chinese (Simplified)": "请 (qǐng)",
        "Hindi": "कृपया (kripya)"
    },
    "sorry": {
        "Chinese (Simplified)": "对不起 (duì bù qǐ)",
        "Hindi": "माफ़ करना (maaf karna)"
    },
    "good": {
        "Chinese (Simplified)": "好 (hǎo)",
        "Hindi": "अच्छा (acchā)"
    },
    "bad": {
        "Chinese (Simplified)": "坏 (huài)",
        "Hindi": "बुरा (burā)"
    },
    "big": {
        "Chinese (Simplified)": "大 (dà)",
        "Hindi": "बड़ा (baṛā)"
    },
    "small": {
        "Chinese (Simplified)": "小 (xiǎo)",
        "Hindi": "छोटा (choṭā)"
    },
    "fast": {
        "Chinese (Simplified)": "快 (kuài)",
        "Hindi": "तेज़ (tez)"
    },
    "slow": {
        "Chinese (Simplified)": "慢 (màn)",
        "Hindi": "धीमा (dhīma)"
    },
    "hot": {
        "Chinese (Simplified)": "热 (rè)",
        "Hindi": "गर्म (garm)"
    },
    "cold": {
        "Chinese (Simplified)": "冷 (lěng)",
        "Hindi": "ठंडा (ṭhaṇḍā)"
    },
    "water": {
        "Chinese (Simplified)": "水 (shuǐ)",
        "Hindi": "पानी (pānī)"
    },
    "food": {
        "Chinese (Simplified)": "食物 (shí wù)",
        "Hindi": "खाना (khānā)"
    },
    "constitution": {
        "Hindi": "संविधान (saṃvidhān)",
        "Chinese (Simplified)": "宪法 (xiànfǎ)"
    },
    "bring": {
        "Hindi": "लाना (lānā)",
        "Chinese (Simplified)": "带来 (dài lái)"
    },
    "worst": {
        "Hindi": "सबसे बुरा (sabse burā)",
        "Chinese (Simplified)": "最坏的 (zuì huài de)"
    },
    "extent": {
        "Hindi": "सीमा (sīmā)",
        "Chinese (Simplified)": "程度 (chéngdù)"
    },
    "suicide": {
        "Hindi": "आत्महत्या (ātmahatyā)",
        "Chinese (Simplified)": "自杀 (zìshā)"
    },
    "card": {
        "Hindi": "कार्ड (kārd)",
        "Chinese (Simplified)": "卡片 (kǎpiàn)"
    },
    "under": {
        "Hindi": "नीचे (nīce)",
        "Chinese (Simplified)": "在...下面 (zài...xiàmian)"
    },
    "cover": {
        "Hindi": "ढकना (ḍhaknā)",
        "Chinese (Simplified)": "覆盖 (fùgài)"
    },
    "killer": {
        "Hindi": "हत्यारा (hatyarā)",
        "Chinese (Simplified)": "杀手 (shāshǒu)"
    },
    "assassin": {
        "Hindi": "हत्यारा (hatyarā)",
        "Chinese (Simplified)": "刺客 (cìkè)"
    },
    "celebrate": {
        "Hindi": "मनाना (manānā)",
        "Chinese (Simplified)": "庆祝 (qìngzhù)"
    },
    "using": {
        "Hindi": "इस्तेमाल करके (istēmāl karke)",
        "Chinese (Simplified)": "使用 (shǐyòng)"
    },
    "open": {
        "Hindi": "खोलना (kholnā)",
        "Chinese (Simplified)": "打开 (dǎkāi)"
    },
    "close": {
        "Hindi": "बंद करना (band karnā)",
        "Chinese (Simplified)": "关闭 (guānbì)"
    },
    "will": {
        "Hindi": "इच्छाशक्ति (icchāśakti)",
        "Chinese (Simplified)": "意志 (yìzhì)"
    },
    "fit": {
        "Hindi": "फिट होना (fit honā)",
        "Chinese (Simplified)": "适合 (shìhé)"
    },
    "fill": {
        "Hindi": "भरना (bharna)",
        "Chinese (Simplified)": "填满 (tiánmǎn)"
    },
    "chaos": {
        "Hindi": "अव्यवस्था (avyavasthā)",
        "Chinese (Simplified)": "混乱 (hùnluàn)"
    },
    "explain": {
        "Hindi": "समझाना (samajhānā)",
        "Chinese (Simplified)": "解释 (jiěshì)"
    },
    "response": {
        "Hindi": "प्रतिक्रिया (pratikriyā)",
        "Chinese (Simplified)": "回应 (huíyìng)"
    },
    "respond": {
        "Hindi": "जवाब देना (javāb denā)",
        "Chinese (Simplified)": "回应 (huíyìng)"
    },
    "figure": {
        "Hindi": "आकृति (ākṛti)",
        "Chinese (Simplified)": "数字 (shùzì)"
    },
    "insane": {
        "Hindi": "पागल (pāgal)",
        "Chinese (Simplified)": "疯狂的 (fēngkuáng de)"
    },
    "bomb": {
        "Hindi": "बम (bam)",
        "Chinese (Simplified)": "炸弹 (zhàdàn)"
    },
    "blast": {
        "Hindi": "विस्फोट (visphot)",
        "Chinese (Simplified)": "爆炸 (bàozhà)"
    },
    "emotional": {
        "Hindi": "भावनात्मक (bhāvnātmak)",
        "Chinese (Simplified)": "情感的 (qínggǎn de)"
    },
    "damage": {
        "Hindi": "नुकसान (nuksān)",
        "Chinese (Simplified)": "损害 (sǔnhài)"
    },
    "build": {
        "Hindi": "बनाना (banānā)",
        "Chinese (Simplified)": "建造 (jiànzào)"
    },
    "control": {
        "Hindi": "नियंत्रण (niyantṛaṇ)",
        "Chinese (Simplified)": "控制 (kòngzhì)"
    },
    "debt": {
        "Hindi": "ऋण (ṛṇa)",
        "Chinese (Simplified)": "债务 (zhàiwù)"
    },
    "theory": {
        "Hindi": "सिद्धांत (siddhānt)",
        "Chinese (Simplified)": "理论 (lǐlùn)"
    },
    "invasion": {
        "Hindi": "आक्रमण (ākramṇa)",
        "Chinese (Simplified)": "入侵 (rùqīn)"
    },
    "civilization": {
        "Hindi": "सभ्यता (sabhyatā)",
        "Chinese (Simplified)": "文明 (wénmíng)"
    },
    "between": {
        "Hindi": "के बीच (ke bīc)",
        "Chinese (Simplified)": "之间 (zhījiān)"
    },
    "race": {
        "Hindi": "दौड़ (dauṛ)",
        "Chinese (Simplified)": "种族 (zǒngzú)"
    },
    "racism": {
        "Hindi": "नस्लवाद (naslavād)",
        "Chinese (Simplified)": "种族歧视 (zǒngzú qíshì)"
    },
    "recognize": {
        "Hindi": "पहचानना (pahcānna)",
        "Chinese (Simplified)": "认出 (rènchū)"
    },
    "react": {
        "Hindi": "प्रतिक्रिया करना (pratikriyā karnā)",
        "Chinese (Simplified)": "反应 (fǎnyìng)"
    },
    "reaction": {
        "Hindi": "प्रतिक्रिया (pratikriyā)",
        "Chinese (Simplified)": "反应 (fǎnyìng)"
    },
    "without": {
        "Hindi": "बिना (binā)",
        "Chinese (Simplified)": "没有 (méiyǒu)"
    },
    "keys": {
        "Hindi": "चाबियाँ (cābiyāṅ)",
        "Chinese (Simplified)": "钥匙 (yàoshi)"
    },
    "key": {
        "Hindi": "चाभी (cābhī)",
        "Chinese (Simplified)": "钥匙 (yàoshi)"
    },
    "solution": {
        "Hindi": "समाधान (samādhān)",
        "Chinese (Simplified)": "解决方案 (jiějué fāngàn)"
    },
    "trash": {
        "Hindi": "कचरा (kacrā)",
        "Chinese (Simplified)": "垃圾 (lājī)"
    },
    "everything": {
        "Hindi": "सब कुछ (sab kuch)",
        "Chinese (Simplified)": "一切 (yīqiè)"
    },
    "every": {
        "Hindi": "हर (har)",
        "Chinese (Simplified)": "每个 (měigè)"
    },
    "consistent": {
        "Hindi": "संगत (sangat)",
        "Chinese (Simplified)": "一致的 (yīzhì de)"
    },
    "final": {
        "Hindi": "अंतिम (antim)",
        "Chinese (Simplified)": "最后的 (zuìhòu de)"
    },
    "overtake": {
        "Hindi": "पछाड़ना (pachāṛnā)",
        "Chinese (Simplified)": "超越 (chāoyue)"
    },
    "legacy": {
        "Hindi": "विरासत (virāsat)",
        "Chinese (Simplified)": "遗产 (yíchǎn)"
    },
    "legends": {
        "Hindi": "किंवदंतियाँ (kinvandanṭiyāँ)",
        "Chinese (Simplified)": "传说 (chuánshuō)"
    },
    "die": {
        "Hindi": "मरना (marnā)",
        "Chinese (Simplified)": "死亡 (sǐwáng)"
    },
    "never": {
        "Hindi": "कभी नहीं (kabhī nahī̃)",
        "Chinese (Simplified)": "从来没有 (cóng méiyǒu)"
    },
    "legend": {
        "Hindi": "किंवदंती (kinvandanṭī)",
        "Chinese (Simplified)": "传奇 (chuánqí)"
    },
    "beginner": {
        "Hindi": "शुरुआत करने वाला (śurūāt karne vāla)",
        "Chinese (Simplified)": "初学者 (chūxuézhě)"
    },
    "medicine": {
        "Chinese (Simplified)": "药 (yào)",
        "Hindi": "दवा (davā)"
    },
    "student": {
        "Chinese (Simplified)": "学生 (xué shēng)",
        "Hindi": "विद्यार्थी (vidyārthī)"
    },
    "library": {
        "Chinese (Simplified)": "图书馆 (tú shū guǎn)",
        "Hindi": "पुस्तकालय (pustakālay)"
    },
    "office": {
        "Chinese (Simplified)": "办公室 (bàn gōng shì)",
        "Hindi": "कार्यालय (kāryālaya)"
    },
    "market": {
        "Chinese (Simplified)": "市场 (shì chǎng)",
        "Hindi": "बाज़ार (bāzār)"
    },
    "phone": {
        "Chinese (Simplified)": "电话 (diàn huà)",
        "Hindi": "फोन (phon)"
    },
    "computer": {
        "Chinese (Simplified)": "电脑 (diàn nǎo)",
        "Hindi": "कंप्यूटर (kampyūṭar)"
    },
    "internet": {
        "Chinese (Simplified)": "互联网 (hù lián wǎng)",
        "Hindi": "इंटरनेट (inṭarneṭ)"
    },
    "book": {
        "Chinese (Simplified)": "书 (shū)",
        "Hindi": "किताब (kitāb)"
    },
    "pen": {
        "Chinese (Simplified)": "钢笔 (gāng bǐ)",
        "Hindi": "कलम (kalam)"
    },
    "paper": {
        "Chinese (Simplified)": "纸 (zhǐ)",
        "Hindi": "कागज (kāgaz)"
    },
    "bag": {
        "Chinese (Simplified)": "包 (bāo)",
        "Hindi": "बैग (baig)"
    },
    "clothes": {
        "Chinese (Simplified)": "衣服 (yī fú)",
        "Hindi": "कपड़े (kapṛe)"
    },
    "shoes": {
        "Chinese (Simplified)": "鞋子 (xié zi)",
        "Hindi": "जूते (jūte)"
    },
    "sky": {
        "Chinese (Simplified)": "天空 (tiān kōng)",
        "Hindi": "आकाश (aakaash)"
    },
    "river": {
        "Chinese (Simplified)": "河流 (hé liú)",
        "Hindi": "नदी (nadi)"
    },
    "mountain": {
        "Chinese (Simplified)": "山 (shān)",
        "Hindi": "पहाड़ (pahaad)"
    },
    "nepal": {
        "Chinese (Simplified)": "尼泊尔 (Níbó'ěr)",
        "Hindi": "नेपाल (Nepāl)"
    },
    "sri Lanka": {
        "Chinese (Simplified)": "斯里兰卡 (Sīlǐlánkǎ)",
        "Hindi": "श्रीलंका (Shrīlāṅkā)"
    },
    "taiwan": {
        "Chinese (Simplified)": "台湾 (Táiwān)",
        "Hindi": "ताइवान (Tāiwān)"
    },
    "bangladesh": {
        "Chinese (Simplified)": "孟加拉国 (Mèngjiālāguó)",
        "Hindi": "बांगलादेश (Bāṅglādēś)"
    },
    "iran": {
        "Chinese (Simplified)": "伊朗 (Yīlǎng)",
        "Hindi": "ईरान (Īrān)"
    },
    "tree": {
        "Chinese (Simplified)": "树 (shù)",
        "Hindi": "पेड़ (ped)"
    },
    "welcome": {
        "Chinese (Simplified)": "欢迎 (huān yíng)",
        "Hindi": "स्वागत है (swāgat hai)"
    },
    "flower": {
        "Chinese (Simplified)": "花 (huā)",
        "Hindi": "फूल (phool)"
    },
    "road": {
        "Chinese (Simplified)": "路 (lù)",
        "Hindi": "सड़क (sadak)"
    },
    "city": {
        "Chinese (Simplified)": "城市 (chéng shì)",
        "Hindi": "शहर (shahar)"
    },
    "village": {
        "Chinese (Simplified)": "村庄 (cūn zhuāng)",
        "Hindi": "गांव (gaon)"
    },
    "ocean": {
        "Chinese (Simplified)": "海洋 (hǎi yáng)",
        "Hindi": "समुद्र (samudra)"
    },
    "child": {
        "Chinese (Simplified)": "孩子 (hái zi)",
        "Hindi": "बच्चा (bachcha)"
    },
    "star": {
        "Chinese (Simplified)": "星星 (xīng xīng)",
        "Hindi": "तारा (taara)"
    },
    "chair": {
        "Chinese (Simplified)": "椅子 (yǐ zi)",
        "Hindi": "कुर्सी (kursi)"
    },
    "please wait": {
        "Chinese (Simplified)": "请等一下 (qǐng děng yī xià)",
        "Hindi": "कृपया इंतजार करें (kripya intezaar karein)"
    },
    "how much": {
        "Chinese (Simplified)": "多少钱 (duō shǎo qián)",
        "Hindi": "कितना (kitna)"
    },
    "stop": {
        "Chinese (Simplified)": "停 (tíng)",
        "Hindi": "रोकें (roken)"
    },
    "start": {
        "Chinese (Simplified)": "开始 (kāi shǐ)",
        "Hindi": "शुरू करें (shuru karein)"
    },
    "danger": {
        "Chinese (Simplified)": "危险 (wēi xiǎn)",
        "Hindi": "खतरा (khatra)"
    },
    "help me": {
        "Chinese (Simplified)": "帮助我 (bāng zhù wǒ)",
        "Hindi": "मदद करें (madad karein)"
    },
    "fire": {
        "Chinese (Simplified)": "火 (huǒ)",
        "Hindi": "आग (aag)"
    },
    "water bottle": {
        "Chinese (Simplified)": "水瓶 (shuǐ píng)",
        "Hindi": "पानी की बोतल (paani ki botal)"
    },
    "food delivery": {
        "Chinese (Simplified)": "送餐 (sòng cān)",
        "Hindi": "खाना डिलीवरी (khana delivery)"
    },
    "coffee": {
        "Chinese (Simplified)": "咖啡 (kā fēi)",
        "Hindi": "कॉफ़ी (coffee)"
    },
    "music": {
        "Chinese (Simplified)": "音乐 (yīn yuè)",
        "Hindi": "संगीत (sangeet)"
    },
    "movie": {
        "Chinese (Simplified)": "电影 (diàn yǐng)",
        "Hindi": "फिल्म (film)"
    },
    "bookstore": {
        "Chinese (Simplified)": "书店 (shū diàn)",
        "Hindi": "पुस्तकालय (pustakalaya)"
    },
    "celebrate": {
        "Chinese (Simplified)": "庆祝 (qìng zhù)",
        "Hindi": "जश्न मनाना (jashn manāna)"
    },
    "journey": {
        "Chinese (Simplified)": "旅程 (lǚ chéng)",
        "Hindi": "यात्रा (yātrā)"
    },
    "adventure": {
        "Chinese (Simplified)": "冒险 (mào xiǎn)",
        "Hindi": "साहसिक यात्रा (sāhasik yātrā)"
    },
    "freedom": {
        "Chinese (Simplified)": "自由 (zì yóu)",
        "Hindi": "स्वतंत्रता (svatantrtā)"
    },
    "success": {
        "Chinese (Simplified)": "成功 (chéng gōng)",
        "Hindi": "सफलता (safaltā)"
    },
    "unity": {
        "Chinese (Simplified)": "团结 (tuán jié)",
        "Hindi": "एकता (ektā)"
    },
    "explore": {
        "Chinese (Simplified)": "探索 (tàn suǒ)",
        "Hindi": "अन्वेषण (anvēṣaṇ)"
    },
    "innovate": {
        "Chinese (Simplified)": "创新 (chuàng xīn)",
        "Hindi": "नवोन्मेष (navonmeṣ)"
    },
    "enlightenment": {
        "Chinese (Simplified)": "启蒙 (qǐ méng)",
        "Hindi": "प्रकाश (prakāś)"
    },
    "passion": {
        "Chinese (Simplified)": "激情 (jī qíng)",
        "Hindi": "उत्साह (utsāh)"
    },
    "knowledgeable": {
        "Chinese (Simplified)": "博学 (bó xué)",
        "Hindi": "ज्ञानी (jñānī)"
    },
    "resilience": {
        "Chinese (Simplified)": "韧性 (rèn xìng)",
        "Hindi": "लचीलापन (lachīlāpan)"
    },
    "achievement": {
        "Chinese (Simplified)": "成就 (chéng jiù)",
        "Hindi": "उपलब्धि (uplabdhī)"
    },
    "purpose": {
        "Chinese (Simplified)": "目的 (mù dì)",
        "Hindi": "उद्देश्य (uddeśya)"
    },
    "fruit": {
        "Hindi": "फल (phal)",
        "Chinese (Simplified)": "水果 (shuǐguǒ)"
    },
    "bread": {
        "Hindi": "रोटी (roṭī)",
        "Chinese (Simplified)": "面包 (miànbāo)"
    },
    "tea": {
        "Hindi": "चाय (chāy)",
        "Chinese (Simplified)": "茶 (chá)"
    },
    "see": {
        "Hindi": "देखना (dekhna)",
        "Chinese (Simplified)": "看 (kàn)"
    },
    "speak": {
        "Hindi": "बोलना (bolnā)",
        "Chinese (Simplified)": "说 (shuō)"
    },
    "kid": {
        "Hindi": "बच्चा (bachchā)",
        "Chinese (Simplified)": "孩子 (háizi)"
    },
    "hear": {
        "Hindi": "सुनना (sunnā)",
        "Chinese (Simplified)": "听 (tīng)"
    },
    "sea": {
        "Hindi": "समुद्र (samudra)",
        "Chinese (Simplified)": "海 (hǎi)"
    },
    "wall": {
        "Hindi": "दीवार (dīvār)",
        "Chinese (Simplified)": "墙 (qiáng)"
    },
    "nature": {
        "Hindi": "प्रकृति (prakṛti)",
        "Chinese (Simplified)": "自然 (zìrán)"
    },
    "milk": {
        "Hindi": "दूध (dūdh)",
        "Chinese (Simplified)": "牛奶 (niúnǎi)"
    },
    "air": {
        "Hindi": "हवा (havā)",
        "Chinese (Simplified)": "空气 (kōngqì)"
    },
    "hair": {
        "Hindi": "बाल (bāl)",
        "Chinese (Simplified)": "头发 (tóufǎ)"
    },    
    "bottle": {
        "Hindi": "बोतल (botal)",
        "Chinese (Simplified)": "瓶子 (píngzi)"
    },
    "fingers": {
        "Hindi": "उंगलियां (ungaliyāṇ)",
        "Chinese (Simplified)": "手指 (shǒuzhǐ)"
    },
    "lips": {
        "Hindi": "होठ (hoṭh)",
        "Chinese (Simplified)": "嘴唇 (zuǐchún)"
    },
    "pinch": {
        "Hindi": "चुटकी (chuṭkī)",
        "Chinese (Simplified)": "捏 (niē)"
    },
    "room": {
        "Hindi": "कमरा (kamrā)",
        "Chinese (Simplified)": "房间 (fángjiān)"
    },
    "season": {
        "Hindi": "ऋतु (ṛtu)",
        "Chinese (Simplified)": "季节 (jìjié)"
    },
    "fire": {
        "Hindi": "आग (āg)",
        "Chinese (Simplified)": "火 (huǒ)"
    },
    "baby": {
        "Hindi": "शिशु (śiśu)",
        "Chinese (Simplified)": "婴儿 (yīng'ér)"
    },
    "old": {
        "Hindi": "पुराना (purānā)",
        "Chinese (Simplified)": "旧 (jiù)"
    },
    "new": {
        "Hindi": "नया (nayā)",
        "Chinese (Simplified)": "新 (xīn)"
    },
    "tall": {
        "Hindi": "लंबा (lambā)",
        "Chinese (Simplified)": "高 (gāo)"
    },
    "short": {
        "Hindi": "छोटा (choṭā)",
        "Chinese (Simplified)": "短 (duǎn)"
    },
    "floor": {
        "Hindi": "फ़र्श (farś)",
        "Chinese (Simplified)": "地板 (dìbǎn)"
    },
    "balloon": {
        "Hindi": "गुब्बारा (gubbārā)",
        "Chinese (Simplified)": "气球 (qìqiú)"
    },
    "bowl": {
        "Hindi": "कटोरा (kaṭorā)",
        "Chinese (Simplified)": "碗 (wǎn)"
    },
    "festival": {
        "Hindi": "त्यौहार (tyauhār)",
        "Chinese (Simplified)": "节日 (jiérì)"
    },
    "up": {
        "Hindi": "ऊपर (ūpar)",
        "Chinese (Simplified)": "上 (shàng)"
    },
    "down": {
        "Hindi": "नीचे (nīche)",
        "Chinese (Simplified)": "下 (xià)"
    },
    "naughty": {
        "Hindi": "शरारती (śarāratī)",
        "Chinese (Simplified)": "调皮 (tiáopí)"
    },
    "smart": {
        "Hindi": "स्मार्ट (smart)",
        "Chinese (Simplified)": "聪明 (cōngmíng)"
    },
    "moron": {
        "Hindi": "मूर्ख (mūrkh)",
        "Chinese (Simplified)": "笨蛋 (bèndàn)"
    },
    "resident": {
        "Hindi": "निवासी (nivāsī)",
        "Chinese (Simplified)": "居民 (jūmín)"
    },
    "evil": {
        "Hindi": "बुराई (burāī)",
        "Chinese (Simplified)": "邪恶 (xié'è)"
    },
    "thief": {
        "Hindi": "चोर (chor)",
        "Chinese (Simplified)": "小偷 (xiǎotōu)"
    },
    "police": {
        "Hindi": "पुलिस (pulis)",
        "Chinese (Simplified)": "警察 (jǐngchá)"
    },
    "shadow": {
        "Hindi": "छाया (chhāyā)",
        "Chinese (Simplified)": "影子 (yǐngzi)"
    },
    "bright": {
        "Hindi": "चमकदार (chamakdār)",
        "Chinese (Simplified)": "明亮 (míngliàng)"
    },
    "sound": {
        "Hindi": "ध्वनि (dhvani)",
        "Chinese (Simplified)": "声音 (shēngyīn)"
    },
    "silence": {
        "Hindi": "शांति (śānti)",
        "Chinese (Simplified)": "沉默 (chénmò)"
    },
    "silent": {
        "Hindi": "मौन (maun)",
        "Chinese (Simplified)": "安静 (ānjìng)"
    },
    "supermarket": {
        "Hindi": "सुपरमार्केट (suparmārkeṭ)",
        "Chinese (Simplified)": "超市 (chāoshì)"
    },
    "button": {
        "Hindi": "बटन (baṭan)",
        "Chinese (Simplified)": "按钮 (ànniǔ)"
    },
    "left": {
        "Hindi": "बाएँ (bāẽ)",
        "Chinese (Simplified)": "左 (zuǒ)"
    },
    "right": {
        "Hindi": "दाएँ (dāẽ)",
        "Chinese (Simplified)": "右 (yòu)"
    },
    "hole": {
        "Hindi": "छेद (chhed)",
        "Chinese (Simplified)": "洞 (dòng)"
    },
    "whole": {
        "Hindi": "संपूर्ण (sampūrṇ)",
        "Chinese (Simplified)": "整体 (zhěngtǐ)"
    },
    "all": {
        "Hindi": "सभी (sabhī)",
        "Chinese (Simplified)": "所有 (suǒyǒu)"
    },
    "empty": {
        "Hindi": "खाली (khālī)",
        "Chinese (Simplified)": "空 (kōng)"
    },
    "part": {
        "Hindi": "भाग (bhāg)",
        "Chinese (Simplified)": "部分 (bùfèn)"
    },
    "game": {
        "Hindi": "खेल (khel)",
        "Chinese (Simplified)": "游戏 (yóuxì)"
    },
    "grace": {
        "Chinese (Simplified)": "优雅 (yōu yǎ)",
        "Hindi": "कृपा (kripā)"
    },
    "honesty": {
        "Chinese (Simplified)": "诚实 (chéng shí)",
        "Hindi": "ईमानदारी (īmāndārī)"
    },
    "loyal": {
        "Chinese (Simplified)": "忠诚 (zhōng chéng)",
        "Hindi": "निष्ठावान (niṣṭhāvān)"
    },
    "understand": {
        "Chinese (Simplified)": "理解 (lǐ jiě)",
        "Hindi": "समझना (samajhnā)"
    },
    "compassion": {
        "Chinese (Simplified)": "同情 (tóng qíng)",
        "Hindi": "दया (dayā)"
    },
    "openness": {
        "Chinese (Simplified)": "开放 (kāi fàng)",
        "Hindi": "खुलापन (khulāpan)"
    },
    "communication": {
        "Chinese (Simplified)": "沟通 (gōu tōng)",
        "Hindi": "संचार (sanchār)"
    },
    "transformation": {
        "Chinese (Simplified)": "转变 (zhuǎn biàn)",
        "Hindi": "रूपांतरण (rūpāntaraṇ)"
    },
    "adversity": {
        "Chinese (Simplified)": "逆境 (nì jìng)",
        "Hindi": "कठिनाई (kaṭhināī)"
    },
    "appreciation": {
        "Chinese (Simplified)": "欣赏 (xīn shǎng)",
        "Hindi": "स्मरण (smaraṇ)"
    },
    "balance": {
        "Chinese (Simplified)": "平衡 (píng héng)",
        "Hindi": "संतुलन (santulan)"
    },
    "mindfulness": {
        "Chinese (Simplified)": "正念 (zhèng niàn)",
        "Hindi": "सचेतता (sacētatā)"
    },
    "empower": {
        "Chinese (Simplified)": "赋能 (fù néng)",
        "Hindi": "सशक्त बनाना (saśakt banānā)"
    },
    "reflection": {
        "Chinese (Simplified)": "反思 (fǎn sī)",
        "Hindi": "प्रतिबिंब (pratibimb)"
    },
    "courageous": {
        "Chinese (Simplified)": "勇敢 (yǒng gǎn)",
        "Hindi": "साहसी (sāhasī)"
    },
    "gratitude": {
        "Chinese (Simplified)": "感恩 (gǎn ēn)",
        "Hindi": "आभार (ābhār)"
    },
    "respectful": {
        "Chinese (Simplified)": "尊重 (zūn zhòng)",
        "Hindi": "आदरपूर्ण (ādar pūrṇ)"
    },
    "collaboration": {
        "Chinese (Simplified)": "合作 (hé zuò)",
        "Hindi": "सहयोग (sahyog)"
    },
    "determination": {
        "Chinese (Simplified)": "决心 (jué xīn)",
        "Hindi": "निश्चय (niśchay)"
    },
    "enrich": {
        "Chinese (Simplified)": "丰富 (fēng fù)",
        "Hindi": "समृद्ध करना (samṛddh karnā)"
    },
    "serenity": {
        "Chinese (Simplified)": "宁静 (níng jìng)",
        "Hindi": "शांति (shānti)"
    },
    "strength": {
        "Chinese (Simplified)": "力量 (lì liàng)",
        "Hindi": "शक्ति (shakti)"
    },
    "peace": {
        "Chinese (Simplified)": "和平 (hé píng)",
        "Hindi": "शांति (shānti)"
    },
    "health": {
        "Chinese (Simplified)": "健康 (jiàn kāng)",
        "Hindi": "स्वास्थ्य (svāsthya)"
    },
    "hope": {
        "Chinese (Simplified)": "希望 (xī wàng)",
        "Hindi": "आशा (āshā)"
    },
    "courage": {
        "Chinese (Simplified)": "勇气 (yǒng qì)",
        "Hindi": "साहस (sāhas)"
    },
    "knowledge": {
        "Chinese (Simplified)": "知识 (zhī shi)",
        "Hindi": "ज्ञान (gyān)"
    },
    "opportunity": {
        "Chinese (Simplified)": "机会 (jī huì)",
        "Hindi": "अवसर (avsar)"
    },
    "friendship": {
        "Chinese (Simplified)": "友谊 (yǒu yì)",
        "Hindi": "मित्रता (mitratā)"
    },
    "loyalty": {
        "Chinese (Simplified)": "忠诚 (zhōng chéng)",
        "Hindi": "निष्ठा (niṣṭhā)"
    },
    "imagination": {
        "Chinese (Simplified)": "想象 (xiǎng xiàng)",
        "Hindi": "कल्पना (kalpanā)"
    },
    "wisdom": {
        "Chinese (Simplified)": "智慧 (zhì huì)",
        "Hindi": "बुद्धिमत्ता (buddhimattā)"
    },
    "bravery": {
        "Chinese (Simplified)": "勇敢 (yǒng gǎn)",
        "Hindi": "वीरता (vīrtā)"
    },
    "patience": {
        "Chinese (Simplified)": "耐心 (nài xīn)",
        "Hindi": "धैर्य (dhairya)"
    },
    "journey": {
        "Chinese (Simplified)": "旅行 (lǚ xíng)",
        "Hindi": "यात्रा (yātrā)"
    },
    "dream": {
        "Chinese (Simplified)": "梦想 (mèng xiǎng)",
        "Hindi": "सपना (sapnā)"
    },
    "kindness": {
        "Chinese (Simplified)": "善良 (shàn liáng)",
        "Hindi": "दयालुता (dayālutā)"
    },
    "honor": {
        "Chinese (Simplified)": "荣誉 (róng yù)",
        "Hindi": "सम्मान (sammān)"
    },
    "trust": {
        "Chinese (Simplified)": "信任 (xìn rèn)",
        "Hindi": "विश्वास (vishwās)"
    },
    "teamwork": {
        "Chinese (Simplified)": "团队合作 (tuán duì hé zuò)",
        "Hindi": "टीमवर्क (ṭīmvarq)"
    },
    "door": {
        "Chinese (Simplified)": "门 (mén)",
        "Hindi": "दरवाज़ा (darwaza)"
    },
    "window": {
        "Chinese (Simplified)": "窗户 (chuāng hu)",
        "Hindi": "खिड़की (khidki)"
    },
    "animal": {
        "Chinese (Simplified)": "动物 (dòng wù)",
        "Hindi": "जानवर (jaanvar)"
    },
    "bird": {
        "Chinese (Simplified)": "鸟 (niǎo)",
        "Hindi": "पक्षी (pakshi)"
    },
    "fish": {
        "Chinese (Simplified)": "鱼 (yú)",
        "Hindi": "मछली (machhli)"
    },
    "dream": {
        "Chinese (Simplified)": "梦 (mèng)",
        "Hindi": "सपना (sapna)"
    },
    "dance": {
        "Chinese (Simplified)": "跳舞 (tiào wǔ)",
        "Hindi": "नृत्य (nritya)"
    },
    "family": {
        "Chinese (Simplified)": "家庭 (jiā tíng)",
        "Hindi": "परिवार (parivaar)"
    },
    "money": {
        "Chinese (Simplified)": "钱 (qián)",
        "Hindi": "पैसा (paisaa)"
    },
    "health": {
        "Chinese (Simplified)": "健康 (jiàn kāng)",
        "Hindi": "स्वास्थ्य (swasthya)"
    },
    "strength": {
        "Chinese (Simplified)": "力量 (lì liàng)",
        "Hindi": "ताकत (taakat)"
    },
    "moon": {
        "Chinese (Simplified)": "月亮 (yuè liàng)",
        "Hindi": "चंद्रमा (chandramā)"
    },
    "star": {
        "Chinese (Simplified)": "星星 (xīng xing)",
        "Hindi": "तारा (tārā)"
    },
    "cloud": {
        "Chinese (Simplified)": "云 (yún)",
        "Hindi": "बादल (bādal)"
    },
    "rain": {
        "Chinese (Simplified)": "雨 (yǔ)",
        "Hindi": "बारिश (bārish)"
    },
    "snow": {
        "Chinese (Simplified)": "雪 (xuě)",
        "Hindi": "बर्फ़ (barf)"
    },
    "mountain range": {
        "Chinese (Simplified)": "山脉 (shān mài)",
        "Hindi": "पर्वत श्रृंखला (parvat shrinkhalā)"
    },
    "valley": {
        "Chinese (Simplified)": "山谷 (shān gǔ)",
        "Hindi": "घाटी (ghātī)"
    },
    "desert": {
        "Chinese (Simplified)": "沙漠 (shā mò)",
        "Hindi": "रेगिस्तान (registān)"
    },
    "island": {
        "Chinese (Simplified)": "岛 (dǎo)",
        "Hindi": "द्वीप (dvīp)"
    },
    "lake": {
        "Chinese (Simplified)": "湖 (hú)",
        "Hindi": "झील (jheel)"
    },
    "riverbank": {
        "Chinese (Simplified)": "河岸 (hé àn)",
        "Hindi": "नदी का किनारा (nadi kā kinārā)"
    },
    "cave": {
        "Chinese (Simplified)": "洞穴 (dòng xué)",
        "Hindi": "गुफा (gufā)"
    },
    "waterfall": {
        "Chinese (Simplified)": "瀑布 (pù bù)",
        "Hindi": "झरना (jharanā)"
    },
    "earthquake": {
        "Chinese (Simplified)": "地震 (dì zhèn)",
        "Hindi": "भूकंप (bhūkamp)"
    },
    "volcano": {
        "Chinese (Simplified)": "火山 (huǒ shān)",
        "Hindi": "ज्वालामुखी (jvālāmukhī)"
    },
    "lightning": {
        "Chinese (Simplified)": "闪电 (shǎn diàn)",
        "Hindi": "बिजली (bijlī)"
    },
    "thunder": {
        "Chinese (Simplified)": "雷声 (léi shēng)",
        "Hindi": "गरज (garaj)"
    },
    "rainbow": {
        "Chinese (Simplified)": "彩虹 (cǎi hóng)",
        "Hindi": "इंद्रधनुष (indradhanush)"
    },
    "sunrise": {
        "Chinese (Simplified)": "日出 (rì chū)",
        "Hindi": "सूर्योदय (sūryoday)"
    },
    "sunset": {
        "Chinese (Simplified)": "日落 (rì luò)",
        "Hindi": "सूर्यास्त (sūryāst)"
    },
    "vision": {
        "Chinese (Simplified)": "视野 (shì yě)",
        "Hindi": "दृष्टि (dṛṣṭi)"
    },
    "god": {
        "Chinese (Simplified)": "上帝 Shàngdì",
        "Hindi": "भगवान (bhagwaan)"  
    },
    "independence": {
        "Chinese (Simplified)": "独立 (dú lì)",
        "Hindi": "स्वतंत्रता (svatantratā)"
    },
    "balance": {
        "Chinese (Simplified)": "平衡 (píng héng)",
        "Hindi": "संतुलन (santulan)"
    },
    "equality": {
        "Chinese (Simplified)": "平等 (píng děng)",
        "Hindi": "समानता (samāntā)"
    },
    "transparency": {
        "Chinese (Simplified)": "透明 (tòu míng)",
        "Hindi": "पारदर्शिता (pārdarśitā)"
    },
    "faith": {
        "Chinese (Simplified)": "信仰 (xìn yǎng)",
        "Hindi": "विश्वास (viśvās)"
    },
    "diversity": {
        "Chinese (Simplified)": "多样性 (duō yàng xìng)",
        "Hindi": "विविधता (vividhatā)"
    },
    "curiosity": {
        "Chinese (Simplified)": "好奇心 (hào qí xīn)",
        "Hindi": "जिज्ञासा (jijñāsā)"
    },
    "innovation": {
        "Chinese (Simplified)": "创新 (chuàng xīn)",
        "Hindi": "नवाचार (navācār)"
    },
    "gratitude": {
        "Chinese (Simplified)": "感恩 (gǎn ēn)",
        "Hindi": "आभार (ābhār)"
    },
    "integrity": {
        "Chinese (Simplified)": "正直 (zhèng zhí)",
        "Hindi": "ईमानदारी (īmāndārī)"
    },
    "hope": {
        "Chinese (Simplified)": "希望 (xī wàng)",
        "Hindi": "आशा (āśā)"
    },
    "strength": {
        "Chinese (Simplified)": "力量 (lì liàng)",
        "Hindi": "शक्ति (śakti)"
    },
    "patience": {
        "Chinese (Simplified)": "耐心 (nài xīn)",
        "Hindi": "धैर्य (dhairya)"
    },
    "wisdom": {
        "Chinese (Simplified)": "智慧 (zhì huì)",
        "Hindi": "ज्ञान (jñān)"
    },
    "creativity": {
        "Chinese (Simplified)": "创造力 (chuàng zào lì)",
        "Hindi": "रचनात्मकता (rāchnātmaktā)"
    },
    "empowerment": {
        "Chinese (Simplified)": "赋能 (fù néng)",
        "Hindi": "सशक्तिकरण (saśaktikaraṇ)"
    },
    "legacy": {
        "Chinese (Simplified)": "遗产 (yí chǎn)",
        "Hindi": "विरासत (virāsat)"
    },
    "contribution": {
        "Chinese (Simplified)": "贡献 (gòng xiàn)",
        "Hindi": "योगदान (yogdān)"
    },
    "opportunity": {
        "Chinese (Simplified)": "机会 (jī huì)",
        "Hindi": "अवसर (avsar)"
    },
    "courage": {
        "Chinese (Simplified)": "勇气 (yǒng qì)",
        "Hindi": "साहस (sāhas)"
    },
    "perspective": {
        "Chinese (Simplified)": "视角 (shì jiǎo)",
        "Hindi": "दृष्टिकोण (dṛṣṭikoṇa)"
    },
    "ambition": {
        "Chinese (Simplified)": "雄心 (xióng xīn)",
        "Hindi": "महत्वाकांक्षा (mahatvākāṅkṣā)"
    },
    "determination": {
        "Chinese (Simplified)": "决心 (jué xīn)",
        "Hindi": "निश्चय (niśchay)"
    },
    "serenity": {
        "Chinese (Simplified)": "宁静 (níng jìng)",
        "Hindi": "शांति (shānti)"
    },
    "balance": {
        "Chinese (Simplified)": "平衡 (píng héng)",
        "Hindi": "संतुलन (santulan)"
    },
    "truth": {
        "Chinese (Simplified)": "真理 (zhēn lǐ)",
        "Hindi": "सत्य (satya)"
    },
    "China": { #Countries
        "Chinese (Simplified)": "中国 (Zhōngguó)",
        "Hindi": "चीन (Chīn)"
    },
    "japan": {
        "Chinese (Simplified)": "日本 (Rìběn)",
        "Hindi": "जापान (Jāpān)"
    },
    "france": {
        "Chinese (Simplified)": "法国 (Fàguó)",
        "Hindi": "फ्रांस (Frāns)"
    },
    "australia": {
        "Chinese (Simplified)": "澳大利亚 (Àodàlìyà)",
        "Hindi": "ऑस्ट्रेलिया (Ōsṭrelīyā)"
    },
    "mexico": {
        "Chinese (Simplified)": "墨西哥 (Mòxīgē)",
        "Hindi": "मैक्सिको (Maiksikō)"
    },
    "south Korea": {
        "Chinese (Simplified)": "韩国 (Hánguó)",
        "Hindi": "दक्षिण कोरिया (Dakṣiṇ Kōrīyā)"
    },
    "italy": {
        "Chinese (Simplified)": "意大利 (Yìdàlì)",
        "Hindi": "इटली (Iṭlī)"
    },
    "spain": {
        "Chinese (Simplified)": "西班牙 (Xībānyá)",
        "Hindi": "स्पेन (Spēn)"
    },
    "south Africa": {
        "Chinese (Simplified)": "南非 (Nánfēi)",
        "Hindi": "दक्षिण अफ्रीका (Dakṣiṇ Afrīkā)"
    },
    "argentina": {
        "Chinese (Simplified)": "阿根廷 (Āgēntíng)",
        "Hindi": "अर्जेंटीना (Arjenṭīnā)"
    },
    "saudi Arabia": {
        "Chinese (Simplified)": "沙特阿拉伯 (Shātè Ālābó)",
        "Hindi": "सऊदी अरब (Saudī Arab)"
    },
    "pakistan": {
        "Chinese (Simplified)": "巴基斯坦 (Bājīsītǎn)",
        "Hindi": "पाकिस्तान (Pākistān)"
    },
    "thailand": {
        "Chinese (Simplified)": "泰国 (Tàiguó)",
        "Hindi": "थाईलैंड (Thā'īlānḍ)"
    },
    "malaysia": {
        "Chinese (Simplified)": "马来西亚 (Mǎláixīyà)",
        "Hindi": "मलेशिया (Malēśiyā)"
    },
    "israel": {
        "Chinese (Simplified)": "以色列 (Yǐsèliè)",
        "Hindi": "इज़राइल (Izrā'īl)"
    },
    "singapore": {
        "Chinese (Simplified)": "新加坡 (Xīnjiāpō)",
        "Hindi": "सिंगापुर (Siṅgāpūr)"
    },
    "nigeria": {
        "Chinese (Simplified)": "尼日利亚 (Nírìlìyà)",
        "Hindi": "नाइजीरिया (Nā'ījīriyā)"
    },
    "philippines": {
        "Chinese (Simplified)": "菲律宾 (Fēilǜbīn)",
        "Hindi": "फ़िलिपीन्स (Philīpīnsa)"
    },
    "belgium": {
        "Chinese (Simplified)": "比利时 (Bǐlìshí)",
        "Hindi": "बेल्जियम (Beljiam)"
    },
    "brazil": {
        "Chinese (Simplified)": "巴西 (Bāxī)",
        "Hindi": "ब्राज़ील (Brāzīl)"
    },
    "canada": {
        "Chinese (Simplified)": "加拿大 (Jiānádà)",
        "Hindi": "कनाडा (Kanāḍā)"
    },
    "chile": {
        "Chinese (Simplified)": "智利 (Zhìlì)",
        "Hindi": "चिली (Chilī)"
    },
    "denmark": {
        "Chinese (Simplified)": "丹麦 (Dānmài)",
        "Hindi": "डेनमार्क (Ḍenmārk)"
    },
    "egypt": {
        "Chinese (Simplified)": "埃及 (Āijí)",
        "Hindi": "मिस्र (Misr)"
    },
    "finland": {
        "Chinese (Simplified)": "芬兰 (Fēnlán)",
        "Hindi": "फिनलैंड (Finlāṇḍ)"
    },
    "germany": {
        "Chinese (Simplified)": "德国 (Déguó)",
        "Hindi": "जर्मनी (Jarmani)"
    },
    "greece": {
        "Chinese (Simplified)": "希腊 (Xīlà)",
        "Hindi": "ग्रीस (Grīs)"
    },
    "hungary": {
        "Chinese (Simplified)": "匈牙利 (Xiōngyálì)",
        "Hindi": "हंगरी (Haṅgarī)"
    },
    "india": {
        "Chinese (Simplified)": "印度 (Yìndù)",
        "Hindi": "भारत (Bhārat)"
    },
    "indonesia": {
        "Chinese (Simplified)": "印度尼西亚 (Yìndùníxīyà)",
        "Hindi": "इंडोनेशिया (Iṇḍonēśiyā)"
    },
    "netherlands": {
        "Chinese (Simplified)": "荷兰 (Hélán)",
        "Hindi": "नीदरलैंड (Nīdaralēnḍ)"
    },
    "new Zealand": {
        "Chinese (Simplified)": "新西兰 (Xīnxīlán)",
        "Hindi": "न्यू ज़ीलैंड (Nyū Zīlānḍ)"
    },
    "norway": {
        "Chinese (Simplified)": "挪威 (Nuówēi)",
        "Hindi": "नॉर्वे (Nŏrvē)"
    },
    "poland": {
        "Chinese (Simplified)": "波兰 (Bōlán)",
        "Hindi": "पोलैंड (Polāṇḍ)"
    },
    "russia": {
        "Chinese (Simplified)": "俄罗斯 (Èluósī)",
        "Hindi": "रूस (Rūs)"
    },
    "sweden": {
        "Chinese (Simplified)": "瑞典 (Ruìdiǎn)",
        "Hindi": "स्वीडन (Swīḍan)"
    },
    "switzerland": {
        "Chinese (Simplified)": "瑞士 (Ruìshì)",
        "Hindi": "स्विट्ज़रलैंड (Swiṭzarlēnḍ)"
    },
    "turkey": {
        "Chinese (Simplified)": "土耳其 (Tǔ'ěrqí)",
        "Hindi": "तुर्की (Turkī)"
    },
    "united Kingdom": {
        "Chinese (Simplified)": "英国 (Yīngguó)",
        "Hindi": "संयुक्त राज्य (Saṁyukta Rājya)"
    },
    "united States": {
        "Chinese (Simplified)": "美国 (Měiguó)",
        "Hindi": "संयुक्त राज्य अमेरिका (Saṁyukta Rājya Amērikā)"
    },
    "venezuela": {
        "Chinese (Simplified)": "委内瑞拉 (Wěinèiruìlā)",
        "Hindi": "वेनेज़ुएला (Venēzū'ēlā)"
    },
    "vietnam": {
        "Chinese (Simplified)": "越南 (Yuènán)",
        "Hindi": "वियतनाम (Viyanām)"
    },
    "dog": { #Animals
        "Chinese (Simplified)": "狗 (gǒu)",
        "Hindi": "कुत्ता (Kuttā)"
    },
    "cat": {
        "Chinese (Simplified)": "猫 (māo)",
        "Hindi": "बिल्ली (Billī)"
    },
    "elephant": {
        "Chinese (Simplified)": "大象 (dà xiàng)",
        "Hindi": "हाथी (Hāthī)"
    },
    "tiger": {
        "Chinese (Simplified)": "老虎 (lǎo hǔ)",
        "Hindi": "बाघ (Bāgh)"
    },
    "lion": {
        "Chinese (Simplified)": "狮子 (shī zi)",
        "Hindi": "शेर (Sher)"
    },
    "cow": {
        "Chinese (Simplified)": "牛 (niú)",
        "Hindi": "गाय (Gāy)"
    },
    "horse": {
        "Chinese (Simplified)": "马 (mǎ)",
        "Hindi": "घोड़ा (Ghoṛā)"
    },
    "monkey": {
        "Chinese (Simplified)": "猴子 (hóu zi)",
        "Hindi": "बंदर (Bandar)"
    },
    "rabbit": {
        "Chinese (Simplified)": "兔子 (tù zi)",
        "Hindi": "खरगोश (Khargosh)"
    },
    "deer": {
        "Chinese (Simplified)": "鹿 (lù)",
        "Hindi": "हिरण (Hiraṇ)"
    },
    "bear": {
        "Chinese (Simplified)": "熊 (xióng)",
        "Hindi": "भालू (Bhālū)"
    },
    "wolf": {
        "Chinese (Simplified)": "狼 (láng)",
        "Hindi": "भेड़िया (Bheṛiyā)"
    },
    "sheep": {
        "Chinese (Simplified)": "羊 (yáng)",
        "Hindi": "भेड़ (Bheṛ)"
    },
    "goat": {
        "Chinese (Simplified)": "山羊 (shān yáng)",
        "Hindi": "बकरी (Bakrī)"
    },
    "pig": {
        "Chinese (Simplified)": "猪 (zhū)",
        "Hindi": "सुअर (Su’ar)"
    },
    "fox": {
        "Chinese (Simplified)": "狐狸 (hú lí)",
        "Hindi": "लोमड़ी (Lomaṛī)"
    },
    "frog": {
        "Chinese (Simplified)": "青蛙 (qīng wā)",
        "Hindi": "मेंढक (Meṇḍhak)"
    },
    "snake": {
        "Chinese (Simplified)": "蛇 (shé)",
        "Hindi": "साँप (Sāṅp)"
    },
    "fish": {
        "Chinese (Simplified)": "鱼 (yú)",
        "Hindi": "मछली (Machhalī)"
    },
    "dolphin": {
        "Chinese (Simplified)": "海豚 (hǎi tún)",
        "Hindi": "डॉल्फिन (Dolphin)"
    },
    "whale": {
        "Chinese (Simplified)": "鲸鱼 (jīng yú)",
        "Hindi": "व्हेल (Vheil)"
    },
    "crocodile": {
        "Chinese (Simplified)": "鳄鱼 (è yú)",
        "Hindi": "मगरमच्छ (Magarmachchh)"
    },
    "peacock": {
        "Chinese (Simplified)": "孔雀 (kǒng què)",
        "Hindi": "मोर (Mor)"
    },
    "parrot": {
        "Chinese (Simplified)": "鹦鹉 (yīng wǔ)",
        "Hindi": "तोता (Totā)"
    },
    "chicken": {
        "Chinese (Simplified)": "鸡 (jī)",
        "Hindi": "मुर्गी (Murgī)"
    },
    "duck": {
        "Chinese (Simplified)": "鸭子 (yā zi)",
        "Hindi": "बतख (Batakh)"
    },
    "camel": {
        "Chinese (Simplified)": "骆驼 (luò tuó)",
        "Hindi": "ऊँट (Ūṅṭ)"
    },
    "zebra": {
        "Chinese (Simplified)": "斑马 (bān mǎ)",
        "Hindi": "ज़ेबरा (Zebarā)"
    },
    "giraffe": {
        "Chinese (Simplified)": "长颈鹿 (cháng jǐng lù)",
        "Hindi": "जिराफ़ (Jirāf)"
    },
    "panda": {
        "Chinese (Simplified)": "熊猫 (xióng māo)",
        "Hindi": "पांडा (Pāṇḍā)"
    },
    "kangaroo": {
        "Chinese (Simplified)": "袋鼠 (dài shǔ)",
        "Hindi": "कंगारू (Kaṅgārū)"
    },
    "nercury": { #Planets
        "Chinese (Simplified)": "水星 (shuǐ xīng)",
        "Hindi": "बुध (budh)"
    },
    "venus": {
        "Chinese (Simplified)": "金星 (jīn xīng)",
        "Hindi": "शुक्र (shukra)"
    },
    "earth": {
        "Chinese (Simplified)": "地球 (dì qiú)",
        "Hindi": "पृथ्वी (prithvi)"
    },
    "mars": {
        "Chinese (Simplified)": "火星 (huǒ xīng)",
        "Hindi": "मंगल (mangal)"
    },
    "jupiter": {
        "Chinese (Simplified)": "木星 (mù xīng)",
        "Hindi": "बृहस्पति (brihaspati)"
    },
    "saturn": {
        "Chinese (Simplified)": "土星 (tǔ xīng)",
        "Hindi": "शनि (shani)"
    },
    "uranus": {
        "Chinese (Simplified)": "天王星 (tiān wáng xīng)",
        "Hindi": "अरुण (arun)"
    },
    "neptune": {
        "Chinese (Simplified)": "海王星 (hǎi wáng xīng)",
        "Hindi": "वरुण (varun)"
    },
    "pluto": {
        "Chinese (Simplified)": "冥王星 (míng wáng xīng)",
        "Hindi": "यम (yam)"
    },
    "taj mahal": {
        "Chinese (Simplified)": "泰姬陵 (Tài jī líng)",
        "Hindi": "ताजमहल (Taj Mahal)"
    },
    "great wall of china": {
        "Chinese (Simplified)": "长城 (Cháng chéng)",
        "Hindi": "चीन की महान दीवार (Cheen ki mahaan deewar)"
    },
    "eiffel tower": {
        "Chinese (Simplified)": "埃菲尔铁塔 (Āi fēi ěr tiě tǎ)",
        "Hindi": "आइफ़िल टॉवर (Aifel Tower)"
    },
    "statue of liberty": {
        "Chinese (Simplified)": "自由女神像 (Zì yóu nǚ shén xiàng)",
        "Hindi": "स्वतंत्रता की मूर्ति (Swatantrata ki moorti)"
    },
    "machu picchu": {
        "Chinese (Simplified)": "马丘比丘 (Mǎ qiū bǐ qiū)",
        "Hindi": "माचू पिच्चू (Machu Picchu)"
    },
    "colosseum": {
        "Chinese (Simplified)": "斗兽场 (Dòu shòu chǎng)",
        "Hindi": "कोलोसियम (Colosseum)"
    },
    "sydney opera house": {
        "Chinese (Simplified)": "悉尼歌剧院 (Xī ní gē jù yuàn)",
        "Hindi": "सिडनी ओपेरा हाउस (Sidney Opera House)"
    },
    "burj khalifa": {
        "Chinese (Simplified)": "哈利法塔 (Hā lì fǎ tǎ)",
        "Hindi": "बुर्ज खलीफा (Burj Khalifa)"
    },
    "pyramids of giza": {
        "Chinese (Simplified)": "吉萨金字塔 (Jí sà jīn zì tǎ)",
        "Hindi": "गीज़ा के पिरामिड (Giza ke Pyramids)"
    },
    "golden gate bridge": {
        "Chinese (Simplified)": "金门大桥 (Jīn mén dà qiáo)",
        "Hindi": "गोल्डन गेट ब्रिज (Golden Gate Bridge)"
    },
    "mount everest": {
        "Chinese (Simplified)": "珠穆朗玛峰 (Zhū mù lǎng mǎ fēng)",
        "Hindi": "माउंट एवरेस्ट (Mount Everest)"
    },
    "stonehenge": {
        "Chinese (Simplified)": "巨石阵 (Jù shí zhèn)",
        "Hindi": "स्टोनहेंज (Stonehenge)"
    },
    "angkor wat": {
        "Chinese (Simplified)": "吴哥窟 (Wú gē kū)",
        "Hindi": "अंगकोर वाट (Angkor Wat)"
    },
    "petra": {
        "Chinese (Simplified)": "佩特拉 (Pèi tè lā)",
        "Hindi": "पेट्रा (Petra)"
    },
    "big ben": {
        "Chinese (Simplified)": "大本钟 (Dà běn zhōng)",
        "Hindi": "बिग बेन (Big Ben)"
    },
    "christ the redeemer": {
        "Chinese (Simplified)": "基督救世主像 (Jī dū jiù shì zhǔ xiàng)",
        "Hindi": "क्राइस्ट द रिडीमर (Christ the Redeemer)"
    },
    "empire state building": {
        "Chinese (Simplified)": "帝国大厦 (Dì guó dà shà)",
        "Hindi": "एम्पायर स्टेट बिल्डिंग (Empire State Building)"
    },
    "leaning tower of pisa": {
        "Chinese (Simplified)": "比萨斜塔 (Bǐ sà xié tǎ)",
        "Hindi": "पीसा की झुकी हुई मीनार (Pisa ki Jhuki Hui Meenar)"
    },
    "forbidden city": {
        "Chinese (Simplified)": "故宫 (Gù gōng)",
        "Hindi": "निषिद्ध शहर (Nishiddh Shahar)"
    },
    "santorini": {
        "Chinese (Simplified)": "圣托里尼 (Shèng tuō lǐ ní)",
        "Hindi": "सैंटोरिनी (Santorini)"
    },
    "mount fuji": {
        "Chinese (Simplified)": "富士山 (Fù shì shān)",
        "Hindi": "माउंट फूजी (Mount Fuji)"
    },
    "buckingham palace": {
        "Chinese (Simplified)": "白金汉宫 (Bái jīn hàn gōng)",
        "Hindi": "बकिंघम पैलेस (Buckingham Palace)"
    },
    "niagara falls": {
        "Chinese (Simplified)": "尼亚加拉瀑布 (Ní yà jiā lā pù bù)",
        "Hindi": "नियाग्रा फॉल्स (Niagara Falls)"
    },
    "versailles palace": {
        "Chinese (Simplified)": "凡尔赛宫 (Fán ěr sài gōng)",
        "Hindi": "वर्साय पैलेस (Versailles Palace)"
    },
    "i": {
        "Chinese (Simplified)": "我 (wǒ)",
        "Hindi": "मैं (main)"
    },
    "you": {
        "Chinese (Simplified)": "你 (nǐ)",
        "Hindi": "तुम (tum)"
    },
    "he": {
        "Chinese (Simplified)": "他 (tā)",
        "Hindi": "वह (vah)"
    },
    "she": {
        "Chinese (Simplified)": "她 (tā)",
        "Hindi": "वह (vah)"
    },
    "we": {
        "Chinese (Simplified)": "我们 (wǒ men)",
        "Hindi": "हम (ham)"
    },
    "they": {
        "Chinese (Simplified)": "他们 (tā men)",
        "Hindi": "वे (ve)"
    },
    "me": {
        "Chinese (Simplified)": "我 (wǒ)",
        "Hindi": "मुझे (mujhe)"
    },
    "us": {
        "Chinese (Simplified)": "我们 (wǒ men)",
        "Hindi": "हमें (humein)"
    },
    "him": {
        "Chinese (Simplified)": "他 (tā)",
        "Hindi": "उसे (use)"
    },
    "her": {
        "Chinese (Simplified)": "她 (tā)",
        "Hindi": "उसे (use)"
    },
    "my": {
        "Chinese (Simplified)": "我的 (wǒ de)",
        "Hindi": "मेरा (mera)"
    },
    "your": {
        "Chinese (Simplified)": "你的 (nǐ de)",
        "Hindi": "तुम्हारा (tumhara)"
    },
    "his": {
        "Chinese (Simplified)": "他的 (tā de)",
        "Hindi": "उसका (uska)"
    },
    "her": {
        "Chinese (Simplified)": "她的 (tā de)",
        "Hindi": "उसकी (uski)"
    },
    "our": {
        "Chinese (Simplified)": "我们的 (wǒ men de)",
        "Hindi": "हमारा (hamara)"
    },
    "their": {
        "Chinese (Simplified)": "他们的 (tā men de)",
        "Hindi": "उनका (unka)"
    },
    "mine": {
        "Chinese (Simplified)": "我的 (wǒ de)",
        "Hindi": "मेरा (mera)"
    },
    "yours": {
        "Chinese (Simplified)": "你的 (nǐ de)",
        "Hindi": "तुम्हारा (tumhara)"
    },
    "his": {
        "Chinese (Simplified)": "他的 (tā de)",
        "Hindi": "उसका (uska)"
    },
    "hers": {
        "Chinese (Simplified)": "她的 (tā de)",
        "Hindi": "उसकी (uski)"
    },
    # Days of the Week
    "monday": {
        "Hindi": "सोमवार (Somvār)",
        "Chinese (Simplified)": "星期一 (xīngqī yī)"
    },
    "tuesday": {
        "Hindi": "मंगलवार (Mangalvār)",
        "Chinese (Simplified)": "星期二 (xīngqī èr)"
    },
    "wednesday": {
        "Hindi": "बुधवार (Budhvār)",
        "Chinese (Simplified)": "星期三 (xīngqī sān)"
    },
    "thursday": {
        "Hindi": "गुरुवार (Guruvār)",
        "Chinese (Simplified)": "星期四 (xīngqī sì)"
    },
    "friday": {
        "Hindi": "शुक्रवार (Shukravār)",
        "Chinese (Simplified)": "星期五 (xīngqī wǔ)"
    },
    "saturday": {
        "Hindi": "शनिवार (Shanivār)",
        "Chinese (Simplified)": "星期六 (xīngqī liù)"
    },
    "sunday": {
        "Hindi": "रविवार (Ravivār)",
        "Chinese (Simplified)": "星期天 (xīngqī tiān)"
    },
    # Seasons
    "spring": {
        "Hindi": "वसंत (Vasant)",
        "Chinese (Simplified)": "春天 (chūntiān)"
    },
    "summer": {
        "Hindi": "गर्मी (Garmī)",
        "Chinese (Simplified)": "夏天 (xiàtiān)"
    },
    "autumn": {
        "Hindi": "पतझड़ (Patjhaṛ)",
        "Chinese (Simplified)": "秋天 (qiūtiān)"
    },
    "winter": {
        "Hindi": "सर्दी (Sardī)",
        "Chinese (Simplified)": "冬天 (dōngtiān)"
    },
    "fruit": {
        "Hindi": "फल (phal)",
        "Chinese (Simplified)": "水果 (shuǐguǒ)"
    },
    "tea": {
        "Hindi": "चाय (chāy)",
        "Chinese (Simplified)": "茶 (chá)"
    },
    "see": {
        "Hindi": "देखना (dekhna)",
        "Chinese (Simplified)": "看 (kàn)"
    },
    "speak": {
        "Hindi": "बोलना (bolnā)",
        "Chinese (Simplified)": "说 (shuō)"
    },
    "kid": {
        "Hindi": "बच्चा (bachchā)",
        "Chinese (Simplified)": "孩子 (háizi)"
    },
    "hear": {
        "Hindi": "सुनना (sunnā)",
        "Chinese (Simplified)": "听 (tīng)"
    },
    "sea": {
        "Hindi": "समुद्र (samudra)",
        "Chinese (Simplified)": "海 (hǎi)"
    },
    "wall": {
        "Hindi": "दीवार (dīvār)",
        "Chinese (Simplified)": "墙 (qiáng)"
    },
    "nature": {
        "Hindi": "प्रकृति (prakṛti)",
        "Chinese (Simplified)": "自然 (zìrán)"
    },
    "milk": {
        "Hindi": "दूध (dūdh)",
        "Chinese (Simplified)": "牛奶 (niúnǎi)"
    },
    "air": {
        "Hindi": "हवा (havā)",
        "Chinese (Simplified)": "空气 (kōngqì)"
    },
    "hair": {
        "Hindi": "बाल (bāl)",
        "Chinese (Simplified)": "头发 (tóufǎ)"
    },
    # Weather Conditions
    "sunny": {
        "Hindi": "धूप (Dhūp)",
        "Chinese (Simplified)": "晴天 (qíngtiān)"
    },
    "cloudy": {
        "Hindi": "बादल (Bādal)",
        "Chinese (Simplified)": "多云 (duōyún)"
    },
    "rainy": {
        "Hindi": "बारिश (Bāriś)",
        "Chinese (Simplified)": "下雨 (xià yǔ)"
    },
    "snowy": {
        "Hindi": "बर्फबारी (Barfbarī)",
        "Chinese (Simplified)": "下雪 (xià xuě)"
    },
    "windy": {
        "Hindi": "हवाएँ (Hawāen)",
        "Chinese (Simplified)": "刮风 (guā fēng)"
    },
    "stormy": {
        "Hindi": "आंधी (Āndhī)",
        "Chinese (Simplified)": "风暴 (fēngbào)"
    },
    # Common Phrases
    "how much is this": {
        "Hindi": "यह कितना है? (Yeh kitna hai?)",
        "Chinese (Simplified)": "这个多少钱？ (zhège duōshao qián?)"
    },
    "i don't understand": {
        "Hindi": "मुझे समझ में नहीं आ रहा है (Mujhe samajh mein nahīn ā rahā hai)",
        "Chinese (Simplified)": "我不明白 (wǒ bù míngbái)"
    },
    "can you help me": {
        "Hindi": "क्या आप मेरी मदद कर सकते हैं? (Kya āp merī madad kar sakte hain?)",
        "Chinese (Simplified)": "你能帮我吗？ (nǐ néng bāng wǒ ma?)"
    },
    "what time is it": {
        "Hindi": "समय क्या हुआ है? (Samay kyā huā hai?)",
        "Chinese (Simplified)": "现在几点了？ (xiànzài jǐ diǎn le?)"
    },
    "where is the bathroom": {
        "Hindi": "बाथरूम कहाँ है? (Bāthrūm kahān hai?)",
        "Chinese (Simplified)": "洗手间在哪里？ (xǐshǒujiān zài nǎlǐ?)"
    },
    "i need food/water": {
        "Hindi": "मुझे खाना/पानी चाहिए (Mujhe khānā/pānī chāhiye)",
        "Chinese (Simplified)": "我需要食物/水 (wǒ xūyào shíwù/shuǐ)"
    },
    "i am lost": {
        "Hindi": "मैं खो गया हूँ (Main kho gayā hūn)",
        "Chinese (Simplified)": "我迷路了 (wǒ mílùle)"
    },
    # Time Expressions
    "today": {
        "Hindi": "आज (Āj)",
        "Chinese (Simplified)": "今天 (jīntiān)"
    },
    "tomorrow": {
        "Hindi": "कल (Kal)",
        "Chinese (Simplified)": "明天 (míngtiān)"
    },
    "yesterday": {
        "Hindi": "कल (Kal)",
        "Chinese (Simplified)": "昨天 (zuótiān)"
    },
    "now": {
        "Hindi": "अब (Ab)",
        "Chinese (Simplified)": "现在 (xiànzài)"
    },
    "later": {
        "Hindi": "बाद में (Bād mein)",
        "Chinese (Simplified)": "稍后 (shāo hòu)"
    },
    "soon": {
        "Hindi": "जल्द (Jald)",
        "Chinese (Simplified)": "很快 (hěn kuài)"
    },
    # Objects Around the House
    "table": {
        "Hindi": "मेज (Mēz)",
        "Chinese (Simplified)": "桌子 (zhuōzi)"
    },
    "chair": {
        "Hindi": "कुर्सी (Kursī)",
        "Chinese (Simplified)": "椅子 (yǐzi)"
    },
    "bed": {
        "Hindi": "बिस्तर (Bistar)",
        "Chinese (Simplified)": "床 (chuáng)"
    },
    "tv": {
        "Hindi": "टीवी (TīVī)",
        "Chinese (Simplified)": "电视 (diànshì)"
    },
    "refrigerator": {
        "Hindi": "फ्रिज (Frij)",
        "Chinese (Simplified)": "冰箱 (bīngxiāng)"
    },
    "door": {
        "Hindi": "दरवाज़ा (Darwāzā)",
        "Chinese (Simplified)": "门 (mén)"
    },
    "window": {
        "Hindi": "खिड़की (Khiṛkī)",
        "Chinese (Simplified)": "窗户 (chuānghù)"
    },
    # Emotions/Feelings
    "excited": {
        "Hindi": "उत्साहित (Utsāhit)",
        "Chinese (Simplified)": "兴奋 (xīngfèn)"
    },
    "nervous": {
        "Hindi": "नर्वस (Narvas)",
        "Chinese (Simplified)": "紧张 (jǐnzhāng)"
    },
    "angry": {
        "Hindi": "गुस्से में (Gusse mein)",
        "Chinese (Simplified)": "生气 (shēngqì)"
    },
    "surprised": {
        "Hindi": "हैरान (Hairān)",
        "Chinese (Simplified)": "惊讶 (jīngyà)"
    },
    "bore": {
        "Hindi": "बोर (Bore)",
        "Chinese (Simplified)": "无聊 (wúliáo)"
    },
    "confused": {
        "Hindi": "भ्रमित (Bhramit)",
        "Chinese (Simplified)": "困惑 (kùnhuò)"
    },
    "anxious": {
        "Hindi": "चिंतित (Chintit)",
        "Chinese (Simplified)": "焦虑 (jiāolǜ)"
    },
    "hand": {
        "Hindi": "हाथ (haath)",
        "Chinese (Simplified)": "手 (shǒu)"
    },
    "leg": {
        "Hindi": "टांग (taang)",
        "Chinese (Simplified)": "腿 (tuǐ)"
    },
    "nose": {
        "Hindi": "नाक (naak)",
        "Chinese (Simplified)": "鼻子 (bízi)"
    },
    "mouth": {
        "Hindi": "मुंह (munh)",
        "Chinese (Simplified)": "嘴巴 (zuǐba)"
    },
    "ear": {
        "Hindi": "कान (kaan)",
        "Chinese (Simplified)": "耳朵 (ěrduo)"
    },
    "heart": {
        "Hindi": "दिल (dil)",
        "Chinese (Simplified)": "心脏 (xīnzàng)"
    },
    "stomach": {
        "Hindi": "पेट (pet)",
        "Chinese (Simplified)": "胃 (wèi)"
    },
    "head": {
        "Hindi": "सिर (sir)",
        "Chinese (Simplified)": "头 (tóu)"
    },
    "brain": {
        "Hindi": "मस्तिष्क (mastishk)",
        "Chinese (Simplified)": "大脑 (dànǎo)"
    },
    "uncle": {
        "Hindi": "चाचा/फूफा (chacha/fufa)",
        "Chinese (Simplified)": "叔叔 (shūshu)"
    },
    "aunt": {
        "Hindi": "चाची/फूफी (chachi/foofi)",
        "Chinese (Simplified)": "阿姨 (āyí)"
    },
    "son": {
        "Hindi": "पुत्र (putra)",
        "Chinese (Simplified)": "儿子 (érzi)"
    },
    "daughter": {
        "Hindi": "बेटी (beti)",
        "Chinese (Simplified)": "女儿 (nǚ'ér)"
    },
    "grandfather": {
        "Hindi": "दादा/नाना (dada/nana)",
        "Chinese (Simplified)": "祖父 (zǔfù)"
    },
    "grandmother": {
        "Hindi": "दादी/नानी (daadi/naani)",
        "Chinese (Simplified)": "祖母 (zǔmǔ)"
    },
    "car": {
    "Hindi": "कार (kaar)",
    "Chinese (Simplified)": "汽车 (qìchē)"
    },
    "bus": {
        "Hindi": "बस (bas)",
        "Chinese (Simplified)": "公共汽车 (gōnggòng qìchē)"
    },
    "train": {
        "Hindi": "ट्रेन (train)",
        "Chinese (Simplified)": "火车 (huǒchē)"
    },
    "bicycle": {
        "Hindi": "साइकिल (saikil)",
        "Chinese (Simplified)": "自行车 (zìxíngchē)"
    },
    "airplane": {
        "Hindi": "विमान (viman)",
        "Chinese (Simplified)": "飞机 (fēijī)"
    },
    "ship": {
        "Hindi": "जहाज (jahaz)",
        "Chinese (Simplified)": "船 (chuán)"
    },
    "motorcycle": {
        "Hindi": "मोटरसाइकिल (motorcycle)",
        "Chinese (Simplified)": "摩托车 (mótuōchē)"
    },
    "helicopter": {
        "Hindi": "हेलिकॉप्टर (helicopter)",
        "Chinese (Simplified)": "直升机 (zhíshēngjī)"
    },
    "boat": {
        "Hindi": "नौका (nauka)",
        "Chinese (Simplified)": "船 (chuán)"
    },
    "truck": {
        "Hindi": "ट्रक (truck)",
        "Chinese (Simplified)": "卡车 (kǎchē)"
    },
    "pizza": {
    "Hindi": "पिज़्ज़ा (pizza)",
    "Chinese (Simplified)": "比萨 (bǐsà)"
    },
    "burger": {
        "Hindi": "बर्गर (burger)",
        "Chinese (Simplified)": "汉堡 (hànbǎo)"
    },
    "pasta": {
        "Hindi": "पास्ता (pasta)",
        "Chinese (Simplified)": "意大利面 (yìdàlì miàn)"
    },
    "noodles": {
        "Hindi": "नूडल्स (noodles)",
        "Chinese (Simplified)": "面条 (miàntiáo)"
    },
    "salad": {
        "Hindi": "सलाद (salaad)",
        "Chinese (Simplified)": "沙拉 (shālā)"
    },
    "ice cream": {
        "Hindi": "आइस क्रीम (ice cream)",
        "Chinese (Simplified)": "冰淇淋 (bīngqílín)"
    },
    "cake": {
        "Hindi": "केक (cake)",
        "Chinese (Simplified)": "蛋糕 (dàngāo)"
    },
    "juice": {
        "Hindi": "जूस (juice)",
        "Chinese (Simplified)": "果汁 (guǒzhī)"
    },
    "coffee": {
        "Hindi": "कॉफ़ी (coffee)",
        "Chinese (Simplified)": "咖啡 (kāfēi)"
    },
    "tea": {
        "Hindi": "चाय (chaay)",
        "Chinese (Simplified)": "茶 (chá)"
    },
    "run": {
    "Hindi": "दौड़ना (daudna)",
    "Chinese (Simplified)": "跑 (pǎo)"
    },
    "walk": {
        "Hindi": "चलना (chalna)",
        "Chinese (Simplified)": "走 (zǒu)"
    },
    "eat": {
        "Hindi": "खाना (khana)",
        "Chinese (Simplified)": "吃 (chī)"
    },
    "sleep": {
        "Hindi": "सोना (sona)",
        "Chinese (Simplified)": "睡觉 (shuìjiào)"
    },
    "jump": {
        "Hindi": "कूदना (koodna)",
        "Chinese (Simplified)": "跳 (tiào)"
    },
    "laugh": {
        "Hindi": "हँसना (hansna)",
        "Chinese (Simplified)": "笑 (xiào)"
    },
    "cry": {
        "Hindi": "रोना (rona)",
        "Chinese (Simplified)": "哭 (kū)"
    },
    "read": {
        "Hindi": "पढ़ना (padhna)",
        "Chinese (Simplified)": "读 (dú)"
    },
    "write": {
        "Hindi": "लिखना (likhna)",
        "Chinese (Simplified)": "写 (xiě)"
    },
    "sing": {
        "Hindi": "गाना (gana)",
        "Chinese (Simplified)": "唱 (chàng)"
    },
    "circle": {
    "Hindi": "वृत्त (vritt)",
    "Chinese (Simplified)": "圆形 (yuánxíng)"
    },
    "square": {
        "Hindi": "वर्ग (varg)",
        "Chinese (Simplified)": "正方形 (zhèngfāngxíng)"
    },
    "triangle": {
        "Hindi": "त्रिकोण (trikon)",
        "Chinese (Simplified)": "三角形 (sānjiǎoxíng)"
    },
    "rectangle": {
        "Hindi": "आयत (ayat)",
        "Chinese (Simplified)": "矩形 (jǔxíng)"
    },
    "oval": {
        "Hindi": "अंडाकार (andakaar)",
        "Chinese (Simplified)": "椭圆形 (tuǒyuánxíng)"
    },
    "star": {
        "Hindi": "तारा (tara)",
        "Chinese (Simplified)": "星星 (xīngxing)"
    },
    "heart": {
        "Hindi": "दिल (dil)",
        "Chinese (Simplified)": "心形 (xīn xíng)"
    },
    "diamond": {
        "Hindi": "हीरा (heera)",
        "Chinese (Simplified)": "钻石 (zuànshí)"
    },
    "pentagon": {
        "Hindi": "पेंटागन (pentagon)",
        "Chinese (Simplified)": "五边形 (wǔbiānxíng)"
    },
    "hexagon": {
        "Hindi": "षटकोण (shatkona)",
        "Chinese (Simplified)": "六边形 (liùbiānxíng)"
    },
    # 5. **Natural Elements**
    "earth": {
        "Hindi": "पृथ्वी (prithvi)",
        "Chinese (Simplified)": "地球 (dìqiú)"
    },
    "water": {
        "Hindi": "पानी (paani)",
        "Chinese (Simplified)": "水 (shuǐ)"
    },
    "fire": {
        "Hindi": "आग (aag)",
        "Chinese (Simplified)": "火 (huǒ)"
    },
    "air": {
        "Hindi": "हवा (hawa)",
        "Chinese (Simplified)": "空气 (kōngqì)"
    },
    "light": {
        "Hindi": "रोशनी (roshni)",
        "Chinese (Simplified)": "光 (guāng)"
    },
    "dark": {
        "Hindi": "अंधेरा (andhera)",
        "Chinese (Simplified)": "黑暗 (hēi'àn)"
    },
    # 8. **Instruments (Musical)**
    "guitar": {
        "Hindi": "गिटार (guitar)",
        "Chinese (Simplified)": "吉他 (jítā)"
    },
    "piano": {
        "Hindi": "पियानो (piyano)",
        "Chinese (Simplified)": "钢琴 (gāngqín)"
    },
    "drums": {
        "Hindi": "ढोल (dhol)",
        "Chinese (Simplified)": "鼓 (gǔ)"
    },
    "violin": {
        "Hindi": "वायोलिन (violin)",
        "Chinese (Simplified)": "小提琴 (xiǎotíqín)"
    },
    "flute": {
        "Hindi": "बांसुरी (bansuri)",
        "Chinese (Simplified)": "长笛 (chángdí)"
    },
    "trumpet": {
        "Hindi": "तबला (tabla)",
        "Chinese (Simplified)": "小号 (xiǎo hào)"
    },
    # 9. **Occupations**
    "teacher": {
        "Hindi": "शिक्षक (shikshak)",
        "Chinese (Simplified)": "老师 (lǎoshī)"
    },
    "doctor": {
        "Hindi": "डॉक्टर (doctor)",
        "Chinese (Simplified)": "医生 (yīshēng)"
    },
    "engineer": {
        "Hindi": "इंजीनियर (engineer)",
        "Chinese (Simplified)": "工程师 (gōngchéngshī)"
    },
    "lawyer": {
        "Hindi": "वकील (vakil)",
        "Chinese (Simplified)": "律师 (lǜshī)"
    },
    "artist": {
        "Hindi": "कला कलाकार (kala kalakar)",
        "Chinese (Simplified)": "艺术家 (yìshùjiā)"
    },
    "scientist": {
        "Hindi": "वैज्ञानिक (vaigyanik)",
        "Chinese (Simplified)": "科学家 (kēxuéjiā)"
    },
    # 11. **Months of the Year**
    "january": {
        "Hindi": "जनवरी (janvari)",
        "Chinese (Simplified)": "一月 (yī yuè)"
    },
    "february": {
        "Hindi": "फरवरी (farvari)",
        "Chinese (Simplified)": "二月 (èryuè)"
    },
    "march": {
        "Hindi": "मार्च (maarch)",
        "Chinese (Simplified)": "三月 (sān yuè)"
    },
    "april": {
        "Hindi": "अप्रैल (aprail)",
        "Chinese (Simplified)": "四月 (sì yuè)"
    },
    "may": {
        "Hindi": "मई (mai)",
        "Chinese (Simplified)": "五月 (wǔ yuè)"
    },
    "june": {
        "Hindi": "जून (june)",
        "Chinese (Simplified)": "六月 (liù yuè)"
    },
    "july": {
        "Hindi": "जुलाई (julaai)",
        "Chinese (Simplified)": "七月 (qī yuè)"
    },
    "august": {
        "Hindi": "अगस्त (agast)",
        "Chinese (Simplified)": "八月 (bā yuè)"
    },
    "september": {
        "Hindi": "सितंबर (sitamber)",
        "Chinese (Simplified)": "九月 (jiǔ yuè)"
    },
    "october": {
        "Hindi": "अक्टूबर (aktoobar)",
        "Chinese (Simplified)": "十月 (shí yuè)"
    },
    "november": {
        "Hindi": "नवंबर (navambar)",
        "Chinese (Simplified)": "十一月 (shíyī yuè)"
    },
    "december": {
        "Hindi": "दिसंबर (disambar)",
        "Chinese (Simplified)": "十二月 (shí'èr yuè)"
    },
    # 12. **Types of Trees**
    "oak": {
        "Hindi": "बलूत का पेड़ (baloot ka ped)",
        "Chinese (Simplified)": "橡树 (xiàng shù)"
    },
    "pine": {
        "Hindi": "देवदार का पेड़ (devdaar ka ped)",
        "Chinese (Simplified)": "松树 (sōng shù)"
    },
    "maple": {
        "Hindi": "मेपल (maple)",
        "Chinese (Simplified)": "枫树 (fēng shù)"
    },
    "birch": {
        "Hindi": "बर्च (birch)",
        "Chinese (Simplified)": "桦树 (huà shù)"
    },
    "willow": {
        "Hindi": "विलो (willow)",
        "Chinese (Simplified)": "柳树 (liǔ shù)"
    },
    "cherry": {
        "Hindi": "चेरी (cherry)",
        "Chinese (Simplified)": "樱桃 (yīngtáo)"
    },
    # 13. **Types of Flowers**
    "rose": {
        "Hindi": "गुलाब (gulaab)",
        "Chinese (Simplified)": "玫瑰 (méiguī)"
    },
    "tulip": {
        "Hindi": "ट्यूलिप (tulip)",
        "Chinese (Simplified)": "郁金香 (yù jīn xiāng)"
    },
    "lily": {
        "Hindi": "लिली (lily)",
        "Chinese (Simplified)": "百合 (bǎihé)"
    },
    "sunflower": {
        "Hindi": "सूरजमुखी (soorajmukhi)",
        "Chinese (Simplified)": "向日葵 (xiàngrìkuí)"
    },
    "daisy": {
        "Hindi": "डेज़ी (daisy)",
        "Chinese (Simplified)": "雏菊 (chújú)"
    },
    "orchid": {
        "Hindi": "आर्किड (orchid)",
        "Chinese (Simplified)": "兰花 (lánhuā)"
    },
    #Numbers
    "one": {
        "Hindi": "एक (ek)",
        "Chinese (Simplified)": "一 (yī)"
    },
    "two": {
        "Hindi": "दो (do)",
        "Chinese (Simplified)": "二 (èr)"
    },
    "three": {
        "Hindi": "तीन (tīn)",
        "Chinese (Simplified)": "三 (sān)"
    },
    "four": {
        "Hindi": "चार (chār)",
        "Chinese (Simplified)": "四 (sì)"
    },
    "five": {
        "Hindi": "पाँच (pāँch)",
        "Chinese (Simplified)": "五 (wǔ)"
    },
    "six": {
        "Hindi": "छे (che)",
        "Chinese (Simplified)": "六 (liù)"
    },
    "seven": {
        "Hindi": "सात (sāt)",
        "Chinese (Simplified)": "七 (qī)"
    },
    "eight": {
        "Hindi": "आठ (aaṭ)",
        "Chinese (Simplified)": "八 (bā)"
    },
    "nine": {
        "Hindi": "नौ (nau)",
        "Chinese (Simplified)": "九 (jiǒu)"
    },
    "ten": {
        "Hindi": "दस (das)",
        "Chinese (Simplified)": "十 (shí)"
    },
    "okay": {
        "Hindi": "ठीक (ṭhīk)",
        "Chinese (Simplified)": "好 (hǎo)"
    },
    "wrong": {
        "Hindi": "गलत (galat)",
        "Chinese (Simplified)": "错 (cuò)"
    },
    "lock": {
        "Hindi": "ताला (tālā)",
        "Chinese (Simplified)": "锁 (suǒ)"
    },
    "broom": {
        "Hindi": "झाड़ू (jhāṛū)",
        "Chinese (Simplified)": "扫帚 (sàozhǒu)"
    },
    "knife": {
        "Hindi": "चाकू (cākū)",
        "Chinese (Simplified)": "刀 (dāo)"
    },
    "groom": {
        "Hindi": "दूल्हा (dūlhā)",
        "Chinese (Simplified)": "新郎 (xīnláng)"
    },
    "bride": {
        "Hindi": "दुल्हन (dulhan)",
        "Chinese (Simplified)": "新娘 (xīnniáng)"
    },
    "tray": {
        "Hindi": "थाली (thālī)",
        "Chinese (Simplified)": "托盘 (tuōpán)"
    },
    "gun": {
        "Hindi": "बंदूक (bandūk)",
        "Chinese (Simplified)": "枪 (qiāng)"
    },
    "steam": {
        "Hindi": "भाप (bhāp)",
        "Chinese (Simplified)": "蒸汽 (zhēngqì)"
    },
    "box": {
        "Hindi": "डिब्बा (ḍibbā)",
        "Chinese (Simplified)": "盒子 (hézi)"
    },
    "total": {
        "Hindi": "कुल (kul)",
        "Chinese (Simplified)": "总计 (zǒngjì)"
    },
    "end": {
        "Hindi": "अंत (ant)",
        "Chinese (Simplified)": "结束 (jiéshù)"
    },
    "search": {
        "Hindi": "खोज (khoj)",
        "Chinese (Simplified)": "搜索 (sōusuǒ)"
    },
    "line": {
        "Hindi": "रेखा (rekhā)",
        "Chinese (Simplified)": "线 (xiàn)"
    },
    "sphere": {
        "Hindi": "गोला (golā)",
        "Chinese (Simplified)": "球体 (qiútǐ)"
    },
    "space": {
        "Hindi": "अंतरिक्ष (antarikṣ)",
        "Chinese (Simplified)": "空间 (kōngjiān)"
    },
    "seat": {
        "Hindi": "सीट (sīṭ)",
        "Chinese (Simplified)": "座位 (zuòwèi)"
    },
    "straight": {
        "Hindi": "सीधा (sīdhā)",
        "Chinese (Simplified)": "直的 (zhí de)"
    },
    "beautiful": {
        "Hindi": "सुंदर (sundar)",
        "Chinese (Simplified)": "美丽 (měilì)"
    },
    "ugly": {
        "Hindi": "बदसूरत (badsūrat)",
        "Chinese (Simplified)": "丑陋 (chǒulòu)"
    },
    "truth": {
        "Hindi": "सत्य (satya)",
        "Chinese (Simplified)": "真相 (zhēnxiàng)"
    },
    "lie": {
        "Hindi": "झूठ (jhūṭh)",
        "Chinese (Simplified)": "谎言 (huǎngyán)"
    },
    "lean": {
        "Hindi": "झुकना (jhuknā)",
        "Chinese (Simplified)": "倾斜 (qīngxié)"
    },
    "stand": {
        "Hindi": "खड़ा होना (khaḍā honā)",
        "Chinese (Simplified)": "站立 (zhànlì)"
    },
    "sit": {
        "Hindi": "बैठना (baiṭhnā)",
        "Chinese (Simplified)": "坐下 (zuòxià)"
    },
    "solve": {
        "Hindi": "सुलझाना (suljhanā)",
        "Chinese (Simplified)": "解决 (jiějué)"
    },
    "broke": {
        "Hindi": "टूट गया (ṭūṭ gayā)",
        "Chinese (Simplified)": "破了 (pò le)"
    },
    "break": {
        "Hindi": "तोड़ना (toṛnā)",
        "Chinese (Simplified)": "打破 (dǎpò)"
    },
    "suck": {
        "Hindi": "चूसना (chūsna)",
        "Chinese (Simplified)": "吸 (xī)"
    },
    "weight": {
        "Hindi": "वजन (vajan)",
        "Chinese (Simplified)": "重量 (zhòngliàng)"
    },
    "thin": {
        "Hindi": "पतला (patlā)",
        "Chinese (Simplified)": "瘦 (shòu)"
    },
    "villain": {
        "Hindi": "खलनायक (khalnāyak)",
        "Chinese (Simplified)": "反派 (fǎnpài)"
    },
    "thick": {
        "Hindi": "मोटा (moṭā)",
        "Chinese (Simplified)": "厚 (hòu)"
    },
    "male": {
        "Hindi": "पुरुष (puruṣ)",
        "Chinese (Simplified)": "男性 (nánxìng)"
    },
    "female": {
        "Hindi": "महिला (mahilā)",
        "Chinese (Simplified)": "女性 (nǚxìng)"
    },
    "galaxy": {
        "Hindi": "आकाशगंगा (ākāshgaṅgā)",
        "Chinese (Simplified)": "银河系 (yínhéxì)"
    },
    "star": {
        "Hindi": "तारा (tārā)",
        "Chinese (Simplified)": "星 (xīng)"
    },
    "drop": {
        "Hindi": "गिरना (girnā)",
        "Chinese (Simplified)": "掉落 (diàoluò)"
    },
    "catch": {
        "Hindi": "पकड़ना (pakaṛnā)",
        "Chinese (Simplified)": "抓住 (zhuāzhù)"
    },
    "take": {
        "Hindi": "लेना (lenā)",
        "Chinese (Simplified)": "拿 (ná)"
    },
    "throw": {
        "Hindi": "फेंकना (pheṅknā)",
        "Chinese (Simplified)": "扔 (rēng)"
    },
    "talk": {
        "Hindi": "बात करना (bāt karnā)",
        "Chinese (Simplified)": "谈话 (tánhuà)"
    },
    "share": {
        "Hindi": "साझा करना (sājhā karnā)",
        "Chinese (Simplified)": "分享 (fēnxiǎng)"
    },
    "professional": {
        "Hindi": "पेशेवर (peshevar)",
        "Chinese (Simplified)": "专业的 (zhuānyè de)"
    },
    "expert": {
        "Hindi": "विशेषज्ञ (viśeṣajña)",
        "Chinese (Simplified)": "专家 (zhuānjiā)"
    },
    "noob": {
        "Hindi": "नौसिखिया (nausikhiyā)",
        "Chinese (Simplified)": "菜鸟 (càiniǎo)"
    },
    "true": {
        "Hindi": "सच (sach)",
        "Chinese (Simplified)": "真实 (zhēnshí)"
    },
    "false": {
        "Hindi": "झूठा (jhūṭhā)",
        "Chinese (Simplified)": "虚假 (xūjiǎ)"
    },
    "board": {
        "Hindi": "पट्टिका (paṭṭikā)",
        "Chinese (Simplified)": "板 (bǎn)"
    },
    "speed": {
        "Hindi": "गति (gati)",
        "Chinese (Simplified)": "速度 (sùdù)"
    },
    "release": {
        "Hindi": "जारी करना (jārī karnā)",
        "Chinese (Simplified)": "释放 (shìfàng)"
    },
    "limit": {
        "Hindi": "सीमा (sīmā)",
        "Chinese (Simplified)": "限制 (xiànzhì)"
    },
    "loss": {
        "Hindi": "हानि (hāni)",
        "Chinese (Simplified)": "损失 (sǔnshī)"
    },
    "lost": {
        "Hindi": "खो गया (kho gayā)",
        "Chinese (Simplified)": "迷失 (míshī)"
    },
    "found": {
        "Hindi": "मिला (milā)",
        "Chinese (Simplified)": "找到 (zhǎodào)"
    },
    "find": {
        "Hindi": "ढूंढना (ḍhūṇḍhnā)",
        "Chinese (Simplified)": "寻找 (xúnzhǎo)"
    },
    "color": {
        "Hindi": "रंग (raṅg)",
        "Chinese (Simplified)": "颜色 (yánsè)"
    },
    "check": {
        "Hindi": "जांचना (jānchnā)",
        "Chinese (Simplified)": "检查 (jiǎnchá)"
    },
    "question": {
        "Hindi": "प्रश्न (praśn)",
        "Chinese (Simplified)": "问题 (wèntí)"
    },
    "answer": {
        "Hindi": "उत्तर (uttar)",
        "Chinese (Simplified)": "答案 (dáàn)"
    },
    "view": {
        "Hindi": "दृश्य (dṛśya)",
        "Chinese (Simplified)": "视图 (shìtú)"
    },
    "show": {
        "Hindi": "दिखाना (dikhānā)",
        "Chinese (Simplified)": "显示 (xiǎnshì)"
    },
    "hide": {
        "Hindi": "छुपाना (chhupānā)",
        "Chinese (Simplified)": "隐藏 (yǐncáng)"
    },
    "famous": {
        "Hindi": "प्रसिद्ध (prasiddh)",
        "Chinese (Simplified)": "著名 (zhùmíng)"
    },
    "amazing": {
        "Hindi": "शानदार (śāndār)",
        "Chinese (Simplified)": "惊人 (jīngrén)"
    },
    "awesome": {
        "Hindi": "कमाल (kamāl)",
        "Chinese (Simplified)": "太棒了 (tài bàng le)"
    },
    "expand": {
        "Hindi": "फैलाना (phailānā)",
        "Chinese (Simplified)": "扩展 (kuòzhǎn)"
    },
    "shrink": {
        "Hindi": "सिकुड़ना (sikuṛnā)",
        "Chinese (Simplified)": "收缩 (shōusuō)"
    },
    "opposite": {
        "Hindi": "विपरीत (viparīt)",
        "Chinese (Simplified)": "相反 (xiāngfǎn)"
    },
    "buy": {
        "Hindi": "खरीदना (kharīdnā)",
        "Chinese (Simplified)": "买 (mǎi)"
    },
    "sell": {
        "Hindi": "बेचना (bechnā)",
        "Chinese (Simplified)": "卖 (mài)"
    },
    "trade": {
        "Hindi": "वाणिज्य (vāṇijya)",
        "Chinese (Simplified)": "贸易 (màoyì)"
    },
    "travel": {
        "Hindi": "यात्रा (yātrā)",
        "Chinese (Simplified)": "旅行 (lǚxíng)"
    },
    "land": {
        "Hindi": "भूमि (bhūmi)",
        "Chinese (Simplified)": "土地 (tǔdì)"
    },
    "farm": {
        "Hindi": "खेती (khetī)",
        "Chinese (Simplified)": "农场 (nóngchǎng)"
    },
    "crow man": {
        "Hindi": "कौआ आदमी (kauā ādmī)",
        "Chinese (Simplified)": "乌鸦人 (wūyā rén)"
    },
    "year": {
        "Hindi": "वर्ष (varṣ)",
        "Chinese (Simplified)": "年 (nián)"
    },
    "weak": {
        "Hindi": "कमज़ोर (kamzōr)",
        "Chinese (Simplified)": "弱 (ruò)"
    },
    "strong": {
        "Hindi": "मजबूत (majabūt)",
        "Chinese (Simplified)": "强 (qiáng)"
    },
    "powerful": {
        "Hindi": "शक्तिशाली (śaktishālī)",
        "Chinese (Simplified)": "强大 (qiángdà)"
    },
    "month": {
        "Hindi": "महीना (mahinā)",
        "Chinese (Simplified)": "月 (yuè)"
    },
    "week": {
        "Hindi": "सप्ताह (saptāh)",
        "Chinese (Simplified)": "周 (zhōu)"
    },
    "decade": {
        "Hindi": "दशक (daśak)",
        "Chinese (Simplified)": "十年 (shí nián)"
    },
    "century": {
        "Hindi": "सदी (sadī)",
        "Chinese (Simplified)": "世纪 (shìjì)"
    },
    # Bird names
    "crow": {
        "Hindi": "कौआ (kauā)",
        "Chinese (Simplified)": "乌鸦 (wūyā)"
    },
    "parrot": {
        "Hindi": "तोता (totā)",
        "Chinese (Simplified)": "鹦鹉 (yīngwǔ)"
    },
    "eagle": {
        "Hindi": "गरुड़ (garuḍ)",
        "Chinese (Simplified)": "鹰 (yīng)"
    },
    "sparrow": {
        "Hindi": "गौरैया (gauraiyā)",
        "Chinese (Simplified)": "麻雀 (máquè)"
    },
    "pigeon": {
        "Hindi": "कबूतर (kabūtar)",
        "Chinese (Simplified)": "鸽子 (gēzi)"
    },
    "owl": {
        "Hindi": "उल्लू (ullū)",
        "Chinese (Simplified)": "猫头鹰 (māo tóu yīng)"
    },
    "peacock": {
        "Hindi": "मोर (mor)",
        "Chinese (Simplified)": "孔雀 (kǒngquè)"
    },
    "duck": {
        "Hindi": "बतख (batakh)",
        "Chinese (Simplified)": "鸭子 (yāzi)"
    },
    "flamingo": {
        "Hindi": "फ्लेमिंगो (phlemīngō)",
        "Chinese (Simplified)": "火烈鸟 (huǒ liè niǎo)"
    },
    "hawk": {
        "Hindi": "बाज़ (bāz)",
        "Chinese (Simplified)": "猎鹰 (liè yīng)"
    },
    "eagle": {
        "Hindi": "गरुड़ (garuḍ)",
        "Chinese (Simplified)": "鹰 (yīng)"
    },
    "vulture": {
        "Hindi": "गिद्ध (giddh)",
        "Chinese (Simplified)": "秃鹰 (tū yīng)"
    },
    "woodpecker": {
        "Hindi": "तोता (totā)",
        "Chinese (Simplified)": "啄木鸟 (zhuó mù niǎo)"
    },
    "seagull": {
        "Hindi": "समुद्री गULL (samudrī gull)",
        "Chinese (Simplified)": "海鸥 (hǎi'ōu)"
    },
    "swallow": {
        "Hindi": "स्वालो (swālō)",
        "Chinese (Simplified)": "燕子 (yànzi)"
    },
    "peacock": {
        "Hindi": "मोर (mor)",
        "Chinese (Simplified)": "孔雀 (kǒngquè)"
    },
    "robin": {
        "Hindi": "रोबिन (robin)",
        "Chinese (Simplified)": "知更鸟 (zhī gèng niǎo)"
    },
    "flamingo": {
        "Hindi": "फ्लेमिंगो (phlemīngō)",
        "Chinese (Simplified)": "火烈鸟 (huǒ liè niǎo)"
    },
    "pigeon": {
        "Hindi": "कबूतर (kabūtar)",
        "Chinese (Simplified)": "鸽子 (gēzi)"
    },
    "cockatoo": {
        "Hindi": "कॉकाटू (cockatoo)",
        "Chinese (Simplified)": "凤头鹦鹉 (fèng tóu yīngwǔ)"
    },
    "exam": {
        "Hindi": "परीक्षा (parīkṣā)",
        "Chinese (Simplified)": "考试 (kǎoshì)"
    },
    "result": {
        "Hindi": "परिणाम (pariṇām)",
        "Chinese (Simplified)": "结果 (jiéguǒ)"
    },
    "pass": {
        "Hindi": "उत्तीर्ण (uttīrṇ)",
        "Chinese (Simplified)": "通过 (tōngguò)"
    },
    "fail": {
        "Hindi": "असफल (asafal)",
        "Chinese (Simplified)": "失败 (shībài)"
    },
    "failure": {
        "Hindi": "विफलता (viphalatā)",
        "Chinese (Simplified)": "失败 (shībài)"
    },
    "like": {
        "Hindi": "पसंद (pasand)",
        "Chinese (Simplified)": "喜欢 (xǐhuān)"
    },
    "dislike": {
        "Hindi": "नापसंद (nāpasand)",
        "Chinese (Simplified)": "不喜欢 (bù xǐhuān)"
    },
    "fine": {
        "Hindi": "ठीक (ṭhīk)",
        "Chinese (Simplified)": "好 (hǎo)"
    },
    "more": {
        "Hindi": "अधिक (adhik)",
        "Chinese (Simplified)": "更多 (gèng duō)"
    },
    "less": {
        "Hindi": "कम (kam)",
        "Chinese (Simplified)": "更少 (gèng shǎo)"
    },
    "change": {
        "Hindi": "परिवर्तन (parivartan)",
        "Chinese (Simplified)": "改变 (gǎibiàn)"
    },
    "know": {
        "Hindi": "जानना (jānānā)",
        "Chinese (Simplified)": "知道 (zhīdào)"
    },
    "alive": {
        "Hindi": "जीवित (jīvit)",
        "Chinese (Simplified)": "活着 (huózhe)"
    },
    "dead": {
        "Hindi": "मृत (mṛt)",
        "Chinese (Simplified)": "死 (sǐ)"
    },
    "use": {
        "Hindi": "उपयोग (upayog)",
        "Chinese (Simplified)": "使用 (shǐyòng)"
    },
    "with": {
        "Hindi": "साथ (sāth)",
        "Chinese (Simplified)": "与 (yǔ)"
    },
    "of": {
        "Hindi": "का (kā)",
        "Chinese (Simplified)": "的 (de)"
    },
    "off": {
        "Hindi": "बंद (band)",
        "Chinese (Simplified)": "关 (guān)"
    },
    "much": {
        "Hindi": "काफ़ी (kāfī)",
        "Chinese (Simplified)": "多 (duō)"
    },
    "done": {
        "Hindi": "पूरा (pūrā)",
        "Chinese (Simplified)": "完成 (wánchéng)"
    },
    "yet": {
        "Hindi": "अभी तक (abhī tak)",
        "Chinese (Simplified)": "还 (hái)"
    },
    "not": {
        "Hindi": "नहीं (nahīṁ)",
        "Chinese (Simplified)": "不 (bù)"
    },
    "increase": {
        "Hindi": "बढ़ाना (baṛhānā)",
        "Chinese (Simplified)": "增加 (zēngjiā)"
    },
    "decrease": {
        "Hindi": "घटाना (ghaṭānā)",
        "Chinese (Simplified)": "减少 (jiǎnshǎo)"
    },
    "curve": {
        "Hindi": "वक्र (vakra)",
        "Chinese (Simplified)": "曲线 (qūxiàn)"
    },
    "come": {
        "Hindi": "आना (ānā)",
        "Chinese (Simplified)": "来 (lái)"
    },
    "out": {
        "Hindi": "बाहर (bāhar)",
        "Chinese (Simplified)": "出去 (chūqù)"
    },
    "chest": {
        "Hindi": "छाती (chātī)",
        "Chinese (Simplified)": "胸部 (xiōngbù)"
    },
    "muscle": {
        "Hindi": "पेशी (peśī)",
        "Chinese (Simplified)": "肌肉 (jīròu)"
    },
    "image": {
        "Hindi": "चित्र (citra)",
        "Chinese (Simplified)": "图像 (túxiàng)"
    },
    "street": {
        "Hindi": "सड़क (saṛak)",
        "Chinese (Simplified)": "街道 (jiēdào)"
    },
    "candle": {
        "Hindi": "मोमबत्ती (mombaṭṭī)",
        "Chinese (Simplified)": "蜡烛 (làzhú)"
    },
    "put": {
        "Hindi": "रखना (rakhānā)",
        "Chinese (Simplified)": "放 (fàng)"
    },
    "pull": {
        "Hindi": "खींचना (khīnchnā)",
        "Chinese (Simplified)": "拉 (lā)"
    },
    "height": {
        "Hindi": "ऊंचाई (ūnchāī)",
        "Chinese (Simplified)": "高度 (gāodù)"
    },
    "information": {
        "Hindi": "जानकारी (jānkārī)",
        "Chinese (Simplified)": "信息 (xìnxī)"
    },
    "mistake": {
        "Hindi": "गलती (galatī)",
        "Chinese (Simplified)": "错误 (cuòwù)"
    },
    "just": {
        "Hindi": "सिर्फ (sirf)",
        "Chinese (Simplified)": "只是 (zhǐshì)"
    },
    "and": {
        "Hindi": "और (aur)",
        "Chinese (Simplified)": "和 (hé)"
    },
    "hat": {
        "Hindi": "टोपी (ṭopī)",
        "Chinese (Simplified)": "帽子 (màozi)"
    },
    "or": {
        "Hindi": "या (yā)",
        "Chinese (Simplified)": "或 (huò)"
    },
    "some": {
        "Hindi": "कुछ (kuch)",
        "Chinese (Simplified)": "一些 (yīxiē)"
    },
    "thing": {
        "Hindi": "चीज (chīz)",
        "Chinese (Simplified)": "东西 (dōngxī)"
    },
    "object": {
        "Hindi": "वस्तु (vastu)",
        "Chinese (Simplified)": "物体 (wùtǐ)"
    },
    "piece": {
        "Hindi": "टुकड़ा (ṭukṛā)",
        "Chinese (Simplified)": "块 (kuài)"
    },
    "simple": {
        "Hindi": "सादा (sādā)",
        "Chinese (Simplified)": "简单 (jiǎndān)"
    },
    "difficult": {
        "Hindi": "कठिन (kaṭhin)",
        "Chinese (Simplified)": "困难 (kùnnán)"
    },
    "easy": {
        "Hindi": "आसान (āsān)",
        "Chinese (Simplified)": "容易 (róngyì)"
    },
    "normal": {
        "Hindi": "सामान्य (sāmānya)",
        "Chinese (Simplified)": "正常 (zhèngcháng)"
    },
    "heaven": {
        "Hindi": "स्वर्ग (svarg)",
        "Chinese (Simplified)": "天堂 (tiāntáng)"
    },
    "hell": {
        "Hindi": "नरक (narak)",
        "Chinese (Simplified)": "地狱 (dìyù)"
    },
    "privilege": {
        "Hindi": "विशेषाधिकार (viśeṣādhikār)",
        "Chinese (Simplified)": "特权 (tèquán)"
    },
    "secret": {
        "Hindi": "रहस्य (rahasya)",
        "Chinese (Simplified)": "秘密 (mìmì)"
    },
    "expose": {
        "Hindi": "उघाड़ना (ughāṛnā)",
        "Chinese (Simplified)": "揭露 (jiēlù)"
    },
    "talent": {
        "Hindi": "प्रतिभा (pratibhā)",
        "Chinese (Simplified)": "天赋 (tiānfù)"
    },
    "inspire": {
        "Hindi": "प्रेरित करना (prērit karnā)",
        "Chinese (Simplified)": "激励 (jīlì)"
    },
    "aspire": {
        "Hindi": "आकांक्षा रखना (ākāṅkṣā rakhnā)",
        "Chinese (Simplified)": "渴望 (kěwàng)"
    },
    "poor": {
        "Hindi": "गरीब (garīb)",
        "Chinese (Simplified)": "贫穷 (pínqióng)"
    },
    "rich": {
        "Hindi": "अमीर (amīr)",
        "Chinese (Simplified)": "富有 (fùyǒu)"
    },
    "middle": {
        "Hindi": "मध्य (madhya)",
        "Chinese (Simplified)": "中间 (zhōngjiān)"
    },
    "medium": {
        "Hindi": "मध्यम (madhyam)",
        "Chinese (Simplified)": "中等 (zhōngděng)"
    },
    "sword": {
        "Hindi": "तलवार (talvār)",
        "Chinese (Simplified)": "剑 (jiàn)"
    },
    "shield": {
        "Hindi": "ढाल (ḍhāl)",
        "Chinese (Simplified)": "盾牌 (dùn pái)"
    },
    "attack": {
        "Hindi": "हमला (hamlā)",
        "Chinese (Simplified)": "攻击 (gōngjí)"
    },
    "watch": {
        "Hindi": "घड़ी (ghaṛī)",
        "Chinese (Simplified)": "手表 (shǒubiǎo)"
    },
    "super": {
        "Hindi": "सुपर (supar)",
        "Chinese (Simplified)": "超级 (chāojí)"
    },
    "crazy": {
        "Hindi": "पागल (pāgal)",
        "Chinese (Simplified)": "疯狂 (fēngkuáng)"
    },
    "college": {
        "Hindi": "कॉलेज (kōlej)",
        "Chinese (Simplified)": "大学 (dàxué)"
    },
    "education": {
        "Hindi": "शिक्षा (śikṣā)",
        "Chinese (Simplified)": "教育 (jiàoyù)"
    },
    "stress": {
        "Hindi": "तनाव (tanāv)",
        "Chinese (Simplified)": "压力 (yālì)"
    },
    "waste": {
        "Hindi": "अपशिष्ट (apśiṣṭ)",
        "Chinese (Simplified)": "浪费 (làngfèi)"
    },
    "improve": {
        "Hindi": "सुधारना (sudhārnā)",
        "Chinese (Simplified)": "改善 (gǎishàn)"
    },
    "palm": {
        "Hindi": "हाथ की हथेली (hāth kī hathelī)",
        "Chinese (Simplified)": "手掌 (shǒuzhǎng)"
    },
    "eye": {
        "Hindi": "आंख (āṅkh)",
        "Chinese (Simplified)": "眼睛 (yǎnjīng)"
    },
    "lick": {
        "Hindi": "चाटना (chāṭnā)",
        "Chinese (Simplified)": "舔 (tiǎn)"
    },
    "luck": {
        "Hindi": "भाग्य (bhāgya)",
        "Chinese (Simplified)": "运气 (yùnqì)"
    },
    "copy": {
        "Hindi": "नकल (nakal)",
        "Chinese (Simplified)": "复制 (fùzhì)"
    },
    "title": {
        "Hindi": "शीर्षक (śīrṣak)",
        "Chinese (Simplified)": "标题 (biāotí)"
    },
    "clean": {
        "Hindi": "साफ (sāf)",
        "Chinese (Simplified)": "干净 (gānjìng)"
    },
    "soft": {
        "Hindi": "मुलायम (mulāyam)",
        "Chinese (Simplified)": "软 (ruǎn)"
    },
    "wet": {
        "Hindi": "गीला (gīlā)",
        "Chinese (Simplified)": "湿 (shī)"
    },
    "dirt": {
        "Hindi": "मिट्टी (miṭṭī)",
        "Chinese (Simplified)": "泥土 (nítǔ)"
    },
    "plant": {
        "Hindi": "पौधा (paudhā)",
        "Chinese (Simplified)": "植物 (zhíwù)"
    },
    "dry": {
        "Hindi": "सूखा (sūkhā)",
        "Chinese (Simplified)": "干 (gān)"
    },
    "make": {
        "Hindi": "बनाना (banānā)",
        "Chinese (Simplified)": "做 (zuò)"
    },
    "action": {
        "Hindi": "क्रिया (kriyā)",
        "Chinese (Simplified)": "行动 (xíngdòng)"
    },
    "idea": {
        "Hindi": "विचार (vicār)",
        "Chinese (Simplified)": "主意 (zhǔyì)"
    },
    "choose": {
        "Hindi": "चुनना (chunnā)",
        "Chinese (Simplified)": "选择 (xuǎnzé)"
    },
    "best": {
        "Hindi": "सर्वश्रेष्ठ (sarvasreṣṭh)",
        "Chinese (Simplified)": "最好 (zuì hǎo)"
    },
    "shake": {
        "Hindi": "हिलाना (hilānā)",
        "Chinese (Simplified)": "摇动 (yáodòng)"
    },
    "shock": {
        "Hindi": "आघात (āghāt)",
        "Chinese (Simplified)": "震惊 (zhènjīng)"
    },
    "shy": {
        "Hindi": "लिजलिजा (lijalijā)",
        "Chinese (Simplified)": "害羞 (hàixiū)"
    },
    "stupid": {
        "Hindi": "मूर्ख (mūrkh)",
        "Chinese (Simplified)": "愚蠢 (yúchǔn)"
    },
    "meat": {
        "Hindi": "मांस (māns)",
        "Chinese (Simplified)": "肉 (ròu)"
    },
    "meet": {
        "Hindi": "मिलना (milnā)",
        "Chinese (Simplified)": "见面 (jiànmiàn)"
    },
    "together": {
        "Hindi": "साथ (sāth)",
        "Chinese (Simplified)": "一起 (yīqǐ)"
    },
    "butt": {
        "Hindi": "नितंब (nitamb)",
        "Chinese (Simplified)": "屁股 (pìgu)"
    },
    "humanity": {
        "Hindi": "मानवता (mānavtā)",
        "Chinese (Simplified)": "人类 (rénlèi)"
    },
    "group": {
        "Hindi": "समूह (samūh)",
        "Chinese (Simplified)": "群体 (qúntǐ)"
    },
    "community": {
        "Hindi": "समुदाय (samudāy)",
        "Chinese (Simplified)": "社区 (shèqū)"
    },
    "society": {
        "Hindi": "समाज (samāj)",
        "Chinese (Simplified)": "社会 (shèhuì)"
    },
    "town": {
        "Hindi": "कस्बा (kasbā)",
        "Chinese (Simplified)": "镇 (zhèn)"
    },
    "entry": {
        "Hindi": "प्रवेश (praveś)",
        "Chinese (Simplified)": "入口 (rùkǒu)"
    },
    "thigh": {
        "Hindi": "जांघ (jāṅgh)",
        "Chinese (Simplified)": "大腿 (dàtuǐ)"
    },
    "hand": {
        "Hindi": "हाथ (hāth)",
        "Chinese (Simplified)": "手 (shǒu)"
    },
    "foot": {
        "Hindi": "पैर (pēr)",
        "Chinese (Simplified)": "脚 (jiǎo)"
    },
    "bucket": {
        "Hindi": "बाल्टी (bālṭī)",
        "Chinese (Simplified)": "桶 (tǒng)"
    },
    "play": {
        "Hindi": "खेलना (khelnā)",
        "Chinese (Simplified)": "玩 (wán)"
    },
    "draw": {
        "Hindi": "खींचना (khīnchnā)",
        "Chinese (Simplified)": "画 (huà)"
    },
    "trick": {
        "Hindi": "चाल (chāl)",
        "Chinese (Simplified)": "把戏 (bǎxì)"
    },
    "trigger": {
        "Hindi": "ट्रिगर (ṭrigar)",
        "Chinese (Simplified)": "触发 (chùfā)"
    },
    "special": {
        "Hindi": "विशेष (viśeṣ)",
        "Chinese (Simplified)": "特别 (tèbié)"
    },
    "interact": {
        "Hindi": "परस्पर क्रिया करना (paraspar kriyā karnā)",
        "Chinese (Simplified)": "互动 (hùdòng)"
    },
    "count": {
        "Hindi": "गिनती (gintī)",
        "Chinese (Simplified)": "计数 (jìshù)"
    },
    "agree": {
        "Hindi": "सहमत होना (sahamat honā)",
        "Chinese (Simplified)": "同意 (tóngyì)"
    },
    "disagree": {
        "Hindi": "असहमत होना (asahamat honā)",
        "Chinese (Simplified)": "不同意 (bùtóngyì)"
    },
    "naked": {
        "Hindi": "नग्न (nagna)",
        "Chinese (Simplified)": "裸体 (luǒtǐ)"
    },
    "business": {
        "Hindi": "व्यवसाय (vyavasāy)",
        "Chinese (Simplified)": "生意 (shēngyì)"
    },
    "hardworking": {
        "Hindi": "मेहनती (mehanatī)",
        "Chinese (Simplified)": "勤奋 (qínfèn)"
    },
    "gone": {
        "Hindi": "चला गया (calā gayā)",
        "Chinese (Simplified)": "走了 (zǒule)"
    },
    "person": {
        "Hindi": "व्यक्ति (vyakti)",
        "Chinese (Simplified)": "人 (rén)"
    },
    "people": {
        "Hindi": "लोग (log)",
        "Chinese (Simplified)": "人们 (rénmen)"
    },
    "transgender": {
        "Hindi": "ट्रांसजेंडर (ṭrānsjeṇḍar)",
        "Chinese (Simplified)": "变性人 (biànxìng rén)"
    },
    "lose": {
        "Hindi": "खोना (khonā)",
        "Chinese (Simplified)": "失去 (shīqù)"
    },
    "news": {
        "Hindi": "समाचार (samācār)",
        "Chinese (Simplified)": "新闻 (xīnwén)"
    },
    "mini": {
        "Hindi": "छोटा (choṭā)",
        "Chinese (Simplified)": "迷你 (mínǐ)"
    },
    "hour": {
        "Hindi": "घंटा (ghaṇṭā)",
        "Chinese (Simplified)": "小时 (xiǎoshí)"
    },
    "seconds": {
        "Hindi": "सेकंड (sekaṇḍ)",
        "Chinese (Simplified)": "秒 (miǎo)"
    },
    "days": {
        "Hindi": "दिन (din)",
        "Chinese (Simplified)": "天 (tiān)"
    },
    "mock": {
        "Hindi": "मज़ाक उड़ाना (mazāk uḍānā)",
        "Chinese (Simplified)": "嘲笑 (cháoxiào)"
    },
    "pleasure": {
        "Hindi": "सुख (sukh)",
        "Chinese (Simplified)": "快乐 (kuàilè)"
    },
    "pain": {
        "Hindi": "दर्द (dard)",
        "Chinese (Simplified)": "痛苦 (tòngkǔ)"
    },
    "tiredness": {
        "Hindi": "थकावट (thakāvaṭ)",
        "Chinese (Simplified)": "疲劳 (píláo)"
    },
    "tired": {
        "Hindi": "थका हुआ (thakā huā)",
        "Chinese (Simplified)": "累 (lèi)"
    },
    "depressed": {
        "Hindi": "उदास (udās)",
        "Chinese (Simplified)": "沮丧 (jǔsàng)"
    },
    "fun": {
        "Hindi": "मज़ा (mazā)",
        "Chinese (Simplified)": "乐趣 (lèqù)"
    },
    "just": {
        "Hindi": "बस (bas)",
        "Chinese (Simplified)": "刚刚 (gānggāng)"
    },
    "who": {
        "Hindi": "कौन (kaun)",
        "Chinese (Simplified)": "谁 (shéi)"
    },
    "here": {
        "Hindi": "यहाँ (yahān)",
        "Chinese (Simplified)": "这里 (zhèlǐ)"
    },
    "curse": {
        "Hindi": "शाप (śāp)",
        "Chinese (Simplified)": "诅咒 (zǔzhòu)"
    },
    "add": {
        "Hindi": "जोड़ना (joṛnā)",
        "Chinese (Simplified)": "添加 (tiānjiā)"
    },
    "divide": {
        "Hindi": "विभाजित करना (vibhājit karnā)",
        "Chinese (Simplified)": "划分 (huàfēn)"
    },
    "multiply": {
        "Hindi": "गुणा करना (guṇā karnā)",
        "Chinese (Simplified)": "乘以 (chéngyǐ)"
    },
    "minus": {
        "Hindi": "घटाना (ghaṭānā)",
        "Chinese (Simplified)": "减 (jiǎn)"
    },
    "loop": {
        "Hindi": "घेरा (gherā)",
        "Chinese (Simplified)": "循环 (xúnhuán)"
    },
    "great": {
        "Hindi": "महान (mahān)",
        "Chinese (Simplified)": "伟大 (wěidà)"
    },
    "history": {
        "Hindi": "इतिहास (itihās)",
        "Chinese (Simplified)": "历史 (lìshǐ)"
    },
    "popular": {
        "Hindi": "लोकप्रिय (lokpriya)",
        "Chinese (Simplified)": "受欢迎 (shòu huānyíng)"
    },
    "stick": {
        "Hindi": "छड़ी (chaṛī)",
        "Chinese (Simplified)": "棍 (gùn)"
    },
    "spot": {
        "Hindi": "स्थान (sthān)",
        "Chinese (Simplified)": "地点 (dìdiǎn)"
    },
    "enter": {
        "Hindi": "प्रवेश करना (praveś karnā)",
        "Chinese (Simplified)": "进入 (jìnrù)"
    },
    "service": {
        "Hindi": "सेवा (sevā)",
        "Chinese (Simplified)": "服务 (fúwù)"
    },
    "if": {
        "Hindi": "यदि (yadi)",
        "Chinese (Simplified)": "如果 (rúguǒ)"
    },
    "top": {
        "Hindi": "शीर्ष (śīrṣ)",
        "Chinese (Simplified)": "顶部 (dǐngbù)"
    },
    "clear": {
        "Hindi": "साफ़ (sāf)",
        "Chinese (Simplified)": "清楚 (qīngchǔ)"
    },
    "have": {
        "Hindi": "है (hai)",
        "Chinese (Simplified)": "有 (yǒu)"
    },
    "word": {
        "Hindi": "शब्द (śabd)",
        "Chinese (Simplified)": "单词 (dāncí)"
    },
    "request": {
        "Hindi": "अनुरोध (anurodh)",
        "Chinese (Simplified)": "请求 (qǐngqiú)"
    },
    "need": {
        "Hindi": "आवश्यकता (āvaśyaktā)",
        "Chinese (Simplified)": "需要 (xūyào)"
    },
    "want": {
        "Hindi": "चाहना (cāhnā)",
        "Chinese (Simplified)": "想要 (xiǎngyào)"
    },
    "recent": {
        "Hindi": "हाल का (hāl kā)",
        "Chinese (Simplified)": "最近 (zuìjìn)"
    },
    "difference": {
        "Hindi": "अंतर (antar)",
        "Chinese (Simplified)": "差异 (chāyì)"
    },
    "different": {
        "Hindi": "भिन्न (bhinn)",
        "Chinese (Simplified)": "不同 (bùtóng)"
    },
    "why": {
        "Hindi": "क्यों (kyon)",
        "Chinese (Simplified)": "为什么 (wèishéme)"
    },
    "what": {
        "Hindi": "क्या (kyā)",
        "Chinese (Simplified)": "什么 (shénme)"
    },
    "learn": {
        "Hindi": "सीखना (sīkhnā)",
        "Chinese (Simplified)": "学习 (xuéxí)"
    },
    "learning": {
        "Hindi": "सीखने (sīkhnē)",
        "Chinese (Simplified)": "学习中 (xuéxí zhōng)"
    },
    "sick": {
        "Hindi": "बीमार (bīmār)",
        "Chinese (Simplified)": "生病 (shēngbìng)"
    },
    "oil": {
        "Hindi": "तेल (tel)",
        "Chinese (Simplified)": "油 (yóu)"
    },
    "gas": {
        "Hindi": "गैस (gais)",
        "Chinese (Simplified)": "气体 (qìtǐ)"
    },
    "evolution": {
        "Hindi": "विकास (vikās)",
        "Chinese (Simplified)": "进化 (jìnhuà)"
    },
    "revolution": {
        "Hindi": "क्रांति (krānti)",
        "Chinese (Simplified)": "革命 (gémìng)"
    },
    "mathematics": {
        "Hindi": "गणित (Gaṇit)",
        "Chinese (Simplified)": "数学 (shùxué)"
    },
    "science": {
        "Hindi": "विज्ञान (Vijñān)",
        "Chinese (Simplified)": "科学 (kēxué)"
    },
    "physics": {
        "Hindi": "भौतिकी (Bhautikī)",
        "Chinese (Simplified)": "物理 (wùlǐ)"
    },
    "chemistry": {
        "Hindi": "रसायन विज्ञान (Rasāyan Vijñān)",
        "Chinese (Simplified)": "化学 (huàxué)"
    },
    "biology": {
        "Hindi": "जीवविज्ञान (Jīvavijñān)",
        "Chinese (Simplified)": "生物学 (shēngwùxué)"
    },
    "frequency": {
        "Hindi": "आवृत्ति (āvr̥tti)",
        "Chinese (Simplified)": "频率 (pínlǜ)"
    },
    "context": {
        "Hindi": "संदर्भ (sandarbh)",
        "Chinese (Simplified)": "上下文 (shàngxiàwén)"
    },
    "example": {
        "Hindi": "उदाहरण (udāharan)",
        "Chinese (Simplified)": "例子 (lìzi)"
    },
    "provide": {
        "Hindi": "प्रदान करना (pradān karnā)",
        "Chinese (Simplified)": "提供 (tígōng)"
    },
    "translate": {
        "Hindi": "अनुवाद करना (anuvād karnā)",
        "Chinese (Simplified)": "翻译 (fānyì)"
    },
    "account": {
        "Hindi": "खाता (khātā)",
        "Chinese (Simplified)": "账户 (zhànghù)"
    },
    "device": {
        "Hindi": "उपकरण (upakarṇa)",
        "Chinese (Simplified)": "设备 (shèbèi)"
    },
    "machine": {
        "Hindi": "यंत्र (yantr)",
        "Chinese (Simplified)": "机器 (jīqì)"
    },
    "single": {
        "Hindi": "अकेला (akelā)",
        "Chinese (Simplified)": "单一的 (dānyī de)"
    },
    "double": {
        "Hindi": "दोगुना (dogunā)",
        "Chinese (Simplified)": "双重的 (shuāngchóng de)"
    },
    "triple": {
        "Hindi": "तिगुना (tigunā)",
        "Chinese (Simplified)": "三重的 (sānchóng de)"
    },
    "manager": {
        "Hindi": "प्रबंधक (prabhandhak)",
        "Chinese (Simplified)": "经理 (jīnglǐ)"
    },
    "partner": {
        "Hindi": "साझेदार (sāhejēdār)",
        "Chinese (Simplified)": "伙伴 (huǒbàn)"
    },
    "couple": {
        "Hindi": "युगल (yugal)",
        "Chinese (Simplified)": "夫妇 (fūfù)"
    },
    "activity": {
        "Hindi": "गतिविधि (gatividhi)",
        "Chinese (Simplified)": "活动 (huó dòng)"
    },
    "kill": {
        "Hindi": "मारना (mārnā)",
        "Chinese (Simplified)": "杀死 (shā sǐ)"
    },
    "burn": {
        "Hindi": "जलाना (jalānā)",
        "Chinese (Simplified)": "燃烧 (ránshāo)"
    },
    "born": {
        "Hindi": "जन्म लेना (janm lena)",
        "Chinese (Simplified)": "出生 (chūshēng)"
    },
    "citizen": {
        "Hindi": "नागरिक (nāgarik)",
        "Chinese (Simplified)": "公民 (gōngmín)"
    },
    "voice": {
        "Hindi": "आवाज़ (āvāz)",
        "Chinese (Simplified)": "声音 (shēngyīn)"
    },
    "plane": {
        "Hindi": "विमान (vimān)",
        "Chinese (Simplified)": "飞机 (fēijī)"
    },
    "basic": {
        "Hindi": "मूलभूत (mūlabhūt)",
        "Chinese (Simplified)": "基本的 (jīběn de)"
    },
    "advanced": {
        "Hindi": "उन्नत (unnata)",
        "Chinese (Simplified)": "高级的 (gāojí de)"
    },
    "base": {
        "Hindi": "आधार (ādhār)",
        "Chinese (Simplified)": "基础 (jīchǔ)"
    },
    "location": {
        "Hindi": "स्थान (sthān)",
        "Chinese (Simplified)": "位置 (wèizhì)"
    },
    "giant": {
        "Hindi": "विशालकाय (viśālkāya)",
        "Chinese (Simplified)": "巨大的 (jùdà de)"
    },
    "send": {
        "Hindi": "भेजना (bhejnā)",
        "Chinese (Simplified)": "发送 (fāsòng)"
    },
    "letter": {
        "Hindi": "पत्र (patra)",
        "Chinese (Simplified)": "信 (xìn)"
    },
    "grill": {
        "Hindi": "ग्रिल (gril)",
        "Chinese (Simplified)": "烤架 (kǎojià)"
    },
    "balcony": {
        "Hindi": "बालकनी (bālknī)",
        "Chinese (Simplified)": "阳台 (yángtái)"
    },
    "toilet": {
        "Hindi": "शौचालय (śaucalaya)",
        "Chinese (Simplified)": "厕所 (cèsuǒ)"
    },
    "stairs": {
        "Hindi": "सीढ़ियाँ (sīṛhiyāṅ)",
        "Chinese (Simplified)": "楼梯 (lóutī)"
    },
    "protein": {
        "Hindi": "प्रोटीन (protīn)",
        "Chinese (Simplified)": "蛋白质 (dànbái zhì)"
    },
    "nutrients": {
        "Hindi": "पोषक तत्व (poṣak tatva)",
        "Chinese (Simplified)": "营养素 (yíngyǎng sù)"
    },
    "fat": {
        "Hindi": "वसा (vasā)",
        "Chinese (Simplified)": "脂肪 (zhīfáng)"
    },
    "skinny": {
        "Hindi": "दुबला-पतला (dublā-patlā)",
        "Chinese (Simplified)": "瘦的 (shòu de)"
    },
    "skin": {
        "Hindi": "त्वचा (tvacā)",
        "Chinese (Simplified)": "皮肤 (pífū)"
    },
    "cut": {
        "Hindi": "काटना (kātnā)",
        "Chinese (Simplified)": "切 (qiē)"
    },
    "nails": {
        "Hindi": "नाखून (nākhūn)",
        "Chinese (Simplified)": "指甲 (zhǐjiǎ)"
    },
    "switch": {
        "Hindi": "स्विच (svic)",
        "Chinese (Simplified)": "开关 (kāiguān)"
    },
    "trust": {
        "Hindi": "विश्वास (viśvās)",
        "Chinese (Simplified)": "信任 (xìnrèn)"
    },
    "doubt": {
        "Hindi": "संदेह (sandeha)",
        "Chinese (Simplified)": "怀疑 (huáiyí)"
    },
    "distrust": {
        "Hindi": "अविश्वास (aviśvās)",
        "Chinese (Simplified)": "不信任 (bù xìnrèn)"
    },
    "quit": {
        "Hindi": "छोड़ना (chhoṛnā)",
        "Chinese (Simplified)": "退出 (tuìchū)"
    },
    "next": {
        "Hindi": "अगला (aglā)",
        "Chinese (Simplified)": "下一个 (xiàyīgè)"
    },
    "summarize": {
        "Hindi": "सारांशित करना (sārāṃśit karnā)",
        "Chinese (Simplified)": "总结 (zǒngjié)"
    },
    "sweat": {
        "Hindi": "पसीना (pasīnā)",
        "Chinese (Simplified)": "汗水 (hànshuǐ)"
    },
    "tears": {
        "Hindi": "आँसू (āṅsū)",
        "Chinese (Simplified)": "眼泪 (yǎnlèi)"
    },
    "urine": {
        "Hindi": "मूत्र (mūtra)",
        "Chinese (Simplified)": "尿液 (niàoyè)"
    },
    "pee": {
        "Hindi": "पेशाब करना (peśāb karnā)",
        "Chinese (Simplified)": "小便 (xiǎobiàn)"
    },
    "grid": {
        "Hindi": "ग्रिड (grid)",
        "Chinese (Simplified)": "网格 (wǎnggé)"
    },
    "finish": {
        "Hindi": "समाप्त करना (samāpt karnā)",
        "Chinese (Simplified)": "完成 (wánchéng)"
    },
    "beard": {
        "Hindi": "दाढ़ी (dāṛhī)",
        "Chinese (Simplified)": "胡须 (húxū)"
    },
    "mustache": {
        "Hindi": "मूंछ (mūñch)",
        "Chinese (Simplified)": "胡子 (húzi)"
    },
    "current": {
        "Hindi": "वर्तमान (vartman)",
        "Chinese (Simplified)": "当前 (dāngqián)"
    },
    "trend": {
        "Hindi": "रुझान (rujhan)",
        "Chinese (Simplified)": "趋势 (qūshì)"
    },
    "social": {
        "Hindi": "सामाजिक (sāmājik)",
        "Chinese (Simplified)": "社会的 (shèhuì de)"
    },
    "pants": {
        "Hindi": "पैंट (paint)",
        "Chinese (Simplified)": "裤子 (kùzi)"
    },
    "pant": {
        "Hindi": "सांस लेना (sāṃs lena)",
        "Chinese (Simplified)": "喘气 (chuǎnqì)"
    },
    "shirt": {
        "Hindi": "कमीज़ (kamīz)",
        "Chinese (Simplified)": "衬衫 (chènshān)"
    },
    "platform": {
        "Hindi": "मंच (manc)",
        "Chinese (Simplified)": "平台 (píngtái)"
    },
    "geography": {
        "Hindi": "भूगोल (Bhūgol)",
        "Chinese (Simplified)": "地理 (dìlǐ)"
    },
    "english": {
        "Hindi": "अंग्रेज़ी (Aṅgrēzī)",
        "Chinese (Simplified)": "英语 (yīngyǔ)"
    },
    "hindi": {
        "Hindi": "हिंदी (Hindī)",
        "Chinese (Simplified)": "印地语 (yìndìyǔ)"
    },
    "chinese": {
        "Hindi": "चीनी (Chīnī)",
        "Chinese (Simplified)": "中文 (zhōngwén)"
    },
    "economics": {
        "Hindi": "अर्थशास्त्र (Arthaśāstra)",
        "Chinese (Simplified)": "经济学 (jīngjìxué)"
    },
    "political Science": {
        "Hindi": "राजनीति विज्ञान (Rājnīti Vijñān)",
        "Chinese (Simplified)": "政治学 (zhèngzhìxué)"
    },
    "grip": {
        "Hindi": "पकड़ (pakad)",
        "Chinese (Simplified)": "抓握 (zhuāwò)"
    },
    "bridge": {
        "Hindi": "पुल (pul)",
        "Chinese (Simplified)": "桥 (qiáo)"
    },
    "villager": {
        "Hindi": "ग्रामीण (grāmīṇ)",
        "Chinese (Simplified)": "村民 (cūnmín)"
    },
    "worker": {
        "Hindi": "कार्यकर्ता (kāryakartā)",
        "Chinese (Simplified)": "工人 (gōngrén)"
    },
    "back": {
        "Hindi": "पीठ (pīṭh)",
        "Chinese (Simplified)": "背后 (bèihòu)"
    },
    "front": {
        "Hindi": "सामने (sāmnē)",
        "Chinese (Simplified)": "前面 (qiánmiàn)"
    },
    "hospital": {
        "Hindi": "अस्पताल (aspatāl)",
        "Chinese (Simplified)": "医院 (yīyuàn)"
    },
    "sociology": {
        "Hindi": "समाजशास्त्र (Samājśāstra)",
        "Chinese (Simplified)": "社会学 (shèhuìxué)"
    },
    "psychology": {
        "Hindi": "मनोविज्ञान (Manovijñān)",
        "Chinese (Simplified)": "心理学 (xīnlǐxué)"
    },
    "philosophy": {
        "Hindi": "दर्शनशास्त्र (Darśanśāstra)",
        "Chinese (Simplified)": "哲学 (zhéxué)"
    },
    "computer Science": {
        "Hindi": "कंप्यूटर विज्ञान (Kaṃpyūṭar Vijñān)",
        "Chinese (Simplified)": "计算机科学 (jìsuànjī kēxué)"
    },
    "art": {
        "Hindi": "कला (Kalā)",
        "Chinese (Simplified)": "艺术 (yìshù)"
    },
    "music": {
        "Hindi": "संगीत (Saṅgīt)",
        "Chinese (Simplified)": "音乐 (yīnyuè)"
    },
    "physical Education": {
        "Hindi": "शारीरिक शिक्षा (Śārīrik Śikṣā)",
        "Chinese (Simplified)": "体育 (tǐyù)"
    },
    "law": {
        "Hindi": "कानून (Kānūn)",
        "Chinese (Simplified)": "法律 (fǎlǜ)"
    },
    "medicine": {
        "Hindi": "चिकित्सा (Cikitsā)",
        "Chinese (Simplified)": "医学 (yīxué)"
    },
    "astronomy": {
        "Hindi": "खगोलशास्त्र (Khagolśāstra)",
        "Chinese (Simplified)": "天文学 (tiānwénxué)"
    },
    "environmental Science": {
        "Hindi": "पर्यावरण विज्ञान (Paryāvaraṇ Vijñān)",
        "Chinese (Simplified)": "环境科学 (huánjìng kēxué)"
    },
    "engineering": {
        "Hindi": "अभियंत्रिकी (Abhiyantrikī)",
        "Chinese (Simplified)": "工程学 (gōngchéngxué)"
    },
    "study": {
        "Hindi": "अध्ययन (adhyayan)",
        "Chinese (Simplified)": "学习 (xuéxí)"
    },
    "interest": {
        "Hindi": "रुचि (ruci)",
        "Chinese (Simplified)": "兴趣 (xìngqù)"
    },
    "discrimination": {
        "Hindi": "भेदभाव (bhedbhāv)",
        "Chinese (Simplified)": "歧视 (qíshì)"
    },
    "inequality": {
        "Hindi": "असमानता (asamānatā)",
        "Chinese (Simplified)": "不平等 (bù píngděng)"
    },
    "delay": {
        "Hindi": "देर (der)",
        "Chinese (Simplified)": "延迟 (yánchí)"
    },
    "late": {
        "Hindi": "देर से (der se)",
        "Chinese (Simplified)": "迟到 (chídào)"
    },
    "kudos": {
        "Hindi": "सराहना (sarāhanā)",
        "Chinese (Simplified)": "赞扬 (zànyáng)"
    },
    "area": {
        "Hindi": "क्षेत्र (kṣetra)",
        "Chinese (Simplified)": "区域 (qūyù)"
    },
    "verify": {
        "Hindi": "सत्यापित करना (satyāpit karnā)",
        "Chinese (Simplified)": "验证 (yànzhèng)"
    },
    "blink": {
        "Hindi": "पलक झपकना (palak jhapaknā)",
        "Chinese (Simplified)": "眨眼 (zhǎyǎn)"
    },
    "option": {
        "Hindi": "विकल्प (vikalp)",
        "Chinese (Simplified)": "选项 (xuǎnxíàng)"
    },
    "i love you": {
        "Hindi": "मैं तुमसे प्यार करता हूँ (ma͠ĩ tumse pyār kartā hū̃)",
        "Chinese (Simplified)": "我爱你 (wǒ ài nǐ)"
    },
    "hate": {
        "Hindi": "नफरत करना (nafarat karnā)",
        "Chinese (Simplified)": "恨 (hèn)"
    },
    "i hate you": {
        "Hindi": "मुझे तुमसे नफरत है (mujhe tumse nafarat hai)",
        "Chinese (Simplified)": "我恨你 (wǒ hèn nǐ)"
    },
    "insect": {
        "Hindi": "कीड़ा (kīda)",
        "Chinese (Simplified)": "昆虫 (kūnchóng)"
    },
    "mammals": {
        "Hindi": "स्तनधारी (stnandhārī)",
        "Chinese (Simplified)": "哺乳动物 (pǔrǔ dòngwù)"
    },
    "reptiles": {
        "Hindi": "सरीसृप (sarīsr̥p)",
        "Chinese (Simplified)": "爬行动物 (pá xíng dòngwù)"
    },
    "humans": {
        "Hindi": "मनुष्य/इंसान (manuşya/insaan)",
        "Chinese (Simplified)": "人类 (rénlèi)"
    },
    "rubber": {
        "Hindi": "रबर (rabar)",
        "Chinese (Simplified)": "橡胶 (xiàngpiào)"
    },
    "erase": {
        "Hindi": "मिटाना (mitānā)",
        "Chinese (Simplified)": "擦除 (cāchú)"
    },
    "pervert": {
        "Hindi": "विकृत व्यक्ति (vikṛt vyakti)",
        "Chinese (Simplified)": "变态 (biàntài)"
    },
    "undo": {
        "Hindi": "पूर्ववत करना (pūrvavt karnā)",
        "Chinese (Simplified)": "撤销 (chèxiāo)"
    },
    "give": {
        "Hindi": "देना (denā)",
        "Chinese (Simplified)": "给 (gěi)"
    },
    "sacrifice": {
        "Hindi": "बलिदान (balidān)",
        "Chinese (Simplified)": "牺牲 (xīshēng)"
    },
    "health": {
        "Hindi": "स्वास्थ्य (svāsthya)",
        "Chinese (Simplified)": "健康 (jiànkāng)"
    },
    "pregnant": {
        "Hindi": "गर्भवती (garbhavatī)",
        "Chinese (Simplified)": "怀孕的 (huáiyùn de)"
    },
    "honest": {
        "Hindi": "ईमानदार (īmāndār)",
        "Chinese (Simplified)": "诚实的 (chéngshí de)"
    },
    "addiction": {
        "Hindi": "व्यसन (vyasan)",
        "Chinese (Simplified)": "瘾 (yǐn)"
    },
    "addict": {
        "Hindi": "व्यसनी (vyasnī)",
        "Chinese (Simplified)": "瘾君子 (yǐn jūnzǐ)"
    },
    "child": {
        "Hindi": "बच्चा (bacca)",
        "Chinese (Simplified)": "孩子 (háizi)"
    },
    "caught": {
        "Hindi": "पकड़ा गया (pakṛā gayā)",
        "Chinese (Simplified)": "被抓 (bèi zhuā)"
    },
    "crime": {
        "Hindi": "अपराध (apradh)",
        "Chinese (Simplified)": "犯罪 (fànzuì)"
    },
    "loneliness": {
        "Hindi": "अकेलापन (akelāpan)",
        "Chinese (Simplified)": "孤独 (gūdú)"
    },
    "bind": {
        "Hindi": "बाँधना (bāṅdhna)",
        "Chinese (Simplified)": "捆绑 (kǔnbǎng)"
    },
    "bound": {
        "Hindi": "बँधा हुआ (baṅdhā huā)",
        "Chinese (Simplified)": "绑定的 (bǎndìng de)"
    },
    "pot": {
        "Hindi": "गमला (gamalā)",
        "Chinese (Simplified)": "盆 (pén)"
    },
    "health": {
        "Hindi": "स्वास्थ्य (svāsthya)",
        "Chinese (Simplified)": "健康 (jiànkāng)"
    },
    "pregnant": {
        "Hindi": "गर्भवती (garbhavatī)",
        "Chinese (Simplified)": "怀孕的 (huáiyùn de)"
    },
    "honest": {
        "Hindi": "ईमानदार (īmāndār)",
        "Chinese (Simplified)": "诚实的 (chéngshí de)"
    },
    "addiction": {
        "Hindi": "व्यसन/लत (vyasan/lat)",
        "Chinese (Simplified)": "瘾 (yǐn)"
    },
    "addict": {
        "Hindi": "व्यसनी (vyasnī)",
        "Chinese (Simplified)": "瘾君子 (yǐn jūnzǐ)"
    },
    "child": {
        "Hindi": "बच्चा (bacca)",
        "Chinese (Simplified)": "孩子 (háizi)"
    },
    "caught": {
        "Hindi": "पकड़ा गया (pakṛā gayā)",
        "Chinese (Simplified)": "被抓 (bèi zhuā)"
    },
    "crime": {
        "Hindi": "अपराध (apradh)",
        "Chinese (Simplified)": "犯罪 (fànzuì)"
    },
    "loneliness": {
        "Hindi": "अकेलापन (akelāpan)",
        "Chinese (Simplified)": "孤独 (gūdú)"
    },
    "bind": {
        "Hindi": "बाँधना (bāṅdhna)",
        "Chinese (Simplified)": "捆绑 (kǔnbǎng)"
    },
    "illness": {
        "Hindi": "बीमारी (bīmārī)",
        "Chinese (Simplified)": "疾病 (jíbìng)"
    },
    "glow": {
        "Hindi": "चमक (camak)",
        "Chinese (Simplified)": "发光 (fāguāng)"
    },
    "pride": {
        "Hindi": "गर्व (garv)",
        "Chinese (Simplified)": "骄傲 (jiāo'ào)"
    },
    "proud": {
        "Hindi": "गर्वित (garvit)",
        "Chinese (Simplified)": "骄傲的 (jiāo'ào de)"
    },
    "dust": {
        "Hindi": "धूल (dhūl)",
        "Chinese (Simplified)": "灰尘 (huīchén)"
    },
    "bark": {
        "Hindi": "भौंकना (bhaunknā)",
        "Chinese (Simplified)": "吠叫 (fèijiào)"
    },
    "sand": {
        "Hindi": "रेत (ret)",
        "Chinese (Simplified)": "沙子 (shāzi)"
    },
    "bobble": {
        "Hindi": "डगमगाना (dagmagānā)",
        "Chinese (Simplified)": "晃动 (huàngdòng)"
    },
    "mumble": {
        "Hindi": "गुर्राना (gurrānā)",
        "Chinese (Simplified)": "咕哝 (gū nong)"
    },
    "whistle": {
        "Hindi": "सीटी बजाना (sītī bajānā)",
        "Chinese (Simplified)": "吹口哨 (chuī kǒushào)"
    },
    "clap": {
        "Hindi": "ताली बजाना (tālī bajānā)",
        "Chinese (Simplified)": "鼓掌 (gǔzhǎng)"
    },
    "crowd": {
        "Hindi": "भीड़ (bhīṛ)",
        "Chinese (Simplified)": "人群 (rénqún)"
    },
    "pollution": {
        "Hindi": "प्रदूषण (pradūṣaṇ)",
        "Chinese (Simplified)": "污染 (wūrǎn)"
    },
    "noise": {
        "Hindi": "शोर (śor)",
        "Chinese (Simplified)": "噪音 (zàoyīn)"
    },
    "soil": {
        "Hindi": "मिट्टी (mitṭī)",
        "Chinese (Simplified)": "土壤 (tǔrǎng)"
    },
    "population": {
        "Hindi": "जनसंख्या (jansankhyā)",
        "Chinese (Simplified)": "人口 (rénkǒu)"
    },
    "worry": {
        "Hindi": "चिंता (cintā)",
        "Chinese (Simplified)": "担心 (dānxīn)"
    },
    "worried": {
        "Hindi": "चिंतित (cintīt)",
        "Chinese (Simplified)": "担心的 (dānxīn de)"
    },
    "kind": {
        "Hindi": "दयालु (dayālu)",
        "Chinese (Simplified)": "善良的 (shànliáng de)"
    },
    "forest": {
        "Hindi": "जंगल (jangal)",
        "Chinese (Simplified)": "森林 (sēnlín)"
    },
    "side": {
        "Hindi": "पक्ष (pakṣ)",
        "Chinese (Simplified)": "侧面 (cèmiàn)"
    },
    "important": {
        "Hindi": "महत्वपूर्ण (mahatvapūrṇa)",
        "Chinese (Simplified)": "重要的 (zhòngyào de)"
    },
    "hurry": {
        "Hindi": "जल्दी करना (jaldi karnā)",
        "Chinese (Simplified)": "赶快 (gǎnkuài)"
    },
    "hook": {
        "Hindi": "हुक (huk)",
        "Chinese (Simplified)": "钩子 (gōuzi)"
    },
    "pin": {
        "Hindi": "पिन (pin)",
        "Chinese (Simplified)": "别针 (biēzhēn)"
    },
    "surface": {
        "Hindi": "सतह (satah)",
        "Chinese (Simplified)": "表面 (biǎomiàn)"
    },
    "ink": {
        "Hindi": "स्याही (syāhi)",
        "Chinese (Simplified)": "墨水 (mòshuǐ)"
    },
    "grow": {
        "Hindi": "बढ़ना (baṛhnā)",
        "Chinese (Simplified)": "成长 (chéngzhǎng)"
    },
    "age": {
        "Hindi": "उम्र (umr)",
        "Chinese (Simplified)": "年龄 (niánlíng)"
    },
    "brick": {
        "Hindi": "ईंट (īṇṭ)",
        "Chinese (Simplified)": "砖 (zhuān)"
    },
    "category": {
        "Hindi": "श्रेणी (śreṇī)",
        "Chinese (Simplified)": "类别 (lèibìe)"
    },
    "type": {
        "Hindi": "प्रकार (prakār)",
        "Chinese (Simplified)": "类型 (lèixíng)"
    },
    "champion": {
        "Hindi": "चैंपियन (caimpiyan)",
        "Chinese (Simplified)": "冠军 (guànjūn)"
    },
    "winner": {
        "Hindi": "विजेता (vijeta)",
        "Chinese (Simplified)": "胜利者 (shènglì zhě)"
    },
    "bench": {
        "Hindi": "बेंच (beñc)",
        "Chinese (Simplified)": "长凳 (chángdèng)"
    },
    "first": {
        "Hindi": "पहला (pahlā)",
        "Chinese (Simplified)": "第一 (dìyī)"
    },
    "second": {
        "Hindi": "दूसरा (dūsrā)",
        "Chinese (Simplified)": "第二 (dì'èr)"
    },
    "third": {
        "Hindi": "तीसरा (tīsra)",
        "Chinese (Simplified)": "第三 (dìsān)"
    },
    "fourth": {
        "Hindi": "चौथा (cauthā)",
        "Chinese (Simplified)": "第四 (dìsì)"
    },
    "fifth": {
        "Hindi": "पाँचवाँ (pāñcavā̃)",
        "Chinese (Simplified)": "第五 (dìwǔ)"
    },
    "sixth": {
        "Hindi": "छठा (chhaṭhā)",
        "Chinese (Simplified)": "第六 (dìliù)"
    },
    "seventh": {
        "Hindi": "सातवाँ (sātavā̃)",
        "Chinese (Simplified)": "第七 (dìqī)"
    },
    "eighth": {
        "Hindi": "आठवाँ (āṭhvā̃)",
        "Chinese (Simplified)": "第八 (dìbā)"
    },
    "ninth": {
        "Hindi": "नौवाँ (nauvā̃)",
        "Chinese (Simplified)": "第九 (dìjiǔ)"
    },
    "tenth": {
        "Hindi": "दसवाँ (dasvā̃)",
        "Chinese (Simplified)": "第十 (díshi)"
    },
    "glasses": {
        "Hindi": "चश्मा (caśmā)",
        "Chinese (Simplified)": "眼镜 (yǎnjìng)"
    },
    "redo": {
        "Hindi": "दुबारा करना (dubārā karnā)",
        "Chinese (Simplified)": "重做 (chóngzuò)"
    },
    "virus": {
        "Hindi": "वायरस (vāyaras)",
        "Chinese (Simplified)": "病毒 (bìngdú)"
    },
    "pandemic": {
        "Hindi": "महामारी (mahāmārī)",
        "Chinese (Simplified)": "大流行病 (dàliúxíngbìng)"
    },
    "farming": {
        "Hindi": "कृषि (kṛṣi)",
        "Chinese (Simplified)": "农业 (nóngyè)"
    },
    "alert": {
        "Hindi": "चेतावनी (cetāvanī)",
        "Chinese (Simplified)": "警报 (jǐngbào)"
    },
    "corruption": {
        "Hindi": "भ्रष्टाचार (bhraṣṭācār)",
        "Chinese (Simplified)": "腐败 (fǔbài)"
    },
    "warning": {
        "Hindi": "चेतावनी (cetāvanī)",
        "Chinese (Simplified)": "警告 (jǐnggào)"
    },
    "blackmail": {
        "Hindi": "ब्लैकमेल (blakmel)",
        "Chinese (Simplified)": "勒索 (lēsuǒ)"
    },
    "train station": {
        "Hindi": "रेलवे स्टेशन (relve stēśan)",
        "Chinese (Simplified)": "火车站 (huǒchē zhàn)"
    },
    "police station": {
        "Hindi": "पुलिस स्टेशन (pulis stēśan)",
        "Chinese (Simplified)": "警察局 (jǐngchá jú)"
    },
    "confidence": {
        "Hindi": "आत्मविश्वास (ātmaviśvās)",
        "Chinese (Simplified)": "自信 (zìxìn)"
    },
    "confident": {
        "Hindi": "आत्मविश्वासी (ātmaviśvāsī)",
        "Chinese (Simplified)": "自信的 (zìxìn de)"
    },
    "scare": {
        "Hindi": "डराना (ḍarānā)",
        "Chinese (Simplified)": "吓唬 (xiàhǔ)"
    },
    "scary": {
        "Hindi": "डरावना (ḍarāvnā)",
        "Chinese (Simplified)": "吓人的 (xiàrén de)"
    },
    "oh no": {
        "Hindi": "अरे नहीं (are nahī̃)",
        "Chinese (Simplified)": "哦，不 (ó, bù)"
    },
    "return": {
        "Hindi": "वापस आना (vāpas ā nā)",
        "Chinese (Simplified)": "返回 (fǎnhuí)"
    },
    "from": {
        "Hindi": "से (se)",
        "Chinese (Simplified)": "从 (cóng)"
    },
    "complete": {
        "Hindi": "पूर्ण (pūrṇa)",
        "Chinese (Simplified)": "完整的 (wánzhěng de)"
    },
    "guide": {
        "Hindi": "मार्गदर्शक (margdarshak)",
        "Chinese (Simplified)": "指南 (zhǐnán)"
    },
    "wait": {
        "Hindi": "इंतजार करना (intzar karnā)",
        "Chinese (Simplified)": "等待 (dǎidài)"
    },
    "after": {
        "Hindi": "के बाद (ke bād)",
        "Chinese (Simplified)": "之后 (zhīhòu)"
    },
    "before": {
        "Hindi": "के पहले (ke pahle)",
        "Chinese (Simplified)": "之前 (zhīqián)"
    },
    "get": {
        "Hindi": "पाना (pānā)",
        "Chinese (Simplified)": "得到 (dédào)"
    },
    "got": {
        "Hindi": "मिला (milā)",
        "Chinese (Simplified)": "得到 (dédào)"
    },
    "fold": {
        "Hindi": "मोड़ना (moṛnā)",
        "Chinese (Simplified)": "折叠 (zhédié)"
    },
    "bend": {
        "Hindi": "झुकना (jhuknā)",
        "Chinese (Simplified)": "弯曲 (wānqū)"
    },
    "save": {
        "Hindi": "बचाना (bacānā)",
        "Chinese (Simplified)": "拯救 (zhěngjiù)"
    },
    "safe": {
        "Hindi": "सुरक्षित (surakshit)",
        "Chinese (Simplified)": "安全的 (ānquán de)"
    },
    "scam": {
        "Hindi": "धोखाधड़ी (dhokādhaṛī)",
        "Chinese (Simplified)": "诈骗 (zhàpiàn)"
    },
    "fame": {
        "Hindi": "प्रसिद्धि (prasiddhi)",
        "Chinese (Simplified)": "名声 (míngsheng)"
    },
    "patriotism": {
        "Hindi": "देशभक्ति (deśbhaktī)",
        "Chinese (Simplified)": "爱国主义 (àiguó zhǔyì)"
    },
    "patriarchy": {
        "Hindi": "पितृसत्ता (pitṛsattā)",
        "Chinese (Simplified)": "父权制 (fùquánzhì)"
    },
    "feminist": {
        "Hindi": "नारीवादी (nārīvādī)",
        "Chinese (Simplified)": "女权主义者 (nǚquán zhǔyì zhě)"
    },
    "feminism": {
        "Hindi": "नारीवाद (nārīvād)",
        "Chinese (Simplified)": "女权主义 (nǚquán zhǔyì)"
    },
    "ethical": {
        "Hindi": "नैतिक (naitik)",
        "Chinese (Simplified)": "道德的 (dàodé de)"
    },
    "should": {
        "Hindi": "चाहिए (cāhiye)",
        "Chinese (Simplified)": "应该 (yīnggāi)"
    },
    "would": {
        "Hindi": "करता (kartā)",
        "Chinese (Simplified)": "会 (huì)"
    },
    "cult": {
        "Hindi": "सांप्रदायिक समूह (sāmpradāyik samūh)",
        "Chinese (Simplified)": "邪教 (xiéjiào)"
    },
    "culprit": {
        "Hindi": "अपराधी (apradhī)",
        "Chinese (Simplified)": "罪犯 (zuìfàn)"
    },
    "exposed": {
        "Hindi": "बेनकाब (benkāb)",
        "Chinese (Simplified)": "曝光 (pòguāng)"
    },
    "song": {
        "Hindi": "गीत (gīt)",
        "Chinese (Simplified)": "歌曲 (gēqǔ)"
    },
    "modern": {
        "Hindi": "आधुनिक (ādhunik)",
        "Chinese (Simplified)": "现代的 (xiàndài de)"
    },
    "ancient": {
        "Hindi": "प्राचीन (prācīn)",
        "Chinese (Simplified)": "古代的 (gǔdài de)"
    },
    "information": {
        "Hindi": "सूचना (sūcanā)",
        "Chinese (Simplified)": "信息 (xìnxī)"
    },
    "trolling": {
        "Hindi": "मज़ाक में परेशान करना (mazak mein pareshan karna)",
        "Chinese (Simplified)": "网络喷子 (wǎngluò pēnzǐ)"
    },
    "justice": {
        "Hindi": "न्याय (nyāya)",
        "Chinese (Simplified)": "正义 (zhèngyì)"
    },
    "justify": {
        "Hindi": "उचित ठहराना (ucit ṭhahrānā)",
        "Chinese (Simplified)": "证明 (zhèngmíng)"
    },
    "religious": {
        "Hindi": "धार्मिक (dhārmik)",
        "Chinese (Simplified)": "宗教的 (zōngjiào de)"
    },
    "atheist": {
        "Hindi": "नास्तिक (nāstik)",
        "Chinese (Simplified)": "无神论者 (wúshenlùn zhě)"
    },
    "government": {
        "Hindi": "सरकार (sarkār)",
        "Chinese (Simplified)": "政府 (zhèngfǔ)"
    },
    "reveal": {
        "Hindi": "प्रकट करना (prakat karnā)",
        "Chinese (Simplified)": "揭示 (jiēshì)"
    },
    "story": {
        "Hindi": "कहानी (kahānī)",
        "Chinese (Simplified)": "故事 (gùshi)"
    },
    "cause": {
        "Hindi": "कारण (kāraṇ)",
        "Chinese (Simplified)": "原因 (yuányīn)"
    },
    "root": {
        "Hindi": "जड़ (jaṛ)",
        "Chinese (Simplified)": "根 (gēn)"
    },
    "controversy": {
        "Hindi": "विवाद (vivād)",
        "Chinese (Simplified)": "争议 (zhēngyì)"
    },
    "propose": {
        "Hindi": "प्रस्तावित करना (prastavit karnā)",
        "Chinese (Simplified)": "提议 (tíyì)"
    },
    "cute": {
        "Hindi": "प्यारा (pyārā)",
        "Chinese (Simplified)": "可爱的 (kě'ài de)"
    },
    "face": {
        "Hindi": "चेहरा (cehrā)",
        "Chinese (Simplified)": "脸 (liǎn)"
    },
    "permanent": {
        "Hindi": "स्थायी (sthāyī)",
        "Chinese (Simplified)": "永久的 (yǒngjiǔ de)"
    },
    "persistent": {
        "Hindi": "लगातार (lagātār)",
        "Chinese (Simplified)": "持续的 (chíxù de)"
    },
    "hold": {
        "Hindi": "पकड़ना (pakṛnā)",
        "Chinese (Simplified)": "握住 (wòzhù)"
    },
    "judge": {
        "Hindi": "न्यायाधीश (nyāyādhīś)",
        "Chinese (Simplified)": "法官 (fǎguān)"
    },
    "foreigners": {
        "Hindi": "विदेशी (videśī)",
        "Chinese (Simplified)": "外国人 (wàiguórén)"
    },
    "foreign": {
        "Hindi": "विदेशी (videśī)",
        "Chinese (Simplified)": "外国的 (wàiguó de)"
    },
    "act": {
        "Hindi": "अभिनय करना (abhinay karnā)",
        "Chinese (Simplified)": "表演 (biǎoyǎn)"
    },
    "weird": {
        "Hindi": "अजीब (ajīb)",
        "Chinese (Simplified)": "奇怪的 (qíguài de)"
    },
    "shame": {
        "Hindi": "शर्म (śarm)",
        "Chinese (Simplified)": "羞耻 (xiūchǐ)"
    },
    "full": {
        "Hindi": "पूरा (pūrā)",
        "Chinese (Simplified)": "满的 (mǎn de)"
    },
    "mental": {
        "Hindi": "मानसिक (mānasik)",
        "Chinese (Simplified)": "心理的 (xīnlǐ de)"
    },
    "mad": {
        "Hindi": "पागल (pāgal)",
        "Chinese (Simplified)": "疯的 (fēng de)"
    },
    "extra": {
        "Hindi": "अतिरिक्त (atirikt)",
        "Chinese (Simplified)": "额外的 (éiwài de)"
    },
    "ordinary": {
        "Hindi": "साधारण (sādhāraṇ)",
        "Chinese (Simplified)": "普通的 (pǔtōng de)"
    },
    "fresh": {
        "Hindi": "ताजा (tājā)",
        "Chinese (Simplified)": "新鲜的 (xīnxiān de)"
    },
    "push": {
        "Hindi": "धक्का देना (dhakka denā)",
        "Chinese (Simplified)": "推 (tuī)"
    },
    "rush": {
        "Hindi": "जल्दी करना (jaldi karnā)",
        "Chinese (Simplified)": "匆忙 (cōngmáng)"
    },
    "create": {
        "Hindi": "सृजन करना (sr̥jan karnā)",
        "Chinese (Simplified)": "创造 (chuàngzào)"
    },
    "art": {
        "Hindi": "कला (kalā)",
        "Chinese (Simplified)": "艺术 (yìshù)"
    },
    "design": {
        "Hindi": "डिजाइन (dijain)",
        "Chinese (Simplified)": "设计 (shèjì)"
    },
    "better": {
        "Hindi": "बेहतर (behtar)",
        "Chinese (Simplified)": "更好 (gèng hǎo)"
    },
    "than": {
        "Hindi": "से (se)",
        "Chinese (Simplified)": "比 (bǐ)"
    },
    "then": {
        "Hindi": "फिर (phir)",
        "Chinese (Simplified)": "然后 (ránhòu)"
    },
    "rope": {
        "Hindi": "रस्सी (rassī)",
        "Chinese (Simplified)": "绳子 (shéngzi)"
    },
    "happen": {
        "Hindi": "होना (honā)",
        "Chinese (Simplified)": "发生 (fāshēng)"
    },
    "happened": {
        "Hindi": "हुआ (huā)",
        "Chinese (Simplified)": "发生了 (fāshēng le)"
    },
    "strength": {
        "Hindi": "ताकत (tākat)",
        "Chinese (Simplified)": "力量 (lìliàng)"
    },
    "behind": {
        "Hindi": "पीछे (pīche)",
        "Chinese (Simplified)": "后面 (hòumiàn)"
    },
    "infront": {
        "Hindi": "सामने (sāmnē)",
        "Chinese (Simplified)": "前面 (qiánmiàn)"
    },
    "rainfall": {
        "Hindi": "वर्षा (varṣā)",
        "Chinese (Simplified)": "降雨量 (jiàngyǔliàng)"
    },
    "state": {
        "Hindi": "राज्य (rājya)",
        "Chinese (Simplified)": "州 (zhōu)"
    },
    "country": {
        "Hindi": "देश (deś)",
        "Chinese (Simplified)": "国家 (guójiā)"
    },
    "law": {
        "Hindi": "कानून (kānūn)",
        "Chinese (Simplified)": "法律 (fǎlǜ)"
    },
    "rule": {
        "Hindi": "नियम (niyam)",
        "Chinese (Simplified)": "规则 (guīzé)"
    },
    "rules": {
        "Hindi": "नियम (niyam)",
        "Chinese (Simplified)": "规则 (guīzé)"
    },
    "try": {
        "Hindi": "कोशिश करना (kośiš karnā)",
        "Chinese (Simplified)": "尝试 (chángshì)"
    },
    "tried": {
        "Hindi": "कोशिश की (kośiš kī)",
        "Chinese (Simplified)": "尝试了 (chángshì le)"
    },
    "anti": {
        "Hindi": "विरोधी (virōdhī)",
        "Chinese (Simplified)": "反 (fǎn)"
    },
    "superstition": {
        "Hindi": "अंधविश्वास (andhaviśvās)",
        "Chinese (Simplified)": "迷信 (míxìn)"
    },
    "behave": {
        "Hindi": "व्यवहार करना (vyavahār karnā)",
        "Chinese (Simplified)": "表现 (biǎoxiàn)"
    },
    "real": {
        "Hindi": "असली (asalī)",
        "Chinese (Simplified)": "真正的 (zhēnzhèng de)"
    },
    "fake": {
        "Hindi": "नकली (naklī)",
        "Chinese (Simplified)": "假的 (jiǎ de)"
    },
    "accept": {
        "Hindi": "स्वीकार करना (svīkār karnā)",
        "Chinese (Simplified)": "接受 (jiēshòu)"
    },
    "cancel": {
        "Hindi": "रद्द करना (radd karnā)",
        "Chinese (Simplified)": "取消 (qǔxiāo)"
    },
    "inside": {
        "Hindi": "अंदर (andar)",
        "Chinese (Simplified)": "里面 (lǐmiàn)"
    },
    "outside": {
        "Hindi": "बाहर (bāhar)",
        "Chinese (Simplified)": "外面 (wàimiàn)"
    },
    "culture": {
        "Hindi": "संस्कृति (saṃskṛti)",
        "Chinese (Simplified)": "文化 (wénhuà)"
    },
    "tradition": {
        "Hindi": "परंपरा (parampārā)",
        "Chinese (Simplified)": "传统 (chuántǒng)"
    },
    "generation": {
        "Hindi": "पीढ़ी (pīṛhī)",
        "Chinese (Simplified)": "一代 (yīdài)"
    },
    "taboo": {
        "Hindi": "निषिद्ध (niṣiddha)",
        "Chinese (Simplified)": "禁忌 (jìjìn)"
    },
    "again": {
        "Hindi": "फिर (phir)",
        "Chinese (Simplified)": "再次 (zàicì)"
    },
    "against": {
        "Hindi": "के खिलाफ (ke khilaf)",
        "Chinese (Simplified)": "反对 (fǎnduì)"
    },
    "defend": {
        "Hindi": "रक्षा करना (rakṣā karnā)",
        "Chinese (Simplified)": "保护 (bǎohù)"
    },
    "oppose": {
        "Hindi": "विरोध करना (virodh karnā)",
        "Chinese (Simplified)": "反对 (fǎnduì)"
    },
    "criticize": {
        "Hindi": "आलोचना करना (ālocnā karnā)",
        "Chinese (Simplified)": "批评 (pīpíng)"
    },
    "migrate": {
        "Hindi": "प्रवास करना (pravās karnā)",
        "Chinese (Simplified)": "移民 (yímín)"
    },
    "migration": {
        "Hindi": "प्रवास (pravās)",
        "Chinese (Simplified)": "移民 (yímín)"
    },
    "diaspora": {
        "Hindi": "प्रवास (pravās)",
        "Chinese (Simplified)": "侨民 (qiáomín)"
    },
    "bully": {
        "Hindi": "धमकाना (dhamkānā)",
        "Chinese (Simplified)": "欺负 (qīfù)"
    },
    "raid": {
        "Hindi": "छापा मारना (chāpā mārnā)",
        "Chinese (Simplified)": "突袭 (tūxí)"
    },
    "doom": {
        "Hindi": "विनाश (vināś)",
        "Chinese (Simplified)": "厄运 (èyùn)"
    },
    "any": {
        "Hindi": "कोई भी (koī bhī)",
        "Chinese (Simplified)": "任何 (rènhe)"
    },
    "setup": {
        "Hindi": "स्थापना (sthāpanā)",
        "Chinese (Simplified)": "设置 (shèzhì)"
    },
    "tour": {
        "Hindi": "दौरा (daurā)",
        "Chinese (Simplified)": "旅游 (lǚyóu)"
    },
    "shot": {
        "Hindi": "शॉट (śoṭ)",
        "Chinese (Simplified)": "射击 (shèjī)"
    },
    "experience": {
        "Hindi": "अनुभव (anubhav)",
        "Chinese (Simplified)": "经验 (jīngyàn)"
    },
    "map": {
        "Hindi": "नक्शा (nakṣā)",
        "Chinese (Simplified)": "地图 (dìtú)"
    },
    "public": {
        "Hindi": "जनता (janatā)",
        "Chinese (Simplified)": "公共的 (gōnggòng de)"
    },
    "republic": {
        "Hindi": "गणतंत्र (gaṇatantra)",
        "Chinese (Simplified)": "共和国 (gònghéguó)"
    },
    "publish": {
        "Hindi": "प्रकाशित करना (prakāśit karnā)",
        "Chinese (Simplified)": "出版 (chūbǎn)"
    },
    "competition": {
        "Hindi": "प्रतियोगिता (pratiyogitā)",
        "Chinese (Simplified)": "比赛 (bǐsài)"
    },
    "match": {
        "Hindi": "मैच (maic)",
        "Chinese (Simplified)": "比赛 (bǐsài)"
    },
    "bows": {
        "Hindi": "धनुष (dhanuṣ)",
        "Chinese (Simplified)": "弓 (gōng)"
    },
    "bow": {
        "Hindi": "धनुष (dhanuṣ)",
        "Chinese (Simplified)": "弓 (gōng)"
    },
    "arrow": {
        "Hindi": "तीर (tīr)",
        "Chinese (Simplified)": "箭 (jiàn)"
    },
    "arrows": {
        "Hindi": "तीर (tīr)",
        "Chinese (Simplified)": "箭 (jiàn)"
    },
    "chess": {
        "Hindi": "शतरंज (śataranj)",
        "Chinese (Simplified)": "国际象棋 (guójì xiàngqí)"
    },
    "invade": {
        "Hindi": "आक्रमण करना (ākramṇa karnā)",
        "Chinese (Simplified)": "入侵 (rùqīn)"
    },
    "tribe": {
        "Hindi": "जनजाति (janajāti)",
        "Chinese (Simplified)": "部落 (bùluò)"
    },
    "grab": {
        "Hindi": "छीनना (chīnṇā)",
        "Chinese (Simplified)": "抓取 (zhuāqǔ)"
    },
    "master": {
        "Hindi": "उस्ताद (ustād)",
        "Chinese (Simplified)": "大师 (dàshī)"
    },
    "masterpiece": {
        "Hindi": "कृति (kr̥ti)",
        "Chinese (Simplified)": "杰作 (jiézùo)"
    },
    "mixed": {
        "Hindi": "मिश्रित (miśrit)",
        "Chinese (Simplified)": "混合的 (hùnhé de)"
    },
    "mix": {
        "Hindi": "मिलाना (milānā)",
        "Chinese (Simplified)": "混合 (hùnhé)"
    },
    "problem": {
        "Hindi": "समस्या (samasyā)",
        "Chinese (Simplified)": "问题 (wèntí)"
    },
    "material": {
        "Hindi": "सामग्री (sāmagrī)",
        "Chinese (Simplified)": "材料 (cáiliào)"
    },
    "particle": {
        "Hindi": "कण (kaṇa)",
        "Chinese (Simplified)": "粒子 (lìzi)"
    },
    "particles": {
        "Hindi": "कण (kaṇa)",
        "Chinese (Simplified)": "粒子 (lìzi)"
    },
    "rays": {
        "Hindi": "किरणें (kirṇaṃ)",
        "Chinese (Simplified)": "射线 (shèxiàn)"
    },
    "reason": {
        "Hindi": "कारण (kāraṇ)",
        "Chinese (Simplified)": "原因 (yuányīn)"
    },
    "valley": {
        "Hindi": "घाटी (ghāṭī)",
        "Chinese (Simplified)": "山谷 (shāngǔ)"
    },
    "miss": {
        "Hindi": "चूक जाना (cūk jānā)",
        "Chinese (Simplified)": "错过 (cuòguò)"
    },
    "harassment": {
        "Hindi": "उत्पीड़न (utpīḍan)",
        "Chinese (Simplified)": "骚扰 (sāorǎo)"
    },
    "assault": {
        "Hindi": "हमला (hamlā)",
        "Chinese (Simplified)": "袭击 (xíjí)"
    },
    "claim": {
        "Hindi": "दावा (dava)",
        "Chinese (Simplified)": "声称 (shēngchēng)"
    },
    "owner": {
        "Hindi": "मालिक (malik)",
        "Chinese (Simplified)": "所有者 (suǒyǒuzhě)"
    },
    "clown": {
        "Hindi": "जोकर (joker)",
        "Chinese (Simplified)": "小丑 (xiǎochǒu)"
    },
    "clone": {
        "Hindi": "प्रति (prati)",
        "Chinese (Simplified)": "克隆 (kèlóng)"
    },
    "creep": {
        "Hindi": "रेंगना (rengna)",
        "Chinese (Simplified)": "爬行 (páxíng)"
    },
    "batch": {
        "Hindi": "बैच (batch)",
        "Chinese (Simplified)": "批次 (pīcì)"
    },
    "shop": {
        "Hindi": "दुकान (dukan)",
        "Chinese (Simplified)": "商店 (shāngdiàn)"
    },
    "ground": {
        "Hindi": "भूमि (bhumi)",
        "Chinese (Simplified)": "地面 (dìmiàn)"
    },
    "grass": {
        "Hindi": "घास (ghas)",
        "Chinese (Simplified)": "草 (cǎo)"
    },
    "plateau": {
        "Hindi": "पठार (pathar)",
        "Chinese (Simplified)": "高原 (gāoyuán)"
    },
    "plateaus": {
        "Hindi": "पठार (pathar)",
        "Chinese (Simplified)": "高原 (gāoyuán)"
    },
    "grand": {
        "Hindi": "भव्य (bhavya)",
        "Chinese (Simplified)": "宏伟 (hóngwěi)"
    },
    "little": {
        "Hindi": "थोड़ा (thoda)",
        "Chinese (Simplified)": "小 (xiǎo)"
    },
    "lantern": {
        "Hindi": "लालटेन (lalten)",
        "Chinese (Simplified)": "灯笼 (dēnglóng)"
    },
    "hundred": {
        "Hindi": "सौ (sau)",
        "Chinese (Simplified)": "一百 (yībǎi)"
    },
    "hundreds": {
        "Hindi": "सैकड़ों (saikdon)",
        "Chinese (Simplified)": "几百 (jǐbǎi)"
    },
    "thousands": {
        "Hindi": "हजारों (hazaron)",
        "Chinese (Simplified)": "几千 (jǐqiān)"
    },
    "thousand": {
        "Hindi": "हजार (hazar)",
        "Chinese (Simplified)": "一千 (yīqiān)"
    },
    "lakhs": {
        "Hindi": "लाखों (lakhon)",
        "Chinese (Simplified)": "十万 (shíwàn)"
    },
    "lacs": {
        "Hindi": "लाख (lakh)",
        "Chinese (Simplified)": "十万 (shíwàn)"
    },
    "millions": {
        "Hindi": "लाखों (lakhon)",
        "Chinese (Simplified)": "百万 (bǎiwàn)"
    },
    "crore": {
        "Hindi": "करोड़ (karod)",
        "Chinese (Simplified)": "一千万 (yīqiānwàn)"
    },
    "billion": {
        "Hindi": "अरब (arab)",
        "Chinese (Simplified)": "十亿 (shíyì)"
    },
    "billions": {
        "Hindi": "अरबों (arabon)",
        "Chinese (Simplified)": "数十亿 (shùshíyì)"
    },
    "trillion": {
        "Hindi": "खरब (kharab)",
        "Chinese (Simplified)": "万亿 (wànyì)"
    },
    "trillions": {
        "Hindi": "खरबों (kharabon)",
        "Chinese (Simplified)": "数万亿 (shùwànyì)"
    },
    "crunch": {
        "Hindi": "चबाना (chabana)",
        "Chinese (Simplified)": "咬碎 (yǎosuì)"
    },
    "spice": {
        "Hindi": "मसाला (masala)",
        "Chinese (Simplified)": "香料 (xiāngliào)"
    },
    "sugar": {
        "Hindi": "चीनी (chini)",
        "Chinese (Simplified)": "糖 (táng)"
    },
    "salt": {
        "Hindi": "नमक (namak)",
        "Chinese (Simplified)": "盐 (yán)"
    },
    "salty": {
        "Hindi": "नमकीन (namkeen)",
        "Chinese (Simplified)": "咸 (xián)"
    },
    "fault": {
        "Hindi": "गलती (galti)",
        "Chinese (Simplified)": "错误 (cuòwù)"
    },
    "faulty": {
        "Hindi": "खराब (kharab)",
        "Chinese (Simplified)": "有缺陷 (yǒuquēxiàn)"
    },
    "naughty": {
        "Hindi": "शरारती (shararti)",
        "Chinese (Simplified)": "顽皮 (wánpí)"
    },
    "loyal": {
        "Hindi": "वफादार (vafadar)",
        "Chinese (Simplified)": "忠诚 (zhōngchéng)"
    },
    "criminal": {
        "Hindi": "अपराधी (apradhi)",
        "Chinese (Simplified)": "罪犯 (zuìfàn)"
    },
    "modification": {
        "Hindi": "संशोधन (sanshodhan)",
        "Chinese (Simplified)": "修改 (xiūgǎi)"
    },
    "modify": {
        "Hindi": "संशोधित करना (sanshodhit karna)",
        "Chinese (Simplified)": "修改 (xiūgǎi)"
    },
    "few": {
        "Hindi": "कुछ (kuchh)",
        "Chinese (Simplified)": "几个 (jǐgè)"
    },
    "large": {
        "Hindi": "बड़ा (bada)",
        "Chinese (Simplified)": "大 (dà)"
    },
    "many": {
        "Hindi": "बहुत सारे (bahut saare)",
        "Chinese (Simplified)": "许多 (xǔduō)"
    },
    "tell": {
        "Hindi": "बताना (batana)",
        "Chinese (Simplified)": "告诉 (gàosù)"
    },
    "told": {
        "Hindi": "बताया (bataya)",
        "Chinese (Simplified)": "告诉了 (gàosùle)"
    },
    "wow": {
        "Hindi": "वाह (vah)",
        "Chinese (Simplified)": "哇 (wā)"
    },
    "manage": {
        "Hindi": "प्रबंधन करना (prabandhan karna)",
        "Chinese (Simplified)": "管理 (guǎnlǐ)"
    },
    "responsibility": {
        "Hindi": "जिम्मेदारी (zimmedari)",
        "Chinese (Simplified)": "责任 (zérèn)"
    },
    "responsible": {
        "Hindi": "जिम्मेदार (zimmedar)",
        "Chinese (Simplified)": "负责 (fùzé)"
    },
    "collapse": {
        "Hindi": "गिरना (girna)",
        "Chinese (Simplified)": "倒塌 (dǎotā)"
    },
    "introduction": {
        "Hindi": "परिचय (parichay)",
        "Chinese (Simplified)": "介绍 (jièshào)"
    },
    "introduce": {
        "Hindi": "परिचय देना (parichay dena)",
        "Chinese (Simplified)": "介绍 (jièshào)"
    },
    "self": {
        "Hindi": "स्वयं (svayam)",
        "Chinese (Simplified)": "自己 (zìjǐ)"
    },
    "care": {
        "Hindi": "देखभाल (dekhbhal)",
        "Chinese (Simplified)": "照顾 (zhàogù)"
    },
    "careless": {
        "Hindi": "लापरवाह (laparvah)",
        "Chinese (Simplified)": "粗心 (cūxīn)"
    },
    "protect": {
        "Hindi": "सुरक्षित करना (surakshit karna)",
        "Chinese (Simplified)": "保护 (bǎohù)"
    },
    "reality": {
        "Hindi": "वास्तविकता (vastavikta)",
        "Chinese (Simplified)": "现实 (xiànshí)"
    },
    "train": {
        "Hindi": "प्रशिक्षण देना (prashikshan dena)",
        "Chinese (Simplified)": "训练 (xùnliàn)"
    },
    "training": {
        "Hindi": "प्रशिक्षण (prashikshan)",
        "Chinese (Simplified)": "训练 (xùnliàn)"
    },
    "look": {
        "Hindi": "देखना (dekhna)",
        "Chinese (Simplified)": "看 (kàn)"
    },
    "habit": {
        "Hindi": "आदत (aadat)",
        "Chinese (Simplified)": "习惯 (xíguàn)"
    },
    "major": {
        "Hindi": "मुख्य (mukhya)",
        "Chinese (Simplified)": "主要 (zhǔyào)"
    },
    "minor": {
        "Hindi": "छोटा (chhota)",
        "Chinese (Simplified)": "次要 (cìyào)"
    },
    "majority": {
        "Hindi": "बहुमत (bahumat)",
        "Chinese (Simplified)": "多数 (duōshù)"
    },
    "minority": {
        "Hindi": "अल्पसंख्यक (alpasankhyak)",
        "Chinese (Simplified)": "少数 (shǎoshù)"
    },  
    "genius": {
        "Hindi": "प्रतिभाशाली (Pratibhashali)",
        "Chinese (Simplified)": "天才 (tiāncái)"
    },
    "intermediate": {
        "Hindi": "मध्यवर्ती (Madhyavarti)",
        "Chinese (Simplified)": "中级 (zhōngjí)"
    },
    "joke": {
        "Hindi": "मज़ाक (Mazāk)",
        "Chinese (Simplified)": "玩笑 (wánxiào)"
    },
    "ban": {
        "Hindi": "प्रतिबंध (Pratibandh)",
        "Chinese (Simplified)": "禁止 (jìnzhǐ)"
    },
    "unban": {
        "Hindi": "प्रतिबंध हटाना (Pratibandh Hatana)",
        "Chinese (Simplified)": "取消禁止 (qǔxiāo jìnzhǐ)"
    },
    "thug": {
        "Hindi": "गुंडा (Gunda)",
        "Chinese (Simplified)": "暴徒 (bàotú)"
    },
    "steal": {
        "Hindi": "चोरी करना (Chori Karna)",
        "Chinese (Simplified)": "偷窃 (tōuqiè)"
    },
    "fight": {
        "Hindi": "लड़ाई (Ladai)",
        "Chinese (Simplified)": "战斗 (zhàndòu)"
    },
    "war": {
        "Hindi": "युद्ध (Yuddh)",
        "Chinese (Simplified)": "战争 (zhànzhēng)"
    },  
    #Tastes
    "sweet": {
        "Hindi": "मीठा (Meetha)",
        "Chinese (Simplified)": "甜 (tián)"
    },
    "sour": {
        "Hindi": "खट्टा (Khatta)",
        "Chinese (Simplified)": "酸 (suān)"
    },
    "bitter": {
        "Hindi": "कड़वा (Kadwa)",
        "Chinese (Simplified)": "苦 (kǔ)"
    },
    "spicy": {
        "Hindi": "मसालेदार (Masaledar)",
        "Chinese (Simplified)": "辣 (là)"
    },
    "umami": {
        "Hindi": "उमामी (Umami)",
        "Chinese (Simplified)": "鲜 (xiān)"
    },
    "savory": {
        "Hindi": "चटपटा (Chatpata)",
        "Chinese (Simplified)": "美味 (měiwèi)"
    },
    "bland": {
        "Hindi": "फीका (Feeka)",
        "Chinese (Simplified)": "淡 (dàn)"
    },
    "tangy": {
        "Hindi": "चटपटा (Chatpata)",
        "Chinese (Simplified)": "酸辣 (suānlà)"
    },
    "free": {
        "Hindi": "मुफ़्त (Muft)",
        "Chinese (Simplified)": "免费 (miǎnfèi)"
    },
    "paid": {
        "Hindi": "भुगतान किया हुआ (Bhugtan Kiya Hua)",
        "Chinese (Simplified)": "付费 (fùfèi)"
    },
    "leave": {
        "Hindi": "छोड़ना (Chhodna)",
        "Chinese (Simplified)": "离开 (líkāi)"
    },
    "mail": {
        "Hindi": "डाक (Daak)",
        "Chinese (Simplified)": "邮件 (yóujiàn)"
    },
    "calculate": {
        "Hindi": "गणना करना (Ganna Karna)",
        "Chinese (Simplified)": "计算 (jìsuàn)"
    },
    "worship": {
        "Hindi": "पूजा (Pooja)",
        "Chinese (Simplified)": "崇拜 (chóngbài)"
    },
    "viral": {
        "Hindi": "वायरल (Viral)",
        "Chinese (Simplified)": "病毒式 (bìngdúshì)"
    },
    "fever": {
        "Hindi": "बुखार (Bukhar)",
        "Chinese (Simplified)": "发烧 (fāshāo)"
    },
    "disgust": {
        "Hindi": "घृणा (Ghrina)",
        "Chinese (Simplified)": "厌恶 (yànwù)"
    },
    "disgusting": {
        "Hindi": "घिनौना (Ghinauna)",
        "Chinese (Simplified)": "恶心 (ěxīn)"
    },
    "disguise": {
        "Hindi": "भेष (Bhes)",
        "Chinese (Simplified)": "伪装 (wěizhuāng)"
    },
    "update": {
        "Hindi": "अद्यतन (Adyatan)",
        "Chinese (Simplified)": "更新 (gēngxīn)"
    },
    "upgrade": {
        "Hindi": "उन्नयन (Unnayan)",
        "Chinese (Simplified)": "升级 (shēngjí)"
    },
    "because": {
        "Hindi": "क्योंकि (Kyonki)",
        "Chinese (Simplified)": "因为 (yīnwèi)"
    },
    "reuse": {
        "Hindi": "पुनः उपयोग (Punah Upyog)",
        "Chinese (Simplified)": "再利用 (zài lìyòng)"
    },
    "reduce": {
        "Hindi": "कम करना (Kam Karna)",
        "Chinese (Simplified)": "减少 (jiǎnshǎo)"
    },
    "recycle": {
        "Hindi": "पुनर्चक्रण (Punarchakran)",
        "Chinese (Simplified)": "回收 (huíshōu)"
    },
    "practice": {
        "Hindi": "अभ्यास (Abhyas)",
        "Chinese (Simplified)": "练习 (liànxí)"
    },
    "priest": {
        "Hindi": "पुजारी (Pujari)",
        "Chinese (Simplified)": "牧师 (mùshī)"
    },
    "boss": {
        "Hindi": "मालिक (Malik)",
        "Chinese (Simplified)": "老板 (lǎobǎn)"
    },
    "wake": {
        "Hindi": "जागना (Jagna)",
        "Chinese (Simplified)": "醒来 (xǐnglái)"
    },
    "wakeup": {
        "Hindi": "जागना (Jagna)",
        "Chinese (Simplified)": "起床 (qǐchuáng)"
    },
    "lay": {
        "Hindi": "लेटना (Letna)",
        "Chinese (Simplified)": "躺下 (tǎngxià)"
    },
    "makeup": {
        "Hindi": "सौंदर्य प्रसाधन (Saundarya Prasadhan)",
        "Chinese (Simplified)": "化妆 (huàzhuāng)"
    },
    "method": {
        "Hindi": "विधि (Vidhi)",
        "Chinese (Simplified)": "方法 (fāngfǎ)"
    },
    "class": {
        "Hindi": "कक्षा (Kaksha)",
        "Chinese (Simplified)": "班级 (bānjí)"
    },
    "stay": {
        "Hindi": "रुकना (Rukna)",
        "Chinese (Simplified)": "停留 (tíngliú)"
    },
    "neighbor": {
        "Hindi": "पड़ोसी (Padosi)",
        "Chinese (Simplified)": "邻居 (línjū)"
    },
    "mystery": {
        "Hindi": "रहस्य (Rahasya)",
        "Chinese (Simplified)": "神秘 (shénmì)"
    },
    "predict": {
        "Hindi": "भविष्यवाणी करना (Bhavishyavani Karna)",
        "Chinese (Simplified)": "预测 (yùcè)"
    },
    "prediction": {
        "Hindi": "भविष्यवाणी (Bhavishyavani)",
        "Chinese (Simplified)": "预测 (yùcè)"
    },
    "awkward": {
        "Hindi": "अजीब (Ajeeb)",
        "Chinese (Simplified)": "尴尬 (gāngà)"
    },
    "plan": {
        "Hindi": "योजना (Yojana)",
        "Chinese (Simplified)": "计划 (jìhuà)"
    },
    "guarantee": {
        "Hindi": "गारंटी (Guarantee)",
        "Chinese (Simplified)": "保证 (bǎozhèng)"
    },
    "clock": {
        "Hindi": "घड़ी (Ghadi)",
        "Chinese (Simplified)": "时钟 (shízhōng)"
    },
    "humble": {
        "Hindi": "विनम्र (Vinamra)",
        "Chinese (Simplified)": "谦虚 (qiānxū)"
    },
    "narcissistic": {
        "Hindi": "आत्ममुग्ध (Aatmamugdh)",
        "Chinese (Simplified)": "自恋的 (zìliàn de)"
    },
    "interview": {
        "Hindi": "साक्षात्कार (Sakshatkar)",
        "Chinese (Simplified)": "面试 (miànshì)"
    },
    "view": {
        "Hindi": "दृश्य (Drishya)",
        "Chinese (Simplified)": "视图 (shìtú)"
    },
    "think": {
        "Hindi": "सोचना (Sochna)",
        "Chinese (Simplified)": "思考 (sīkǎo)"
    },
    "thinking": {
        "Hindi": "सोच (Soch)",
        "Chinese (Simplified)": "思维 (sīwéi)"
    },
    "nation": {
        "Hindi": "राष्ट्र (Rashtra)",
        "Chinese (Simplified)": "国家 (guójiā)"
    },
    "nationalism": {
        "Hindi": "राष्ट्रीयता (Rashtriyata)",
        "Chinese (Simplified)": "民族主义 (mínzú zhǔyì)"
    },
    "resource": {
        "Hindi": "संसाधन (Sansadhan)",
        "Chinese (Simplified)": "资源 (zīyuán)"
    },
    "into": {
        "Hindi": "में (Mein)",
        "Chinese (Simplified)": "进入 (jìnrù)"
    },
    "gangster": {
        "Hindi": "गैंगस्टर (Gangster)",
        "Chinese (Simplified)": "歹徒 (dǎitú)"
    },
    "vigilante": {
        "Hindi": "संरक्षक (Sanrakshak)",
        "Chinese (Simplified)": "义务警员 (yìwù jǐngyuán)"
    },
    "comfort": {
        "Hindi": "सुविधा (Suvidha)",
        "Chinese (Simplified)": "安慰 (ānwèi)"
    },
    "relax": {
        "Hindi": "आराम (Aaraam)",
        "Chinese (Simplified)": "放松 (fàngsōng)"
    },
    "card": {
        "Hindi": "कार्ड (Kaard)",
        "Chinese (Simplified)": "卡片 (kǎpiàn)"
    },
    "bounce": {
        "Hindi": "उछाल (Uchhaal)",
        "Chinese (Simplified)": "弹跳 (tántiào)"
    },
    "squeeze": {
        "Hindi": "निचोड़ना (Nichodna)",
        "Chinese (Simplified)": "挤压 (jǐyā)"
    },
    "sprint": {
        "Hindi": "दौड़ (Daud)",
        "Chinese (Simplified)": "冲刺 (chōngcì)"
    },
    "round": {
        "Hindi": "गोल (Gol)",
        "Chinese (Simplified)": "圆形 (yuánxíng)"
    },
    "crawl": {
        "Hindi": "रेंगना (Rengna)",
        "Chinese (Simplified)": "爬行 (páxíng)"
    },
    "blood": {
        "Hindi": "खून (Khoon)",
        "Chinese (Simplified)": "血液 (xuèyè)"
    },
    "liquid": {
        "Hindi": "तरल (Taral)",
        "Chinese (Simplified)": "液体 (yètǐ)"
    },
    "bumper": {
        "Hindi": "बम्पर (Bampar)",
        "Chinese (Simplified)": "保险杠 (bǎoxiǎn gàng)"
    },
    "intercourse": {
        "Hindi": "संबंध (Sambandh)",
        "Chinese (Simplified)": "交往 (jiāowǎng)"
    },
    "kidnap": {
        "Hindi": "अपहरण (Apharan)",
        "Chinese (Simplified)": "绑架 (bǎngjià)"
    },
    "kidnapper": {
        "Hindi": "अपहरणकर्ता (Apharankarta)",
        "Chinese (Simplified)": "绑匪 (bǎngfěi)"
    },
    "lava": {
        "Hindi": "लावा (Laava)",
        "Chinese (Simplified)": "熔岩 (róngyán)"
    },
    "cooperate": {
        "Hindi": "सहयोग करना (Sahyog Karna)",
        "Chinese (Simplified)": "合作 (hézuò)"
    },
    "privacy": {
        "Hindi": "गोपनीयता (Gopniyata)",
        "Chinese (Simplified)": "隐私 (yǐnsī)"
    },
    "security": {
        "Hindi": "सुरक्षा (Suraksha)",
        "Chinese (Simplified)": "安全 (ānquán)"
    },
    "international": {
        "Hindi": "अंतरराष्ट्रीय (Antarraashtreey)",
        "Chinese (Simplified)": "国际 (guójì)"
    },
    "ultimate": {
        "Hindi": "अंतिम (Antim)",
        "Chinese (Simplified)": "最终 (zuìzhōng)"
    },
    "safety": {
        "Hindi": "सुरक्षा (Suraksha)",
        "Chinese (Simplified)": "安全 (ānquán)"
    },
    "nest": {
        "Hindi": "घोंसला (Ghonsla)",
        "Chinese (Simplified)": "巢 (cháo)"
    },
    "tribute": {
        "Hindi": "श्रद्धांजलि (Shraddhanjali)",
        "Chinese (Simplified)": "贡品 (gòngpǐn)"
    },
    "touch": {
        "Hindi": "स्पर्श (Sparsh)",
        "Chinese (Simplified)": "触碰 (chùpèng)"
    },
    "electricity": {
        "Hindi": "बिजली (Bijli)",
        "Chinese (Simplified)": "电 (diàn)"
    },
    "wire": {
        "Hindi": "तार (Taar)",
        "Chinese (Simplified)": "电线 (diànxiàn)"
    },
    "penetrate": {
        "Hindi": "प्रवेश करना (Pravesh Karna)",
        "Chinese (Simplified)": "穿透 (chuāntòu)"
    },
    "scratch": {
        "Hindi": "खरोंच (Kharonch)",
        "Chinese (Simplified)": "划痕 (huáhén)"
    },
    "smooth": {
        "Hindi": "चिकना (Chikna)",
        "Chinese (Simplified)": "光滑 (guānghuá)"
    },
    "boundary": {
        "Hindi": "सीमा (Seema)",
        "Chinese (Simplified)": "边界 (biānjiè)"
    },
    "i need comfort after a long day.": {
        "Hindi": "लंबे दिन के बाद मुझे आराम की आवश्यकता है। (Lambe din ke baad mujhe aaraam ki aavashyakta hai)",
        "Chinese (Simplified)": "一天忙碌后我需要安慰。 (Yītiān mánglù hòu wǒ xūyào ānwèi)"
    },
    "it's good to relax and enjoy nature.": {
        "Hindi": "आराम करना और प्रकृति का आनंद लेना अच्छा है। (Aaraam karna aur prakriti ka aanand lena accha hai)",
        "Chinese (Simplified)": "放松并享受大自然是很好的。 (Fàngsōng bìng xiǎngshòu dà zìrán shì hěn hǎo de)"
    },
    "can you give me your card, please?": {
        "Hindi": "क्या आप मुझे अपना कार्ड दे सकते हैं? (Kya aap mujhe apna kaard de sakte hain?)",
        "Chinese (Simplified)": "你能把你的卡给我吗？ (Nǐ néng bǎ nǐ de kǎ gěi wǒ ma?)"
    },
    "the ball bounced high into the air.": {
        "Hindi": "गेंद हवा में ऊँचाई तक उछली। (Gend hawa mein oonchaai tak uchhli)",
        "Chinese (Simplified)": "球弹得很高。 (Qiú tán dé hěn gāo)"
    },
    "he squeezed the toothpaste onto the brush.": {
        "Hindi": "उसने ब्रश पर टूथपेस्ट निचोड़ा। (Usne brush par toothpaste nichoda)",
        "Chinese (Simplified)": "他把牙膏挤到了刷子上。 (Tā bǎ yágāo jǐ dào le shuāzi shàng)"
    },
    "she can sprint faster than anyone in her class.": {
        "Hindi": "वह अपनी कक्षा में किसी से भी तेज दौड़ सकती है। (Vah apni kaksha mein kisi se bhi tez daud sakti hai)",
        "Chinese (Simplified)": "她比班里任何人都跑得快。 (Tā bǐ bān lǐ rènhé rén dōu pǎo dé kuài)"
    },
    "we walked around the park this evening.": {
        "Hindi": "आज शाम हमने पार्क के चारों ओर चहलकदमी की। (Aaj shaam humne park ke chaaro aur chahalkadmi ki)",
        "Chinese (Simplified)": "今晚我们绕着公园散步。 (Jīnwǎn wǒmen ràozhe gōngyuán sànbù)"
    },
    "the baby started to crawl on the floor.": {
        "Hindi": "बच्चा फर्श पर रेंगने लगा। (Baccha farsh par rengne laga)",
        "Chinese (Simplified)": "婴儿开始在地板上爬。 (Yīng'ér kāishǐ zài dìbǎn shàng pá)"
    },
    "erotic": {
        "Hindi": "कामुक (Kaamuk)",
        "Chinese (Simplified)": "色情的 (Sèqíng de)"
    },
    "isolation": {
        "Hindi": "अलगाव (Alagav)",
        "Chinese (Simplified)": "隔离 (Gélí)"
    },
    "deforestation": {
        "Hindi": "वनों की कटाई (Vano ki kataai)",
        "Chinese (Simplified)": "森林砍伐 (Sēnlín kǎnfá)"
    },
    "sex": {
        "Hindi": "लिंग / यौन (Ling / Yaun)",
        "Chinese (Simplified)": "性 (Xìng)"
    },
    "puberty": {
        "Hindi": "किशोरावस्था (Kishoravastha)",
        "Chinese (Simplified)": "青春期 (Qīngchūnqī)"
    },
    "sperm": {
        "Hindi": "शुक्राणु (Shukraanu)",
        "Chinese (Simplified)": "精子 (Jīngzǐ)"
    },
    "ovum": {
        "Hindi": "अंडाणु (Andaanu)",
        "Chinese (Simplified)": "卵子 (Luǎnzǐ)"
    },
    "reproduce": {
        "Hindi": "पुनरुत्पादन करना (Punrutpaadan karna)",
        "Chinese (Simplified)": "繁殖 (Fánzhí)"
    },
    "produce": {
        "Hindi": "उत्पादन करना (Utpaadan karna)",
        "Chinese (Simplified)": "生产 (Shēngchǎn)"
    },
    "cell": {
        "Hindi": "कोशिका (Koshika)",
        "Chinese (Simplified)": "细胞 (Xìbāo)"
    },
    "atom": {
        "Hindi": "परमाणु (Parmaanu)",
        "Chinese (Simplified)": "原子 (Yuánzǐ)"
    },
    "inject": {
        "Hindi": "इंजेक्ट करना (Inject karna)",
        "Chinese (Simplified)": "注射 (Zhùshè)"
    },
    "eject": {
        "Hindi": "निष्कासित करना (Nishkasit karna)",
        "Chinese (Simplified)": "弹出 (Tánchū)"
    },
    "penis": {
        "Hindi": "लिंग (Ling)",
        "Chinese (Simplified)": "阴茎 (Yīnjīng)"
    },
    "vagina": {
        "Hindi": "योनि (Yoni)",
        "Chinese (Simplified)": "阴道 (Yīndào)"
    },
    "breast": {
        "Hindi": "स्तन (Stan)",
        "Chinese (Simplified)": "乳房 (Rǔfáng)"
    },
    "countdown": {
        "Hindi": "उलटी गिनती (Ulti Ginti)",
        "Chinese (Simplified)": "倒计时 (Dào jì shí)"
    },
    "ruin": {
        "Hindi": "बरबाद करना (Barbad Karna)",
        "Chinese (Simplified)": "毁灭 (Huǐmiè)"
    },
    "dungeon": {
        "Hindi": "कालकोठरी (Kaalkothri)",
        "Chinese (Simplified)": "地牢 (Dìláo)"
    },
    "entire": {
        "Hindi": "पूरा (Poora)",
        "Chinese (Simplified)": "整个 (Zhěnggè)"
    },
    "bust": {
        "Hindi": "ध्वस्त करना (Dhvast Karna)",
        "Chinese (Simplified)": "打碎 (Dǎsuì)"
    },
    "busted": {
        "Hindi": "पकड़ा गया (Pakda Gaya)",
        "Chinese (Simplified)": "被抓 (Bèi zhuā)"
    },
    "accident": {
        "Hindi": "दुर्घटना (Durghatna)",
        "Chinese (Simplified)": "事故 (Shìgù)"
    },
    "incident": {
        "Hindi": "घटना (Ghatna)",
        "Chinese (Simplified)": "事件 (Shìjiàn)"
    },
    "logic": {
        "Hindi": "तर्क (Tark)",
        "Chinese (Simplified)": "逻辑 (Luójí)"
    },
    "pillow": {
        "Hindi": "तकिया (Takiya)",
        "Chinese (Simplified)": "枕头 (Zhěntou)"
    },
    "tool": {
        "Hindi": "उपकरण (Upkaran)",
        "Chinese (Simplified)": "工具 (Gōngjù)"
    },
    "gear": {
        "Hindi": "गियर (Gear) / यंत्र (Yantra)",
        "Chinese (Simplified)": "齿轮 (Chǐlún)"
    },
    "guess": {
        "Hindi": "अनुमान लगाना (Anumaan Lagana)",
        "Chinese (Simplified)": "猜测 (Cāicè)"
    },
    "collect": {
        "Hindi": "संग्रह करना (Sangrah Karna)",
        "Chinese (Simplified)": "收集 (Shōují)"
    },
    "hype": {
        "Hindi": "उत्साह (Utsaah)",
        "Chinese (Simplified)": "炒作 (Chǎozuò)"
    },
    "impossible": {
        "Hindi": "असंभव (Asambhav)",
        "Chinese (Simplified)": "不可能 (Bù kěnéng)"
    },
    "possible": {
        "Hindi": "संभव (Sambhav)",
        "Chinese (Simplified)": "可能 (Kěnéng)"
    },
    "path": {
        "Hindi": "पथ (Path)",
        "Chinese (Simplified)": "路径 (Lùjìng)"
    },
    "bribe": {
        "Hindi": "घूस (Ghoos)",
        "Chinese (Simplified)": "贿赂 (Huìlù)"
    },
    "away": {
        "Hindi": "दूर (Door)",
        "Chinese (Simplified)": "远离 (Yuǎnlí)"
    },
    "nearby": {
        "Hindi": "आसपास (Aaspas)",
        "Chinese (Simplified)": "附近 (Fùjìn)"
    },
    "near": {
        "Hindi": "पास (Paas)",
        "Chinese (Simplified)": "靠近 (Kàojìn)"
    },
    "long": {
        "Hindi": "लंबा (Lamba)",
        "Chinese (Simplified)": "长 (Cháng)"
    },
    "alot": {
        "Hindi": "बहुत ज्यादा (Bahut Zyada)",
        "Chinese (Simplified)": "非常多 (Fēicháng duō)"
    },
    "lot": {
        "Hindi": "बहुत (Bahut)",
        "Chinese (Simplified)": "许多 (Xǔduō)"
    },
    "invest": {
        "Hindi": "निवेश करना (Nivesh Karna)",
        "Chinese (Simplified)": "投资 (Tóuzī)"
    },
    "investigate": {
        "Hindi": "जांच करना (Jaanch Karna)",
        "Chinese (Simplified)": "调查 (Diàochá)"
    },
    "skill": {
        "Hindi": "कौशल (Kaushal)",
        "Chinese (Simplified)": "技能 (Jìnéng)"
    },
    "price": {
        "Hindi": "मूल्य (Moolya)",
        "Chinese (Simplified)": "价格 (Jiàgé)"
    },
    "value": {
        "Hindi": "मूल्य (Moolya)",
        "Chinese (Simplified)": "价值 (Jiàzhí)"
    },
    "jackpot": {
        "Hindi": "बड़ी जीत (Badi Jeet)",
        "Chinese (Simplified)": "头奖 (Tóujiǎng)"
    },
    "rod": {
        "Hindi": "छड़ी (Chhadi)",
        "Chinese (Simplified)": "杆 (Gǎn)"
    },
    #Home Rooms names
    "basement": {
        "Hindi": "तहखाना (Tahkhana)",
        "Chinese (Simplified)": "地下室 (Dìxiàshì)"
    },
    "kitchen": {
        "Hindi": "रसोईघर (Rasoighar)",
        "Chinese (Simplified)": "厨房 (Chúfáng)"
    },
    "bedroom": {
        "Hindi": "शयनकक्ष (Shayankaksh)",
        "Chinese (Simplified)": "卧室 (Wòshì)"
    },
    "living room": {
        "Hindi": "बैठक कक्ष (Baithak Kaksh)",
        "Chinese (Simplified)": "客厅 (Kètīng)"
    },
    "bathroom": {
        "Hindi": "स्नानघर (Snaan Ghar)",
        "Chinese (Simplified)": "浴室 (Yùshì)"
    },
    "dining room": {
        "Hindi": "भोजन कक्ष (Bhojan Kaksh)",
        "Chinese (Simplified)": "餐厅 (Cāntīng)"
    },
    "garage": {
        "Hindi": "गेराज (Garage)",
        "Chinese (Simplified)": "车库 (Chēkù)"
    },
    "attic": {
        "Hindi": "अटारी (Atari)",
        "Chinese (Simplified)": "阁楼 (Gélóu)"
    },
    "hallway": {
        "Hindi": "गलियारा (Galiara)",
        "Chinese (Simplified)": "走廊 (Zǒuláng)"
    },
    "study room": {
        "Hindi": "पढ़ाई का कमरा (Padhai Ka Kamra)",
        "Chinese (Simplified)": "书房 (Shūfáng)"
    },
    "laundry room": {
        "Hindi": "धोबीघर (Dhobighar)",
        "Chinese (Simplified)": "洗衣房 (Xǐyīfáng)"
    },
    "balcony": {
        "Hindi": "बालकनी (Balkani)",
        "Chinese (Simplified)": "阳台 (Yángtái)"
    },
    "storage room": {
        "Hindi": "भंडारण कक्ष (Bhandaran Kaksh)",
        "Chinese (Simplified)": "储藏室 (Chǔcángshì)"
    },
    "pantry": {
        "Hindi": "रसदघर (Rasadh Ghar)",
        "Chinese (Simplified)": "食品储藏室 (Shípǐn chǔcáng shì)"
    },
    "porch": {
        "Hindi": "बरामदा (Baramda)",
        "Chinese (Simplified)": "门廊 (Ménláng)"
    },
    "roof": {
        "Hindi": "छत (Chhat)",
        "Chinese (Simplified)": "屋顶 (Wūdǐng)"
    },
    "garden": {
        "Hindi": "बगीचा (Bagicha)",
        "Chinese (Simplified)": "花园 (Huāyuán)"
    },
    "guest room": {
        "Hindi": "अतिथि कक्ष (Atithi Kaksh)",
        "Chinese (Simplified)": "客房 (Kèfáng)"
    },
    "guest": {
        "Hindi": "अतिथि (Atithi)",
        "Chinese (Simplified)": "客人 (Kèrén)"
    },
    "relation": {
        "Hindi": "संबंध (Sambandh)",
        "Chinese (Simplified)": "关系 (Guānxì)"
    },
    "feed": {
        "Hindi": "खिलाना (Khilaana)",
        "Chinese (Simplified)": "喂养 (Wèiyǎng)"
    },
    "down to earth": {
        "Hindi": "व्यवहारिक (Vyavaharik)",
        "Chinese (Simplified)": "脚踏实地 (Jiǎotà shídì)"
    },
    "intellectual": {
        "Hindi": "बौद्धिक (Bauddhik)",
        "Chinese (Simplified)": "知识分子 (Zhīshì fènzǐ)"
    },
    "graduate": {
        "Hindi": "स्नातक (Snatak)",
        "Chinese (Simplified)": "毕业生 (Bìyèshēng)"
    },
    "park": {
        "Hindi": "पार्क (Park)",
        "Chinese (Simplified)": "公园 (Gōngyuán)"
    },
    "lantern": {
        "Hindi": "लालटेन (Laaltein)",
        "Chinese (Simplified)": "灯笼 (Dēnglóng)"
    },
    "torch": {
        "Hindi": "मशाल (Mashaal)",
        "Chinese (Simplified)": "火炬 (Huǒjù)"
    },
    "debate": {
        "Hindi": "विवाद (Vivaad)",
        "Chinese (Simplified)": "辩论 (Biànlùn)"
    },
    "pocket": {
        "Hindi": "जेब (Jeb)",
        "Chinese (Simplified)": "口袋 (Kǒudài)"
    },
    "packet": {
        "Hindi": "पैकेट (Packet)",
        "Chinese (Simplified)": "小包 (Xiǎobāo)"
    },
    "swell": {
        "Hindi": "सूजना (Soojna)",
        "Chinese (Simplified)": "肿胀 (Zhǒngzhàng)"
    },
    "bite": {
        "Hindi": "काटना (Kaatna)",
        "Chinese (Simplified)": "咬 (Yǎo)"
    },
    "bought": {
        "Hindi": "खरीदा (Khareeda)",
        "Chinese (Simplified)": "买了 (Mǎile)"
    },
    "another": {
        "Hindi": "दूसरा (Doosra)",
        "Chinese (Simplified)": "另一个 (Lìng yīgè)"
    },
    "turtle": {
        "Hindi": "कछुआ (Kachhua)",
        "Chinese (Simplified)": "乌龟 (Wūguī)"
    },
    "buffalo": {
        "Hindi": "भैंस (Bhais)",
        "Chinese (Simplified)": "水牛 (Shuǐniú)"
    },
    "bull": {
        "Hindi": "सांड़ (Saand)",
        "Chinese (Simplified)": "公牛 (Gōngniú)"
    },
    "page": {
        "Hindi": "पृष्ठ (Prashth)",
        "Chinese (Simplified)": "页面 (Yèmiàn)"
    },
    "servant": {
        "Hindi": "नौकर (Naukar)",
        "Chinese (Simplified)": "仆人 (Púrén)"
    },
    "lazy": {
        "Hindi": "आलसी (Aalsi)",
        "Chinese (Simplified)": "懒惰 (Lǎnduò)"
    },
    "sea port": {
        "Hindi": "समुद्र बंदरगाह (Samudra Bandaragaah)",
        "Chinese (Simplified)": "海港 (Hǎigǎng)"
    },
    "follow": {
        "Hindi": "अनुसरण करना (Anusaran Karna)",
        "Chinese (Simplified)": "跟随 (Gēnsuí)"
    },
    "followers": {
        "Hindi": "अनुयायी (Anuyaayi)",
        "Chinese (Simplified)": "追随者 (Zhuīsuí zhě)"
    },
    "following": {
        "Hindi": "आगे (Aage)",
        "Chinese (Simplified)": "以下 (Yǐxià)"
    },
    "blind": {
        "Hindi": "अंधा (Andha)",
        "Chinese (Simplified)": "盲人 (Mángrén)"
    },
    "advice": {
        "Hindi": "सलाह (Salaah)",
        "Chinese (Simplified)": "建议 (Jiànyì)"
    },
    "recommend": {
        "Hindi": "सिफारिश करना (Sifaarish Karna)",
        "Chinese (Simplified)": "推荐 (Tuījiàn)"
    },
    "nor": {
        "Hindi": "और नहीं (Aur Nahin)",
        "Chinese (Simplified)": "也不 (Yě bù)"
    },
    "neither": {
        "Hindi": "न तो (Na To)",
        "Chinese (Simplified)": "既不 (Jì bù)"
    },
    "wedding": {
        "Hindi": "शादी (Shaadi)",
        "Chinese (Simplified)": "婚礼 (Hūnlǐ)"
    },
    "pure": {
        "Hindi": "शुद्ध (Shuddh)",
        "Chinese (Simplified)": "纯净 (Chúnjìng)"
    },
    "discovery": {
        "Hindi": "खोज (Khoj)",
        "Chinese (Simplified)": "发现 (Fāxiàn)"
    },
    "split": {
        "Hindi": "विभाजन (Vibhaajan)",
        "Chinese (Simplified)": "分裂 (Fēnliè)"
    },
    "beast": {
        "Hindi": "जानवर (Jaanwar)",
        "Chinese (Simplified)": "野兽 (Yěshòu)"
    },
    "parliament": {
        "Hindi": "संसद (Sansad)",
        "Chinese (Simplified)": "议会 (Yìhuì)"
    },
    "trauma": {
        "Hindi": "आघात (Aaghaat)",
        "Chinese (Simplified)": "创伤 (Chuāngshāng)"
    },
    "invisible": {
        "Hindi": "अदृश्य (Adrishya)",
        "Chinese (Simplified)": "隐形 (Yǐnxíng)"
    },
    "invincible": {
        "Hindi": "अजेय (Ajey)",
        "Chinese (Simplified)": "无敌 (Wúdí)"
    },
    "actual": {
        "Hindi": "वास्तविक (Vastavik)",
        "Chinese (Simplified)": "实际 (Shíjì)"
    },
    "expensive": {
        "Hindi": "महंगा (Mehnga)",
        "Chinese (Simplified)": "昂贵 (Ángguì)"
    },
    "cheap": {
        "Hindi": "सस्ता (Sasta)",
        "Chinese (Simplified)": "便宜 (Piányi)"
    },
    "regret": {
        "Hindi": "पछतावा (Pachhtaava)",
        "Chinese (Simplified)": "遗憾 (Yíhàn)"
    },
    "conflict": {
        "Hindi": "संघर्ष (Sangharsh)",
        "Chinese (Simplified)": "冲突 (Chōngtū)"
    },
    "development": {
        "Hindi": "विकास (Vikaas)",
        "Chinese (Simplified)": "发展 (Fāzhǎn)"
    },
    "handle": {
        "Hindi": "हैंडल (Handle)",
        "Chinese (Simplified)": "把手 (Bǎshǒu)"
    },
    "slave": {
        "Hindi": "गुलाम (Gulaam)",
        "Chinese (Simplified)": "奴隶 (Núlì)"
    },
    "handling": {
        "Hindi": "संपादन (Sampaadan)",
        "Chinese (Simplified)": "处理 (Chǔlǐ)"
    },
    "explode": {
        "Hindi": "विस्फोट करना (Visphot Karna)",
        "Chinese (Simplified)": "爆炸 (Bàozhà)"
    },
    "caste": {
        "Hindi": "जाति (Jaati)",
        "Chinese (Simplified)": "种姓 (Zhǒngxìng)"
    },
    "job": {
        "Hindi": "नौकरी (Naukri)",
        "Chinese (Simplified)": "工作 (Gōngzuò)"
    },
    "profession": {
        "Hindi": "पेशा (Pesha)",
        "Chinese (Simplified)": "职业 (Zhíyè)"
    },
    "everyone": {
        "Hindi": "हर कोई (Har Koi)",
        "Chinese (Simplified)": "每个人 (Měi gèrén)"
    },
    "he always speaks with confidence.": {
        "Hindi": "वह हमेशा आत्मविश्वास के साथ बोलता है। (Vah hamesha atmavishwas ke saath bolta hai.)",
        "Chinese (Simplified)": "他总是自信地说话。 (Tā zǒng shì zìxìn de shuōhuà.)"
    },
    "the cat jumped over the wall effortlessly.": {
        "Hindi": "बिल्ली ने दीवार के ऊपर आसानी से छलांग लगाई। (Billi ne deewar ke upar aasani se chhalang lagayi.)",
        "Chinese (Simplified)": "猫轻松地跳过了墙。 (Māo qīngsōng de tiàoguòle qiáng.)"
    },
    "this cake tastes better than it looks.": {
        "Hindi": "यह केक देखने से ज्यादा स्वादिष्ट है। (Yeh cake dekhne se zyada swadisht hai.)",
        "Chinese (Simplified)": "这个蛋糕吃起来比看起来更好。 (Zhège dàngāo chī qǐlái bǐ kàn qǐlái gèng hǎo.)"
    },
    "he reads a new book every month.": {
        "Hindi": "वह हर महीने एक नई किताब पढ़ता है। (Vah har mahine ek nayi kitaab padhta hai.)",
        "Chinese (Simplified)": "他每个月读一本新书。 (Tā měi gè yuè dú yī běn xīn shū.)"
    },
    "the sunrise was absolutely breathtaking.": {
        "Hindi": "सूर्योदय वाकई मनमोहक था। (Suryoday vaakai manmohak tha.)",
        "Chinese (Simplified)": "日出美得令人叹为观止。 (Rìchū měi de lìng rén tànwéi guānzhǐ.)"
    },
    "he practices the piano for hours daily.": {
        "Hindi": "वह रोज घंटों तक पियानो का अभ्यास करता है। (Vah roz ghanton tak piano ka abhyas karta hai.)",
        "Chinese (Simplified)": "他每天练习钢琴好几个小时。 (Tā měitiān liànxí gāngqín hǎo jǐ gè xiǎoshí.)"
    },
    "she paints landscapes in her free time.": {
        "Hindi": "वह अपने खाली समय में परिदृश्य पेंट करती है। (Vah apne khaali samay mein paridrishya paint karti hai.)",
        "Chinese (Simplified)": "她在空闲时间画风景画。 (Tā zài kòngxián shíjiān huà fēngjǐng huà.)"
    },
    "the dog wagged its tail happily.": {
        "Hindi": "कुत्ते ने खुशी से अपनी पूंछ हिलाई। (Kutte ne khushi se apni poonch hilayi.)",
        "Chinese (Simplified)": "狗高兴地摇着尾巴。 (Gǒu gāoxìng de yáozhe wěibā.)"
    },
    "he built this table from scratch.": {
        "Hindi": "उसने यह मेज शुरुआत से बनाई। (Usne yeh mej shuruaat se banayi.)",
        "Chinese (Simplified)": "他从零开始做了这张桌子。 (Tā cóng líng kāishǐ zuòle zhè zhāng zhuōzi.)"
    },
    "she writes poetry to express her emotions.": {
        "Hindi": "वह अपनी भावनाओं को व्यक्त करने के लिए कविता लिखती है। (Vah apni bhavnaon ko vyakt karne ke liye kavita likhti hai.)",
        "Chinese (Simplified)": "她通过写诗表达自己的情感。 (Tā tōngguò xiě shī biǎodá zìjǐ de qínggǎn.)"
    },
    "he solved the puzzle in just a few minutes.": {
        "Hindi": "उसने पहेली को कुछ ही मिनटों में हल कर लिया। (Usne paheli ko kuch hi minton mein hal kar liya.)",
        "Chinese (Simplified)": "他几分钟内就解决了这个谜题。 (Tā jǐ fēnzhōng nèi jiù jiějuéle zhège mí tí.)"
    },
    "the kids were excited to see the magician perform.": {
        "Hindi": "बच्चे जादूगर का प्रदर्शन देखकर उत्साहित थे। (Bacche jadugar ka pradarshan dekhkar utsahit the.)",
        "Chinese (Simplified)": "孩子们看到魔术师表演时很兴奋。 (Háizimen kàndào móshùshī biǎoyǎn shí hěn xīngfèn.)"
    },
    "she sang a beautiful song at the event.": {
        "Hindi": "उसने कार्यक्रम में एक खूबसूरत गाना गाया। (Usne karyakram mein ek khoobsurat gaana gaya.)",
        "Chinese (Simplified)": "她在活动上唱了一首美丽的歌。 (Tā zài huódòng shàng chàngle yī shǒu měilì de gē.)"
    },
    "the train arrived earlier than expected.": {
        "Hindi": "ट्रेन उम्मीद से पहले पहुंच गई। (Train umeed se pehle pahunch gayi.)",
        "Chinese (Simplified)": "火车比预期早到了。 (Huǒchē bǐ yùqí zǎo dàole.)"
    },
    "he is learning to bake delicious cakes.": {
        "Hindi": "वह स्वादिष्ट केक बनाना सीख रहा है। (Vah swadisht cake banana seekh raha hai.)",
        "Chinese (Simplified)": "他正在学习烘焙美味的蛋糕。 (Tā zhèngzài xuéxí hōngbèi měiwèi de dàngāo.)"
    },
    "they planted trees to make the area greener.": {
        "Hindi": "उन्होंने क्षेत्र को हरा-भरा बनाने के लिए पेड़ लगाए। (Unhone kshetra ko hara-bhara banane ke liye ped lagaye.)",
        "Chinese (Simplified)": "他们种树让这个地区更加绿色。 (Tāmen zhòngshù ràng zhège dìqū gèng jiā lǜsè.)"
    },
    "she saved enough money to buy a new laptop.": {
        "Hindi": "उसने नया लैपटॉप खरीदने के लिए पर्याप्त पैसे बचाए। (Usne naya laptop kharidne ke liye paryapt paise bachaaye.)",
        "Chinese (Simplified)": "她攒够了钱买了一台新笔记本电脑。 (Tā zǎn gòule qián mǎile yī tái xīn bǐjìběn diànnǎo.)"
    },
    "the fireworks lit up the night sky beautifully.": {
        "Hindi": "आतिशबाजी ने रात के आसमान को खूबसूरती से रोशन कर दिया। (Aatishbaazi ne raat ke aasmaan ko khoobsurti se roshan kar diya.)",
        "Chinese (Simplified)": "烟花美丽地点亮了夜空。 (Yānhuā měilì de diǎnliàngle yèkōng.)"
    },
    "he enjoys hiking in the mountains during weekends.": {
        "Hindi": "वह सप्ताहांत में पहाड़ों में ट्रेकिंग का आनंद लेता है। (Vah saptahant mein pahadon mein trekking ka anand leta hai.)",
        "Chinese (Simplified)": "他喜欢周末在山里徒步。 (Tā xǐhuān zhōumò zài shān lǐ túbù.)"
    },
    "the artist painted a masterpiece that amazed everyone.": {
        "Hindi": "कलाकार ने एक ऐसी कृति बनाई जिसने सभी को चकित कर दिया। (Kalakaar ne ek aisi kriti banayi jisne sabhi ko chakit kar diya.)",
        "Chinese (Simplified)": "艺术家创作了一件让所有人惊叹的杰作。 (Yìshùjiā chuàngzuòle yī jiàn ràng suǒyǒu rén jīngtàn de jiézuò.)"
    },
    "he gave a speech that inspired the audience.": {
        "Hindi": "उसने एक ऐसा भाषण दिया जिसने दर्शकों को प्रेरित किया। (Usne ek aisa bhaashan diya jisne darshakon ko prerit kiya.)",
        "Chinese (Simplified)": "他发表了一次鼓舞人心的演讲。 (Tā fābiǎole yīcì gǔwǔ rén xīn de yǎnjiǎng.)"
    },
    "the dog chased the ball across the park.": {
        "Hindi": "कुत्ते ने पार्क के उस पार गेंद का पीछा किया। (Kutte ne park ke us paar gend ka peecha kiya.)",
        "Chinese (Simplified)": "狗在公园里追着球跑。 (Gǒu zài gōngyuán lǐ zhuīzhe qiú pǎo.)"
    },
    "she opened the gift box and smiled brightly.": {
        "Hindi": "उसने गिफ्ट बॉक्स खोला और चमकते हुए मुस्कुराई। (Usne gift box khola aur chamakte hue muskuraayi.)",
        "Chinese (Simplified)": "她打开礼物盒，灿烂地笑了起来。 (Tā dǎkāi lǐwù hé, cànlàn de xiàole qǐlái.)"
    },
    "the scientist worked tirelessly on the new invention.": {
        "Hindi": "वैज्ञानिक ने नए आविष्कार पर अथक मेहनत की। (Vaigyanik ne naye avishkar par athak mehnat ki.)",
        "Chinese (Simplified)": "科学家不知疲倦地研究新发明。 (Kēxuéjiā bù zhī píjuàn de yánjiū xīn fāmíng.)"
    },
    "the children played happily in the rain.": {
        "Hindi": "बच्चे बारिश में खुशी से खेल रहे थे। (Bacche barish mein khushi se khel rahe the.)",
        "Chinese (Simplified)": "孩子们在雨中快乐地玩耍。 (Háizimen zài yǔ zhōng kuàilè de wánshuǎ.)"
    },
    "she learned to cook her favorite dish from her grandmother.": {
        "Hindi": "उसने अपनी दादी से अपना पसंदीदा व्यंजन बनाना सीखा। (Usne apni dadi se apna pasandida vyanjan banana seekha.)",
        "Chinese (Simplified)": "她从奶奶那里学会了做她最喜欢的菜。 (Tā cóng nǎinai nàlǐ xuéhuìle zuò tā zuì xǐhuān de cài.)"
    },
    "the sunrise over the mountains was breathtaking.": {
        "Hindi": "पहाड़ों पर सूर्योदय बेहद सुंदर था। (Pahadon par sooryoday behad sundar tha.)",
        "Chinese (Simplified)": "山上的日出令人叹为观止。 (Shānshàng de rìchū lìngrén tàn wéi guānzhǐ.)"
    },
    "he built a small treehouse in the backyard.": {
        "Hindi": "उसने पिछवाड़े में एक छोटा सा ट्रीहाउस बनाया। (Usne pichwade mein ek chhota sa treehouse banaya.)",
        "Chinese (Simplified)": "他在后院建了一个小树屋。 (Tā zài hòuyuàn jiànle yīgè xiǎo shùwū.)"
    },
    "the book was so interesting that she finished it in one day.": {
        "Hindi": "किताब इतनी रोचक थी कि उसने इसे एक दिन में खत्म कर दिया। (Kitab itni rochak thi ki usne ise ek din mein khatam kar diya.)",
        "Chinese (Simplified)": "这本书太有趣了，她一天就看完了。 (Zhè běn shū tài yǒuqùle, tā yītiān jiù kàn wánle.)"
    },
    "they danced together under the starry sky.": {
        "Hindi": "वे तारों से भरे आसमान के नीचे साथ में नाचे। (Ve taaron se bhare aasman ke neeche saath mein nache.)",
        "Chinese (Simplified)": "他们在星空下一起跳舞。 (Tāmen zài xīngkōng xià yīqǐ tiàowǔ.)"
    },
    "the old clock in the hallway still works perfectly.": {
        "Hindi": "हॉलवे में पुरानी घड़ी अभी भी पूरी तरह से काम करती है। (Hallway mein purani ghadi abhi bhi poori tarah se kaam karti hai.)",
        "Chinese (Simplified)": "走廊里的老钟仍然完美运转。 (Zǒuláng lǐ de lǎo zhōng réngrán wánměi yùnzhuǎn.)"
    },
    "he enjoys reading history books in his free time.": {
        "Hindi": "वह खाली समय में इतिहास की किताबें पढ़ना पसंद करता है। (Vah khaali samay mein itihaas ki kitabein padhna pasand karta hai.)",
        "Chinese (Simplified)": "他在空闲时间喜欢读历史书。 (Tā zài kòngxián shíjiān xǐhuān dú lìshǐ shū.)"
    },
    "the flowers in the garden bloom beautifully in spring.": {
        "Hindi": "बगीचे के फूल वसंत में खूबसूरती से खिलते हैं। (Bagiche ke phool vasant mein khoobsurti se khilte hain.)",
        "Chinese (Simplified)": "花园里的花在春天盛开得很美。 (Huāyuán lǐ de huā zài chūntiān shèngkāi dé hěn měi.)"
    },
    "the cat curled up by the fireplace to stay warm.": {
        "Hindi": "बिल्ली गर्म रहने के लिए चिमनी के पास गोल होकर बैठ गई। (Billi garm rehne ke liye chimney ke paas gol hokar baith gayi.)",
        "Chinese (Simplified)": "猫蜷缩在壁炉旁取暖。 (Māo quánsuō zài bìlú páng qǔnuǎn.)"
    },
    "she painted a picture of a beautiful sunset.": {
        "Hindi": "उसने एक सुंदर सूर्यास्त की तस्वीर बनाई। (Usne ek sundar sooryaast ki tasveer banayi.)",
        "Chinese (Simplified)": "她画了一幅美丽的日落画。 (Tā huàle yī fú měilì de rìluò huà.)"
    },
    "the little boy gave his mother a handmade card.": {
        "Hindi": "छोटे लड़के ने अपनी माँ को एक हाथ से बना कार्ड दिया। (Chhote ladke ne apni maa ko ek haath se bana card diya.)",
        "Chinese (Simplified)": "小男孩给了妈妈一张手工卡片。 (Xiǎo nánhái gěile māmā yī zhāng shǒugōng kǎpiàn.)"
    },
    "he started learning a new language last month.": {
        "Hindi": "उसने पिछले महीने एक नई भाषा सीखना शुरू किया। (Usne pichhle mahine ek nayi bhaasha seekhna shuru kiya.)",
        "Chinese (Simplified)": "他上个月开始学习一种新语言。 (Tā shàng gè yuè kāishǐ xuéxí yī zhǒng xīn yǔyán.)"
    },
    "the storm knocked down several trees in the neighborhood.": {
        "Hindi": "तूफान ने पड़ोस में कई पेड़ों को गिरा दिया। (Toofaan ne pados mein kai pedon ko gira diya.)",
        "Chinese (Simplified)": "风暴摧倒了附近的几棵树。 (Fēngbào cuī dǎole fùjìn de jǐ kē shù.)"
    },
    "the family gathered to celebrate the festival together.": {
        "Hindi": "परिवार त्योहार को एक साथ मनाने के लिए इकट्ठा हुआ। (Parivaar tyohaar ko ek saath manane ke liye ikattha hua.)",
        "Chinese (Simplified)": "一家人聚在一起庆祝节日。 (Yījiārén jù zài yīqǐ qìngzhù jiérì.)"
    },
    "he built a sandcastle on the beach with his friends.": {
        "Hindi": "उसने अपने दोस्तों के साथ समुद्र तट पर एक रेत का महल बनाया। (Usne apne doston ke saath samudra tat par ek ret ka mahal banaya.)",
        "Chinese (Simplified)": "他和朋友们在海滩上堆了一个沙堡。 (Tā hé péngyǒumen zài hǎitān shàng duīle yīgè shā bǎo.)"
    },
    "she wrote a heartfelt letter to her best friend.": {
        "Hindi": "उसने अपनी सबसे अच्छी दोस्त को एक भावुक पत्र लिखा। (Usne apni sabse acchi dost ko ek bhaavuk patra likha.)",
        "Chinese (Simplified)": "她给她最好的朋友写了一封真挚的信。 (Tā gěi tā zuì hǎo de péngyǒu xiěle yī fēng zhēnzhì de xìn.)"
    },
    "he discovered a hidden trail while exploring the forest.": {
        "Hindi": "उसने जंगल में खोजबीन करते हुए एक छिपा हुआ रास्ता खोजा। (Usne jangal mein khojbheen karte hue ek chhupa hua rasta khoja.)",
        "Chinese (Simplified)": "他在探索森林时发现了一条隐藏的小路。 (Tā zài tànsuǒ sēnlín shí fāxiànle yītiáo yǐncáng de xiǎolù.)"
    },
    "the dog wagged its tail happily when it saw its owner.": {
        "Hindi": "कुत्ते ने अपने मालिक को देखकर खुशी से अपनी पूंछ हिलाई। (Kutte ne apne maalik ko dekhkar khushi se apni poonch hilaai.)",
        "Chinese (Simplified)": "狗看到主人时高兴地摇着尾巴。 (Gǒu kàn dào zhǔrén shí gāoxìng de yáozhe wěibā.)"
    },
    "the students worked together to complete the science project.": {
        "Hindi": "छात्रों ने मिलकर विज्ञान परियोजना को पूरा किया। (Chhatron ne milkar vigyaan pariyojna ko poora kiya.)",
        "Chinese (Simplified)": "学生们一起合作完成了科学项目。 (Xuéshēngmen yīqǐ hézuò wánchéngle kēxué xiàngmù.)"
    },
    "a gentle breeze made the leaves rustle softly.": {
        "Hindi": "हल्की हवा ने पत्तों को धीरे-धीरे सरसराने दिया। (Halki hawa ne patton ko dheere-dheere sarsarane diya.)",
        "Chinese (Simplified)": "一阵微风轻轻地吹动了树叶。 (Yī zhèn wéifēng qīngqīng de chuīdòngle shùyè.)"
    },
    "she felt a sense of accomplishment after finishing her painting.": {
        "Hindi": "अपनी पेंटिंग खत्म करने के बाद उसे गर्व महसूस हुआ। (Apni painting khatam karne ke baad use garv mehsoos hua.)",
        "Chinese (Simplified)": "完成画作后，她感到了一种成就感。 (Wánchéng huàzuò hòu, tā gǎndàole yī zhǒng chéngjiù gǎn.)"
    },
    "the children built a snowman during the winter break.": {
        "Hindi": "बच्चों ने सर्दियों की छुट्टी में एक स्नोमैन बनाया। (Bachchon ne sardiyon ki chhutti mein ek snowman banaya.)",
        "Chinese (Simplified)": "孩子们在寒假期间堆了一个雪人。 (Háizimen zài hánjià qíjiān duīle yīgè xuěrén.)"
    },
    "the farmer planted seeds in the field at dawn.": {
        "Hindi": "किसान ने सुबह-सुबह खेत में बीज बोए। (Kisaan ne subah-subah khet mein beej boe.)",
        "Chinese (Simplified)": "农民在黎明时在田地里播种。 (Nóngmín zài límíng shí zài tiándì lǐ bōzhǒng.)"
    },
    "she smiled as she read the heartfelt note.": {
        "Hindi": "उसने दिल को छूने वाला नोट पढ़ते समय मुस्कुराई। (Usne dil ko chhoone wala note padhte samay muskurai.)",
        "Chinese (Simplified)": "她读到那封感人的便条时微笑了。 (Tā dú dào nà fēng gǎnrén de biàntiáo shí wéixiàole.)"
    },
    "the stars sparkled brightly in the night sky.": {
        "Hindi": "रात के आसमान में तारे चमक रहे थे। (Raat ke aasman mein taare chamak rahe the.)",
        "Chinese (Simplified)": "夜空中的星星闪闪发光。 (Yèkōng zhōng de xīngxīng shǎnshǎn fāguāng.)"
    },
    "they shared a laugh over an old memory.": {
        "Hindi": "उन्होंने एक पुरानी याद पर हंसकर समय बिताया। (Unhone ek purani yaad par hanskar samay bitaya.)",
        "Chinese (Simplified)": "他们一起回忆旧时光时笑了起来。 (Tāmen yīqǐ huíyì jiù shíguāng shí xiàole qǐlái.)"
    },
    "the museum showcased ancient artifacts from different cultures.": {
        "Hindi": "संग्रहालय ने विभिन्न संस्कृतियों की प्राचीन वस्तुएं प्रदर्शित कीं। (Sangrahalaya ne vibhinn sanskritiyon ki praacheen vastuyein pradarshit keen.)",
        "Chinese (Simplified)": "博物馆展示了来自不同文化的古代文物。 (Bówùguǎn zhǎnshìle láizì bùtóng wénhuà de gǔdài wénwù.)"
    },
    "the chef prepared a delicious meal for the guests.": {
        "Hindi": "शेफ ने मेहमानों के लिए एक स्वादिष्ट भोजन तैयार किया। (Chef ne mehmaanon ke liye ek swaadisht bhojan tayar kiya.)",
        "Chinese (Simplified)": "厨师为客人准备了一顿美味的饭菜。 (Chúshī wèi kèrén zhǔnbèile yī dùn měiwèi de fàncài.)"
    },
    "he took a deep breath before stepping on stage.": {
        "Hindi": "मंच पर कदम रखने से पहले उसने गहरी सांस ली। (Manch par kadam rakhne se pehle usne gahri saans li.)",
        "Chinese (Simplified)": "在上台之前，他深吸了一口气。 (Zài shàngtái zhīqián, tā shēn xīle yī kǒuqì.)"
    },
    "the young girl sang a song that touched everyone’s heart.": {
        "Hindi": "छोटी लड़की ने एक गीत गाया जिसने सबका दिल छू लिया। (Chhoti ladki ne ek geet gaya jisne sabka dil chhoo liya.)",
        "Chinese (Simplified)": "小女孩唱了一首动人的歌，感动了所有人。 (Xiǎo nǚhái chàngle yī shǒu dòngrén de gē, gǎndòngle suǒyǒu rén.)"
    },
    "the scientist made a groundbreaking discovery in her lab.": {
        "Hindi": "वैज्ञानिक ने अपनी प्रयोगशाला में एक क्रांतिकारी खोज की। (Vaigyanik ne apni prayogshala mein ek krantikari khoj ki.)",
        "Chinese (Simplified)": "科学家在她的实验室里有了突破性的发现。 (Kēxuéjiā zài tā de shíyànshì lǐ yǒule tūpò xìng de fāxiàn.)"
    },
    "the little boy dreamed of becoming an astronaut.": {
        "Hindi": "छोटा लड़का एक अंतरिक्ष यात्री बनने का सपना देखता था। (Chhota ladka ek antariksh yatri banne ka sapna dekhta tha.)",
        "Chinese (Simplified)": "小男孩梦想成为一名宇航员。 (Xiǎo nánhái mèngxiǎng chéngwéi yī míng yǔhángyuán.)"
    },
    "the artist sketched a beautiful portrait in just a few minutes.": {
        "Hindi": "कलाकार ने कुछ ही मिनटों में एक सुंदर चित्र बना दिया। (Kalakar ne kuch hi minute mein ek sundar chitra bana diya.)",
        "Chinese (Simplified)": "艺术家在几分钟内画出了一幅美丽的画像。 (Yìshùjiā zài jǐ fēnzhōng nèi huàchūle yī fú měilì de huàxiàng.)"
    },
    "the new park was filled with colorful flowers and tall trees.": {
        "Hindi": "नया पार्क रंग-बिरंगे फूलों और ऊंचे पेड़ों से भरा हुआ था। (Naya park rang-birange phoolon aur oonche pedon se bhara hua tha.)",
        "Chinese (Simplified)": "新公园里满是五彩缤纷的花朵和高大的树木。 (Xīn gōngyuán lǐ mǎn shì wǔcǎi bīnfēn de huāduǒ hé gāodà de shùmù.)"
    },
    "the cat curled up on the couch to take a nap.": {
        "Hindi": "बिल्ली सोफे पर घूम कर आराम से सोने के लिए लेट गई। (Billi sofe par ghoom kar aaram se sone ke liye let gayi.)",
        "Chinese (Simplified)": "猫蜷缩在沙发上打盹。 (Māo quán suō zài shāfā shàng dǎdǔn.)"
    },
    "he gave a heartfelt speech at the graduation ceremony.": {
        "Hindi": "उसने स्नातक समारोह में दिल से एक भाषण दिया। (Usne snatak samaroh mein dil se ek bhashan diya.)",
        "Chinese (Simplified)": "他在毕业典礼上发表了发自内心的演讲。 (Tā zài bìyè diǎnlǐ shàng fābiǎole fā zì nèixīn de yǎnjiǎng.)"
    },
    "the magician amazed the audience with his tricks.": {
        "Hindi": "जादूगर ने अपने जादू से दर्शकों को चौंका दिया। (Jadugar ne apne jaadu se darshako ko chonka diya.)",
        "Chinese (Simplified)": "魔术师用他的把戏让观众惊叹。 (Móshùshī yòng tā de bǎxì ràng guānzhòng jīngtàn.)"
    },
    "the children eagerly waited for the ice cream truck to arrive.": {
        "Hindi": "बच्चे बेसब्री से आइस क्रीम ट्रक के आने का इंतजार कर रहे थे। (Bachche besabri se ice cream truck ke aane ka intezaar kar rahe the.)",
        "Chinese (Simplified)": "孩子们迫不及待地等着冰淇淋车的到来。 (Háizimen pò bù jí dài de děngzhe bīngqílín chē de dào lái.)"
    },
    "the professor explained the complex theory in simple terms.": {
        "Hindi": "प्रोफेसर ने जटिल सिद्धांत को आसान शब्दों में समझाया। (Professor ne jatil siddhant ko aasaan shabdon mein samjhaya.)",
        "Chinese (Simplified)": "教授用简单的术语解释了复杂的理论。 (Jiàoshòu yòng jiǎndān de shùyǔ jiěshìle fùzá de lǐlùn.)"
    },
    "the old man shared stories of his youth with the children.": {
        "Hindi": "बूढ़े आदमी ने बच्चों के साथ अपनी जवानी की कहानियाँ साझा की। (Boodhe aadmi ne bachon ke saath apni jawani ki kahaniyan saanjha ki.)",
        "Chinese (Simplified)": "老人和孩子们分享了他年轻时的故事。 (Lǎorén hé háizimen fēnxiǎngle tā niánqīng shí de gùshì.)"
    },
    "the children ran outside to play as soon as school ended.": {
        "Hindi": "जैसे ही स्कूल खत्म हुआ, बच्चे बाहर खेलने दौड़ पड़े। (Jaise hi school khatam hua, bachche bahar khelne daud pade.)",
        "Chinese (Simplified)": "学校一放学，孩子们就跑出去玩了。 (Xuéxiào yī fàngxué, háizimen jiù pǎo chūqù wánle.)"
    },
    "the author spent years writing the novel before publishing it.": {
        "Hindi": "लेखक ने उपन्यास लिखने में वर्षों बिताए, फिर उसे प्रकाशित किया। (Lekhak ne upanyaas likhne mein varsho bitaye, phir use prakaashit kiya.)",
        "Chinese (Simplified)": "作者花了几年时间写这本小说，然后才出版。 (Zuòzhě huāle jǐ nián shíjiān xiě zhè běn xiǎoshuō, ránhòu cái chūbǎn.)"
    },
    "the chef carefully garnished the dish with fresh herbs.": {
        "Hindi": "शेफ ने डिश को ताजे हर्ब्स से सजा कर पेश किया। (Chef ne dish ko tazey herbs se saza kar pesh kiya.)",
        "Chinese (Simplified)": "厨师小心翼翼地用新鲜香草装饰了菜肴。 (Chúshī xiǎoxīn yìyì de yòng xīnxiān xiāngcǎo zhuāngshìle càiyáo.)"
    },
    "the doctor advised the patient to rest for a few days.": {
        "Hindi": "डॉक्टर ने मरीज को कुछ दिनों तक आराम करने की सलाह दी। (Doctor ne mareez ko kuch dinon tak aaram karne ki salah di.)",
        "Chinese (Simplified)": "医生建议病人休息几天。 (Yīshēng jiànyì bìngrén xiūxí jǐ tiān.)"
    },
    "the storm caused significant damage to the village.": {
        "Hindi": "तूफान ने गांव में भारी नुकसान पहुँचाया। (Toofan ne gaon mein bhaari nuksan pahunchaya.)",
        "Chinese (Simplified)": "暴风雨给村庄带来了严重的破坏。 (Bàofēngyǔ gěi cūnzhuāng dàilái le yánzhòng de pòhuài.)"
    },
    "the teacher explained the math problem step by step.": {
        "Hindi": "शिक्षक ने गणित की समस्या को चरण दर चरण समझाया। (Shikshak ne ganit ki samasya ko charan dar charan samjhaya.)",
        "Chinese (Simplified)": "老师一步一步地解释了数学问题。 (Lǎoshī yī bù yī bù de jiěshìle shùxué wèntí.)"
    },
    "the bird flew gracefully across the sky.": {
        "Hindi": "पक्षी आकाश में सुंदरता से उड़ते हुए गया। (Pakshi aakash mein sundarta se udte hue gaya.)",
        "Chinese (Simplified)": "鸟优雅地飞过了天空。 (Niǎo yōuyǎ de fēiguòle tiānkōng.)"
    },
    "the children sang songs around the campfire.": {
        "Hindi": "बच्चों ने अलाव के चारों ओर गीत गाए। (Bachon ne alav ke chaaron or geet gaaye.)",
        "Chinese (Simplified)": "孩子们围着篝火唱歌。 (Háizimen wéizhe gōuhuǒ chànggē.)"
    },
    "the artist painted a mural on the side of the building.": {
        "Hindi": "कलाकार ने इमारत की दीवार पर एक भित्ति चित्र बनाया। (Kalakar ne imarat ki deewar par ek bhitti chitra banaya.)",
        "Chinese (Simplified)": "艺术家在建筑物的墙面上画了一幅壁画。 (Yìshùjiā zài jiànzhùwù de qiángmiàn shàng huàle yī fú bìhuà.)"
    },
    "the athlete trained every day to improve his skills.": {
        "Hindi": "खिलाड़ी ने अपनी क्षमताओं में सुधार के लिए रोज़ अभ्यास किया। (Khiladi ne apni kshamataon mein sudhaar ke liye roz abhyas kiya.)",
        "Chinese (Simplified)": "运动员每天都训练以提高他的技能。 (Yùndòngyuán měitiān dōu xùnliàn yǐ tígāo tā de jìnéng.)"
    },
    "the children eagerly awaited their turn to perform on stage.": {
        "Hindi": "बच्चे मंच पर प्रदर्शन करने का अपना बारी का बेसब्री से इंतजार कर रहे थे। (Bachche manch par pradarshan karne ka apna baari ka besabri se intezaar kar rahe the.)",
        "Chinese (Simplified)": "孩子们迫不及待地等待轮到他们在舞台上表演。 (Háizimen pò bù jí dài de děngdài lún dào tāmen zài wǔtái shàng biǎoyǎn.)"
    },
    "the city lights twinkled as the night fell.": {
        "Hindi": "रात होने पर शहर की बत्तियाँ चमकने लगीं। (Raat hone par shahar ki battiyaan chamakne lagi.)",
        "Chinese (Simplified)": "夜幕降临时，城市的灯光闪烁。 (Yèmù jiànglín shí, chéngshì de dēngguāng shǎnshuò.)"
    },
    "she danced with grace at the recital.": {
        "Hindi": "वह रचनामंच पर grace के साथ नृत्य कर रही थी। (Vah rachnamanch par grace ke saath nritya kar rahi thi.)",
        "Chinese (Simplified)": "她在音乐会上优雅地跳舞。 (Tā zài yīnyuè huì shàng yōuyǎ de tiàowǔ.)"
    },
    "they enjoyed a peaceful walk along the beach at sunrise.": {
        "Hindi": "उन्होंने सूर्योदय के समय समुद्र तट पर एक शांतिपूर्ण सैर का आनंद लिया। (Unhone suryoday ke samay samundra tat par ek shaantipoorn sair ka anand liya.)",
        "Chinese (Simplified)": "他们在日出时享受了沿海滩的宁静散步。 (Tāmen zài rìchū shí xiǎngshòule yán hǎitān de níngjìng sànbù.)"
    },
    "the dog barked loudly when the stranger approached the house.": {
        "Hindi": "कुत्ता जोर से भौंका जब अजनबी घर के पास आया। (Kutta zor se bhonka jab ajnabi ghar ke paas aaya.)",
        "Chinese (Simplified)": "当陌生人接近房子时，狗大声叫了起来。 (Dāng mòshēngrén jiējìn fángzi shí, gǒu dà shēng jiàole qǐlái.)"
    },
    "he was able to fix the car after a few attempts.": {
        "Hindi": "कुछ प्रयासों के बाद वह कार को ठीक करने में सक्षम था। (Kuch prayaason ke baad vah car ko theek karne mein saksham tha.)",
        "Chinese (Simplified)": "他经过几次尝试后终于修好了车。 (Tā jīngguò jǐ cì chángshì hòu zhōngyú xiū hǎo le chē.)"
    },
    "the sun set behind the mountains, casting a golden glow over the valley.": {
        "Hindi": "सूरज पहाड़ों के पीछे अस्त हो गया, घाटी पर सुनहरा आभा छोड़ता हुआ। (Suraj pahadon ke peeche ast ho gaya, ghaati par sunahra aabha chhodta hua.)",
        "Chinese (Simplified)": "太阳在山后落下，金色的光辉洒在山谷上。 (Tàiyáng zài shān hòu luò xià, jīnsè de guānghuī sǎ zài shāngǔ shàng.)"
    },
    "the crowd cheered as the team scored the winning goal.": {
        "Hindi": "जब टीम ने विजयी गोल किया, तो भीड़ ने उत्साह से जयकारे लगाए। (Jab team ne vijayi goal kiya, to bheed ne utsah se jaykaare lagaye.)",
        "Chinese (Simplified)": "当队伍进了决定胜负的进球时，人群欢呼起来。 (Dāng duìwǔ jìnle juédìng shèngfù de jìnqiú shí, rénqún huānhū qǐlái.)"
    },
    "the singer captivated the audience with her powerful voice.": {
        "Hindi": "गायक ने अपनी मजबूत आवाज से दर्शकों को मंत्रमुग्ध कर दिया। (Gaayak ne apni mazboot awaaz se darshako ko mantramugdh kar diya.)",
        "Chinese (Simplified)": "歌手以她强大的嗓音吸引了观众。 (Gēshǒu yǐ tā qiángdà de sǎngyīn xīyǐnle guānzhòng.)"
    },
    "they enjoyed a delicious meal at the new restaurant.": {
        "Hindi": "उन्होंने नए रेस्तरां में एक स्वादिष्ट भोजन का आनंद लिया। (Unhone naye restoran mein ek swaadisht bhojan ka anand liya.)",
        "Chinese (Simplified)": "他们在新餐厅享用了美味的餐点。 (Tāmen zài xīn cāntīng xiǎngyòngle měiwèi de cāndiǎn.)"
    },
    "the baby giggled as the puppy licked her face.": {
        "Hindi": "बेबी ने हंसी उड़ाई जब पप्पी ने उसका चेहरा चाटा। (Baby ne hansi udaayi jab puppy ne uska chehra chata.)",
        "Chinese (Simplified)": "小宝宝咯咯笑着，刚刚小狗舔了她的脸。 (Xiǎo bǎobǎo gēgē xiàozhe, gānggāng xiǎo gǒu tiǎnle tā de liǎn.)"
    },
    "he carefully organized his study materials before the exam.": {
        "Hindi": "उसने परीक्षा से पहले अपने अध्ययन सामग्री को सावधानीपूर्वक व्यवस्थित किया। (Usne pariksha se pehle apne adhyayan saamagri ko saavdhaanipurvak vyavasthit kiya.)",
        "Chinese (Simplified)": "他在考试前小心地整理了自己的学习资料。 (Tā zài kǎoshì qián xiǎoxīn de zhěnglǐle zìjǐ de xuéxí zīliào.)"
    },
    "the clock struck midnight, signaling the start of the new year.": {
        "Hindi": "घड़ी ने आधी रात को बजाया, नए साल की शुरुआत का संकेत देते हुए। (Ghadi ne aadhi raat ko bajaya, naye saal ki shuruat ka sanket dete hue.)",
        "Chinese (Simplified)": "钟声敲响了午夜，标志着新的一年的开始。 (Zhōngshēng qiāo xiǎngle wǔyè, biāozhìzhe xīn de yī nián de kāishǐ.)"
    },
    "the student worked hard to complete the project on time.": {
        "Hindi": "छात्र ने परियोजना को समय पर पूरा करने के लिए कड़ी मेहनत की। (Chhaatr ne pariyojna ko samay par poora karne ke liye kadi mehnat ki.)",
        "Chinese (Simplified)": "学生努力工作，按时完成了项目。 (Xuéshēng nǔlì gōngzuò, ànshí wánchéngle xiàngmù.)"
    },
    "the artist painted a beautiful landscape on the canvas.": {
        "Hindi": "कलाकार ने कैनवास पर एक सुंदर परिदृश्य चित्रित किया। (Kalaakar ne canvas par ek sundar paridrishya chitrit kiya.)",
        "Chinese (Simplified)": "艺术家在画布上画了一幅美丽的风景。 (Yìshùjiā zài huàbù shàng huàle yī fú měilì de fēngjǐng.)"
    },
    "he made a promise to always be there for his friends.": {
        "Hindi": "उसने अपने दोस्तों के लिए हमेशा वहाँ रहने का वादा किया। (Usne apne doston ke liye hamesha wahan rehne ka wada kiya.)",
        "Chinese (Simplified)": "他承诺永远会在那里支持他的朋友们。 (Tā chéngnuò yǒngyuǎn huì zài nàlǐ zhīchí tā de péngyǒumen.)"
    },
    "the mountain air was fresh and invigorating.": {
        "Hindi": "पहाड़ों की हवा ताजगी और ताजगी से भरी हुई थी। (Pahaadon ki hawa taazgi aur taazgi se bhari hui thi.)",
        "Chinese (Simplified)": "山上的空气新鲜而令人振奋。 (Shān shàng de kōngqì xīnxiān ér lìng rén zhènfèn.)"
    },
    "the children laughed as they played in the park.": {
        "Hindi": "बच्चे हँसते हुए पार्क में खेल रहे थे। (Bachche hanste hue park mein khel rahe the.)",
        "Chinese (Simplified)": "孩子们在公园里玩耍时笑了。 (Háizimen zài gōngyuán lǐ wánshuǎ shí xiàole.)"
    },
    "the scientist made a groundbreaking discovery in his research.": {
        "Hindi": "वैज्ञानिक ने अपने अनुसंधान में एक क्रांतिकारी खोज की। (Vaigyanik ne apne anusandhan mein ek kraantikaari khoj ki.)",
        "Chinese (Simplified)": "科学家在他的研究中做出了重大发现。 (Kēxuéjiā zài tā de yánjiū zhōng zuòchūle zhòngdà fāxiàn.)"
    },
    "the rain created a peaceful ambiance in the forest.": {
        "Hindi": "बारिश ने जंगल में एक शांतिपूर्ण वातावरण उत्पन्न किया। (Baarish ne jangal mein ek shaantipoorn vatavaran utpann kiya.)",
        "Chinese (Simplified)": "雨水在森林中创造了宁静的氛围。 (Yǔshuǐ zài sēnlín zhōng chuàngzàole níngjìng de fēnwéi.)"
    },
    "he enjoys reading books in his free time.": {
        "Hindi": "वह अपने फुर्सत के समय में किताबें पढ़ना पसंद करता है। (Vah apne fursat ke samay mein kitaabein padhna pasand karta hai.)",
        "Chinese (Simplified)": "他喜欢在空闲时间阅读书籍。 (Tā xǐhuān zài kòngxián shíjiān yuèdú shūjí.)"
    },
    "the crowd gathered in excitement for the concert.": {
        "Hindi": "भीड़ कंसर्ट के लिए उत्तेजना के साथ इकट्ठा हुई। (Bheed concert ke liye uttejana ke saath ikattha hui.)",
        "Chinese (Simplified)": "人群激动地聚集在一起等待音乐会。 (Rénqún jīdòng de jùjí zài yīqǐ děngdài yīnyuè huì.)"
    },
    "she found a beautiful seashell on the shore.": {
        "Hindi": "उसने समुद्र के किनारे एक सुंदर शंख पाया। (Usne samundra ke kinare ek sundar shankh paaya.)",
        "Chinese (Simplified)": "她在海岸上找到了一个美丽的贝壳。 (Tā zài hǎi'àn shàng zhǎodàole yīgè měilì de bèiké.)"
    },
    "the chef prepared a delicious meal for the guests.": {
        "Hindi": "शेफ ने मेहमानों के लिए स्वादिष्ट भोजन तैयार किया। (Chef ne mehmanon ke liye swaadisht bhojan taiyar kiya.)",
        "Chinese (Simplified)": "厨师为客人准备了一顿美味的餐点。 (Chúshī wèi kèrén zhǔnbèile yī dùn měiwèi de cāndiǎn.)"
    },
    "the students eagerly awaited their final exam results.": {
        "Hindi": "छात्र अपने अंतिम परीक्षा के परिणाम का बेसब्री से इंतजार कर रहे थे। (Chhaatr apne antim pariksha ke parinaam ka besabri se intezaar kar rahe the.)",
        "Chinese (Simplified)": "学生们迫不及待地等待他们的期末考试结果。 (Xuéshēngmen pò bù jí dài de děngdài tāmen de qīmò kǎoshì jiéguǒ.)"
    },
    "the dog barked loudly at the stranger.": {
        "Hindi": "कुत्ते ने अजनबी पर जोर से भौंका। (Kutte ne ajnabi par zor se bhonka.)",
        "Chinese (Simplified)": "狗对陌生人大声吠叫。 (Gǒu duì mòshēngrén dàshēng fèi jiào.)"
    },
    "they traveled to the mountains for their vacation.": {
        "Hindi": "उन्होंने अपनी छुट्टियों के लिए पहाड़ों की यात्रा की। (Unhone apni chuttiyon ke liye pahaadon ki yatra ki.)",
        "Chinese (Simplified)": "他们为度假去了山区。 (Tāmen wèi dùjià qùle shānqū.)"
    },
    "the movie was filled with thrilling action scenes.": {
        "Hindi": "फिल्म रोमांचक एक्शन दृश्यों से भरी हुई थी। (Film romaanchak action drishyon se bhari hui thi.)",
        "Chinese (Simplified)": "电影充满了令人兴奋的动作场面。 (Diànyǐng chōngmǎnle lìng rén xīngfèn de dòngzuò chǎngmiàn.)"
    },
    "she wore a beautiful red dress to the party.": {
        "Hindi": "उसने पार्टी में एक सुंदर लाल ड्रेस पहनी। (Usne party mein ek sundar laal dress pehni.)",
        "Chinese (Simplified)": "她穿着一件美丽的红色裙子参加派对。 (Tā chuānzhuó yī jiàn měilì de hóngsè qúnzi cānjiā pàiduì.)"
    },
    "the teacher explained the lesson clearly to the students.": {
        "Hindi": "शिक्षक ने छात्रों को पाठ स्पष्ट रूप से समझाया। (Shikshak ne chhaatron ko paath spasht roop se samjhaya.)",
        "Chinese (Simplified)": "老师清楚地向学生们解释了课文。 (Lǎoshī qīngchǔ de xiàng xuéshēngmen jiěshìle kèwén.)"
    },
    "the children built a sandcastle on the beach.": {
        "Hindi": "बच्चों ने समुद्र तट पर एक बालू का किला बनाया। (Bachchon ne samundra tat par ek baalu ka kila banaya.)",
        "Chinese (Simplified)": "孩子们在沙滩上建了一个沙堡。 (Háizimen zài shātān shàng jiànle yīgè shā bǎo.)"
    },
    "the library is a quiet place to study and read.": {
        "Hindi": "पुस्तकालय अध्ययन और पढ़ाई के लिए एक शांतिपूर्ण स्थान है। (Pustakalay adhyayan aur padhai ke liye ek shaantipoorn sthan hai.)",
        "Chinese (Simplified)": "图书馆是一个安静的地方，用来学习和阅读。 (Túshūguǎn shì yīgè ānjìng de dìfāng, yòng lái xuéxí hé yuèdú.)"
    },
    "the farmer harvested the crops at the end of the season.": {
        "Hindi": "किसान ने मौसम के अंत में फसलें काटी। (Kisaan ne mausam ke ant mein fasle kaati.)",
        "Chinese (Simplified)": "农民在季节结束时收获了庄稼。 (Nóngmín zài jìjié jiéshù shí shōuhuòle zhuāngjià.)"
    },
    "the team celebrated their victory with a party.": {
        "Hindi": "टीम ने अपनी जीत का जश्न एक पार्टी के साथ मनाया। (Team ne apni jeet ka jashn ek party ke saath manaya.)",
        "Chinese (Simplified)": "团队通过聚会庆祝他们的胜利。 (Tuánduì tōngguò jùhuì qìngzhù tāmen de shènglì.)"
    },
    "the sun set over the horizon, painting the sky with colors.": {
        "Hindi": "सूरज क्षितिज पर अस्त हो गया, आकाश को रंगों से रंगते हुए। (Suraj kshitij par ast ho gaya, aakash ko rangon se rangte hue.)",
        "Chinese (Simplified)": "太阳在地平线下沉，给天空涂上了颜色。 (Tàiyáng zài dìpíngxiàn xiàchén, gěi tiānkōng tú shàngle yánsè.)"
    },
    "the park is a great place for a morning jog.": {
        "Hindi": "पार्क सुबह की जॉगिंग के लिए एक बेहतरीन जगह है। (Park subah ki jogging ke liye ek behtareen jagah hai.)",
        "Chinese (Simplified)": "公园是晨跑的好地方。 (Gōngyuán shì chén pǎo de hǎo dìfāng.)"
    },
    "the library has a vast collection of books.": {
        "Hindi": "पुस्तकालय में किताबों का विशाल संग्रह है। (Pustakalay mein kitabon ka vishal sangrah hai.)",
        "Chinese (Simplified)": "图书馆有着大量的书籍收藏。 (Túshūguǎn yǒuzhe dàliàng de shūjí shōucáng.)"
    },
    "the mountain trail was steep and challenging.": {
        "Hindi": "पहाड़ की पगडंडी खड़ी और चुनौतीपूर्ण थी। (Pahaad ki pagdandi khadi aur chunautipurn thi.)",
        "Chinese (Simplified)": "山间小径陡峭且具有挑战性。 (Shān jiān xiǎojìng dǒuqiào qiě jùyǒu tiǎozhàn xìng.)"
    },
    "the company launched a new product in the market.": {
        "Hindi": "कंपनी ने बाजार में एक नया उत्पाद लॉन्च किया। (Company ne bazaar mein ek naya utpad launch kiya.)",
        "Chinese (Simplified)": "公司在市场上推出了新产品。 (Gōngsī zài shìchǎng shàng tuīchūle xīn chǎnpǐn.)"
    },
    "the teacher encouraged the students to ask questions.": {
        "Hindi": "शिक्षक ने छात्रों को सवाल पूछने के लिए प्रोत्साहित किया। (Shikshak ne chhaatron ko sawaal poochhne ke liye protsaahit kiya.)",
        "Chinese (Simplified)": "老师鼓励学生们提出问题。 (Lǎoshī gǔlì xuéshēngmen tíchū wèntí.)"
    },
    "the chef garnished the dish with fresh herbs.": {
        "Hindi": "शेफ ने पकवान को ताजे हर्ब्स से सजाया। (Chef ne pakwan ko taaze herbs se sajaya.)",
        "Chinese (Simplified)": "厨师用新鲜的香草装饰了这道菜。 (Chúshī yòng xīnxiān de xiāngcǎo zhuāngshìle zhè dào cài.)"
    },
    "the concert was filled with energetic performances.": {
        "Hindi": "संगीत कार्यक्रम ऊर्जा से भरी हुई प्रस्तुतियों से भरा हुआ था। (Sangeet karyakram oorja se bhari hui prastutiyon se bhara hua tha.)",
        "Chinese (Simplified)": "音乐会充满了充满活力的表演。 (Yīnyuè huì chōngmǎnle chōngmǎn huólì de biǎoyǎn.)"
    },
    "the dog ran after the ball in the yard.": {
        "Hindi": "कुत्ता यार्ड में गेंद के पीछे दौड़ा। (Kutta yard mein gend ke peeche dauda.)",
        "Chinese (Simplified)": "狗在院子里追着球跑。 (Gǒu zài yuànzi lǐ zhuīzhe qiú pǎo.)"
    },
    "she decorated the room with beautiful flowers.": {
        "Hindi": "उसने कमरे को सुंदर फूलों से सजाया। (Usne kamre ko sundar phoolon se sajaya.)",
        "Chinese (Simplified)": "她用美丽的花朵装饰了房间。 (Tā yòng měilì de huāduǒ zhuāngshìle fángjiān.)"
    },
    "the children enjoyed playing in the snow.": {
        "Hindi": "बच्चों ने बर्फ में खेलकर आनंद लिया। (Bachchon ne baraf mein khelkar anand liya.)",
        "Chinese (Simplified)": "孩子们在雪地里玩得很开心。 (Háizimen zài xuědì lǐ wán dé hěn kāixīn.)"
    },
    "the sun rose over the horizon, signaling a new day.": {
        "Hindi": "सूरज क्षितिज पर उगते हुए, एक नए दिन की शुरुआत का संकेत दिया। (Suraj kshitij par ugte hue, ek naye din ki shuruat ka sanket diya.)",
        "Chinese (Simplified)": "太阳从地平线升起，标志着新的一天的到来。 (Tàiyáng cóng dìpíngxiàn shēngqǐ, biāozhìzhe xīn de yītiān de dào lái.)"
    },
    "he fixed the broken chair in no time.": {
        "Hindi": "उसने टूटे हुए कुर्सी को तुरंत ठीक किया। (Usne toote huye kursi ko turant theek kiya.)",
        "Chinese (Simplified)": "他很快修好了坏掉的椅子。 (Tā hěn kuài xiū hǎole huài diào de yǐzi.)"
    },
    "the teacher gave each student a certificate of achievement.": {
        "Hindi": "शिक्षक ने प्रत्येक छात्र को उपलब्धि प्रमाण पत्र दिया। (Shikshak ne pratyek chhaatr ko uplabdhi pramaan patra diya.)",
        "Chinese (Simplified)": "老师给每个学生颁发了成就证书。 (Lǎoshī gěi měi gè xuéshēng bānfāle chéngjiù zhèngshū.)"
    },
    "the couple enjoyed a romantic dinner by the candlelight.": {
        "Hindi": "जोड़े ने मोमबत्ती की रोशनी में एक रोमांटिक डिनर का आनंद लिया। (Jode ne mombatti ki roshni mein ek romantic dinner ka anand liya.)",
        "Chinese (Simplified)": "这对情侣在烛光下享受了浪漫的晚餐。 (Zhè duì qínglǚ zài zhúguāng xià xiǎngshòule làngmàn de wǎncān.)"
    },
    "the city was lit up beautifully for the festival.": {
        "Hindi": "महल त्योहार के लिए खूबसूरती से सजाया गया था। (Mahal tyohar ke liye khoobsurti se sajaya gaya tha.)",
        "Chinese (Simplified)": "城市为节日装饰得美丽动人。 (Chéngshì wèi jiérì zhuāngshì dé měilì dòngrén.)"
    },
    "the weather was perfect for a day at the beach.": {
        "Hindi": "समुद्र तट पर एक दिन बिताने के लिए मौसम बिल्कुल सही था। (Samundra tat par ek din bitane ke liye mausam bilkul sahi tha.)",
        "Chinese (Simplified)": "天气非常适合去海滩度过一天。 (Tiānqì fēicháng shìhé qù hǎitān dùguò yītiān.)"
    },
    "she painted the fence with a fresh coat of white paint.": {
        "Hindi": "उसने बाड़ को सफेद रंग की ताजा कोट से रंगा। (Usne baad ko safed rang ki taaza coat se ranga.)",
        "Chinese (Simplified)": "她给篱笆刷上了一层新的白漆。 (Tā gěi líbā shuā shàngle yī céng xīn de bái qī.)"
    },
    "the fisherman cast his net into the sea.": {
        "Hindi": "मछुआरे ने अपना जाल समुद्र में फेंका। (Machhuaare ne apna jaal samundra mein phenka.)",
        "Chinese (Simplified)": "渔夫把他的网撒进了大海。 (Yúfū bǎ tā de wǎng sā jìnle dàhǎi.)"
    },
    "the airplane soared high above the clouds.": {
        "Hindi": "विमान बादलों के ऊपर ऊँचाई पर उड़ रहा था। (Vimaan baadlon ke upar unchaai par ud raha tha.)",
        "Chinese (Simplified)": "飞机飞得高高的，穿越了云层。 (Fēijī fēi dé gāo gāo de, chuānyuèle yúncéng.)"
    },
    "the scientist studied the effects of climate change on the environment.": {
        "Hindi": "वैज्ञानिक ने पर्यावरण पर जलवायु परिवर्तन के प्रभाव का अध्ययन किया। (Vaigyanik ne paryavaran par jalvayu parivartan ke prabhav ka adhyayan kiya.)",
        "Chinese (Simplified)": "科学家研究了气候变化对环境的影响。 (Kēxuéjiā yánjiūle qìhòu biànhuà duì huánjìng de yǐngxiǎng.)"
    },
    "the couple walked hand in hand along the beach.": {
        "Hindi": "जोड़े समुद्र तट पर हाथ में हाथ डालकर चल रहे थे। (Jode samundra tat par haath mein haath daalkar chal rahe the.)",
        "Chinese (Simplified)": "这对情侣手牵着手沿着海滩走。 (Zhè duì qínglǚ shǒu qiānzhe shǒu yánzhe hǎitān zǒu.)"
    },
    "the car broke down in the middle of the road.": {
        "Hindi": "गाड़ी सड़क के बीच में खराब हो गई। (Gaadi sadak ke beech mein kharaab ho gayi.)",
        "Chinese (Simplified)": "汽车在路中间抛锚了。 (Qìchē zài lù zhōngjiān pāo mánle.)"
    },
    "the artist created a masterpiece that everyone admired.": {
        "Hindi": "कलाकार ने एक उत्कृष्ट कृति बनाई जिसे सभी ने सराहा। (Kalaakar ne ek utkrsht kruti banayi jise sabhi ne saraha.)",
        "Chinese (Simplified)": "艺术家创作了一部大家都钦佩的杰作。 (Yìshùjiā chuàngzuòle yī bù dàjiā dōu qīnpèi de jiézuò.)"
    },
    "the train arrived on time at the station.": {
        "Hindi": "ट्रेन स्टेशन पर समय पर पहुंची। (Train station par samay par pahunchi.)",
        "Chinese (Simplified)": "火车准时到达了车站。 (Huǒchē zhǔnshí dàodále chēzhàn.)"
    },
    "the children laughed and played in the park.": {
        "Hindi": "बच्चे पार्क में हंसी-मज़ाक कर रहे थे। (Bachche park mein hansi-mazaak kar rahe the.)",
        "Chinese (Simplified)": "孩子们在公园里欢笑玩耍。 (Háizimen zài gōngyuán lǐ huānxiào wánshuǎ.)"
    },
    "he solved the complex problem in no time.": {
        "Hindi": "उसने जटिल समस्या को तुरंत हल कर दिया। (Usne jatil samasya ko turant hal kar diya.)",
        "Chinese (Simplified)": "他很快解决了复杂的问题。 (Tā hěn kuài jiějuéle fùzá de wèntí.)"
    },
    "she gave an insightful speech at the conference.": {
        "Hindi": "उसने सम्मेलन में एक सूझबूझ भरी भाषण दी। (Usne sammelan mein ek soojhboojh bhari bhashan di.)",
        "Chinese (Simplified)": "她在会议上做了一个富有洞察力的演讲。 (Tā zài huìyì shàng zuòle yīgè fùyǒu dòngchálì de yǎnjiǎng.)"
    },
    "the children decorated the Christmas tree with colorful lights.": {
        "Hindi": "बच्चों ने क्रिसमस के पेड़ को रंगीन बत्तियों से सजाया। (Bachchon ne Christmas ke ped ko rangeen battion se sajaya.)",
        "Chinese (Simplified)": "孩子们用五彩缤纷的灯饰装饰了圣诞树。 (Háizimen yòng wǔcǎi bīnfēn de dēngshì zhuāngshìle shèngdàn shù.)"
    },
    "the rain stopped, and the sun came out.": {
        "Hindi": "बारिश रुक गई, और सूरज निकल आया। (Barish ruk gayi, aur suraj nikal aaya.)",
        "Chinese (Simplified)": "雨停了，太阳出来了。 (Yǔ tíngle, tàiyáng chūláile.)"
    },
    "the book was filled with interesting facts and stories.": {
        "Hindi": "किताब दिलचस्प तथ्यों और कहानियों से भरी हुई थी। (Kitaab dilchasp tathyon aur kahaniyon se bhari hui thi.)",
        "Chinese (Simplified)": "这本书充满了有趣的事实和故事。 (Zhè běn shū chōngmǎnle yǒuqù de shìshí hé gùshì.)"
    },
    "the cat curled up on the couch and fell asleep.": {
        "Hindi": "बिल्ली सोफे पर लिपटी और सो गई। (Billi sofe par lipti aur so gayi.)",
        "Chinese (Simplified)": "猫蜷缩在沙发上，睡着了。 (Māo quán suō zài shāfā shàng, shuìzhele.)"
    },
    "the athlete broke the record with an incredible performance.": {
        "Hindi": "एथलीट ने एक अद्वितीय प्रदर्शन के साथ रिकॉर्ड तोड़ा। (Athlete ne ek advitiya pradarshan ke saath record toda.)",
        "Chinese (Simplified)": "运动员凭借出色的表现打破了记录。 (Yùndòngyuán píngjiè chūsè de biǎoxiàn dǎpòle jìlù.)"
    },
    "the room was filled with the sweet aroma of freshly baked cookies.": {
        "Hindi": "कमरा ताजे बेक्ड कुकीज की मीठी खुशबू से भर गया था। (Kamra taze baked cookies ki meethi khushboo se bhar gaya tha.)",
        "Chinese (Simplified)": "房间里弥漫着新鲜烤制的饼干的甜香味。 (Fángjiān lǐ mímànzhe xīnxiān kǎo zhì de bǐnggān de tián xiāngwèi.)"
    },
    "she has a talent for playing musical instruments.": {
        "Hindi": "उसके पास संगीत वाद्ययंत्र बजाने का कौशल है। (Uske paas sangeet vaadyayantra bajane ka kaushal hai.)",
        "Chinese (Simplified)": "她有演奏乐器的天赋。 (Tā yǒu yǎnzòu yuèqì de tiānfù.)"
    },
    "the city was buzzing with excitement during the festival.": {
        "Hindi": "त्योहार के दौरान शहर रोमांच से गूंज रहा था। (Tyohar ke dauran shehar romanch se goonj raha tha.)",
        "Chinese (Simplified)": "在节日期间，城市充满了兴奋的气氛。 (Zài jiérì qījiān, chéngshì chōngmǎnle xīngfèn de qìfēn.)"
    },
    "the chef prepared a delicious meal for the guests.": {
        "Hindi": "शेफ ने मेहमानों के लिए स्वादिष्ट भोजन तैयार किया। (Chef ne mehmano ke liye swaadisht bhojan tayar kiya.)",
        "Chinese (Simplified)": "厨师为客人准备了美味的餐点。 (Chúshī wèi kèrén zhǔnbèile měiwèi de cāndiǎn.)"
    },
    "the sunset painted the sky with beautiful colors.": {
        "Hindi": "सूर्यास्त ने आकाश को सुंदर रंगों से रंग दिया। (Suryasta ne aakash ko sundar rangon se rang diya.)",
        "Chinese (Simplified)": "夕阳将天空染上了美丽的色彩。 (Xīyáng jiāng tiānkōng rǎn shàngle měilì de sècǎi.)"
    },
    "the student asked a thoughtful question during the lecture.": {
        "Hindi": "छात्र ने व्याख्यान के दौरान एक विचारशील प्रश्न पूछा। (Chhatr ne vyakhyan ke dauran ek vicharshil prashna poocha.)",
        "Chinese (Simplified)": "学生在讲座中提出了一个深思熟虑的问题。 (Xuéshēng zài jiǎngzuò zhōng tíchūle yīgè shēn sī shú lǜ de wèntí.)"
    },
    "the bird flew gracefully across the sky.": {
        "Hindi": "पक्षी आकाश में सुंदरता से उड़ते हुए गया। (Pakshi aakash mein sundarta se udte hue gaya.)",
        "Chinese (Simplified)": "鸟优雅地飞过天空。 (Niǎo yōuyǎ de fēiguò tiānkōng.)"
    },
    "she was filled with joy after hearing the good news.": {
        "Hindi": "उसे खुशखबरी सुनकर खुशी से भर गई। (Use khushkhabri sunkar khushi se bhar gayi.)",
        "Chinese (Simplified)": "她听到好消息后充满了喜悦。 (Tā tīngdào hǎo xiāoxī hòu chōngmǎnle xǐyuè.)"
    },
    "the mountain hike was both challenging and rewarding.": {
        "Hindi": "पहाड़ की चढ़ाई चुनौतीपूर्ण और संतोषजनक थी। (Pahaad ki chadhai chunautipurn aur santoshjanak thi.)",
        "Chinese (Simplified)": "登山既具有挑战性又充满了回报。 (Dēngshān jì jùyǒu tiǎozhàn xìng yòu chōngmǎnle huíbào.)"
    },
    "he wore a bright red shirt to the party.": {
        "Hindi": "उसने पार्टी में एक चमकदार लाल शर्ट पहनी। (Usne party mein ek chamakdaar laal shirt pehni.)",
        "Chinese (Simplified)": "他穿了一件鲜红色的衬衫去参加聚会。 (Tā chuānle yī jiàn xiān hóng sè de chènshān qù cānjiā jùhuì.)"
    },
    "the moonlight reflected off the surface of the lake.": {
        "Hindi": "चाँदनी झील की सतह पर परिलक्षित हो रही थी। (Chaandani jheel ki satah par parilakshit ho rahi thi.)",
        "Chinese (Simplified)": "月光照在湖面上。 (Yuèguāng zhào zài hùmiàn shàng.)"
    },
    "the flowers in the garden bloomed beautifully in spring.": {
        "Hindi": "गार्डन में फूल वसंत में सुंदरता से खिले। (Garden mein phool vasant mein sundarta se khile.)",
        "Chinese (Simplified)": "花园里的花在春天盛开得很美丽。 (Huāyuán lǐ de huā zài chūntiān shèngkāi dé hěn měilì.)"
    },
    "they traveled across the country to visit their family.": {
        "Hindi": "उन्होंने अपने परिवार से मिलने के लिए पूरे देश में यात्रा की। (Unhone apne parivaar se milne ke liye poore desh mein yatra ki.)",
        "Chinese (Simplified)": "他们穿越全国去拜访家人。 (Tāmen chuānyuè quánguó qù bàifǎng jiārén.)"
    },
    "the scientist made a groundbreaking discovery in the lab.": {
        "Hindi": "वैज्ञानिक ने प्रयोगशाला में एक क्रांतिकारी खोज की। (Vaigyanik ne prayogshala mein ek krantikari khoj ki.)",
        "Chinese (Simplified)": "科学家在实验室做出了突破性的发现。 (Kēxuéjiā zài shíyànshì zuòchūle tūpò xìng de fāxiàn.)"
    },
    "the book was so captivating that I couldn't put it down.": {
        "Hindi": "किताब इतनी दिलचस्प थी कि मैं उसे छोड़ नहीं सका। (Kitaab itni dilchasp thi ki main use chhod nahi saka.)",
        "Chinese (Simplified)": "这本书非常吸引人，我无法放下它。 (Zhè běn shū fēicháng xīyǐn rén, wǒ wúfǎ fàngxià tā.)"
    },
    "the children were excited to go on their first field trip.": {
        "Hindi": "बच्चे अपनी पहली फील्ड ट्रिप पर जाने के लिए उत्साहित थे। (Bachche apni pehli field trip par jaane ke liye utsahit the.)",
        "Chinese (Simplified)": "孩子们兴奋地准备去他们的第一次实地考察。 (Háizimen xīngfèn de zhǔnbèi qù tāmen de dì yī cì shídì kǎochá.)"
    },
    "the party was a huge success with everyone dancing and laughing.": {
        "Hindi": "पार्टी एक बड़ी सफलता रही, सभी लोग नाच रहे थे और हंसी मजाक कर रहे थे। (Party ek badi safalta rahi, sabhi log naach rahe the aur hansi mazaak kar rahe the.)",
        "Chinese (Simplified)": "派对非常成功，大家都在跳舞和笑声中度过。 (Pàiduì fēicháng chénggōng, dàjiā dōu zài tiàowǔ hé xiàoshēng zhōng dùguò.)"
    },
    "she loves to read books about adventure and exploration.": {
        "Hindi": "वह साहसिकता और अन्वेषण पर आधारित किताबें पढ़ना पसंद करती है। (Woh saahasikta aur anveshan par aadharit kitaabein padhna pasand karti hai.)",
        "Chinese (Simplified)": "她喜欢阅读关于冒险和探索的书籍。 (Tā xǐhuān yuèdú guānyú màoxiǎn hé tànsuǒ de shūjí.)"
    },
    "the ocean was calm and peaceful, with the waves gently lapping the shore.": {
        "Hindi": "समुद्र शांत और शांतिपूर्ण था, लहरें धीरे-धीरे किनारे से टकरा रही थीं। (Samudra shaant aur shaantipoorn tha, lahrain dheere-dheere kinare se takra rahi thin.)",
        "Chinese (Simplified)": "海洋平静而宁静，海浪轻轻拍打着海岸。 (Hǎiyáng píngjìng ér níngjìng, hǎilàng qīngqīng pāi dǎzhe hǎi'àn.)"
    },
    "he runs fast.": {
        "Hindi": "वह तेज दौड़ता है। (Vah tez daudta hai.)",
        "Chinese (Simplified)": "他跑得很快。 (Tā pǎo dé hěn kuài.)"
    },
    "she is reading a book.": {
        "Hindi": "वह एक किताब पढ़ रही है। (Vah ek kitaab padh rahi hai.)",
        "Chinese (Simplified)": "她在读一本书。 (Tā zài dú yī běn shū.)"
    },
    "it is raining today.": {
        "Hindi": "आज बारिश हो रही है। (Aaj baarish ho rahi hai.)",
        "Chinese (Simplified)": "今天下雨。 (Jīntiān xià yǔ.)"
    },
    "he is my friend.": {
        "Hindi": "वह मेरा दोस्त है। (Vah mera dost hai.)",
        "Chinese (Simplified)": "他是我的朋友。 (Tā shì wǒ de péngyǒu.)"
    },
    "I like pizza.": {
        "Hindi": "मुझे पिज़्ज़ा पसंद है। (Mujhe pizza pasand hai.)",
        "Chinese (Simplified)": "我喜欢披萨。 (Wǒ xǐhuān pīsà.)"
    },
    "the sun is shining.": {
        "Hindi": "सूरज चमक रहा है। (Suraj chamak raha hai.)",
        "Chinese (Simplified)": "太阳在照耀。 (Tàiyáng zài zhàoyào.)"
    },
    "she sings beautifully.": {
        "Hindi": "वह सुंदर गाती है। (Vah sundar gaati hai.)",
        "Chinese (Simplified)": "她唱得很美。 (Tā chàng dé hěn měi.)"
    },
    "the cat is sleeping.": {
        "Hindi": "बिल्ली सो रही है। (Billi so rahi hai.)",
        "Chinese (Simplified)": "猫正在睡觉。 (Māo zhèngzài shuìjiào.)"
    },
    "he is tall.": {
        "Hindi": "वह लंबा है। (Vah lamba hai.)",
        "Chinese (Simplified)": "他很高。 (Tā hěn gāo.)"
    },
    "I am hungry.": {
        "Hindi": "मुझे भूख लगी है। (Mujhe bhukh lagi hai.)",
        "Chinese (Simplified)": "我饿了。 (Wǒ è le.)"
    },
    "it is a gift.": {
        "Hindi": "यह एक उपहार है। (Yeh ek uphaar hai.)",
        "Chinese (Simplified)": "这是一个礼物。 (Zhè shì yīgè lǐwù.)"
    },
    "she has a dog.": {
        "Hindi": "उसके पास एक कुत्ता है। (Uske paas ek kutta hai.)",
        "Chinese (Simplified)": "她有一只狗。 (Tā yǒu yī zhī gǒu.)"
    },
    "he is playing.": {
        "Hindi": "वह खेल रहा है। (Vah khel raha hai.)",
        "Chinese (Simplified)": "他在玩。 (Tā zài wán.)"
    },
    "the door is open.": {
        "Hindi": "दरवाजा खुला है। (Darwaza khula hai.)",
        "Chinese (Simplified)": "门是开着的。 (Mén shì kāizhe de.)"
    },
    "I am learning.": {
        "Hindi": "मैं सीख रहा हूँ। (Main seekh raha hoon.)",
        "Chinese (Simplified)": "我在学习。 (Wǒ zài xuéxí.)"
    },
    "she is happy.": {
        "Hindi": "वह खुश है। (Vah khush hai.)",
        "Chinese (Simplified)": "她很高兴。 (Tā hěn gāoxìng.)"
    },
    "the dog is barking.": {
        "Hindi": "कुत्ता भौंक रहा है। (Kutta bhonk raha hai.)",
        "Chinese (Simplified)": "狗在叫。 (Gǒu zài jiào.)"
    },
    "I am tired.": {
        "Hindi": "मैं थका हुआ हूँ। (Main thaka hua hoon.)",
        "Chinese (Simplified)": "我累了。 (Wǒ lèi le.)"
    },
    "he is running.": {
        "Hindi": "वह दौड़ रहा है। (Vah daud raha hai.)",
        "Chinese (Simplified)": "他在跑。 (Tā zài pǎo.)"
    },
    "this is mine.": {
        "Hindi": "यह मेरा है। (Yeh mera hai.)",
        "Chinese (Simplified)": "这是我的。 (Zhè shì wǒ de.)"
    },
    "I am busy.": {
        "Hindi": "मैं व्यस्त हूँ। (Main vyast hoon.)",
        "Chinese (Simplified)": "我很忙。 (Wǒ hěn máng.)"
    },
    "she is tall.": {
        "Hindi": "वह लंबी है। (Vah lambi hai.)",
        "Chinese (Simplified)": "她很高。 (Tā hěn gāo.)"
    },
    "he is sleeping.": {
        "Hindi": "वह सो रहा है। (Vah so raha hai.)",
        "Chinese (Simplified)": "他在睡觉。 (Tā zài shuìjiào.)"
    },
    "the book is new.": {
        "Hindi": "किताब नई है। (Kitaab nai hai.)",
        "Chinese (Simplified)": "这本书是新的。 (Zhè běn shū shì xīn de.)"
    },
    "it is cold.": {
        "Hindi": "यह ठंडा है। (Yeh thanda hai.)",
        "Chinese (Simplified)": "天气很冷。 (Tiānqì hěn lěng.)"
    },
    "they are friends.": {
        "Hindi": "वे दोस्त हैं। (Ve dost hain.)",
        "Chinese (Simplified)": "他们是朋友。 (Tāmen shì péngyǒu.)"
    },
    "I am learning Python.": {
        "Hindi": "मैं पायथन सीख रहा हूँ। (Main Python seekh raha hoon.)",
        "Chinese (Simplified)": "我在学习Python。 (Wǒ zài xuéxí Python.)"
    },
    "the sky is blue.": {
        "Hindi": "आसमान नीला है। (Aasmaan neela hai.)",
        "Chinese (Simplified)": "天空是蓝色的。 (Tiānkōng shì lán sè de.)"
    },
    "it is a pen.": {
        "Hindi": "यह एक पेन है। (Yeh ek pen hai.)",
        "Chinese (Simplified)": "这是一支笔。 (Zhè shì yī zhī bǐ.)"
    },
    "i am happy.": {
        "Hindi": "मैं खुश हूँ। (Main khush hoon.)",
        "Chinese (Simplified)": "我很高兴。 (Wǒ hěn gāoxìng.)"
    },
    "she loves animals.": {
        "Hindi": "वह जानवरों से प्यार करती है। (Vah janwaron se pyaar karti hai.)",
        "Chinese (Simplified)": "她喜欢动物。 (Tā xǐhuān dòngwù.)"
    },
    "he is a teacher.": {
        "Hindi": "वह एक शिक्षक है। (Vah ek shikshak hai.)",
        "Chinese (Simplified)": "他是一个老师。 (Tā shì yīgè lǎoshī.)"
    },
    "i have a car.": {
        "Hindi": "मेरे पास एक कार है। (Mere paas ek car hai.)",
        "Chinese (Simplified)": "我有一辆车。 (Wǒ yǒu yī liàng chē.)"
    },
    "this is easy.": {
        "Hindi": "यह आसान है। (Yeh aasan hai.)",
        "Chinese (Simplified)": "这很容易。 (Zhè hěn róngyì.)"
    },
    "the coffee is hot.": {
        "Hindi": "कॉफ़ी गरम है। (Coffee garam hai.)",
        "Chinese (Simplified)": "咖啡很热。 (Kāfēi hěn rè.)"
    },
    "she is smiling.": {
        "Hindi": "वह मुस्करा रही है। (Vah muskara rahi hai.)",
        "Chinese (Simplified)": "她在微笑。 (Tā zài wēixiào.)"
    },
    "i like movies.": {
        "Hindi": "मुझे फिल्में पसंद हैं। (Mujhe filmein pasand hain.)",
        "Chinese (Simplified)": "我喜欢电影。 (Wǒ xǐhuān diànyǐng.)"
    },
    "he is playing football.": {
        "Hindi": "वह फुटबॉल खेल रहा है। (Vah football khel raha hai.)",
        "Chinese (Simplified)": "他在踢足球。 (Tā zài tī zúqiú.)"
    },
    "they are singing.": {
        "Hindi": "वे गा रहे हैं। (Ve ga rahe hain.)",
        "Chinese (Simplified)": "他们在唱歌。 (Tāmen zài chànggē.)"
    },
    "i am learning English.": {
        "Hindi": "मैं अंग्रेजी सीख रहा हूँ। (Main angrezi seekh raha hoon.)",
        "Chinese (Simplified)": "我在学习英语。 (Wǒ zài xuéxí yīngyǔ.)"
    },
    "it is a dog.": {
        "Hindi": "यह एक कुत्ता है। (Yeh ek kutta hai.)",
        "Chinese (Simplified)": "这是一只狗。 (Zhè shì yī zhī gǒu.)"
    },
    "he is tall and strong.": {
        "Hindi": "वह लंबा और मजबूत है। (Vah lamba aur majboot hai.)",
        "Chinese (Simplified)": "他又高又强壮。 (Tā yòu gāo yòu qiángzhuàng.)"
    },
    "she is reading a story.": {
        "Hindi": "वह एक कहानी पढ़ रही है। (Vah ek kahani padh rahi hai.)",
        "Chinese (Simplified)": "她在读一个故事。 (Tā zài dú yīgè gùshì.)"
    },
    "the book is interesting.": {
        "Hindi": "किताब दिलचस्प है। (Kitaab dilchasp hai.)",
        "Chinese (Simplified)": "这本书很有趣。 (Zhè běn shū hěn yǒuqù.)"
    },
    "he is always helpful.": {
        "Hindi": "वह हमेशा मददगार रहता है। (Vah hamesha madadgaar rehta hai.)",
        "Chinese (Simplified)": "他总是乐于助人。 (Tā zǒng shì lè yú zhùrén.)"
    },
    "i am thirsty.": {
        "Hindi": "मुझे प्यास लगी है। (Mujhe pyaas lagi hai.)",
        "Chinese (Simplified)": "我渴了。 (Wǒ kě le.)"
    },
    "the sun is shining.": {
        "Hindi": "सूरज चमक रहा है। (Suraj chamak raha hai.)",
        "Chinese (Simplified)": "太阳在照耀。 (Tàiyáng zài zhàoyào.)"
    },
    "she is my friend.": {
        "Hindi": "वह मेरी दोस्त है। (Vah meri dost hai.)",
        "Chinese (Simplified)": "她是我的朋友。 (Tā shì wǒ de péngyǒu.)"
    },
    "it is raining.": {
        "Hindi": "बारिश हो रही है। (Barish ho rahi hai.)",
        "Chinese (Simplified)": "在下雨。 (Zài xiàyǔ.)"
    },
    "he is busy.": {
        "Hindi": "वह व्यस्त है। (Vah vyast hai.)",
        "Chinese (Simplified)": "他很忙。 (Tā hěn máng.)"
    },
    "she likes chocolate.": {
        "Hindi": "वह चॉकलेट पसंद करती है। (Vah chocolate pasand karti hai.)",
        "Chinese (Simplified)": "她喜欢巧克力。 (Tā xǐhuān qiǎokèlì.)"
    },
    "I am learning to swim.": {
        "Hindi": "मैं तैरना सीख रहा हूँ। (Main tairna seekh raha hoon.)",
        "Chinese (Simplified)": "我在学游泳。 (Wǒ zài xué yóuyǒng.)"
    },
    "this is my house.": {
        "Hindi": "यह मेरा घर है। (Yeh mera ghar hai.)",
        "Chinese (Simplified)": "这是我的家。 (Zhè shì wǒ de jiā.)"
    },
    "the food is delicious.": {
        "Hindi": "खाना स्वादिष्ट है। (Khana swadisht hai.)",
        "Chinese (Simplified)": "食物很美味。 (Shíwù hěn měiwèi.)"
    },
    "I love music.": {
        "Hindi": "मुझे संगीत पसंद है। (Mujhe sangeet pasand hai.)",
        "Chinese (Simplified)": "我喜欢音乐。 (Wǒ xǐhuān yīnyuè.)"
    },
    "he is reading a book.": {
        "Hindi": "वह एक किताब पढ़ रहा है। (Vah ek kitaab padh raha hai.)",
        "Chinese (Simplified)": "他在读一本书。 (Tā zài dú yī běn shū.)"
    },
    "they are laughing.": {
        "Hindi": "वे हंस रहे हैं। (Ve hans rahe hain.)",
        "Chinese (Simplified)": "他们在笑。 (Tāmen zài xiào.)"
    },
    "I am going to the market.": {
        "Hindi": "मैं बाजार जा रहा हूँ। (Main bazaar ja raha hoon.)",
        "Chinese (Simplified)": "我去市场。 (Wǒ qù shìchǎng.)"
    },
    "it is a beautiful day.": {
        "Hindi": "यह एक सुंदर दिन है। (Yeh ek sundar din hai.)",
        "Chinese (Simplified)": "今天是美好的一天。 (Jīntiān shì měihǎo de yītiān.)"
    },
    "I have a question.": {
        "Hindi": "मेरे पास एक सवाल है। (Mere paas ek sawaal hai.)",
        "Chinese (Simplified)": "我有一个问题。 (Wǒ yǒu yīgè wèntí.)"
    },
    "this is my book.": {
        "Hindi": "यह मेरी किताब है। (Yeh meri kitaab hai.)",
        "Chinese (Simplified)": "这是我的书。 (Zhè shì wǒ de shū.)"
    },
    "I like to run.": {
        "Hindi": "मुझे दौड़ना पसंद है। (Mujhe daudna pasand hai.)",
        "Chinese (Simplified)": "我喜欢跑步。 (Wǒ xǐhuān pǎobù.)"
    },
    "he is a good singer.": {
        "Hindi": "वह एक अच्छा गायक है। (Vah ek accha gaayak hai.)",
        "Chinese (Simplified)": "他是个好歌手。 (Tā shì gè hǎo gēshǒu.)"
    },
    "she loves the rain.": {
        "Hindi": "वह बारिश को पसंद करती है। (Vah baarish ko pasand karti hai.)",
        "Chinese (Simplified)": "她喜欢雨。 (Tā xǐhuān yǔ.)"
    },
    "the cake is sweet.": {
        "Hindi": "केक मीठा है। (Cake meetha hai.)",
        "Chinese (Simplified)": "蛋糕很甜。 (Dàngāo hěn tián.)"
    },
    "it is too hot today.": {
        "Hindi": "आज बहुत गर्म है। (Aaj bahut garm hai.)",
        "Chinese (Simplified)": "今天太热了。 (Jīntiān tài rè le.)"
    },
    "I am feeling happy.": {
        "Hindi": "मैं खुश महसूस कर रहा हूँ। (Main khush mehsoos kar raha hoon.)",
        "Chinese (Simplified)": "我感觉很高兴。 (Wǒ gǎnjué hěn gāoxìng.)"
    },
    "he is my brother.": {
        "Hindi": "वह मेरा भाई है। (Vah mera bhai hai.)",
        "Chinese (Simplified)": "他是我的兄弟。 (Tā shì wǒ de xiōngdì.)"
    },
    "she is very kind.": {
        "Hindi": "वह बहुत दयालु है। (Vah bahut dayalu hai.)",
        "Chinese (Simplified)": "她非常善良。 (Tā fēicháng shànliáng.)"
    },
    "I love to dance.": {
        "Hindi": "मुझे नृत्य करना पसंद है। (Mujhe nritya karna pasand hai.)",
        "Chinese (Simplified)": "我喜欢跳舞。 (Wǒ xǐhuān tiàowǔ.)"
    },
    "he is always punctual.": {
        "Hindi": "वह हमेशा समय पर रहता है। (Vah hamesha samay par rehta hai.)",
        "Chinese (Simplified)": "他总是准时。 (Tā zǒng shì zhǔnshí.)"
    },
    "she has a cat.": {
        "Hindi": "उसके पास एक बिल्ली है। (Uske paas ek billi hai.)",
        "Chinese (Simplified)": "她有一只猫。 (Tā yǒu yī zhī māo.)"
    },
    "I enjoy reading books.": {
        "Hindi": "मुझे किताबें पढ़ना पसंद है। (Mujhe kitaabein padhna pasand hai.)",
        "Chinese (Simplified)": "我喜欢读书。 (Wǒ xǐhuān dúshū.)"
    },
    "this is my phone.": {
        "Hindi": "यह मेरा फोन है। (Yeh mera phone hai.)",
        "Chinese (Simplified)": "这是我的手机。 (Zhè shì wǒ de shǒujī.)"
    },
    "he is an engineer.": {
        "Hindi": "वह एक इंजीनियर है। (Vah ek engineer hai.)",
        "Chinese (Simplified)": "他是一个工程师。 (Tā shì yīgè gōngchéngshī.)"
    },
    "the book is interesting.": {
        "Hindi": "किताब दिलचस्प है। (Kitaab dilchasp hai.)",
        "Chinese (Simplified)": "这本书很有趣。 (Zhè běn shū hěn yǒuqù.)"
    },
    "i like ice cream.": {
        "Hindi": "मुझे आइस क्रीम पसंद है। (Mujhe ice cream pasand hai.)",
        "Chinese (Simplified)": "我喜欢冰淇淋。 (Wǒ xǐhuān bīngqílín.)"
    },
    "the cat is sleeping.": {
        "Hindi": "बिल्ली सो रही है। (Billi so rahi hai.)",
        "Chinese (Simplified)": "猫在睡觉。 (Māo zài shuìjiào.)"
    },
    "she is very smart.": {
        "Hindi": "वह बहुत स्मार्ट है। (Vah bahut smart hai.)",
        "Chinese (Simplified)": "她非常聪明。 (Tā fēicháng cōngmíng.)"
    },
    "it is a sunny day.": {
        "Hindi": "आज एक धूप वाला दिन है। (Aaj ek dhoop wala din hai.)",
        "Chinese (Simplified)": "今天是晴天。 (Jīntiān shì qíngtiān.)"
    },
    "i enjoy listening to music.": {
        "Hindi": "मुझे संगीत सुनना पसंद है। (Mujhe sangeet sunna pasand hai.)",
        "Chinese (Simplified)": "我喜欢听音乐。 (Wǒ xǐhuān tīng yīnyuè.)"
    },
    "he is a good cook.": {
        "Hindi": "वह एक अच्छा रसोइया है। (Vah ek accha rasoiya hai.)",
        "Chinese (Simplified)": "他是个好厨师。 (Tā shì gè hǎo chúshī.)"
    },
    "she is my teacher.": {
        "Hindi": "वह मेरी शिक्षिका है। (Vah meri shikshika hai.)",
        "Chinese (Simplified)": "她是我的老师。 (Tā shì wǒ de lǎoshī.)"
    },
    "i have a new phone.": {
        "Hindi": "मेरे पास एक नया फोन है। (Mere paas ek naya phone hai.)",
        "Chinese (Simplified)": "我有一部新手机。 (Wǒ yǒu yī bù xīn shǒujī.)"
    },
    "the movie was exciting.": {
        "Hindi": "फिल्म रोमांचक थी। (Film romanchak thi.)",
        "Chinese (Simplified)": "这部电影很刺激。 (Zhè bù diànyǐng hěn cìjī.)"
    },
    "i like playing soccer.": {
        "Hindi": "मुझे फुटबॉल खेलना पसंद है। (Mujhe football khelna pasand hai.)",
        "Chinese (Simplified)": "我喜欢踢足球。 (Wǒ xǐhuān tī zúqiú.)"
    },
    "he is my friend.": {
        "Hindi": "वह मेरा दोस्त है। (Vah mera dost hai.)",
        "Chinese (Simplified)": "他是我的朋友。 (Tā shì wǒ de péngyǒu.)"
    },
    "it is my turn.": {
        "Hindi": "यह मेरी बारी है। (Yeh meri baari hai.)",
        "Chinese (Simplified)": "轮到我了。 (Lún dào wǒ le.)"
    },
    "she is very happy.": {
        "Hindi": "वह बहुत खुश है। (Vah bahut khush hai.)",
        "Chinese (Simplified)": "她非常高兴。 (Tā fēicháng gāoxìng.)"
    },
    "he likes to read books.": {
        "Hindi": "उसे किताबें पढ़ना पसंद है। (Use kitaabein padhna pasand hai.)",
        "Chinese (Simplified)": "他喜欢读书。 (Tā xǐhuān dúshū.)"
    },
    "she runs every morning.": {
        "Hindi": "वह हर सुबह दौड़ती है। (Vah har subah daudti hai.)",
        "Chinese (Simplified)": "她每天早上跑步。 (Tā měitiān zǎoshàng pǎobù.)"
    },
    "the dog is barking loudly.": {
        "Hindi": "कुत्ता जोर से भौंक रहा है। (Kutta zor se bhauk raha hai.)",
        "Chinese (Simplified)": "狗在大声吠叫。 (Gǒu zài dàshēng fèijiào.)"
    },
    "the sky is very clear today.": {
        "Hindi": "आसमान आज बहुत साफ है। (Aasman aaj bahut saaf hai.)",
        "Chinese (Simplified)": "今天天空非常清澈。 (Jīntiān tiānkōng fēicháng qīngchè.)"
    },
    "he is playing football.": {
        "Hindi": "वह फुटबॉल खेल रहा है। (Vah football khel raha hai.)",
        "Chinese (Simplified)": "他在踢足球。 (Tā zài tī zúqiú.)"
    },
    "this is my favorite color.": {
        "Hindi": "यह मेरा पसंदीदा रंग है। (Yeh mera pasandida rang hai.)",
        "Chinese (Simplified)": "这是我最喜欢的颜色。 (Zhè shì wǒ zuì xǐhuān de yánsè.)"
    },
    "she has a beautiful smile.": {
        "Hindi": "उसकी मुस्कान बहुत खूबसूरत है। (Uski muskaan bahut khoobsurat hai.)",
        "Chinese (Simplified)": "她有一个美丽的微笑。 (Tā yǒu yīgè měilì de wēixiào.)"
    },
    "he is an excellent swimmer.": {
        "Hindi": "वह एक उत्कृष्ट तैराक है। (Vah ek utkṛṣṭ tairāk hai.)",
        "Chinese (Simplified)": "他是一个优秀的游泳者。 (Tā shì yīgè yōuxiù de yóuyǒng zhě.)"
    },
    "the teacher is very helpful.": {
        "Hindi": "शिक्षक बहुत मददगार है। (Shikshak bahut madadgar hai.)",
        "Chinese (Simplified)": "老师非常乐于助人。 (Lǎoshī fēicháng lè yú zhùrén.)"
    },
    "she is very creative.": {
        "Hindi": "वह बहुत रचनात्मक है। (Vah bahut rachnatmak hai.)",
        "Chinese (Simplified)": "她非常有创造力。 (Tā fēicháng yǒu chuàngzàolì.)"
    },
    "the sun is setting.": {
        "Hindi": "सूरज डूब रहा है। (Suraj doob raha hai.)",
        "Chinese (Simplified)": "太阳正在落下。 (Tàiyáng zhèngzài luòxià.)"
    },
    "she is very intelligent.": {
        "Hindi": "वह बहुत बुद्धिमान है। (Vah bahut buddhimaan hai.)",
        "Chinese (Simplified)": "她非常聪明。 (Tā fēicháng cōngmíng.)"
    },
    "the train is arriving soon.": {
        "Hindi": "ट्रेन जल्दी आ रही है। (Train jaldi aa rahi hai.)",
        "Chinese (Simplified)": "火车马上就要到了。 (Huǒchē mǎshàng jiù yào dào le.)"
    },
    "i love playing video games.": {
        "Hindi": "मुझे वीडियो गेम खेलना पसंद है। (Mujhe video game khelna pasand hai.)",
        "Chinese (Simplified)": "我喜欢玩电子游戏。 (Wǒ xǐhuān wán diànzǐ yóuxì.)"
    },
    "the book is on the table.": {
        "Hindi": "किताब मेज पर है। (Kitaab mez par hai.)",
        "Chinese (Simplified)": "书在桌子上。 (Shū zài zhuōzi shàng.)"
    },
    "the food smells delicious.": {
        "Hindi": "खाना स्वादिष्ट महक रहा है। (Khana swadisht mahak raha hai.)",
        "Chinese (Simplified)": "食物闻起来很美味。 (Shíwù wén qǐlái hěn měiwèi.)"
    },
    "he loves playing chess.": {
        "Hindi": "उसे शतरंज खेलना पसंद है। (Use shatranj khelna pasand hai.)",
        "Chinese (Simplified)": "他喜欢下棋。 (Tā xǐhuān xià qí.)"
    },
    "the coffee is too hot.": {
        "Hindi": "कॉफी बहुत गर्म है। (Coffee bahut garm hai.)",
        "Chinese (Simplified)": "咖啡太热了。 (Kāfēi tài rè le.)"
    },
    "the children are playing outside.": {
        "Hindi": "बच्चे बाहर खेल रहे हैं। (Bachche baahar khel rahe hain.)",
        "Chinese (Simplified)": "孩子们在外面玩。 (Háizimen zài wàimiàn wán.)"
    },
    "I like to travel.": {
        "Hindi": "मुझे यात्रा करना पसंद है। (Mujhe yatra karna pasand hai.)",
        "Chinese (Simplified)": "我喜欢旅行。 (Wǒ xǐhuān lǚxíng.)"
    },
    "the moon is shining bright.": {
        "Hindi": "चाँद तेज़ी से चमक रहा है। (Chaand tezī se chamak raha hai.)",
        "Chinese (Simplified)": "月亮在亮闪闪地照耀。 (Yuèliàng zài liàng shǎnshǎn de zhàoyào.)"
    },
    "she speaks three languages.": {
        "Hindi": "वह तीन भाषाएँ बोलती है। (Vah teen bhashayein bolti hai.)",
        "Chinese (Simplified)": "她会说三种语言。 (Tā huì shuō sān zhǒng yǔyán.)"
    },
    "he is reading a newspaper.": {
        "Hindi": "वह एक अखबार पढ़ रहा है। (Vah ek akhbaar padh raha hai.)",
        "Chinese (Simplified)": "他在读报纸。 (Tā zài dú bàozhǐ.)"
    },
    "it is a beautiful day.": {
        "Hindi": "आज एक खूबसूरत दिन है। (Aaj ek khoobsurat din hai.)",
        "Chinese (Simplified)": "今天是美丽的一天。 (Jīntiān shì měilì de yītiān.)"
    },
    "he is a great artist.": {
        "Hindi": "वह एक महान कलाकार है। (Vah ek mahaan kalakaar hai.)",
        "Chinese (Simplified)": "他是一个伟大的艺术家。 (Tā shì yīgè wěidà de yìshùjiā.)"
    },
    "i am feeling sleepy.": {
        "Hindi": "मुझे नींद आ रही है। (Mujhe neend aa rahi hai.)",
        "Chinese (Simplified)": "我觉得困。 (Wǒ juédé kùn.)"
    },
    "the book is very interesting.": {
        "Hindi": "किताब बहुत दिलचस्प है। (Kitaab bahut dilchasp hai.)",
        "Chinese (Simplified)": "这本书非常有趣。 (Zhè běn shū fēicháng yǒuqù.)"
    },
    "she is going to the market.": {
        "Hindi": "वह बाजार जा रही है। (Vah bazaar ja rahi hai.)",
        "Chinese (Simplified)": "她要去市场。 (Tā yào qù shìchǎng.)"
    },
    "they are watching a movie.": {
        "Hindi": "वे एक फिल्म देख रहे हैं। (Ve ek film dekh rahe hain.)",
        "Chinese (Simplified)": "他们在看电影。 (Tāmen zài kàn diànyǐng.)"
    },
    "the cat is sleeping on the couch.": {
        "Hindi": "बिल्ली सोफे पर सो रही है। (Billi sofe par so rahi hai.)",
        "Chinese (Simplified)": "猫正在沙发上睡觉。 (Māo zhèngzài shāfā shàng shuìjiào.)"
    },
    "she has a new phone.": {
        "Hindi": "उसके पास नया फोन है। (Uske paas naya phone hai.)",
        "Chinese (Simplified)": "她有一部新手机。 (Tā yǒu yī bù xīn shǒujī.)"
    },
    "the children are laughing.": {
        "Hindi": "बच्चे हंसी कर रहे हैं। (Bachche hansi kar rahe hain.)",
        "Chinese (Simplified)": "孩子们在笑。 (Háizimen zài xiào.)"
    },
    "i love the rain.": {
        "Hindi": "मुझे बारिश पसंद है। (Mujhe baarish pasand hai.)",
        "Chinese (Simplified)": "我喜欢雨天。 (Wǒ xǐhuān yǔtiān.)"
    },
    "this chair is very comfortable.": {
        "Hindi": "यह कुर्सी बहुत आरामदायक है। (Yeh kursi bahut aaraamdayak hai.)",
        "Chinese (Simplified)": "这把椅子非常舒适。 (Zhè bǎ yǐzi fēicháng shūshì.)"
    },
    "they are singing a song.": {
        "Hindi": "वे एक गाना गा रहे हैं। (Ve ek gaana gaa rahe hain.)",
        "Chinese (Simplified)": "他们在唱歌。 (Tāmen zài chàng gē.)"
    },
    "i am going to bed.": {
        "Hindi": "मैं सोने जा रहा हूँ। (Main sone ja raha hoon.)",
        "Chinese (Simplified)": "我要去睡觉了。 (Wǒ yào qù shuìjiào le.)"
    },
    "the shop is closed today.": {
        "Hindi": "दुकान आज बंद है। (Dukaan aaj band hai.)",
        "Chinese (Simplified)": "今天商店关门。 (Jīntiān shāngdiàn guānmén.)"
    },
    "she is wearing a red dress.": {
        "Hindi": "वह लाल रंग की ड्रेस पहने हुई है। (Vah laal rang ki dress pehene hui hai.)",
        "Chinese (Simplified)": "她穿着一件红色的裙子。 (Tā chuānzhuó yī jiàn hóngsè de qúnzi.)"
    },
    "i am learning Python.": {
        "Hindi": "मैं पायथन सीख रहा हूँ। (Main Python seekh raha hoon.)",
        "Chinese (Simplified)": "我在学习Python。 (Wǒ zài xuéxí Python.)"
    },
    "the bird is flying high.": {
        "Hindi": "पक्षी ऊँचा उड़ रहा है। (Pakshi uncha ud raha hai.)",
        "Chinese (Simplified)": "鸟在高空飞翔。 (Niǎo zài gāo kōng fēixiáng.)"
    },
    "they are eating dinner.": {
        "Hindi": "वे डिनर खा रहे हैं। (Ve dinner kha rahe hain.)",
        "Chinese (Simplified)": "他们在吃晚餐。 (Tāmen zài chī wǎncān.)"
    },
    "i have a meeting tomorrow.": {
        "Hindi": "मेरी कल मीटिंग है। (Meri kal meeting hai.)",
        "Chinese (Simplified)": "我明天有一个会议。 (Wǒ míngtiān yǒu yīgè huìyì.)"
    },
    "the phone is charging.": {
        "Hindi": "फोन चार्ज हो रहा है। (Phone charge ho raha hai.)",
        "Chinese (Simplified)": "手机在充电。 (Shǒujī zài chōngdiàn.)"
    },
    "the weather is very cold today.": {
        "Hindi": "आज मौसम बहुत ठंडा है। (Aaj mausam bahut thanda hai.)",
        "Chinese (Simplified)": "今天天气非常冷。 (Jīntiān tiānqì fēicháng lěng.)"
    },
    "delicious": {
        "Hindi": "स्वादिष्ट (Swadisht)",
        "Chinese (Simplified)": "美味的 (Měiwèi de)"
    },
    "crate": {
        "Hindi": "पट्टा (Patta)",
        "Chinese (Simplified)": "箱子 (Xiāngzi)"
    },
    "excuse me": {
        "Hindi": "मुझे माफ़ करें (Mujhe maaf karein)",
        "Chinese (Simplified)": "对不起 (Duìbùqǐ)"
    },
    "literally": {
        "Hindi": "वास्तव में (Vastav mein)",
        "Chinese (Simplified)": "字面上 (Zìmiàn shàng)"
    },
    "charm": {
        "Hindi": "आकर्षण (Aakarshan)",
        "Chinese (Simplified)": "魅力 (Mèilì)"
    },
    "prank": {
        "Hindi": "मज़ाक (Mazaak)",
        "Chinese (Simplified)": "恶作剧 (Èzuòjù)"
    },
    "worth": {
        "Hindi": "क़ीमत (Keemat)",
        "Chinese (Simplified)": "值得 (Zhídé)"
    },
    "worthless": {
        "Hindi": "निर्दयी (Nirdai)",
        "Chinese (Simplified)": "毫无价值的 (Háo wú jiàzhí de)"
    },
    "stage": {
        "Hindi": "मंच (Manch)",
        "Chinese (Simplified)": "舞台 (Wǔtái)"
    },
    "surf": {
        "Hindi": "लहरों पर चलना (Lehron par chalna)",
        "Chinese (Simplified)": "冲浪 (Chōnglàng)"
    },
    "enable": {
        "Hindi": "सक्षम बनाना (Saksham banana)",
        "Chinese (Simplified)": "启用 (Qǐyòng)"
    },
    "disable": {
        "Hindi": "अक्षम बनाना (Aksham banana)",
        "Chinese (Simplified)": "禁用 (Jìnyòng)"
    },
    "disabled": {
        "Hindi": "अक्षम (Aksham)",
        "Chinese (Simplified)": "残疾的 (Cánjí de)"
    },
    "perform": {
        "Hindi": "प्रदर्शन करना (Pradarshan karna)",
        "Chinese (Simplified)": "表演 (Biǎoyǎn)"
    },
    "instead": {
        "Hindi": "इसके बजाय (Iske bajaye)",
        "Chinese (Simplified)": "代替 (Dàitì)"
    },
    "substitute": {
        "Hindi": "प्रतिस्थापन (pratishthapan)",
        "Chinese (Simplified)": "替代 (tìdài)"
    },
    "apart": {
        "Hindi": "अलग (alag)",
        "Chinese (Simplified)": "分开 (fēnkāi)"
    },
    "focus": {
        "Hindi": "ध्यान केंद्रित करना (dhyaan kendrit karna)",
        "Chinese (Simplified)": "专注 (zhuānzhù)"
    },
    "sympathy": {
        "Hindi": "सहानुभूति (sahaanubhuti)",
        "Chinese (Simplified)": "同情 (tóngqíng)"
    },
    "nasty": {
        "Hindi": "घिनौना (Ghinauna)",
        "Chinese (Simplified)": "肮脏的 (Āngzāng de)"
    },
    "the sky is clear.": {
        "Hindi": "आसमान साफ है। (Aasmaan saaf hai.)",
        "Chinese (Simplified)": "天空是清澈的。 (Tiānkōng shì qīngchè de.)"
    },
    "he is running fast.": {
        "Hindi": "वह तेज दौड़ रहा है। (Vah tez daud raha hai.)",
        "Chinese (Simplified)": "他跑得很快。 (Tā pǎo dé hěn kuài.)"
    },
    "I lost my keys.": {
        "Hindi": "मैं अपनी चाबियाँ खो बैठा हूँ। (Main apni chaabiyan kho baitha hoon.)",
        "Chinese (Simplified)": "我丢了我的钥匙。 (Wǒ diūle wǒ de yàoshi.)"
    },
    "she loves to read books.": {
        "Hindi": "वह किताबें पढ़ना पसंद करती है। (Vah kitaabein padhna pasand karti hai.)",
        "Chinese (Simplified)": "她喜欢读书。 (Tā xǐhuān dúshū.)"
    },
    "he is very tall.": {
        "Hindi": "वह बहुत लंबा है। (Vah bahut lamba hai.)",
        "Chinese (Simplified)": "他很高。 (Tā hěn gāo.)"
    },
    "the coffee is hot.": {
        "Hindi": "कॉफी गरम है। (Coffee garam hai.)",
        "Chinese (Simplified)": "咖啡很热。 (Kāfēi hěn rè.)"
    },
    "I enjoy the music.": {
        "Hindi": "मुझे संगीत पसंद है। (Mujhe sangeet pasand hai.)",
        "Chinese (Simplified)": "我喜欢这音乐。 (Wǒ xǐhuān zhè yīnyuè.)"
    },
    "this place is quiet.": {
        "Hindi": "यह स्थान शांत है। (Yeh sthan shaant hai.)",
        "Chinese (Simplified)": "这个地方很安静。 (Zhège dìfāng hěn ānjìng.)"
    },
    "she is my friend.": {
        "Hindi": "वह मेरी दोस्त है। (Vah meri dost hai.)",
        "Chinese (Simplified)": "她是我的朋友。 (Tā shì wǒ de péngyǒu.)"
    },
    "the dog is barking.": {
        "Hindi": "कुत्ता भौंक रहा है। (Kutta bhonk raha hai.)",
        "Chinese (Simplified)": "狗在叫。 (Gǒu zài jiào.)"
    },
    "they are laughing loudly.": {
        "Hindi": "वे जोर से हंस रहे हैं। (Ve zor se hans rahe hain.)",
        "Chinese (Simplified)": "他们大声笑。 (Tāmen dàshēng xiào.)"
    },
    "I like this game.": {
        "Hindi": "मुझे यह खेल पसंद है। (Mujhe yeh khel pasand hai.)",
        "Chinese (Simplified)": "我喜欢这个游戏。 (Wǒ xǐhuān zhège yóuxì.)"
    },
    "he is reading a book.": {
        "Hindi": "वह एक किताब पढ़ रहा है। (Vah ek kitaab padh raha hai.)",
        "Chinese (Simplified)": "他在读一本书。 (Tā zài dú yī běn shū.)"
    },
    "the food smells good.": {
        "Hindi": "खाना अच्छा खुशबू आ रहा है। (Khana accha khushboo aa raha hai.)",
        "Chinese (Simplified)": "食物闻起来很香。 (Shíwù wén qǐlái hěn xiāng.)"
    },
    "dung": {
        "Hindi": "गोबर (Gobar)",
        "Chinese (Simplified)": "粪便 (Fènbiàn)"
    },
    "poetry": {
        "Hindi": "काव्य (Kavya)",
        "Chinese (Simplified)": "诗歌 (Shīgē)"
    },
    "roast": {
        "Hindi": "भूनना (Bhunna)",
        "Chinese (Simplified)": "烤 (Kǎo)"
    },
    "pan": {
        "Hindi": "कढ़ाई (Kadhai)",
        "Chinese (Simplified)": "平底锅 (Píngdǐguō)"
    },
    "sticky": {
        "Hindi": "चिपचिपा (Chipchipa)",
        "Chinese (Simplified)": "粘 (Nián)"
    },
    "spine": {
        "Hindi": "रीढ़ (Reedh)",
        "Chinese (Simplified)": "脊柱 (Jǐzhù)"
    },
    "model": {
        "Hindi": "मॉडल (Model)",
        "Chinese (Simplified)": "模型 (Móxíng)"
    },
    "juice": {
        "Hindi": "रस (Ras)",
        "Chinese (Simplified)": "果汁 (Guǒzhī)"
    },
    "gang": {
        "Hindi": "गिरोह (Giroh)",
        "Chinese (Simplified)": "帮派 (Bāngpài)"
    },
    "crown": {
        "Hindi": "मुकुट (Mukut)",
        "Chinese (Simplified)": "王冠 (Wángguàn)"
    },
    "nerd": {
        "Hindi": "विद्वान (Vidwan)",
        "Chinese (Simplified)": "书呆子 (Shūdāizi)"
    },
    "worse": {
        "Hindi": "और बुरा (Aur bura)",
        "Chinese (Simplified)": "更糟 (Gèng zāo)"
    },
    "rob": {
        "Hindi": "लूटना (Lootna)",
        "Chinese (Simplified)": "抢劫 (Qiǎngjié)"
    },
    "robbery": {
        "Hindi": "डाका (Daka)",
        "Chinese (Simplified)": "抢劫 (Qiǎngjié)"
    },
    "hit": {
        "Hindi": "मारा (Mara)",
        "Chinese (Simplified)": "打击 (Dǎjí)"
    },
    "cartel": {
        "Hindi": "गिरोह (Giroh)",
        "Chinese (Simplified)": "卡特尔 (Kǎtè'ěr)"
    },
    "sport": {
        "Hindi": "खेल (Khel)",
        "Chinese (Simplified)": "体育 (Tǐyù)"
    },
    "live": {
        "Hindi": "जीवित (Jeevit)",
        "Chinese (Simplified)": "生活 (Shēnghuó)"
    },
    "rip": {
        "Hindi": "फाड़ना (Fadna)",
        "Chinese (Simplified)": "撕裂 (Sīliè)"
    },
    "heist": {
        "Hindi": "डाका (Daka)",
        "Chinese (Simplified)": "劫案 (Jié'àn)"
    },
    "jesus": {
        "Hindi": "यीशु (Yeeshu)",
        "Chinese (Simplified)": "耶稣 (Yēsū)"
    },
    "buddha": {
        "Hindi": "बुद्ध (Buddh)",
        "Chinese (Simplified)": "佛陀 (Fótuó)"
    },
    "blush": {
        "Hindi": "शर्मिंदा होना (Sharminda hona)",
        "Chinese (Simplified)": "脸红 (Liǎn hóng)"
    },
    "attention": {
        "Hindi": "ध्यान (Dhyan)",
        "Chinese (Simplified)": "注意 (Zhùyì)"
    },
    "victory": {
        "Hindi": "विजय (Vijay)",
        "Chinese (Simplified)": "胜利 (Shènglì)"
    },
    "soup": {
        "Hindi": "सूप (Soup)",
        "Chinese (Simplified)": "汤 (Tāng)"
    },
    "curry": {
        "Hindi": "करी (Curry)",
        "Chinese (Simplified)": "咖喱 (Gālí)"
    },
    "aside": {
        "Hindi": "साइड (Side)",
        "Chinese (Simplified)": "旁边 (Pángbiān)"
    },
    "beside": {
        "Hindi": "के पास (Ke paas)",
        "Chinese (Simplified)": "在旁边 (Zài pángbiān)"
    },
    "prime minister": {
        "Hindi": "प्रधान मंत्री (Pradhan Mantri)",
        "Chinese (Simplified)": "总理 (Zǒnglǐ)"
    },
    "president": {
        "Hindi": "राष्ट्रपति (Rashtrapati)",
        "Chinese (Simplified)": "总统 (Zǒngtǒng)"
    },
    "chief minister": {
        "Hindi": "मुख्यमंत्री (Mukhyamantri)",
        "Chinese (Simplified)": "首席部长 (Shǒuxí bùzhǎng)"
    },
    "district minister": {
        "Hindi": "जिला मंत्री (Jila Mantri)",
        "Chinese (Simplified)": "地区部长 (Dìqū bùzhǎng)"
    },
    "supported": {
        "Hindi": "समर्थित (Samarthit)",
        "Chinese (Simplified)": "支持 (Zhīchí)"
    },
    "turban": {
        "Hindi": "पगड़ी (Pagdi)",
        "Chinese (Simplified)": "头巾 (Tóujīn)"
    },
    "cap": {
        "Hindi": "टोपी (Topi)",
        "Chinese (Simplified)": "帽子 (Màozi)"
    },
    "lessons": {
        "Hindi": "पाठ (Paath)",
        "Chinese (Simplified)": "课程 (Kèchéng)"
    },
    "lesson": {
        "Hindi": "पाठ (Paath)",
        "Chinese (Simplified)": "课 (Kè)"
    },
    "parody": {
        "Hindi": "पैरोडी (Parody)",
        "Chinese (Simplified)": "恶搞 (Ègǎo)"
    },
    "dominate": {
        "Hindi": "प्रभुत्व (Prabhutva)",
        "Chinese (Simplified)": "支配 (Zhīpèi)"
    },
    "ghost": {
        "Hindi": "भूत (Bhoot)",
        "Chinese (Simplified)": "鬼 (Guǐ)"
    },
    "devotee": {
        "Hindi": "भक्त (Bhakt)",
        "Chinese (Simplified)": "信徒 (Xìntú)"
    },
    "bark": {
        "Hindi": "छाल (Chhaal)",
        "Chinese (Simplified)": "树皮 (Shùpí)"
    },
    "mewing": {
        "Hindi": "बिल्ली की आवाज (Billi ki awaaz)",
        "Chinese (Simplified)": "猫叫声 (Māo jiàoshēng)"
    },
    "pop corn": {
        "Hindi": "पॉपकॉर्न (Popcorn)",
        "Chinese (Simplified)": "爆米花 (Bàomǐhuā)"
    },
    "thread": {
        "Hindi": "धागा (Dhaaga)",
        "Chinese (Simplified)": "线 (Xiàn)"
    },
    "online": {
        "Hindi": "ऑनलाइन (Online)",
        "Chinese (Simplified)": "在线 (Zàixiàn)"
    },
    "offline": {
        "Hindi": "ऑफलाइन (Offline)",
        "Chinese (Simplified)": "离线 (Líxiàn)"
    },
    "going": {
        "Hindi": "जाना (Jana)",
        "Chinese (Simplified)": "去 (Qù)"
    },
    "cartoon": {
        "Hindi": "कार्टून (Cartoon)",
        "Chinese (Simplified)": "卡通 (Kǎtōng)"
    },
    "carton": {
        "Hindi": "कार्टन (Carton)",
        "Chinese (Simplified)": "纸箱 (Zhǐxiāng)"
    },
    "jail": {
        "Hindi": "जेल (Jail)",
        "Chinese (Simplified)": "监狱 (Jiānyù)"
    },
    "loot": {
        "Hindi": "लूट (Loot)",
        "Chinese (Simplified)": "掠夺 (Luèduó)"
    },
    "cream": {
        "Hindi": "क्रीम (Cream)",
        "Chinese (Simplified)": "奶油 (Nǎiyóu)"
    },
    "flour": {
        "Hindi": "आटा (Aata)",
        "Chinese (Simplified)": "面粉 (Miànfěn)"
    },
    "define": {
        "Hindi": "परिभाषित करना (Paribhashit Karna)",
        "Chinese (Simplified)": "定义 (Dìngyì)"
    },
    "employee": {
        "Hindi": "कर्मचारी (Karmchari)",
        "Chinese (Simplified)": "员工 (Yuángōng)"
    },
    "breakdown": {
        "Hindi": "विखंडन (Vikhndan)",
        "Chinese (Simplified)": "故障 (Gùzhàng)"
    },
    "dinosaur": {
        "Hindi": "डायनासोर (Dinosaur)",
        "Chinese (Simplified)": "恐龙 (Kǒnglóng)"
    },
    "mammoth": {
        "Hindi": "मैमथ (Mammoth)",
        "Chinese (Simplified)": "猛犸象 (Měngmǎxiàng)"
    },
    "ally": {
        "Hindi": "सहयोगी (Sahyogi)",
        "Chinese (Simplified)": "盟友 (Méngyǒu)"
    },
    "personality": {
        "Hindi": "व्यक्तित्व (Vyaktitva)",
        "Chinese (Simplified)": "个性 (Gèxìng)"
    },
    "disorder": {
        "Hindi": "विकार (Vikar)",
        "Chinese (Simplified)": "失调 (Shītiáo)"
    },
    "personality disorder": {
        "Hindi": "व्यक्तित्व विकार (Vyaktitva Vikar)",
        "Chinese (Simplified)": "人格障碍 (Réngé zhàng'ài)"
    },
    "aura": {
        "Hindi": "आभा (Aabha)",
        "Chinese (Simplified)": "气场 (Qìchǎng)"
    },
    "favor": {
        "Hindi": "अनुग्रह (Anugrah)",
        "Chinese (Simplified)": "恩惠 (Ēnhuì)"
    },
    "suspend": {
        "Hindi": "निलंबित करना (Nilambit Karna)",
        "Chinese (Simplified)": "暂停 (Zàntíng)"
    },
    "eliminate": {
        "Hindi": "उन्मूलन करना (Unmoolan Karna)",
        "Chinese (Simplified)": "消除 (Xiāochú)"
    },
    "revive": {
        "Hindi": "पुनर्जीवित करना (Punarjeevit Karna)",
        "Chinese (Simplified)": "复活 (Fùhuó)"
    },
    "revoke": {
        "Hindi": "रद्द करना (Radd Karna)",
        "Chinese (Simplified)": "撤销 (Chèxiāo)"
    },
    "prime": {
        "Hindi": "प्राथमिक (Prathamik)",
        "Chinese (Simplified)": "主要 (Zhǔyào)"
    },
    "challenge": {
        "Hindi": "चुनौती (Chunauti)",
        "Chinese (Simplified)": "挑战 (Tiǎozhàn)"
    },
    "hyper": {
        "Hindi": "अत्यधिक सक्रिय (Atyadhik Sakriya)",
        "Chinese (Simplified)": "过度活跃 (Guòdù huóyuè)"
    },
    "old age": {
        "Hindi": "बुढ़ापा (Budhapa)",
        "Chinese (Simplified)": "老年 (Lǎonián)"
    },
    "young age": {
        "Hindi": "युवा अवस्था (Yuva Avstha)",
        "Chinese (Simplified)": "年轻 (Niánqīng)"
    },
    "medium age": {
        "Hindi": "मध्यम आयु (Madhyam Aayu)",
        "Chinese (Simplified)": "中年 (Zhōngnián)"
    },
    "low": {
        "Hindi": "निचा (Nicha)",
        "Chinese (Simplified)": "低 (Dī)"
    },
    "high": {
        "Hindi": "ऊँचा (Uncha)",
        "Chinese (Simplified)": "高 (Gāo)"
    },
    "lower": {
        "Hindi": "निम्न (Nimn)",
        "Chinese (Simplified)": "降低 (Jiàngdī)"
    },
    "higher": {
        "Hindi": "उच्च (Ucch)",
        "Chinese (Simplified)": "更高 (Gèng gāo)"
    },
    "infinity": {
        "Hindi": "अनंत (Anant)",
        "Chinese (Simplified)": "无限 (Wúxiàn)"
    },
    "unit": {
        "Hindi": "इकाई (Ikai)",
        "Chinese (Simplified)": "单位 (Dānwèi)"
    },
    "measure": {
        "Hindi": "माप (Maap)",
        "Chinese (Simplified)": "测量 (Cèliàng)"
    },
    "bypass": {
        "Hindi": "बाइपास (Bypass)",
        "Chinese (Simplified)": "旁路 (Pánglù)"
    },
    "what's up": {
        "Hindi": "क्या हो रहा है? (Kya ho raha hai?)",
        "Chinese (Simplified)": "怎么了? (Zěnme le?)"
    },
    "genome": {
        "Hindi": "जीनोम (Genom)",
        "Chinese (Simplified)": "基因组 (Jīyīn zǔ)"
    },
    "my name is": {
        "Hindi": "मेरा नाम है (Mera naam hai)",
        "Chinese (Simplified)": "我的名字是 (Wǒ de míngzì shì)"
    },
    "who are you": {
        "Hindi": "आप कौन हैं? (Aap kaun hain?)",
        "Chinese (Simplified)": "你是谁? (Nǐ shì shuí?)"
    },
    "how are you": {
        "Hindi": "कैसे हो? (Kaise ho?)",
        "Chinese (Simplified)": "你好吗? (Nǐ hǎo ma?)"
    },
    "you are cute": {
        "Hindi": "तुम प्यारे हो (Tum pyaare ho)",
        "Chinese (Simplified)": "你很可爱 (Nǐ hěn kě'ài)"
    },
    "you are cool": {
        "Hindi": "तुम कूल हो (Tum cool ho)",
        "Chinese (Simplified)": "你很酷 (Nǐ hěn kù)"
    },
    "you are amazing": {
        "Hindi": "तुम अद्भुत हो (Tum adbhut ho)",
        "Chinese (Simplified)": "你太棒了 (Nǐ tài bàngle)"
    },
    "i am a servant": {
        "Hindi": "मैं एक नौकर हूँ (Main ek naukar hoon)",
        "Chinese (Simplified)": "我是一个仆人 (Wǒ shì yīgè púrén)"
    },
    "i am an employee": {
        "Hindi": "मैं एक कर्मचारी हूँ (Main ek karmachari hoon)",
        "Chinese (Simplified)": "我是一个员工 (Wǒ shì yīgè yuángōng)"
    },
    "what are you doing": {
        "Hindi": "तुम क्या कर रहे हो? (Tum kya kar rahe ho?)",
        "Chinese (Simplified)": "你在做什么? (Nǐ zài zuò shénme?)"
    },
    "come on": {
        "Hindi": "आओ (Aao)",
        "Chinese (Simplified)": "来吧 (Lái ba)"
    },
    "are you okay": {
        "Hindi": "क्या तुम ठीक हो? (Kya tum theek ho?)",
        "Chinese (Simplified)": "你还好吗? (Nǐ hái hǎo ma?)"
    },
    "so much years": {
        "Hindi": "इतने साल (Itne saal)",
        "Chinese (Simplified)": "这么多年 (Zhème duō nián)"
    },
    "exploit": {
        "Hindi": "शोषण (Shoshan)",
        "Chinese (Simplified)": "剥削 (Bāoxuē)"
    },
    "frame": {
        "Hindi": "फ्रेम (Frame)",
        "Chinese (Simplified)": "框架 (Kuàngjià)"
    },
    "painting": {
        "Hindi": "चित्रकारी (Chitrakari)",
        "Chinese (Simplified)": "绘画 (Huìhuà)"
    },
    "print": {
        "Hindi": "प्रिंट (Print)",
        "Chinese (Simplified)": "打印 (Dǎyìn)"
    },
    "paint": {
        "Hindi": "पेंट (Paint)",
        "Chinese (Simplified)": "油漆 (Yóuqī)"
    },
    "but why": {
        "Hindi": "लेकिन क्यों? (Lekin kyon?)",
        "Chinese (Simplified)": "但为什么? (Dàn wèishéme?)"
    },
    "incredible": {
        "Hindi": "अविश्वसनीय (Avishwasniya)",
        "Chinese (Simplified)": "难以置信 (Nányǐ zhìxìn)"
    },
    "performance": {
        "Hindi": "प्रदर्शन (Pradarshan)",
        "Chinese (Simplified)": "表现 (Biǎoxiàn)"
    },
    "i like it": {
        "Hindi": "मुझे यह पसंद है (Mujhe yeh pasand hai)",
        "Chinese (Simplified)": "我喜欢它 (Wǒ xǐhuān tā)"
    },
    "let's go": {
        "Hindi": "चलिए (Chaliye)",
        "Chinese (Simplified)": "我们走吧 (Wǒmen zǒu ba)"
    },
    "pattern": {
        "Hindi": "पैटर्न (Pattern)",
        "Chinese (Simplified)": "模式 (Móshì)"
    },
    "reference": {
        "Hindi": "संदर्भ (Sandarbh)",
        "Chinese (Simplified)": "参考 (Cānkǎo)"
    },
    "level": {
        "Hindi": "स्तर (Sthar)",
        "Chinese (Simplified)": "水平 (Shuǐpíng)"
    },
    "illuminate": {
        "Hindi": "प्रकाशित करना (Prakashit Karna)",
        "Chinese (Simplified)": "照亮 (Zhàoliàng)"
    },
    "web": {
        "Hindi": "वेब (Web)",
        "Chinese (Simplified)": "网络 (Wǎngluò)"
    },
    "spider": {
        "Hindi": "मकड़ी (Makdi)",
        "Chinese (Simplified)": "蜘蛛 (Zhīzhū)"
    },
    "coming": {
        "Hindi": "आ रहा है (A raha hai)",
        "Chinese (Simplified)": "来 (Lái)"
    },
    "coming soon": {
        "Hindi": "जल्द आ रहा है (Jald aa raha hai)",
        "Chinese (Simplified)": "即将到来 (Jíjiāng dàolái)"
    },
    "urban": {
        "Hindi": "शहरी (Shehri)",
        "Chinese (Simplified)": "城市 (Chéngshì)"
    },
    "rural": {
        "Hindi": "ग्रामीण (Gramin)",
        "Chinese (Simplified)": "乡村 (Xiāngcūn)"
    },
    "reserve": {
        "Hindi": "आरक्षित (Aarakshit)",
        "Chinese (Simplified)": "预订 (Yùdìng)"
    },
    "cinema": {
        "Hindi": "सिनेमाघर (Cinema Ghar)",
        "Chinese (Simplified)": "电影院 (Diànyǐngyuàn)"
    },
    "reservation": {
        "Hindi": "आरक्षण (Aarakshan)",
        "Chinese (Simplified)": "预定 (Yùdìng)"
    },
    "architect": {
        "Hindi": "वास्तुकार (Vastukaar)",
        "Chinese (Simplified)": "建筑师 (Jiànzhú shī)"
    },
    "too hard": {
        "Hindi": "बहुत कठिन (Bahut kathin)",
        "Chinese (Simplified)": "太难了 (Tài nánle)"
    },
    "freeze": {
        "Hindi": "जमना (Jamna)",
        "Chinese (Simplified)": "冻结 (Dòngjié)"
    },
    "melt": {
        "Hindi": "पिघलना (Pighalna)",
        "Chinese (Simplified)": "融化 (Rónghuà)"
    },
    "surround": {
        "Hindi": "घेरना (Gherna)",
        "Chinese (Simplified)": "包围 (Bāowéi)"
    },
    "surrounding": {
        "Hindi": "आसपास (Aaspas)",
        "Chinese (Simplified)": "周围 (Zhōuwéi)"
    },
    "hidden": {
        "Hindi": "छिपा हुआ (Chhupa Hua)",
        "Chinese (Simplified)": "隐藏 (Yǐn cáng)"
    },
    "pedophile": {
        "Hindi": "बाल यौन शोषक (Baal Youn Shoshak)",
        "Chinese (Simplified)": "恋童癖 (Liàntóngpī)"
    },
    "crack": {
        "Hindi": "दरार (Darar)",
        "Chinese (Simplified)": "裂缝 (Lièfèng)"
    },
    "approach": {
        "Hindi": "पास आना (Paas Aana)",
        "Chinese (Simplified)": "接近 (Jiējìn)"
    },
    "miner": {
        "Hindi": "खनिक (Khanik)",
        "Chinese (Simplified)": "矿工 (Kuànggōng)"
    },
    "fleet": {
        "Hindi": "बेड़ा (Beda)",
        "Chinese (Simplified)": "舰队 (Jiànduì)"
    },
    "circus": {
        "Hindi": "सर्कस (Sarkas)",
        "Chinese (Simplified)": "马戏团 (Mǎxìtuán)"
    },
    "jealous": {
        "Hindi": "जलन (Jalan)",
        "Chinese (Simplified)": "嫉妒 (Jídù)"
    },
    "one shot": {
        "Hindi": "एक ही शॉट (Ek Hi Shot)",
        "Chinese (Simplified)": "一击 (Yī jí)"
    },
    "fluent": {
        "Hindi": "धाराप्रवाह (Dharaprawah)",
        "Chinese (Simplified)": "流利 (Liúlì)"
    },
    "open mind": {
        "Hindi": "खुला दिमाग (Khula Dimaag)",
        "Chinese (Simplified)": "开放思想 (Kāifàng sīxiǎng)"
    },
    "review": {
        "Hindi": "समीक्षा (Sameeksha)",
        "Chinese (Simplified)": "审查 (Shěnchá)"
    },
    "superman": {
        "Hindi": "सुपरमैन (Superman)",
        "Chinese (Simplified)": "超人 (Chāo rén)"
    },
    "bad leader": {
        "Hindi": "बुरा नेता (Bura Neta)",
        "Chinese (Simplified)": "糟糕的领导者 (Zāogāo de lǐngdǎo zhě)"
    },
    "bat": {
        "Hindi": "बिल्ली (Billi)",
        "Chinese (Simplified)": "蝙蝠 (Biānfú)"
    },
    "fly": {
        "Hindi": "उड़ना (Udna)",
        "Chinese (Simplified)": "飞 (Fēi)"
    },
    "walker": {
        "Hindi": "चलने वाला (Chalne Wala)",
        "Chinese (Simplified)": "行走者 (Xíngzǒu zhě)"
    },
    "not like us": {
        "Hindi": "हम जैसे नहीं (Hum Jaise Nahi)",
        "Chinese (Simplified)": "不像我们 (Bù xiàng wǒmen)"
    },
    "exist": {
        "Hindi": "अस्तित्व में होना (Astitv Mein Hona)",
        "Chinese (Simplified)": "存在 (Cúnzài)"
    },
    "egg": {
        "Hindi": "अंडा (Anda)",
        "Chinese (Simplified)": "蛋 (Dàn)"
    },
    "expire": {
        "Hindi": "समाप्त होना (Samaapt Hona)",
        "Chinese (Simplified)": "过期 (Guòqī)"
    },
    "pass away": {
        "Hindi": "स्वर्गवास हो जाना (Swargvaas Ho Jana)",
        "Chinese (Simplified)": "去世 (Qùshì)"
    },
    "importance": {
        "Hindi": "महत्व (Mahattva)",
        "Chinese (Simplified)": "重要性 (Zhòngyàoxìng)"
    },
    "shit": {
        "Hindi": "गंदगी (Gandagi)",
        "Chinese (Simplified)": "屎 (Shǐ)"
    },
    "layer": {
        "Hindi": "परत (Parat)",
        "Chinese (Simplified)": "层 (Céng)"
    },
    "meal": {
        "Hindi": "भोजन (Bhojan)",
        "Chinese (Simplified)": "餐 (Cān)"
    },
    "write a song": {
        "Hindi": "एक गाना लिखो (Ek Gaana Likho)",
        "Chinese (Simplified)": "写一首歌 (Xiě yī shǒu gē)"
    },
    "can you do that for me": {
        "Hindi": "क्या तुम मेरे लिए यह कर सकते हो? (Kya Tum Mere Liye Yeh Kar Sakte Ho?)",
        "Chinese (Simplified)": "你能为我做这个吗? (Nǐ néng wèi wǒ zuò zhège ma?)"
    },
    "i am calling": {
        "Hindi": "मैं कॉल कर रहा हूँ (Main Call Kar Raha Hoon)",
        "Chinese (Simplified)": "我在打电话 (Wǒ zài dǎ diànhuà)"
    },
    "hey listen": {
        "Hindi": "हे सुनो (Hey Suno)",
        "Chinese (Simplified)": "嘿，听着 (Hēi, tīngzhe)"
    },
    "ignore": {
        "Hindi": "नज़रअंदाज़ करना (Nazarandaaz Karna)",
        "Chinese (Simplified)": "忽视 (Hūshì)"
    },
    "listen": {
        "Hindi": "सुनो (Suno)",
        "Chinese (Simplified)": "听 (Tīng)"
    },
    "out of hands": {
        "Hindi": "हाथ से बाहर (Haath Se Baahar)",
        "Chinese (Simplified)": "脱手 (Tuō shǒu)"
    },
    "threat": {
        "Hindi": "धमकी (Dhamki)",
        "Chinese (Simplified)": "威胁 (Wēixié)"
    },
    "shoot my shot": {
        "Hindi": "अपना मौका आजमाना (Apna Mauka Azmana)",
        "Chinese (Simplified)": "射击我的机会 (Shèjī wǒ de jīhuì)"
    },
    "here we go again": {
        "Hindi": "फिर से शुरू करते हैं (Phir Se Shuru Karte Hain)",
        "Chinese (Simplified)": "我们又来了 (Wǒmen yòu láile)"
    },
    "shack": {
        "Hindi": "झोपड़ी (Jhopdi)",
        "Chinese (Simplified)": "小屋 (Xiǎowū)"
    },
    "plank": {
        "Hindi": "पट्टी (Patti)",
        "Chinese (Simplified)": "木板 (Mùbǎn)"
    },
    "wood": {
        "Hindi": "लकड़ी (Lakdi)",
        "Chinese (Simplified)": "木头 (Mùtóu)"
    },
    "fatal": {
        "Hindi": "घातक (Ghatak)",
        "Chinese (Simplified)": "致命 (Zhìmìng)"
    },
    "apology": {
        "Hindi": "माफी (Maafi)",
        "Chinese (Simplified)": "道歉 (Dàoqiàn)"
    },
    "apologize": {
        "Hindi": "माफी मांगना (Maafi Maangna)",
        "Chinese (Simplified)": "道歉 (Dàoqiàn)"
    },
    "i am sorry": {
        "Hindi": "मुझे खेद है (Mujhe Khed Hai)",
        "Chinese (Simplified)": "对不起 (Duìbuqǐ)"
    },
    "is everything good": {
        "Hindi": "क्या सब ठीक है? (Kya Sab Theek Hai?)",
        "Chinese (Simplified)": "一切都好吗? (Yīqiè dōu hǎo ma?)"
    },
    "i am ok": {
        "Hindi": "मैं ठीक हूँ (Main Theek Hoon)",
        "Chinese (Simplified)": "我很好 (Wǒ hěn hǎo)"
    },
    "evidence": {
        "Hindi": "साक्ष्य (Saakshya)",
        "Chinese (Simplified)": "证据 (Zhèngjù)"
    },
    "exposure": {
        "Hindi": "प्रदर्शन (Pradarshan)",
        "Chinese (Simplified)": "曝光 (Bàoguāng)"
    },
    "nick": {
        "Hindi": "चोट (Chot)",
        "Chinese (Simplified)": "小伤 (Xiǎo shāng)"
    },
    "suggestion": {
        "Hindi": "सुझाव (Sujhav)",
        "Chinese (Simplified)": "建议 (Jiànyì)"
    },
    "announcement": {
        "Hindi": "घोषणा (Ghoshna)",
        "Chinese (Simplified)": "公告 (Gōnggào)"
    },
    "trip": {
        "Hindi": "यात्रा (Yatra)",
        "Chinese (Simplified)": "旅行 (Lǚxíng)"
    },
    "fantasy": {
        "Hindi": "काल्पनिक (Kalpanik)",
        "Chinese (Simplified)": "幻想 (Huànxiǎng)"
    },
    "carpenter": {
        "Hindi": "बढ़ई (Badhai)",
        "Chinese (Simplified)": "木匠 (Mùjiàng)"
    },
    "default": {
        "Hindi": "डिफ़ॉल्ट (Default)",
        "Chinese (Simplified)": "默认 (Mòrèn)"
    },
    "hug": {
        "Hindi": "गले लगाना (Gale Lagana)",
        "Chinese (Simplified)": "拥抱 (Yǒngbào)"
    },
    "post": {
        "Hindi": "पोस्ट (Post)",
        "Chinese (Simplified)": "帖子 (Tiězi)"
    },
    "terms": {
        "Hindi": "शर्तें (Shartein)",
        "Chinese (Simplified)": "条款 (Tiáokuǎn)"
    },
    "contact": {
        "Hindi": "संपर्क (Sampark)",
        "Chinese (Simplified)": "联系 (Liánxì)"
    },
    "upload": {
        "Hindi": "अपलोड (Upload)",
        "Chinese (Simplified)": "上传 (Shàngchuán)"
    },
    "micro": {
        "Hindi": "सूक्ष्म (Sookshm)",
        "Chinese (Simplified)": "微型 (Wēixíng)"
    },
    "official": {
        "Hindi": "आधिकारिक (Aadhikarik)",
        "Chinese (Simplified)": "官方 (Guānfāng)"
    },
    "original": {
        "Hindi": "मूल (Mool)",
        "Chinese (Simplified)": "原始 (Yuánshǐ)"
    },
    "remake": {
        "Hindi": "पुनःनिर्माण (Punah Nirman)",
        "Chinese (Simplified)": "重拍 (Chóng pāi)"
    },
    "structure": {
        "Hindi": "संरचना (Sanrachna)",
        "Chinese (Simplified)": "结构 (Jiégòu)"
    },
    "statue": {
        "Hindi": "मूर्ति (Murti)",
        "Chinese (Simplified)": "雕像 (Diāoxiàng)"
    },
    "iconic": {
        "Hindi": "प्रसिद्ध (Prasiddh)",
        "Chinese (Simplified)": "标志性 (Biāozhìxìng)"
    },
    "sign": {
        "Hindi": "चिन्ह (Chinh)",
        "Chinese (Simplified)": "符号 (Fúhào)"
    },
    "symbol": {
        "Hindi": "प्रतीक (Prateek)",
        "Chinese (Simplified)": "符号 (Fúhào)"
    },
    "locket": {
        "Hindi": "लॉकेट (Locket)",
        "Chinese (Simplified)": "项链盒 (Xiàngliàn hé)"
    },
    "accurate": {
        "Hindi": "सटीक (Sateek)",
        "Chinese (Simplified)": "准确 (Zhǔnquè)"
    },
    "natural": {
        "Hindi": "प्राकृतिक (Praakritik)",
        "Chinese (Simplified)": "自然的 (Zìrán de)"
    },
    "balance": {
        "Hindi": "संतुलन (Santulan)",
        "Chinese (Simplified)": "平衡 (Pínghéng)"
    },
    "cover": {
        "Hindi": "कवर (Cover)",
        "Chinese (Simplified)": "封面 (Fēngmiàn)"
    },
    "coverage": {
        "Hindi": "कवरेज (Coverage)",
        "Chinese (Simplified)": "覆盖范围 (Fùgài fànwéi)"
    },
    "capable": {
        "Hindi": "सक्षम (Saksham)",
        "Chinese (Simplified)": "有能力的 (Yǒu nénglì de)"
    },
    "phrase": {
        "Hindi": "वाक्यांश (Vaakyansh)",
        "Chinese (Simplified)": "短语 (Duǎnyǔ)"
    },
    "idiom": {
        "Hindi": "मुहावरा (Muhavra)",
        "Chinese (Simplified)": "成语 (Chéngyǔ)"
    },
    "include": {
        "Hindi": "शामिल करना (Shamil Karna)",
        "Chinese (Simplified)": "包括 (Bāokuò)"
    },
    "exclude": {
        "Hindi": "बाहर करना (Bahar Karna)",
        "Chinese (Simplified)": "排除 (Páichú)"
    },
    "various": {
        "Hindi": "विभिन्न (Vibhinn)",
        "Chinese (Simplified)": "各种 (Gèzhǒng)"
    },
    "aim": {
        "Hindi": "उद्देश्य (Uddeshya)",
        "Chinese (Simplified)": "目标 (Mùbiāo)"
    },
    "target": {
        "Hindi": "लक्ष्य (Lakshya)",
        "Chinese (Simplified)": "目标 (Mùbiāo)"
    },
    "additional": {
        "Hindi": "अतिरिक्त (Atirikt)",
        "Chinese (Simplified)": "附加的 (Fùjiā de)"
    },
    "extra": {
        "Hindi": "अतिरिक्त (Atirikt)",
        "Chinese (Simplified)": "额外的 (Éwài de)"
    },
    "magic": {
        "Hindi": "जादू (Jadoo)",
        "Chinese (Simplified)": "魔法 (Mófǎ)"
    },
    "magical": {
        "Hindi": "जादुई (Jadooee)",
        "Chinese (Simplified)": "魔幻的 (Móhuàn de)"
    },
    "specific": {
        "Hindi": "विशिष्ट (Vishisht)",
        "Chinese (Simplified)": "具体的 (Jùtǐ de)"
    },
    "common": {
        "Hindi": "सामान्य (Samanya)",
        "Chinese (Simplified)": "普通的 (Pǔtōng de)"
    },
    "unique": {
        "Hindi": "अद्वितीय (Advitiya)",
        "Chinese (Simplified)": "独特的 (Dútè de)"
    },
    "a blessing in disguise": {
        "Hindi": "बुरे में भी अच्छा होता है (Bure mein bhi accha hota hai)",
        "Chinese (Simplified)": "因祸得福 (Yīn huò dé fú)"
    },
    "burn bridges": {
        "Hindi": "रिश्ते तोड़ना (Rishte todna)",
        "Chinese (Simplified)": "断绝关系 (Duànjué guānxi)"
    },
    "a penny for your thoughts": {
        "Hindi": "आप क्या सोच रहे हैं? (Aap kya soch rahe hain?)",
        "Chinese (Simplified)": "你在想什么? (Nǐ zài xiǎng shénme?)"
    },
    "cat's out of the bag": {
        "Hindi": "राज़ खुल गया (Raaz khul gaya)",
        "Chinese (Simplified)": "猫已经从袋子里出来了 (Māo yǐjīng cóng dàizi lǐ chūlái le)"
    },
    "cut to the chase": {
        "Hindi": "साफ़ बात कहो (Saaf baat kaho)",
        "Chinese (Simplified)": "直接进入主题 (Zhíjiē jìnrù zhǔtí)"
    },
    "cry over spilled milk": {
        "Hindi": "बता चुका हुआ काम पर रोना (Bata chuka hua kaam par rona)",
        "Chinese (Simplified)": "为打翻的牛奶哭泣 (Wèi dǎ fān de niúnǎi kūqì)"
    },
    "don't count your chickens before they hatch": {
        "Hindi": "अभी से कुछ ना सोचो (Abhi se kuch na socho)",
        "Chinese (Simplified)": "不要过早下结论 (Bùyào guò zǎo xià jiélùn)"
    },
    "the ball is in your court": {
        "Hindi": "अब यह तुम्हारी बारी है (Ab yeh tumhari baari hai)",
        "Chinese (Simplified)": "球在你这边 (Qiú zài nǐ zhèbiān)"
    },
    "a bird in the hand is worth two in the bush": {
        "Hindi": "जो तुम्हारे पास है वही ज्यादा बेहतर है (Jo tumhare paas hai wahi zyada behtar hai)",
        "Chinese (Simplified)": "手中的鸟胜过林中的两只 (Shǒu zhōng de niǎo shèngguò lín zhōng de liǎng zhī)"
    },
    "to get cold feet": {
        "Hindi": "घबराना (Ghabraana)",
        "Chinese (Simplified)": "感到紧张 (Gǎndào jǐnzhāng)"
    },
    "a blessing in disguise": {
        "Hindi": "बुरे में भी अच्छा होता है (Bure mein bhi accha hota hai)",
        "Chinese (Simplified)": "因祸得福 (Yīn huò dé fú)"
    },
    "actions speak louder than words": {
        "Hindi": "कर्म शब्दों से ज्यादा बोलते हैं (Karm shabdon se zyada bolte hain)",
        "Chinese (Simplified)": "行动胜于言辞 (Xíngdòng shèng yú yáncí)"
    },
    "break the ice": {
        "Hindi": "बर्फ तोड़ना (Baraf todna)",
        "Chinese (Simplified)": "打破僵局 (Dǎ pò jiāngjú)"
    },
    "hit the nail on the head": {
        "Hindi": "सच्चाई को ठीक से कहना (Sachai ko theek se kehna)",
        "Chinese (Simplified)": "一针见血 (Yī zhēn jiàn xiě)"
    },
    "under the weather": {
        "Hindi": "बीमार महसूस करना (Beemar mehsoos karna)",
        "Chinese (Simplified)": "身体不适 (Shēntǐ bù shì)"
    },
    "spill the beans": {
        "Hindi": "राज़ खोलना (Raaz kholna)",
        "Chinese (Simplified)": "泄露秘密 (Xièlòu mìmì)"
    },
    "once in a blue moon": {
        "Hindi": "कभी कभार (Kabhi kabhaar)",
        "Chinese (Simplified)": "千载难逢 (Qiān zǎi nán féng)"
    },
    "burn the midnight oil": {
        "Hindi": "रात भर काम करना (Raat bhar kaam karna)",
        "Chinese (Simplified)": "开夜车 (Kāi yè chē)"
    },
    "beat around the bush": {
        "Hindi": "सीधे मुद्दे की बात न करना (Seedhe mudde ki baat na karna)",
        "Chinese (Simplified)": "拐弯抹角 (Guǎi wān mò jiǎo)"
    },
    "bite the bullet": {
        "Hindi": "मुसीबत को सहना (Musibat ko sehna)",
        "Chinese (Simplified)": "硬着头皮做 (Yìngzhe tóupí zuò)"
    },
    "the early bird catches the worm": {
        "Hindi": "जो जल्दी उठता है उसे फायदा होता है (Jo jaldi uthta hai use faida hota hai)",
        "Chinese (Simplified)": "早起的鸟儿有虫吃 (Zǎo qǐ de niǎo er yǒu huǐ chī)"
    },
    "every cloud has a silver lining": {
        "Hindi": "हर बुरी चीज में कुछ अच्छा होता है (Har buri cheez mein kuch accha hota hai)",
        "Chinese (Simplified)": "黑暗中总有一线光明 (Hēi'àn zhōng zǒng yǒu yī xiàn guāngmíng)"
    },
    "you can't judge a book by its cover": {
        "Hindi": "किसी को बाहर से न आँको (Kisi ko baahar se na aankho)",
        "Chinese (Simplified)": "人不可貌相 (Rén bù kě mào xiàng)"
    },
    "too good to be true": {
        "Hindi": "विश्वास करना कठिन (Vishwas karna kathin)",
        "Chinese (Simplified)": "好得令人难以置信 (Hǎo dé lìng rén nán yǐ zhìxìn)"
    },
    "put all your eggs in one basket": {
        "Hindi": "सभी आशाएँ एक ही जगह लगाना (Sabhi aashaen ek hi jagah lagana)",
        "Chinese (Simplified)": "孤注一掷 (Gū zhù yī zhì)"
    },
    "the apple doesn't fall far from the tree": {
        "Hindi": "बच्चे अपने माता-पिता से मिलते हैं (Bacche apne mata-pita se milte hain)",
        "Chinese (Simplified)": "有其父必有其子 (Yǒu qí fù bì yǒu qí zǐ)"
    },
    "hit the sack": {
        "Hindi": "सोने जाना (Sone jana)",
        "Chinese (Simplified)": "去睡觉 (Qù shuìjiào)"
    },
    "cost an arm and a leg": {
        "Hindi": "बहुत महंगा होना (Bahut mehenga hona)",
        "Chinese (Simplified)": "花费很多 (Huā fèi hěn duō)"
    },
    "raining cats and dogs": {
        "Hindi": "बहुत जोर से बारिश होना (Bahut zor se baarish hona)",
        "Chinese (Simplified)": "倾盆大雨 (Qīngpén dàyǔ)"
    },
    "let the cat out of the bag": {
        "Hindi": "राज़ खोल देना (Raaz khol dena)",
        "Chinese (Simplified)": "泄露秘密 (Xièlòu mìmì)"
    },
    "kill two birds with one stone": {
        "Hindi": "एक तीर से दो शिकार (Ek teer se do shikar)",
        "Chinese (Simplified)": "一箭双雕 (Yī jiàn shuāng diāo)"
    },
    "bite off more than you can chew": {
        "Hindi": "अपनी क्षमता से अधिक काम लेना (Apni kshamata se adhik kaam lena)",
        "Chinese (Simplified)": "贪多嚼不烂 (Tān duō jiáo bù làn)"
    },
    "it's not rocket science": {
        "Hindi": "यह बहुत कठिन नहीं है (Yeh bahut kathin nahi hai)",
        "Chinese (Simplified)": "这不是什么火箭科学 (Zhè bù shì shénme huǒjiàn kēxué)"
    },
    "in the heat of the moment": {
        "Hindi": "जोश में आकर (Josh mein aakar)",
        "Chinese (Simplified)": "一时激动 (Yīshí jīdòng)"
    },
    "the tip of the iceberg": {
        "Hindi": "सिर्फ़ शुरुआत (Sirf shuruat)",
        "Chinese (Simplified)": "冰山一角 (Bīngshān yī jiǎo)"
    },
    "a watched pot never boils": {
        "Hindi": "जो चीज़ देखी जाती है वह जल्दी नहीं होती (Jo cheez dekhi jati hai woh jaldi nahi hoti)",
        "Chinese (Simplified)": "看锅不会开 (Kàn guō bù huì kāi)"
    },
    "out of the frying pan and into the fire": {
        "Hindi": "मुसीबत से और बड़ी मुसीबत में फंसना (Musibat se aur badi musibat mein fansna)",
        "Chinese (Simplified)": "从锅里跳到火里 (Cóng guō lǐ tiào dào huǒ lǐ)"
    },
    "don't cry over spilled milk": {
        "Hindi": "जो हो चुका है उस पर पछतावा मत करो (Jo ho chuka hai us par pachtawa mat karo)",
        "Chinese (Simplified)": "覆水难收 (Fù shuǐ nán shōu)"
    },
    "a picture is worth a thousand words": {
        "Hindi": "एक तस्वीर हजार शब्दों के बराबर होती है (Ek tasveer hazar shabdon ke barabar hoti hai)",
        "Chinese (Simplified)": "一图胜千言 (Yī tú shèng qiān yán)"
    },
    "actions speak louder than words": {
        "Hindi": "कर्म शब्दों से अधिक बोलते हैं (Karm shabdon se adhik bolte hain)",
        "Chinese (Simplified)": "行动胜于言辞 (Xíngdòng shèng yú yáncí)"
    },
    "better late than never": {
        "Hindi": "देरी से आना कभी नहीं आने से बेहतर है (Der se aana kabhi nahi aane se behtar hai)",
        "Chinese (Simplified)": "迟到总比不到好 (Chídào zǒng bǐ bù dào hǎo)"
    },
    "don't bite the hand that feeds you": {
        "Hindi": "जो तुम्हारी मदद करता है उसे नुकसान मत पहुँचाओ (Jo tumhari madad karta hai use nuqsan mat pahuchao)",
        "Chinese (Simplified)": "不要咬那只喂你的人 (Bùyào yǎo nà zhī wèi nǐ de rén)"
    },
    "burning the midnight oil": {
        "Hindi": "रातों को जागकर काम करना (Raaton ko jaagkar kaam karna)",
        "Chinese (Simplified)": "熬夜 (Áo yè)"
    },
    "hit the nail on the head": {
        "Hindi": "सही बात कहना (Sahi baat kehna)",
        "Chinese (Simplified)": "一针见血 (Yī zhēn jiàn xuè)"
    },
    "a bird in the hand is worth two in the bush": {
        "Hindi": "जो है वही बेहतर है (Jo hai wahi behtar hai)",
        "Chinese (Simplified)": "一鸟在手胜过二鸟在林 (Yī niǎo zài shǒu shèngguò èr niǎo zài lín)"
    },
    "rome wasn't built in a day": {
        "Hindi": "कुछ भी बड़ी चीज़ जल्दी नहीं बनती (Kuch bhi badi cheez jaldi nahi banti)",
        "Chinese (Simplified)": "罗马不是一天建成的 (Luómǎ bù shì yī tiān jiànchéng de)"
    },
    "the grass is always greener on the other side": {
        "Hindi": "दूसरों के पास जो है वह हमेशा बेहतर लगता है (Doosron ke paas jo hai wah hamesha behtar lagta hai)",
        "Chinese (Simplified)": "别人的草地总是更绿 (Biérén de cǎodì zǒng shì gèng lǜ)"
    },
    "a leopard can't change its spots": {
        "Hindi": "व्यक्ति का स्वभाव नहीं बदलता (Vyakti ka swabhav nahi badalta)",
        "Chinese (Simplified)": "本性难移 (Běnxìng nán yí)"
    },
    "put your money where your mouth is": {
        "Hindi": "जो कहो वह करो (Jo kaho wah karo)",
        "Chinese (Simplified)": "言行一致 (Yánxíng yīzhì)"
    },
    "the ball is in your court": {
        "Hindi": "अब तुम्हारी बारी है (Ab tumhari baari hai)",
        "Chinese (Simplified)": "球在你这边 (Qiú zài nǐ zhèbiān)"
    },
    "don't count your chickens before they hatch": {
        "Hindi": "अभी से खुशी मत मनाओ (Abhi se khushi mat manao)",
        "Chinese (Simplified)": "不要过早打算 (Bùyào guòzǎo dǎsuàn)"
    },
    "a watched pot never boils": {
        "Hindi": "जल्दी मत करो (Jaldi mat karo)",
        "Chinese (Simplified)": "看锅永远不会沸腾 (Kàn guō yǒngyuǎn bù huì fèiténg)"
    },
    "mafia": {
        "Hindi": "माफिया (Mafia)",
        "Chinese (Simplified)": "黑手党 (Hēi shǒu dǎng)"
    },
    "witch": {
        "Hindi": "जादूगरनी (Jadoogarni)",
        "Chinese (Simplified)": "女巫 (Nǚwū)"
    },
    "dope": {
        "Hindi": "नशा (Nasha)",
        "Chinese (Simplified)": "毒品 (Dúpǐn)"
    },
    "crop": {
        "Hindi": "फसल (Fasal)",
        "Chinese (Simplified)": "农作物 (Nóngzuòwù)"
    },
    "seat": {
        "Hindi": "सीट (Seat)",
        "Chinese (Simplified)": "座位 (Zuòwèi)"
    },
    "prepare": {
        "Hindi": "तैयार करना (Taiyaar Karna)",
        "Chinese (Simplified)": "准备 (Zhǔnbèi)"
    },
    "engine": {
        "Hindi": "इंजन (Engine)",
        "Chinese (Simplified)": "引擎 (Yǐnqíng)"
    },
    "kick": {
        "Hindi": "लात (Laat)",
        "Chinese (Simplified)": "踢 (Tī)"
    },
    "procedure": {
        "Hindi": "प्रक्रिया (Prakriya)",
        "Chinese (Simplified)": "程序 (Chéngxù)"
    },
    "tame": {
        "Hindi": "पालना (Paala)",
        "Chinese (Simplified)": "驯服 (Xùnfú)"
    },
    "early": {
        "Hindi": "जल्दी (Jaldi)",
        "Chinese (Simplified)": "早 (Zǎo)"
    },
    "time pass": {
        "Hindi": "समय बिताना (Samay bitana)",
        "Chinese (Simplified)": "消磨时间 (Xiāo mó shíjiān)"
    },
    "creature": {
        "Hindi": "प्राणी (PraaNi)",
        "Chinese (Simplified)": "生物 (Shēngwù)"
    },
    "prison": {
        "Hindi": "जेल (Jail)",
        "Chinese (Simplified)": "监狱 (Jiānyù)"
    },
    "charges": {
        "Hindi": "आरोप (Aarop)",
        "Chinese (Simplified)": "指控 (Zhǐkòng)"
    },
    "imprisonment": {
        "Hindi": "कारावास (Kaarawaas)",
        "Chinese (Simplified)": "监禁 (Jiānjìn)"
    },
    "demand": {
        "Hindi": "मांग (Maang)",
        "Chinese (Simplified)": "需求 (Xūqiú)"
    },
    "reply": {
        "Hindi": "उत्तर (Uttar)",
        "Chinese (Simplified)": "回复 (Huífù)"
    },
    "boycott": {
        "Hindi": "बहिष्कार (Bahishkaar)",
        "Chinese (Simplified)": "抵制 (Dǐzhì)"
    },
    "biceps": {
        "Hindi": "बाइसेप्स (Biceps)",
        "Chinese (Simplified)": "肱二头肌 (Gōng èr tóu jī)"
    },
    "shameful": {
        "Hindi": "लज्जाजनक (Lajjajanak)",
        "Chinese (Simplified)": "可耻 (Kěchǐ)"
    },
    "shot him": {
        "Hindi": "उसे गोली मारी (Use goli maari)",
        "Chinese (Simplified)": "射击他 (Shèjí tā)"
    },
    "shoot her": {
        "Hindi": "उसे गोली मारो (Use goli maaro)",
        "Chinese (Simplified)": "射击她 (Shèjí tā)"
    },
    "shoot them": {
        "Hindi": "उन्हें गोली मारो (Unhein goli maaro)",
        "Chinese (Simplified)": "射击他们 (Shèjí tāmen)"
    },
    "creepy": {
        "Hindi": "भयानक (Bhayaank)",
        "Chinese (Simplified)": "令人毛骨悚然 (Lìng rén máo gǔ sǒng rán)"
    },
    "buzz": {
        "Hindi": "गूँज (Goonj)",
        "Chinese (Simplified)": "嗡嗡声 (Wēng wēng shēng)"
    },
    "wave": {
        "Hindi": "लहर (Lahar)",
        "Chinese (Simplified)": "波浪 (Bōlàng)"
    },
    "butter": {
        "Hindi": "मक्खन (Makkhan)",
        "Chinese (Simplified)": "黄油 (Huángyóu)"
    },
    "yet to come": {
        "Hindi": "आना बाकी है (Aana baaki hai)",
        "Chinese (Simplified)": "还未到来 (Hái wèi dàolái)"
    },
    "self love": {
        "Hindi": "स्वयं प्रेम (Swayam prem)",
        "Chinese (Simplified)": "自爱 (Zì ài)"
    },
    "fragile": {
        "Hindi": "नाजुक (Naazuk)",
        "Chinese (Simplified)": "易碎 (Yì suì)"
    },
    "antifragile": {
        "Hindi": "एंटी-फ्रैजाइल (Anti-fragile)",
        "Chinese (Simplified)": "抗脆弱 (Kàng cuìruò)"
    },
    "praise the lord": {
        "Hindi": "प्रभु की प्रशंसा करो (Prabhu ki prashansa karo)",
        "Chinese (Simplified)": "赞美上帝 (Zànměi shàngdì)"
    },
    "out of control": {
        "Hindi": "नियंत्रण से बाहर (Niyantran se baahar)",
        "Chinese (Simplified)": "失控 (Shīkòng)"
    },
    "ambition": {
        "Hindi": "महत्वाकांक्षा (Mahattvakansha)",
        "Chinese (Simplified)": "雄心 (Xióngxīn)"
    },
    "kush": {
        "Hindi": "कुश (Kush)",
        "Chinese (Simplified)": "大麻 (Dàmá)"
    },
    "lush": {
        "Hindi": "हरा-भरा (Hara-bhara)",
        "Chinese (Simplified)": "茂盛 (Màoshèng)"
    },
    "coma": {
        "Hindi": "कोमा (Coma)",
        "Chinese (Simplified)": "昏迷 (Hūnmí)"
    },
    "still": {
        "Hindi": "अभी भी (Abhi bhi)",
        "Chinese (Simplified)": "仍然 (Réngrán)"
    },
    "deep": {
        "Hindi": "गहरा (Gehra)",
        "Chinese (Simplified)": "深 (Shēn)"
    },
    "dose": {
        "Hindi": "खुराक (Khuraak)",
        "Chinese (Simplified)": "剂量 (Jìliàng)"
    },
    "bet": {
        "Hindi": "सट्टा (Satta)",
        "Chinese (Simplified)": "打赌 (Dǎdǔ)"
    },
    "you like that": {
        "Hindi": "क्या तुम्हें वह पसंद है (Kya tumhein wah pasand hai)",
        "Chinese (Simplified)": "你喜欢那个 (Nǐ xǐhuān nàgè)"
    },
    "boys like you": {
        "Hindi": "लड़के तुमसे प्यार करते हैं (Ladke tumse pyaar karte hain)",
        "Chinese (Simplified)": "男孩喜欢你 (Nán hái xǐhuān nǐ)"
    },
    "girls like you": {
        "Hindi": "लड़कियाँ तुमसे प्यार करती हैं (Ladkiyaan tumse pyaar karti hain)",
        "Chinese (Simplified)": "女孩喜欢你 (Nǚhái xǐhuān nǐ)"
    },
    "love it": {
        "Hindi": "इसे प्यार करो (Ise pyaar karo)",
        "Chinese (Simplified)": "爱它 (Ài tā)"
    },
    "exclusive": {
        "Hindi": "विशेष (Vishesh)",
        "Chinese (Simplified)": "独家 (Dújiā)"
    },
    "biscuit": {
        "Hindi": "बिस्किट (Biscuit)",
        "Chinese (Simplified)": "饼干 (Bǐnggān)"
    },
    "cookie": {
        "Hindi": "कुकी (Cookie)",
        "Chinese (Simplified)": "曲奇 (Qūqí)"
    },
    "calm down": {
        "Hindi": "शांत हो जाओ (Shaant ho jao)",
        "Chinese (Simplified)": "冷静下来 (Lěngjìng xiàlái)"
    },
    "far from death": {
        "Hindi": "मृत्यु से दूर (Mrityu se door)",
        "Chinese (Simplified)": "远离死亡 (Yuǎnlí sǐwáng)"
    },
    "far from alive": {
        "Hindi": "जीवन से दूर (Jeevan se door)",
        "Chinese (Simplified)": "远离活着 (Yuǎnlí huózhe)"
    },
    "edge": {
        "Hindi": "किनारा (Kinara)",
        "Chinese (Simplified)": "边缘 (Biānyuán)"
    },
    "ready or not": {
        "Hindi": "तैयार हो या नहीं (Taiyaar ho ya nahin)",
        "Chinese (Simplified)": "准备好还是没准备 (Zhǔnbèi hǎo háishì méi zhǔnbèi)"
    },
    "on my way": {
        "Hindi": "मैं रास्ते में हूँ (Main raaste mein hoon)",
        "Chinese (Simplified)": "在路上 (Zài lùshàng)"
    },
    "coming down": {
        "Hindi": "नीचे आ रहा है (Neeche aa raha hai)",
        "Chinese (Simplified)": "下来 (Xiàlái)"
    },
    "myself": {
        "Hindi": "खुद (Khud)",
        "Chinese (Simplified)": "我自己 (Wǒ zìjǐ)"
    },
    "best friend": {
        "Hindi": "सबसे अच्छा दोस्त (Sabse accha dost)",
        "Chinese (Simplified)": "最好的朋友 (Zuì hǎo de péngyǒu)"
    },
    "boyfriend": {
        "Hindi": "प्रेमी (Premi)",
        "Chinese (Simplified)": "男朋友 (Nán péngyǒu)"
    },
    "girlfriend": {
        "Hindi": "प्रेमिका (Premika)",
        "Chinese (Simplified)": "女朋友 (Nǚ péngyǒu)"
    },
    "shutdown": {
        "Hindi": "बंद करना (Band karna)",
        "Chinese (Simplified)": "关机 (Guānjī)"
    },
    "shut up": {
        "Hindi": "चुप रहो (Chup raho)",
        "Chinese (Simplified)": "闭嘴 (Bìzuǐ)"
    },
    "startup": {
        "Hindi": "शुरुआत (Shuruaat)",
        "Chinese (Simplified)": "启动 (Qǐdòng)"
    },
    "forgiven": {
        "Hindi": "क्षमा किया गया (Kshama kiya gaya)",
        "Chinese (Simplified)": "被原谅 (Bèi yuánliàng)"
    },
    "unforgiven": {
        "Hindi": "अक्षम्य (Akshamya)",
        "Chinese (Simplified)": "不可原谅 (Bùkě yuánliàng)"
    },
    "welcome there": {
        "Hindi": "वहां स्वागत है (Wahan swaagat hai)",
        "Chinese (Simplified)": "欢迎在那里 (Huānyíng zài nàlǐ)"
    },
    "welcome here": {
        "Hindi": "यहाँ स्वागत है (Yahan swaagat hai)",
        "Chinese (Simplified)": "欢迎在这里 (Huānyíng zài zhèlǐ)"
    },
    "forgive": {
        "Hindi": "क्षमा करना (Kshama karna)",
        "Chinese (Simplified)": "原谅 (Yuánliàng)"
    },
    "punish": {
        "Hindi": "दंड देना (Dand dena)",
        "Chinese (Simplified)": "惩罚 (Chéngfá)"
    },
    "punishment": {
        "Hindi": "दंड (Dand)",
        "Chinese (Simplified)": "惩罚 (Chéngfá)"
    },
    "despite": {
        "Hindi": "के बावजूद (Ke bavajood)",
        "Chinese (Simplified)": "尽管 (Jǐnguǎn)"
    },
    "bargain": {
        "Hindi": "सौदा (Sauda)",
        "Chinese (Simplified)": "讨价还价 (Tǎojià huányjià)"
    },
    "award": {
        "Hindi": "पुरस्कार (Puraskar)",
        "Chinese (Simplified)": "奖项 (Jiǎngxiàng)"
    },
    "tail": {
        "Hindi": "पूंछ (Poonch)",
        "Chinese (Simplified)": "尾巴 (Wěibā)"
    },
    "subtle": {
        "Hindi": "सूक्ष्म (Sookshm)",
        "Chinese (Simplified)": "微妙 (Wēimiào)"
    },
    "celebrity": {
        "Hindi": "सेलिब्रिटी (Selibriti)",
        "Chinese (Simplified)": "名人 (Míngrén)"
    },
    "celebrities": {
        "Hindi": "सेलिब्रिटीज़ (Selibritiz)",
        "Chinese (Simplified)": "名人们 (Míngrénmen)"
    },
    "junk": {
        "Hindi": "कबाड़ (Kabaad)",
        "Chinese (Simplified)": "垃圾 (Lājī)"
    },
    "debunk": {
        "Hindi": "ख़ारिज करना (Khaarij karna)",
        "Chinese (Simplified)": "揭穿 (Jiēchuān)"
    },
    "react": {
        "Hindi": "प्रतिक्रिया करना (Pratikriya karna)",
        "Chinese (Simplified)": "反应 (Fǎnyìng)"
    },
    "reaction": {
        "Hindi": "प्रतिक्रिया (Pratikriya)",
        "Chinese (Simplified)": "反应 (Fǎnyìng)"
    },
    "realistic": {
        "Hindi": "यथार्थवादी (Yatharthvadi)",
        "Chinese (Simplified)": "现实主义的 (Xiànshízhǔyì de)"
    },
    "thought": {
        "Hindi": "विचार (Vichaar)",
        "Chinese (Simplified)": "想法 (Xiǎngfǎ)"
    },
    "moment": {
        "Hindi": "क्षण (Kshan)",
        "Chinese (Simplified)": "时刻 (Shíkè)"
    },
    "movement": {
        "Hindi": "आंदोलन (Aandolan)",
        "Chinese (Simplified)": "运动 (Yùndòng)"
    },
    "sensitive": {
        "Hindi": "संवेदनशील (Sanvedansheel)",
        "Chinese (Simplified)": "敏感的 (Mǐngǎn de)"
    },
    "insensitive": {
        "Hindi": "असंवेदनशील (Asanvedansheel)",
        "Chinese (Simplified)": "不敏感的 (Bù mǐngǎn de)"
    },
    "accent": {
        "Hindi": "उच्चारण (Ucchaaran)",
        "Chinese (Simplified)": "口音 (Kǒuyīn)"
    },
    "brilliant": {
        "Hindi": "प्रतिभाशाली (Pratbhaashaali)",
        "Chinese (Simplified)": "杰出的 (Jiéchū de)"
    },
    "threaten": {
        "Hindi": "धमकाना (Dhamakaana)",
        "Chinese (Simplified)": "威胁 (Wēixié)"
    },
    "become": {
        "Hindi": "बनना (Bannaa)",
        "Chinese (Simplified)": "成为 (Chéngwéi)"
    },
    "health": {
        "Hindi": "स्वास्थ्य (Swaasthya)",
        "Chinese (Simplified)": "健康 (Jiànkāng)"
    },
    "health minister": {
        "Hindi": "स्वास्थ्य मंत्री (Swaasthya Mantri)",
        "Chinese (Simplified)": "卫生部长 (Wèishēng bùzhǎng)"
    },
    "support": {
        "Hindi": "समर्थन (Samarthan)",
        "Chinese (Simplified)": "支持 (Zīchí)"
    },
    "arrive": {
        "Hindi": "आना (Aana)",
        "Chinese (Simplified)": "到达 (Dàodá)"
    },
    "depart": {
        "Hindi": "प्रस्थान करना (Prasthaan karna)",
        "Chinese (Simplified)": "离开 (Líkāi)"
    },
    "export": {
        "Hindi": "निर्यात (Niryaat)",
        "Chinese (Simplified)": "出口 (Chūkǒu)"
    },
    "import": {
        "Hindi": "आयात (Aayaat)",
        "Chinese (Simplified)": "进口 (Jìnkǒu)"
    },
    "fresh": {
        "Hindi": "ताजा (Taaja)",
        "Chinese (Simplified)": "新鲜的 (Xīnxiān de)"
    },
    "refresh": {
        "Hindi": "ताज़ा करना (Taaza karna)",
        "Chinese (Simplified)": "刷新 (Shūnxīn)"
    },
    "carry": {
        "Hindi": "ले जाना (Le jaana)",
        "Chinese (Simplified)": "携带 (Xiédài)"
    },
    "turn": {
        "Hindi": "मुड़ना (Mudna)",
        "Chinese (Simplified)": "转弯 (Zhuǎnwān)"
    },
    "turn left": {
        "Hindi": "बाएँ मुड़ें (Baen muden)",
        "Chinese (Simplified)": "左转 (Zuǒ zhuǎn)"
    },
    "turn right": {
        "Hindi": "दाएँ मुड़ें (Daen muden)",
        "Chinese (Simplified)": "右转 (Yòu zhuǎn)"
    },
    "able": {
        "Hindi": "सक्षम (Sakshyam)",
        "Chinese (Simplified)": "能够 (Nénggòu)"
    },
    "pack": {
        "Hindi": "पैक करना (Paek karna)",
        "Chinese (Simplified)": "打包 (Dǎbāo)"
    },
    "triggered": {
        "Hindi": "चला गया (Chala gaya)",
        "Chinese (Simplified)": "触发 (Cūfā)"
    },
    "trigger": {
        "Hindi": "चलाना (Chalaana)",
        "Chinese (Simplified)": "触发 (Cūfā)"
    },
    "spin": {
        "Hindi": "घूमना (Ghoomna)",
        "Chinese (Simplified)": "旋转 (Xuànzhuǎn)"
    },
    "destroy": {
        "Hindi": "नष्ट करना (Nashta karna)",
        "Chinese (Simplified)": "破坏 (Pòhuài)"
    },
    "really": {
        "Hindi": "वास्तव में (Vaastav mein)",
        "Chinese (Simplified)": "真的 (Zhēnde)"
    },
    "similar": {
        "Hindi": "सदृश (Sadrish)",
        "Chinese (Simplified)": "相似的 (Xiāngsì de)"
    },
    "entered": {
        "Hindi": "दर्ज किया गया (Darj kiya gaya)",
        "Chinese (Simplified)": "输入 (Shūrù)"
    },
    "pop": {
        "Hindi": "पॉप (Pop)",
        "Chinese (Simplified)": "流行音乐 (Liúxíng yīnyuè)"
    },
    "pin": {
        "Hindi": "पिन (Pin)",
        "Chinese (Simplified)": "别针 (Biézhēn)"
    },
    "lower": {
        "Hindi": "निम्न (Nimn)",
        "Chinese (Simplified)": "较低的 (Jiàodī de)"
    },
    "pajama": {
        "Hindi": "पजामा (Pajaama)",
        "Chinese (Simplified)": "睡裤 (Shuìkù)"
    },
    "grind": {
        "Hindi": "पीसना (Peesna)",
        "Chinese (Simplified)": "磨 (Mó)"
    },
    "desserts": {
        "Hindi": "मिठाईयाँ (Mithaiyaan)",
        "Chinese (Simplified)": "甜点 (Tiándiǎn)"
    },
    "sweets": {
        "Hindi": "मिठाई (Mithai)",
        "Chinese (Simplified)": "糖果 (Tángguǒ)"
    },
    "beggar": {
        "Hindi": "भिखारी (Bhikhaari)",
        "Chinese (Simplified)": "乞丐 (Qǐgài)"
    },
    "Indus Valley": {
        "Hindi": "सिंधु घाटी (Sindhu Ghaati)",
        "Chinese (Simplified)": "印度河流域文明 (Yìndù héliúyù wénmíng)"
    },
    "snacks": {
        "Hindi": "नाश्ता (Naashta)",
        "Chinese (Simplified)": "小吃 (Xiǎochī)"
    },
    "first time": {
        "Hindi": "पहली बार (Pehli baar)",
        "Chinese (Simplified)": "第一次 (Dì yī cì)"
    },
    "last time": {
        "Hindi": "पिछली बार (Pichhli baar)",
        "Chinese (Simplified)": "上次 (Shàngcì)"
    },
    "flirt": {
        "Hindi": "छेड़खानी करना (Chheddkhaani karna)",
        "Chinese (Simplified)": "调情 (Tiáoqíng)"
    },
    "manipulate": {
        "Hindi": "हस्तक्षेप करना (Hastakshep karna)",
        "Chinese (Simplified)": "操纵 (Cāozòng)"
    },
    "i got hate comments": {
        "Hindi": "मुझे नफरत भरे कमेंट मिले (Mujhe nafrat bhare comment mile)",
        "Chinese (Simplified)": "我收到了很多仇恨评论 (Wǒ shōudào le hěnduō chóuhèn pínlùn)"
    },
    "how to learn": {
        "Hindi": "कैसे सीखें (Kaise seekhen)",
        "Chinese (Simplified)": "如何学习 (Rúhé xuéxí)"
    },
    "twice": {
        "Hindi": "दो बार (Do baar)",
        "Chinese (Simplified)": "两次 (Liǎng cì)"
    },
    "list": {
        "Hindi": "सूची (Soochi)",
        "Chinese (Simplified)": "列表 (Lièbiǎo)"
    },
    "tragedy": {
        "Hindi": "त्रासदी (Traasdi)",
        "Chinese (Simplified)": "悲剧 (Bēijù)"
    },
    "flag": {
        "Hindi": "झंडा (Jhanda)",
        "Chinese (Simplified)": "旗帜 (Qízhì)"
    },
    "red flag": {
        "Hindi": "लाल झंडा (Laal jhanda)",
        "Chinese (Simplified)": "红旗 (Hóngqí)"
    },
    "green flag": {
        "Hindi": "हरा झंडा (Hara jhanda)",
        "Chinese (Simplified)": "绿旗 (Lǜqí)"
    },
    "toxic": {
        "Hindi": "विषाक्त (Vishaakt)",
        "Chinese (Simplified)": "有毒的 (Yǒudú de)"
    },
    "no one tells": {
        "Hindi": "कोई नहीं बताता (Koi nahi batata)",
        "Chinese (Simplified)": "没有人说 (Méiyǒu rén shuō)"
    },
    "ground reality": {
        "Hindi": "जमीनी हकीकत (Jamini hakikat)",
        "Chinese (Simplified)": "现实情况 (Xiànshí qíngkuàng)"
    },
    "Megan": {
        "Hindi": "मेगन (Megan)",
        "Chinese (Simplified)": "梅根 (Méigēn)"
    },
    "who it possible": {
        "Hindi": "यह किसके लिए संभव है (Yah kiske liye sambhav hai)",
        "Chinese (Simplified)": "这对谁来说可能 (Duì shéi lái shuō kěnéng)"
    },
    "this it impossible": {
        "Hindi": "यह असंभव है (Yah asambhav hai)",
        "Chinese (Simplified)": "这是不可能的 (Zhè shì bù kěnéng de)"
    },
    "come on let's go": {
        "Hindi": "चलो चलते हैं (Chalo chalte hain)",
        "Chinese (Simplified)": "来吧，我们走吧 (Lái ba, wǒmen zǒu ba)"
    },
    "oh my god": {
        "Hindi": "हे भगवान (He bhagwaan)",
        "Chinese (Simplified)": "哦，我的天哪 (Ó, wǒ de tiān ne)"
    },
    "wow that's so cool": {
        "Hindi": "वाह, यह बहुत अच्छा है (Vah, yah bahut accha hai)",
        "Chinese (Simplified)": "哇，太酷了 (Wā, tài kù le)"
    },
    "she is bride": {
        "Hindi": "वह दुल्हन है (Vah dulhan hai)",
        "Chinese (Simplified)": "她是新娘 (Tā shì xīnniáng)"
    },
    "he is groom": {
        "Hindi": "वह दूल्हा है (Vah dulha hai)",
        "Chinese (Simplified)": "他是新郎 (Tā shì xīnláng)"
    },
    "gate": {
        "Hindi": "गेट (Gate)",
        "Chinese (Simplified)": "大门 (Dàmén)"
    },
    "scene": {
        "Hindi": "दृश्य (Drishya)",
        "Chinese (Simplified)": "场景 (Chǎngjǐng)"
    },
    "situation": {
        "Hindi": "स्थिति (Sthiti)",
        "Chinese (Simplified)": "情况 (Qíngkuàng)"
    },
    "events": {
        "Hindi": "घटनाएँ (Ghatnaen)",
        "Chinese (Simplified)": "事件 (Shìjiàn)"
    },
    "current events": {
        "Hindi": "समाचार (Samaachaar)",
        "Chinese (Simplified)": "时事 (Shíshì)"
    },
    "current affairs": {
        "Hindi": "समाचार (Samaachaar)",
        "Chinese (Simplified)": "时事 (Shíshì)"
    },
    "affair": {
        "Hindi": "चक्कर (Chakkar)",
        "Chinese (Simplified)": "风流韵事 (Fēngliú yùnshì)"
    },
    "process": {
        "Hindi": "प्रक्रिया (Prakriya)",
        "Chinese (Simplified)": "过程 (Guòchéng)"
    },
    "direct": {
        "Hindi": "सीधा (Seedha)",
        "Chinese (Simplified)": "直接的 (Zhíjiē de)"
    },
    "indirect": {
        "Hindi": "अप्रत्यक्ष (Apraatyaksh)",
        "Chinese (Simplified)": "间接的 (Jiànjiē de)"
    },
    "indirectly": {
        "Hindi": "अप्रत्यक्ष रूप से (Apraatyaksh roop se)",
        "Chinese (Simplified)": "间接地 (Jiànjiē de)"
    },
    "directly": {
        "Hindi": "सीधे (Seedhe)",
        "Chinese (Simplified)": "直接地 (Zhíjiē de)"
    },
    "access": {
        "Hindi": "पहुँच (Pauhnch)",
        "Chinese (Simplified)": "访问 (Fǎngwèn)"
    },
    "allow": {
        "Hindi": "अनुमति देना (Anumati dena)",
        "Chinese (Simplified)": "允许 (Yǔnxǔ)"
    },
    "allowed": {
        "Hindi": "अनुमति दी गई (Anumati di gayi)",
        "Chinese (Simplified)": "被允许的 (Bèi yǔnxǔ de)"
    },
    "not allowed": {
        "Hindi": "अनुमति नहीं है (Anumati nahi hai)",
        "Chinese (Simplified)": "不允许 (Bù yǔnxǔ)"
    },
    "quick": {
        "Hindi": "तेज़ (Tez)",
        "Chinese (Simplified)": "快的 (Kuài de)"
    },
    "quicker": {
        "Hindi": "तेज़तर (Teztar)",
        "Chinese (Simplified)": "更快的 (Gèng kuài de)"
    },
    "faster": {
        "Hindi": "तेज़तर (Teztar)",
        "Chinese (Simplified)": "更快的 (Gèng kuài de)"
    },
    "slower": {
        "Hindi": "धीमा (Dheema)",
        "Chinese (Simplified)": "更慢的 (Gèng màn de)"
    },
    "query": {
        "Hindi": "प्रश्न (Prashn)",
        "Chinese (Simplified)": "查询 (Cháxún)"
    },
    "complicated": {
        "Hindi": "जटिल (Jatil)",
        "Chinese (Simplified)": "复杂的 (Fùzá de)"
    },
    "complex": {
        "Hindi": "जटिल (Jatil)",
        "Chinese (Simplified)": "复杂的 (Fùzá de)"
    },
    "deal": {
        "Hindi": "सौदा (Sauda)",
        "Chinese (Simplified)": "交易 (Jiāoyì)"
    },
    "dealing": {
        "Hindi": "सौदा करना (Sauda karna)",
        "Chinese (Simplified)": "交易 (Jiāoyì)"
    },
    "advantage": {
        "Hindi": "लाभ (Laabh)",
        "Chinese (Simplified)": "优势 (Yōushì)"
    },
    "disadvantage": {
        "Hindi": "नुकसान (Nuksaan)",
        "Chinese (Simplified)": "劣势 (Lièshì)"
    },
    "i love to read books.": {
        "Hindi": "मुझे किताबें पढ़ना पसंद है। (Mujhe kitaabein padhna pasand hai.)",
        "Chinese (Simplified)": "我喜欢读书。 (Wǒ xǐhuān dúshū.)"
    },
    "she is a talented artist.": {
        "Hindi": "वह एक प्रतिभाशाली कलाकार है। (Vah ek pratibhāshālī kalākār hai.)",
        "Chinese (Simplified)": "她是一个有才华的艺术家。 (Tā shì yīgè yǒu cáihuá de yìshùjiā.)"
    },
    "he plays guitar very well.": {
        "Hindi": "वह गिटार बहुत अच्छा बजाता है। (Vah gītār bahut acchā bajātā hai.)",
        "Chinese (Simplified)": "他吉他弹得非常好。 (Tā jítā tán de fēicháng hǎo.)"
    },
    "we went to the park yesterday.": {
        "Hindi": "हम कल पार्क गए थे। (Ham kal pārk gaye the.)",
        "Chinese (Simplified)": "我们昨天去了公园。 (Wǒmen zuótiān qùle gōngyuán.)"
    },
    "they are studying for the exam.": {
        "Hindi": "वे परीक्षा की तैयारी कर रहे हैं। (Ve parīkṣā kī taiyārī kar rahe hain.)",
        "Chinese (Simplified)": "他们正在为考试学习。 (Tāmen zhèngzài wèi kǎoshì xuéxí.)"
    },
    "let's go for a walk.": {
        "Hindi": "चलो चलने चलते हैं। (Chalo chalne chalte hain.)",
        "Chinese (Simplified)": "我们去散步吧。 (Wǒmen qù sànbù ba.)"
    },
    "can you help me with this?": {
        "Hindi": "क्या आप मेरी इसमें मदद कर सकते हैं? (Kya āp meri ismein madad kar sakte hain?)",
        "Chinese (Simplified)": "你能帮我这个忙吗？ (Nǐ néng bāng wǒ zhège máng ma?)"
    },
    "i don't like spicy food.": {
        "Hindi": "मुझे मसालेदार खाना पसंद नहीं है। (Mujhe masāledār khānā pasand nahin hai.)",
        "Chinese (Simplified)": "我不喜欢辛辣的食物。 (Wǒ bù xǐhuān xīnlà de shíwù.)"
    },
    "he is a kind and gentle person.": {
        "Hindi": "वह एक दयालु और सौम्य व्यक्ति है। (Vah ek dayālu aur saumya vyakti hai.)",
        "Chinese (Simplified)": "他是一个善良温柔的人。 (Tā shì yīgè shànliáng wēnróu de rén.)"
    },
    "the sky is blue and clear.": {
        "Hindi": "आकाश नीला और साफ है। (Ākāsh nīlā aur sāf hai.)",
        "Chinese (Simplified)": "天空是蓝色而晴朗的。 (Tiānkōng shì lán sè ér qínglǎng de.)"
    },
    "i have a pet cat named Luna.": {
        "Hindi": "मेरे पास लूना नाम की पालतू बिल्ली है। (Mere pās Lūnā nām kī pāltū billi hai.)",
        "Chinese (Simplified)": "我有一只名叫卢娜的宠物猫。 (Wǒ yǒu yī zhī míng jiào Lúnà de chǒngwù māo.)"
    },
    "they are planning a surprise party.": {
        "Hindi": "वे एक सरप्राइज़ पार्टी की योजना बना रहे हैं। (Ve ek surprāiz pārtī kī yojnā banā rahe hain.)",
        "Chinese (Simplified)": "他们正在计划一个惊喜派对。 (Tāmen zhèngzài jìhuà yīgè jīngxǐ pàiduì.)"
    },
    "she is a very intelligent student.": {
        "Hindi": "वह एक बहुत ही बुद्धिमान छात्रा है। (Vah ek bahut hī buddhimān chātrā hai.)",
        "Chinese (Simplified)": "她是一个非常聪明的学生。 (Tā shì yīgè fēicháng cōngmíng de xuéshēng.)"
    },
    "he is a good listener.": {
        "Hindi": "वह एक अच्छा श्रोता है। (Vah ek acchā śrotā hai.)",
        "Chinese (Simplified)": "他是一个好的倾听者。 (Tā shì yīgè hǎo de qīngtīng zhě.)"
    },
    "the early bird catches the worm.": {
        "Hindi": "जल्दी उठने वाले को लाभ होता है। (Jaldī uṭhne vāle ko lābh hotā hai.)",
        "Chinese (Simplified)": "早起的鸟儿有虫吃。 (Zǎoqǐ de niǎo ér yǒu chóng chī.)"
    },
    "don't count your chickens before they hatch.": {
        "Hindi": "अंडे से चूजा निकलने से पहले उसकी गिनती मत करो। (Ande se chooja nikalne se pehle uski ginti mat karo.)",
        "Chinese (Simplified)": "不要高兴得太早。 (Bù yào gāo xìng de tài zǎo.)"
    },
    "practice makes perfect.": {
        "Hindi": "अभ्यास परफेक्ट बनाता है। (Abhyas perfect banata hai.)",
        "Chinese (Simplified)": "熟能生巧。 (Shú néng shēng qiǎo.)"
    },
    "time flies when you're having fun.": {
        "Hindi": "मज़े करते समय समय बहुत जल्दी बीत जाता है। (Maze karte samay samay bahut jaldi beet jata hai.)",
        "Chinese (Simplified)": "快乐的时光总是短暂的。 (Kuài lè de shí guāng zǒng shì duǎn zàn de.)"
    },
    "the grass is always greener on the other side.": {
        "Hindi": "दूरी के दर्शन अच्छे लगते हैं। (Dooree ke darshan acche lagte hain.)",
        "Chinese (Simplified)": "邻家更绿的草。 (Lín jiā gèng lǜ de cǎo.)"
    },
    "actions speak louder than words.": {
        "Hindi": "कर्म ही पूजा है। (Karm hi pooja hai.)",
        "Chinese (Simplified)": "行动胜于言语。 (Xíng dòng shèng yú yán yǔ.)"
    },
    "every cloud has a silver lining.": {
        "Hindi": "हर मुश्किल के बाद आसानी आती है। (Har mushkil ke baad aasani aati hai.)",
        "Chinese (Simplified)": "黑暗中总有一线希望。 (Hēi àn zhōng zǒng yǒu yī xiàn xī wàng.)"
    },
    "it's never too late to learn.": {
        "Hindi": "सीखने के लिए कभी देर नहीं होती। (Seekhne ke liye kabhi der nahi hoti.)",
        "Chinese (Simplified)": "活到老，学到老。 (Huó dào lǎo, xué dào lǎo.)"
    },
    "the pen is mightier than the sword.": {
        "Hindi": "कलम तलवार से ताकतवर होती है। (Kalam talwar se taqatvar hoti hai.)",
        "Chinese (Simplified)": "笔比剑更强大。 (Bǐ bǐ jiàn gèng qiáng dà.)"
    },
    "tutorial": {
        "Hindi": "ट्यूटोरियल (Tutorial)",
        "Chinese (Simplified)": "教程 (Jiào chéng)"
    },
    "wear": {
        "Hindi": "पहनना (Pehnna)",
        "Chinese (Simplified)": "穿 (Chuān)"
    },
    "journey": {
        "Hindi": "यात्रा (Yatra)",
        "Chinese (Simplified)": "旅程 (Lǚ chéng)"
    },
    "journey to the west": {
        "Hindi": "पश्चिम की यात्रा (Pashchim ki yatra)",
        "Chinese (Simplified)": "西游记 (Xī yóu jì)"
    },
    "freedom fighter": {
        "Hindi": "स्वतंत्रता सेनानी (Swatantrata senani)",
        "Chinese (Simplified)": "自由战士 (Zì yóu zhàn shì)"
    },
    "tourist": {
        "Hindi": "पर्यटक (Paryatak)",
        "Chinese (Simplified)": "游客 (Yóu kè)"
    },
    "comedy": {
        "Hindi": "कॉमेडी (Comedy)",
        "Chinese (Simplified)": "喜剧 (Xǐ jù)"
    },
    "comedian": {
        "Hindi": "कॉमेडियन (Comedian)",
        "Chinese (Simplified)": "喜剧演员 (Xǐ jù yǎn yuán)"
    },
    "check it": {
        "Hindi": "देखो (Dekho)",
        "Chinese (Simplified)": "看看 (Kàn kàn)"
    },
    "are you excited": {
        "Hindi": "क्या तुम उत्साहित हो? (Kya tum utsahit ho?)",
        "Chinese (Simplified)": "你兴奋吗？ (Nǐ xīng fèn ma?)"
    },
    "are you not excited": {
        "Hindi": "क्या तुम उत्साहित नहीं हो? (Kya tum utsahit nahi ho?)",
        "Chinese (Simplified)": "你不兴奋吗？ (Nǐ bù xīng fèn ma?)"
    },
    "why are you sad": {
        "Hindi": "तुम उदास क्यों हो? (Tum udaas kyun ho?)",
        "Chinese (Simplified)": "你为什么难过？ (Nǐ wèi shén me nán guò?)"
    },
    "hey come here": {
        "Hindi": "अरे यहाँ आओ (Are yahaan aao)",
        "Chinese (Simplified)": "嘿，过来 (Hēi, guò lái)"
    },
    "come here": {
        "Hindi": "यहाँ आओ (Yahaan aao)",
        "Chinese (Simplified)": "过来 (Guò lái)"
    },
    "go there": {
        "Hindi": "वहाँ जाओ (Vahaan jao)",
        "Chinese (Simplified)": "去那里 (Qù nà lǐ)"
    },
    "stop here": {
        "Hindi": "यहाँ रुक जाओ (Yahaan ruk jao)",
        "Chinese (Simplified)": "停在这里 (Tíng zài zhè lǐ)"
    },
    "stop there": {
        "Hindi": "वहाँ रुक जाओ (Vahaan ruk jao)",
        "Chinese (Simplified)": "停在那里 (Tíng zài nà lǐ)"
    },
    "that's it": {
        "Hindi": "बस इतना ही (Bas itna hi)",
        "Chinese (Simplified)": "就这些 (Jiù zhè xiē)"
    },
    "crisp": {
        "Hindi": "कुरकुरा (Kurkura)",
        "Chinese (Simplified)": "脆的 (Cuì de)"
    },
    "pretty": {
        "Hindi": "सुंदर (Sundar)",
        "Chinese (Simplified)": "漂亮的 (Piào liang de)"
    },
    "suspicious": {
        "Hindi": "संदिग्ध (Sandigdh)",
        "Chinese (Simplified)": "可疑的 (Kě yí de)"
    },
    "psychology": {
        "Hindi": "मनोविज्ञान (Manovigyaan)",
        "Chinese (Simplified)": "心理学 (Xīn lǐ xué)"
    },
    "tax": {
        "Hindi": "कर (Kar)",
        "Chinese (Simplified)": "税 (Shuì)"
    },
    "entropy": {
        "Hindi": "एन्ट्रॉपी (Entropy)",
        "Chinese (Simplified)": "熵 (Shāng)"
    },
    "breed": {
    "Hindi": "नस्ल (Nasl)",
    "Chinese (Simplified)": "品种 (Pǐnzhǒng)"
    },
    "cocoon": {
        "Hindi": "कोया (Koya)",
        "Chinese (Simplified)": "茧 (Jiǎn)"
    },
    "worm": {
        "Hindi": "कीड़ा (Keeda)",
        "Chinese (Simplified)": "虫子 (Chóngzi)"
    },
    "racoon": {
        "Hindi": "रैकून (Raccoon)",
        "Chinese (Simplified)": "浣熊 (Huànxióng)"
    },
    "guaranteed": {
        "Hindi": "गारंटीकृत (Guaranteekrit)",
        "Chinese (Simplified)": "保证的 (Bǎozhèng de)"
    },
    "ad": {
        "Hindi": "विज्ञापन (Vigyapan)",
        "Chinese (Simplified)": "广告 (Guǎnggào)"
    },
    "amazing scene": {
        "Hindi": "अद्भुत दृश्य (Adbhut Drishya)",
        "Chinese (Simplified)": "惊人的场景 (Jīngrén de Chǎngjǐng)"
    },
    "darling": {
        "Hindi": "प्रिय (Priya)",
        "Chinese (Simplified)": "亲爱的 (Qīn'ài de)"
    },
    "pickle": {
        "Hindi": "अचार (Achar)",
        "Chinese (Simplified)": "腌菜 (Yāncài)"
    },
    "chilly": {
        "Hindi": "ठंडा (Thanda)",
        "Chinese (Simplified)": "寒冷的 (Hánlěng de)"
    },
    "butterfly": {
        "Hindi": "तितली (Titli)",
        "Chinese (Simplified)": "蝴蝶 (Húdié)"
    },
    "troops": {
        "Hindi": "सैनिक (Sainik)",
        "Chinese (Simplified)": "部队 (Bùduì)"
    },
    "labor": {
        "Hindi": "मजदूरी (Mazdoori)",
        "Chinese (Simplified)": "劳动 (Láodòng)"
    },
    "raw": {
        "Hindi": "कच्चा (Kaccha)",
        "Chinese (Simplified)": "生的 (Shēng de)"
    },
    "extra": {
        "Hindi": "अतिरिक्त (Atirikt)",
        "Chinese (Simplified)": "额外的 (Éwài de)"
    },
    "cooked": {
        "Hindi": "पका हुआ (Paka Hua)",
        "Chinese (Simplified)": "煮熟的 (Zhǔshú de)"
    },
    "uncontrol": {
        "Hindi": "नियंत्रण से बाहर (Niyantran Se Bahar)",
        "Chinese (Simplified)": "失控 (Shīkòng)"
    },
    "automatic": {
        "Hindi": "स्वचालित (Swachalit)",
        "Chinese (Simplified)": "自动的 (Zìdòng de)"
    },
    "menu": {
        "Hindi": "मेन्यू (Menu)",
        "Chinese (Simplified)": "菜单 (Càidān)"
    },
    "manual": {
        "Hindi": "मैन्युअल (Manual)",
        "Chinese (Simplified)": "手动的 (Shǒudòng de)"
    },
    "custom": {
        "Hindi": "रिवाज (Rivaaj)",
        "Chinese (Simplified)": "习俗 (Xísú)"
    },
    "customize": {
        "Hindi": "अनुकूलित (Anukoolit)",
        "Chinese (Simplified)": "定制 (Dìngzhì)"
    },
    "getting": {
        "Hindi": "प्राप्त करना (Prapt Karna)",
        "Chinese (Simplified)": "获取 (Huòqǔ)"
    },
    "got it": {
        "Hindi": "समझ गया (Samajh Gaya)",
        "Chinese (Simplified)": "明白了 (Míngbái le)"
    },
    "using": {
        "Hindi": "उपयोग करना (Upyog Karna)",
        "Chinese (Simplified)": "使用中 (Shǐyòng zhōng)"
    },
    "used": {
        "Hindi": "प्रयुक्त (Prayukt)",
        "Chinese (Simplified)": "已使用 (Yǐ shǐyòng)"
    },
    "proper": {
        "Hindi": "उचित (Uchit)",
        "Chinese (Simplified)": "适当的 (Shìdàng de)"
    },
    "climb": {
        "Hindi": "चढ़ाई करना (Chadhai Karna)",
        "Chinese (Simplified)": "爬 (Pá)"
    },
    "pickaxe": {
        "Hindi": "कुदाल (Kudal)",
        "Chinese (Simplified)": "镐 (Hào)"
    },
    "hammer": {
        "Hindi": "हथौड़ा (Hathoda)",
        "Chinese (Simplified)": "锤子 (Chuízi)"
    },
    "wrench": {
        "Hindi": "पाना (Pana)",
        "Chinese (Simplified)": "扳手 (Bānshǒu)"
    },
    "built": {
        "Hindi": "निर्मित (Nirmit)",
        "Chinese (Simplified)": "建造的 (Jiànzào de)"
    },
    "looking": {
        "Hindi": "देख रहे (Dekh Rahe)",
        "Chinese (Simplified)": "正在看 (Zhèngzài kàn)"
    },
    "topic": {
        "Hindi": "विषय (Vishay)",
        "Chinese (Simplified)": "话题 (Huàtí)"
    },
    "subject": {
        "Hindi": "विषय (Vishay)",
        "Chinese (Simplified)": "主题 (Zhǔtí)"
    },
    "hypocrisy": {
        "Hindi": "पाखंड (Pakhanda)",
        "Chinese (Simplified)": "虚伪 (Xūwěi)"
    },
    "limit": {
        "Hindi": "सीमा (Seema)",
        "Chinese (Simplified)": "限制 (Xiànzhì)"
    },
    "irony": {
        "Hindi": "विडंबना (Vidambana)",
        "Chinese (Simplified)": "讽刺 (Fěngcì)"
    },
    "limited": {
        "Hindi": "सीमित (Seemit)",
        "Chinese (Simplified)": "有限的 (Yǒuxiàn de)"
    },
    "unlimited": {
        "Hindi": "असीमित (Aseemit)",
        "Chinese (Simplified)": "无限的 (Wúxiàn de)"
    },
    "whistle": {
        "Hindi": "सीटी (seetee)",
        "Chinese (Simplified)": "吹口哨 (chuī kǒushào)"
    },
    "wiggle": {
        "Hindi": "लचकना (lachakna)",
        "Chinese (Simplified)": "摆动 (bǎidòng)"
    },
    "jiggle": {
        "Hindi": "हिलाना (hilaana)",
        "Chinese (Simplified)": "晃动 (huàngdòng)"
    },
    "require": {
        "Hindi": "आवश्यक होना (aavashyak hona)",
        "Chinese (Simplified)": "需要 (xūyào)"
    },
    "requirement": {
        "Hindi": "आवश्यकता (aavashyakta)",
        "Chinese (Simplified)": "要求 (yāoqiú)"
    },
    "course": {
        "Hindi": "पाठ्यक्रम (paathyakram)",
        "Chinese (Simplified)": "课程 (kèchéng)"
    },
    "blow": {
        "Hindi": "फूंक मारना (phoonk maarna)",
        "Chinese (Simplified)": "吹 (chuī)"
    },
    "blowing": {
        "Hindi": "फूंकना (phoonkna)",
        "Chinese (Simplified)": "吹动 (chuī dòng)"
    },
    "soul": {
        "Hindi": "आत्मा (aatma)",
        "Chinese (Simplified)": "灵魂 (línghún)"
    },
    "coal": {
        "Hindi": "कोयला (koyla)",
        "Chinese (Simplified)": "煤炭 (méitàn)"
    },
    "pole": {
        "Hindi": "डंडा (danda)",
        "Chinese (Simplified)": "杆 (gǎn)"
    },
    "slip": {
        "Hindi": "फिसलना (fisalna)",
        "Chinese (Simplified)": "滑倒 (huádǎo)"
    },
    "extinct": {
        "Hindi": "विलुप्त (vilupt)",
        "Chinese (Simplified)": "灭绝 (mièjué)"
    },
    "count": {
        "Hindi": "गिनती करना (ginti karna)",
        "Chinese (Simplified)": "计算 (jìsuàn)"
    },
    "less than": {
        "Hindi": "से कम (se kam)",
        "Chinese (Simplified)": "少于 (shǎoyú)"
    },
    "ethical": {
        "Hindi": "नैतिक (naitik)",
        "Chinese (Simplified)": "伦理的 (lúnlǐ de)"
    },
    "unethical": {
        "Hindi": "अनैतिक (anaitik)",
        "Chinese (Simplified)": "不道德的 (bù dàodé de)"
    },
    "income": {
        "Hindi": "आय (aay)",
        "Chinese (Simplified)": "收入 (shōurù)"
    },
    "salary": {
        "Hindi": "वेतन (vetan)",
        "Chinese (Simplified)": "工资 (gōngzī)"
    },
    "moving": {
        "Hindi": "चलना (chalna)",
        "Chinese (Simplified)": "移动 (yídòng)"
    },
    "moving abroad": {
        "Hindi": "विदेश जाना (videsh jaana)",
        "Chinese (Simplified)": "移居国外 (yíjū guówài)"
    },
    "moved abroad": {
        "Hindi": "विदेश चले गए (videsh chale gaye)",
        "Chinese (Simplified)": "搬到国外 (bān dào guówài)"
    },
    "foundation": {
        "Hindi": "आधार (aadhar)",
        "Chinese (Simplified)": "基础 (jīchǔ)"
    },
    "capital": {
        "Hindi": "पूंजी (poonji)",
        "Chinese (Simplified)": "资本 (zīběn)"
    },
    "capital city": {
        "Hindi": "राजधानी (raajdhaani)",
        "Chinese (Simplified)": "首都 (shǒudū)"
    },
    "library": {
        "Hindi": "पुस्तकालय (pustakalay)",
        "Chinese (Simplified)": "图书馆 (túshūguǎn)"
    },
    "border": {
        "Hindi": "सीमा (seema)",
        "Chinese (Simplified)": "边界 (biānjiè)"
    },
    "dispute": {
        "Hindi": "विवाद (vivad)",
        "Chinese (Simplified)": "争端 (zhēngduān)"
    },
    "come back": {
        "Hindi": "वापस आना (wapas aana)",
        "Chinese (Simplified)": "回来 (huílái)"
    },
    "celebrate": {
        "Hindi": "जश्न मनाना (jashn manana)",
        "Chinese (Simplified)": "庆祝 (qìngzhù)"
    },
    "congrats": {
        "Hindi": "बधाई (badhai)",
        "Chinese (Simplified)": "恭喜 (gōngxǐ)"
    },
    "congratulation": {
        "Hindi": "शुभकामना (shubhkaamna)",
        "Chinese (Simplified)": "祝贺 (zhùhè)"
    },
    "work culture": {
        "Hindi": "कार्य संस्कृति (karya sanskriti)",
        "Chinese (Simplified)": "工作文化 (gōngzuò wénhuà)"
    },
    "drill": {
        "Hindi": "ड्रिल (drill) / अभ्यास (abhyas)",
        "Chinese (Simplified)": "钻孔 (zuānkǒng) / 演练 (yǎnliàn)"
    },
    "free of charge": {
        "Hindi": "निःशुल्क (nishulk)",
        "Chinese (Simplified)": "免费 (miǎnfèi)"
    },
    "sale": {
        "Hindi": "बिक्री (bikri)",
        "Chinese (Simplified)": "销售 (xiāoshòu)"
    },
    "publish": {
        "Hindi": "प्रकाशित करना (prakaashit karna)",
        "Chinese (Simplified)": "出版 (chūbǎn)"
    },
    "publisher": {
        "Hindi": "प्रकाशक (prakaashak)",
        "Chinese (Simplified)": "出版商 (chūbǎn shāng)"
    },
    "bill": {
        "Hindi": "बिल (bill)",
        "Chinese (Simplified)": "账单 (zhàngdān)"
    },
    "partition": {
        "Hindi": "विभाजन (vibhaajan)",
        "Chinese (Simplified)": "分隔 (fēngé)"
    },
    "overview": {
        "Hindi": "सारांश (saaraansh)",
        "Chinese (Simplified)": "概述 (gàishù)"
    },
    "overall": {
        "Hindi": "कुल मिलाकर (kul milakar)",
        "Chinese (Simplified)": "总体 (zǒngtǐ)"
    },
    "mixed": {
        "Hindi": "मिश्रित (mishrit)",
        "Chinese (Simplified)": "混合 (hùnhé)"
    },
    "ethnicity": {
        "Hindi": "जातीयता (jaatiyata)",
        "Chinese (Simplified)": "种族 (zhǒngzú)"
    },
    "ethnic": {
        "Hindi": "जातीय (jaatiya)",
        "Chinese (Simplified)": "民族的 (mínzú de)"
    },
    "university": {
        "Hindi": "विश्वविद्यालय (vishwavidyalay)",
        "Chinese (Simplified)": "大学 (dàxué)"
    },
    "relate": {
        "Hindi": "संबंधित करना (sambandhit karna)",
        "Chinese (Simplified)": "关联 (guānlián)"
    },
    "relatives": {
        "Hindi": "रिश्तेदार (rishtedaar)",
        "Chinese (Simplified)": "亲戚 (qīnqì)"
    },
    "related": {
        "Hindi": "संबंधित (sambandhit)",
        "Chinese (Simplified)": "相关的 (xiāngguān de)"
    },
    "unrelated": {
        "Hindi": "असंबंधित (asambandhit)",
        "Chinese (Simplified)": "无关的 (wúguān de)"
    },
    "copied": {
        "Hindi": "नकल की (nakal ki)",
        "Chinese (Simplified)": "复制的 (fùzhì de)"
    },
    "copying": {
        "Hindi": "नकल करना (nakal karna)",
        "Chinese (Simplified)": "复制 (fùzhì)"
    },
    "known": {
        "Hindi": "ज्ञात (gyaat)",
        "Chinese (Simplified)": "已知的 (yǐzhī de)"
    },
    "unknown": {
        "Hindi": "अज्ञात (agyaat)",
        "Chinese (Simplified)": "未知的 (wèizhī de)"
    },
    "army": {
        "Hindi": "सेना (sena)",
        "Chinese (Simplified)": "军队 (jūnduì)"
    },
    "checkmate": {
        "Hindi": "शह और मात (shah aur maat)",
        "Chinese (Simplified)": "将军 (jiàngjūn)"
    },
    "checkout": {
        "Hindi": "चेकआउट (checkout) / भुगतान (bhugtaan)",
        "Chinese (Simplified)": "结账 (jiézhàng)"
    },
    "yourself": {
        "Hindi": "खुद (khud)",
        "Chinese (Simplified)": "你自己 (nǐ zìjǐ)"
    },
    "wonder": {
        "Hindi": "आश्चर्य (aashcharya)",
        "Chinese (Simplified)": "奇迹 (qíjì) / 想知道 (xiǎng zhīdào)"
    },
    "wondering": {
        "Hindi": "सोच रहा हूँ (soch raha hoon)",
        "Chinese (Simplified)": "在想 (zài xiǎng)"
    },
    "lying": {
        "Hindi": "झूठ बोलना (jhooth bolna)",
        "Chinese (Simplified)": "撒谎 (sāhuǎng)"
    },
    "lied": {
        "Hindi": "झूठ बोला (jhooth bola)",
        "Chinese (Simplified)": "撒了谎 (sāle huǎng)"
    },
    "dig": {
        "Hindi": "खोदना (khodna)",
        "Chinese (Simplified)": "挖 (wā)"
    },
    "motivational": {
        "Hindi": "प्रेरणादायक (prernaadayak)",
        "Chinese (Simplified)": "励志的 (lìzhì de)"
    },
    "motivate": {
        "Hindi": "प्रेरित करना (prerit karna)",
        "Chinese (Simplified)": "激励 (jīlì)"
    },
    "singular": {
        "Hindi": "एकवचन (ekvachan)",
        "Chinese (Simplified)": "单数 (dānshù)"
    },
    "happy in life": {
        "Hindi": "जीवन में खुश (jeevan mein khush)",
        "Chinese (Simplified)": "生活幸福 (shēnghuó xìngfú)"
    },
    "sad in life": {
        "Hindi": "जीवन में उदास (jeevan mein udaas)",
        "Chinese (Simplified)": "生活悲伤 (shēnghuó bēishāng)"
    },
    "jimmy": {
        "Hindi": "जिमी (Jimmy)",
        "Chinese (Simplified)": "吉米 (Jímǐ)"
    },
    "jam": {
        "Hindi": "जाम (jam) / मुरब्बा (murabba)",
        "Chinese (Simplified)": "果酱 (guǒjiàng)"
    },
    "honey": {
        "Hindi": "शहद (shahad)",
        "Chinese (Simplified)": "蜂蜜 (fēngmì)"
    },
    "growth": {
        "Hindi": "विकास (vikas)",
        "Chinese (Simplified)": "增长 (zēngzhǎng)"
    },
    "too": {
        "Hindi": "भी (bhi)",
        "Chinese (Simplified)": "也 (yě)"
    },
    "fun fact": {
        "Hindi": "रोचक तथ्य (rochak tathya)",
        "Chinese (Simplified)": "趣闻 (qùwén)"
    },
    "fact": {
        "Hindi": "तथ्य (tathya)",
        "Chinese (Simplified)": "事实 (shìshí)"
    },
    "portfolio": {
        "Hindi": "पोर्टफोलियो (portfolio)",
        "Chinese (Simplified)": "作品集 (zuòpǐn jí)"
    },
    "firecrackers": {
        "Hindi": "पटाखे (patakhe)",
        "Chinese (Simplified)": "烟花爆竹 (yānhuā bàozhú)"
    },
    "organize": {
        "Hindi": "आयोजित करना (aayojit karna)",
        "Chinese (Simplified)": "组织 (zǔzhī)"
    },
    "organizing": {
        "Hindi": "व्यवस्थित करना (vyavasthit karna)",
        "Chinese (Simplified)": "正在组织 (zhèngzài zǔzhī)"
    },
    "organized": {
        "Hindi": "संगठित (sangathit)",
        "Chinese (Simplified)": "已组织 (yǐ zǔzhī)"
    },
    "struggle": {
        "Hindi": "संघर्ष (sangharsh)",
        "Chinese (Simplified)": "奋斗 (fèndòu)"
    },
    "annoy": {
        "Hindi": "परेशान करना (pareshaan karna)",
        "Chinese (Simplified)": "烦扰 (fánrǎo)"
    },
    "irritate": {
        "Hindi": "चिढ़ाना (chidhaana)",
        "Chinese (Simplified)": "激怒 (jīnù)"
    },
    "annoyed": {
        "Hindi": "परेशान (pareshaan)",
        "Chinese (Simplified)": "烦恼的 (fánnǎo de)"
    },
    "annoying": {
        "Hindi": "परेशान करने वाला (pareshaan karne wala)",
        "Chinese (Simplified)": "令人烦恼的 (lìngrén fánnǎo de)"
    },
    "we are": {
        "Hindi": "हम हैं (hum hain)",
        "Chinese (Simplified)": "我们是 (wǒmen shì)"
    },
    "irritated": {
        "Hindi": "चिढ़ा हुआ (chidha hua)",
        "Chinese (Simplified)": "被激怒的 (bèi jīnù de)"
    },
    "irritating": {
        "Hindi": "चिढ़ाने वाला (chidhaane wala)",
        "Chinese (Simplified)": "令人恼火的 (lìngrén nǎohuǒ de)"
    },
    "nominate": {
        "Hindi": "नामांकित करना (naamankit karna)",
        "Chinese (Simplified)": "提名 (tímíng)"
    },
    "physical health": {
        "Hindi": "शारीरिक स्वास्थ्य (sharirik swasthya)",
        "Chinese (Simplified)": "身体健康 (shēntǐ jiànkāng)"
    },
    "mental health": {
        "Hindi": "मानसिक स्वास्थ्य (maanasik swasthya)",
        "Chinese (Simplified)": "心理健康 (xīnlǐ jiànkāng)"
    },
    "yoga": {
        "Hindi": "योग (yog)",
        "Chinese (Simplified)": "瑜伽 (yújiā)"
    },
    "siu": {
        "Hindi": "सिउ (siu)",
        "Chinese (Simplified)": "咻 (xiū)"
    },
    "suit": {
        "Hindi": "सूट (suit)",
        "Chinese (Simplified)": "西装 (xīzhuāng)"
    },
    "boot": {
        "Hindi": "बूट (boot)",
        "Chinese (Simplified)": "靴子 (xuēzi)"
    },
    "sneakers": {
        "Hindi": "स्पोर्ट्स जूते (sports joote)",
        "Chinese (Simplified)": "运动鞋 (yùndòngxié)"
    },
    "skirt": {
        "Hindi": "स्कर्ट (skirt)",
        "Chinese (Simplified)": "裙子 (qúnzi)"
    },
    "shorts": {
        "Hindi": "शॉर्ट्स (shorts)",
        "Chinese (Simplified)": "短裤 (duǎnkù)"
    },
    "lose": {
        "Hindi": "हारना (haarna)",
        "Chinese (Simplified)": "失去 (shīqù)"
    },
    "paragraph": {
        "Hindi": "अनुच्छेद (anuchhed)",
        "Chinese (Simplified)": "段落 (duànluò)"
    },
    "object": {
        "Hindi": "वस्तु (vastu)",
        "Chinese (Simplified)": "物体 (wùtǐ)"
    },
    "odd": {
        "Hindi": "विषम (visham)",
        "Chinese (Simplified)": "奇数 (jīshù)"
    },
    "even": {
        "Hindi": "सम (sam)",
        "Chinese (Simplified)": "偶数 (ǒushù)"
    },
    "arrest": {
        "Hindi": "गिरफ्तारी (girftaari)",
        "Chinese (Simplified)": "逮捕 (dàibǔ)"
    },
    "correct": {
        "Hindi": "सही (sahi)",
        "Chinese (Simplified)": "正确的 (zhèngquè de)"
    },
    "biased": {
        "Hindi": "पक्षपाती (pakshpati)",
        "Chinese (Simplified)": "有偏见的 (yǒu piānjiàn de)"
    },
    "obsessed": {
        "Hindi": "मग्न (magn)",
        "Chinese (Simplified)": "痴迷的 (chīmí de)"
    },
    "hood": {
        "Hindi": "हुड (hood)",
        "Chinese (Simplified)": "兜帽 (dōumào)"
    },
    "article": {
        "Hindi": "लेख (lekh)",
        "Chinese (Simplified)": "文章 (wénzhāng)"
    },
    "track": {
        "Hindi": "पथ (path) / ट्रैक (track)",
        "Chinese (Simplified)": "轨道 (guǐdào)"
    },
    "associate": {
        "Hindi": "संबंधित करना (sambandhit karna)",
        "Chinese (Simplified)": "关联 (guānlián)"
    },
    "association": {
        "Hindi": "संगठन (sangathan)",
        "Chinese (Simplified)": "协会 (xiéhuì)"
    },
    "content": {
        "Hindi": "सामग्री (saamagri)",
        "Chinese (Simplified)": "内容 (nèiróng)"
    },
    "general": {
        "Hindi": "सामान्य (saamanya)",
        "Chinese (Simplified)": "一般的 (yībān de)"
    },
    "magazine": {
        "Hindi": "पत्रिका (patrika)",
        "Chinese (Simplified)": "杂志 (zázhì)"
    },
    "definition": {
        "Hindi": "परिभाषा (paribhaasha)",
        "Chinese (Simplified)": "定义 (dìngyì)"
    },
    "type": {
        "Hindi": "प्रकार (prakaar)",
        "Chinese (Simplified)": "类型 (lèixíng)"
    },
    "scholar": {
        "Hindi": "विद्वान (vidvaan)",
        "Chinese (Simplified)": "学者 (xuézhě)"
    },
    "grammer": {
        "Hindi": "व्याकरण (vyaakaran)",
        "Chinese (Simplified)": "语法 (yǔfǎ)"
    },
    "often": {
        "Hindi": "अक्सर (aksar)",
        "Chinese (Simplified)": "经常 (jīngcháng)"
    },
    "rare": {
        "Hindi": "दुर्लभ (durlabh)",
        "Chinese (Simplified)": "稀有的 (xīyǒu de)"
    },
    "rarely": {
        "Hindi": "कभी-कभार (kabhi-kabhaar)",
        "Chinese (Simplified)": "很少 (hěn shǎo)"
    },
    "mean": {
        "Hindi": "मतलब (matlab)",
        "Chinese (Simplified)": "意思 (yìsi)"
    },
    "meaning": {
        "Hindi": "अर्थ (arth)",
        "Chinese (Simplified)": "意义 (yìyì)"
    },
    "what does mean": {
        "Hindi": "क्या मतलब है (kya matlab hai)",
        "Chinese (Simplified)": "是什么意思 (shì shénme yìsi)"
    },
    "knew": {
        "Hindi": "पता था (pata tha)",
        "Chinese (Simplified)": "知道了 (zhīdào le)"
    },
    "typical": {
        "Hindi": "सामान्य (saamanya)",
        "Chinese (Simplified)": "典型的 (diǎnxíng de)"
    },
    "intense": {
        "Hindi": "तीव्र (teevra)",
        "Chinese (Simplified)": "强烈的 (qiángliè de)"
    },
    "vibe": {
        "Hindi": "माहौल (maahaul)",
        "Chinese (Simplified)": "氛围 (fēnwéi)"
    },
    "intention": {
        "Hindi": "इरादा (irada)",
        "Chinese (Simplified)": "意图 (yìtú)"
    },
    "intentional": {
        "Hindi": "जानबूझकर (jaanboojhkar)",
        "Chinese (Simplified)": "故意的 (gùyì de)"
    },
    "panic": {
        "Hindi": "घबराहट (ghabaraahat)",
        "Chinese (Simplified)": "恐慌 (kǒnghuāng)"
    },
    "mode": {
        "Hindi": "मोड (mode)",
        "Chinese (Simplified)": "模式 (móshì)"
    },
    "heart": {
        "Hindi": "दिल (dil)",
        "Chinese (Simplified)": "心脏 (xīnzàng)"
    },
    "heart attack": {
        "Hindi": "दिल का दौरा (dil ka daura)",
        "Chinese (Simplified)": "心脏病发作 (xīnzàng bìng fāzuò)"
    },
    "stone": {
        "Hindi": "पत्थर (patthar)",
        "Chinese (Simplified)": "石头 (shítou)"
    },
    "defending": {
        "Hindi": "रक्षा करना (raksha karna)",
        "Chinese (Simplified)": "防守 (fángshǒu)"
    },
    "defender": {
        "Hindi": "रक्षक (rakshak)",
        "Chinese (Simplified)": "防守者 (fángshǒu zhě)"
    },
    "corner": {
        "Hindi": "कोना (kona)",
        "Chinese (Simplified)": "角落 (jiǎoluò)"
    },
    "laughing": {
        "Hindi": "हंसना (hansna)",
        "Chinese (Simplified)": "笑 (xiào)"
    },
    "traveler": {
        "Hindi": "यात्री (yaatri)",
        "Chinese (Simplified)": "旅行者 (lǚxíng zhě)"
    },
    "procrastination": {
        "Hindi": "टालमटोल (taalmatol)",
        "Chinese (Simplified)": "拖延 (tuōyán)"
    },
    "speaking": {
        "Hindi": "बोलना (bolna)",
        "Chinese (Simplified)": "说话 (shuōhuà)"
    },
    "mope": {
        "Hindi": "उदास रहना (udaas rehna)",
        "Chinese (Simplified)": "闷闷不乐 (mènmèn bù lè)"
    },
    "mature": {
        "Hindi": "परिपक्व (paripakva)",
        "Chinese (Simplified)": "成熟 (chéngshú)"
    },
    "innocent": {
        "Hindi": "निर्दोष (nirdosh)",
        "Chinese (Simplified)": "无辜 (wúgū)"
    },
    "curly": {
        "Hindi": "घुंघराले (ghunghrale)",
        "Chinese (Simplified)": "卷曲的 (juǎnqū de)"
    },
    "puppet": {
        "Hindi": "कठपुतली (kathputli)",
        "Chinese (Simplified)": "木偶 (mù'ǒu)"
    },
    "doll": {
        "Hindi": "गुड़िया (gudiya)",
        "Chinese (Simplified)": "玩偶 (wán'ǒu)"
    },
    "teen": {
        "Hindi": "किशोर (kishor)",
        "Chinese (Simplified)": "青少年 (qīngshàonián)"
    },
    "load": {
        "Hindi": "भार (bhar)",
        "Chinese (Simplified)": "负载 (fùzài)"
    },
    "scout": {
        "Hindi": "जासूस (jasoos)",
        "Chinese (Simplified)": "侦察员 (zhēncháyuán)"
    },
    "fellow": {
        "Hindi": "साथी (saathi)",
        "Chinese (Simplified)": "伙伴 (huǒbàn)"
    },
    "rotten": {
        "Hindi": "सड़ा हुआ (sada hua)",
        "Chinese (Simplified)": "腐烂的 (fǔlàn de)"
    },
    "flesh": {
        "Hindi": "मांस (maans)",
        "Chinese (Simplified)": "肉 (ròu)"
    },
    "surgery": {
        "Hindi": "शल्य चिकित्सा (shalya chikitsa)",
        "Chinese (Simplified)": "手术 (shǒushù)"
    },
    "pardon": {
        "Hindi": "क्षमा (kshama)",
        "Chinese (Simplified)": "原谅 (yuánliàng)"
    },
    "courage": {
        "Hindi": "साहस (sahas)",
        "Chinese (Simplified)": "勇气 (yǒngqì)"
    },
    "coward": {
        "Hindi": "कायर (kayar)",
        "Chinese (Simplified)": "懦夫 (nuòfū)"
    },
    "cowardly": {
        "Hindi": "कायरता (kayarta)",
        "Chinese (Simplified)": "胆小的 (dǎnxiǎo de)"
    },
    "swear": {
        "Hindi": "शपथ लेना (shapath lena)",
        "Chinese (Simplified)": "发誓 (fāshì)"
    },
    "mask": {
        "Hindi": "मुखौटा (mukhauta)",
        "Chinese (Simplified)": "面具 (miànjù)"
    },
    "draft": {
        "Hindi": "प्रारूप (praaroop)",
        "Chinese (Simplified)": "草稿 (cǎogǎo)"
    },
    "listed": {
        "Hindi": "सूचीबद्ध (soochibaddh)",
        "Chinese (Simplified)": "列出的 (lièchū de)"
    },
    "unnatural": {
        "Hindi": "अप्राकृतिक (apraakritik)",
        "Chinese (Simplified)": "不自然的 (bù zìrán de)"
    },
    "dowry": {
        "Hindi": "दहेज (dahej)",
        "Chinese (Simplified)": "嫁妆 (jiàzhuāng)"
    },
    "universe": {
        "Hindi": "ब्रह्मांड (brahmaand)",
        "Chinese (Simplified)": "宇宙 (yǔzhòu)"
    },
    "multiple": {
        "Hindi": "कई (kai)",
        "Chinese (Simplified)": "多个 (duō gè)"
    },
    "unbreaking": {
        "Hindi": "अटूट (aṭūṭ)",
        "Chinese (Simplified)": "不破的 (bù pò de)"
    },
    "moron": {
        "Hindi": "मूर्ख (mūrkh)",
        "Chinese (Simplified)": "傻瓜 (shǎguā)"
    },
    "bald": {
        "Hindi": "गंजा (ganjā)",
        "Chinese (Simplified)": "秃头 (tūtóu)"
    },
    "ship": {
        "Hindi": "जहाज (jahāj)",
        "Chinese (Simplified)": "船 (chuán)"
    },
    "sip": {
        "Hindi": "घूंट (ghūnṭ)",
        "Chinese (Simplified)": "小口喝 (xiǎo kǒu hē)"
    },
    "whoop": {
        "Hindi": "जयकार (jaikār)",
        "Chinese (Simplified)": "欢呼 (huānhū)"
    },
    "martial law": {
        "Hindi": "सैन्य कानून (sainya kānūn)",
        "Chinese (Simplified)": "戒严法 (jièyán fǎ)"
    },
    "dictatorship": {
        "Hindi": "तानाशाही (tānāshāhī)",
        "Chinese (Simplified)": "独裁 (dúcái)"
    },
    "democracy": {
        "Hindi": "लोकतंत्र (loktantra)",
        "Chinese (Simplified)": "民主 (mínzhǔ)"
    },
    "heavy": {
        "Hindi": "भारी (bhārī)",
        "Chinese (Simplified)": "重的 (zhòng de)"
    },
    "issue": {
        "Hindi": "मुद्दा (mudda)",
        "Chinese (Simplified)": "问题 (wèntí)"
    },
    "around the world": {
        "Hindi": "दुनिया भर में (duniyā bhar mein)",
        "Chinese (Simplified)": "全世界 (quán shìjiè)"
    },
    "titan": {
        "Hindi": "महानायक (mahānāyak)",
        "Chinese (Simplified)": "巨人 (jùrén)"
    },
    "merge": {
        "Hindi": "विलय करना (vilay karnā)",
        "Chinese (Simplified)": "合并 (hébìng)"
    },
    "quiz": {
        "Hindi": "प्रश्नोत्तरी (prashnottarī)",
        "Chinese (Simplified)": "测验 (cèyàn)"
    },
    "strip": {
        "Hindi": "पट्टी (paṭṭī)",
        "Chinese (Simplified)": "条 (tiáo)"
    },
    "useless": {
        "Hindi": "बेकार (bekār)",
        "Chinese (Simplified)": "无用的 (wúyòng de)"
    },
    "invaders": {
        "Hindi": "आक्रमणकारी (ākramaṇkārī)",
        "Chinese (Simplified)": "侵略者 (qīnlüè zhě)"
    },
    "natives": {
        "Hindi": "स्थानीय (sthānīya)",
        "Chinese (Simplified)": "本地人 (běndì rén)"
    },
    "brutal": {
        "Hindi": "क्रूर (krūr)",
        "Chinese (Simplified)": "残忍的 (cánrěn de)"
    },
    "brutally": {
        "Hindi": "निर्दयता से (nirdayatā se)",
        "Chinese (Simplified)": "残酷地 (cánkù de)"
    },
    "long hairs": {
        "Hindi": "लंबे बाल (lambe bāl)",
        "Chinese (Simplified)": "长头发 (cháng tóufa)"
    },
    "silk": {
        "Hindi": "रेशम (resham)",
        "Chinese (Simplified)": "丝绸 (sīchóu)"
    },
    "silky": {
        "Hindi": "रेशमी (reshamī)",
        "Chinese (Simplified)": "丝滑的 (sī huá de)"
    },
    "rough": {
        "Hindi": "खुरदरा (khurdarā)",
        "Chinese (Simplified)": "粗糙的 (cūcāo de)"
    },
    "fair": {
        "Hindi": "साफ (sāf)",
        "Chinese (Simplified)": "公平的 (gōngpíng de)"
    },
    "analyze": {
        "Hindi": "विश्लेषण करना (vishleṣaṇ karnā)",
        "Chinese (Simplified)": "分析 (fēnxī)"
    },
    "disrespect": {
        "Hindi": "असम्मान (asamman)",
        "Chinese (Simplified)": "不尊重 (bù zūnzhòng)"
    },
    "estimate": {
        "Hindi": "अनुमान (anumān)",
        "Chinese (Simplified)": "估计 (gūjì)"
    },
    "fool": {
        "Hindi": "बेवकूफ (bevakūph)",
        "Chinese (Simplified)": "傻瓜 (shǎguā)"
    },
    "grateful": {
        "Hindi": "आभारी (ābhārī)",
        "Chinese (Simplified)": "感激的 (gǎnjī de)"
    },
    "ban": {
        "Hindi": "प्रतिबंध (pratibandh)",
        "Chinese (Simplified)": "禁止 (jìnzhǐ)"
    },
    "cruel": {
        "Hindi": "क्रूर (krūr)",
        "Chinese (Simplified)": "残忍的 (cánrěn de)"
    },
    "hit": {
        "Hindi": "मारना (mārnā)",
        "Chinese (Simplified)": "打 (dǎ)"
    },
    "beat": {
        "Hindi": "पीटना (pīṭnā)",
        "Chinese (Simplified)": "击打 (jīdǎ)"
    },
    "keep": {
        "Hindi": "रखना (rakhnā)",
        "Chinese (Simplified)": "保持 (bǎochí)"
    },
    "mess": {
        "Hindi": "गड़बड़ (gaḍbaḍ)",
        "Chinese (Simplified)": "混乱 (hùnluàn)"
    },
    "messing": {
        "Hindi": "गड़बड़ करना (gaḍbaḍ karnā)",
        "Chinese (Simplified)": "搞乱 (gǎo luàn)"
    },
    "act": {
        "Hindi": "कार्य (kārya)",
        "Chinese (Simplified)": "行动 (xíngdòng)"
    },
    "acting": {
        "Hindi": "अभिनय (abhinay)",
        "Chinese (Simplified)": "表演 (biǎoyǎn)"
    },
    "toast": {
        "Hindi": "टोस्ट (ṭosṭ)",
        "Chinese (Simplified)": "吐司 (tǔsī)"
    },
    "slightly": {
        "Hindi": "थोड़ा (thodā)",
        "Chinese (Simplified)": "稍微 (shāowēi)"
    },
    "whispers": {
        "Hindi": "फुसफुसाहट (fusfusāhaṭ)",
        "Chinese (Simplified)": "耳语 (ěryǔ)"
    },
    "whispered": {
        "Hindi": "फुसफुसाया (fusfusāyā)",
        "Chinese (Simplified)": "低声说 (dīshēng shuō)"
    },
    "whispering": {
        "Hindi": "फुसफुसाते हुए (fusfusāte huye)",
        "Chinese (Simplified)": "低声耳语 (dīshēng ěryǔ)"
    },
    "drink up": {
        "Hindi": "पी लो (pī lo)",
        "Chinese (Simplified)": "喝完 (hē wán)"
    },
    "cake": {
        "Hindi": "केक (kek)",
        "Chinese (Simplified)": "蛋糕 (dàngāo)"
    },
    "occasional": {
        "Hindi": "मौक़े पर (mauqe par)",
        "Chinese (Simplified)": "偶尔的 (ǒu'ěr de)"
    },
    "occasionally": {
        "Hindi": "कभी-कभी (kabhi-kabhi)",
        "Chinese (Simplified)": "偶尔 (ǒu'ěr)"
    },
    "alternate": {
        "Hindi": "वैकल्पिक (vaikalpik)",
        "Chinese (Simplified)": "交替的 (jiāotì de)"
    },
    "moan": {
        "Hindi": "कराह (karāh)",
        "Chinese (Simplified)": "呻吟 (shēnyín)"
    },
    "alternative": {
        "Hindi": "विकल्प (vikalp)",
        "Chinese (Simplified)": "替代方案 (tìdài fāng'àn)"
    },
    "invitation": {
        "Hindi": "निमंत्रण (nimantraṇ)",
        "Chinese (Simplified)": "邀请 (yāoqǐng)"
    },
    "invite": {
        "Hindi": "आमंत्रित करना (āmantrit karnā)",
        "Chinese (Simplified)": "邀请 (yāoqǐng)"
    },
    "lust": {
        "Hindi": "वासना (vāsanā)",
        "Chinese (Simplified)": "欲望 (yùwàng)"
    },
    "treat": {
        "Hindi": "इलाज करना (ilāj karnā)",
        "Chinese (Simplified)": "对待 (duìdài)"
    },
    "special treat": {
        "Hindi": "विशेष भोज (viśeṣ bhoj)",
        "Chinese (Simplified)": "特别款待 (tèbié kuǎndài)"
    },
    "bury": {
        "Hindi": "दफनाना (dafnānā)",
        "Chinese (Simplified)": "埋葬 (máizàng)"
    },
    "mushroom": {
        "Hindi": "मशरूम (mashrūm)",
        "Chinese (Simplified)": "蘑菇 (mógu)"
    },
    "cleavage": {
        "Hindi": "दरार (darār)",
        "Chinese (Simplified)": "乳沟 (rǔgōu)"
    },
    "inhale": {
        "Hindi": "साँस लेना (sāns lenā)",
        "Chinese (Simplified)": "吸气 (xīqì)"
    },
    "exhale": {
        "Hindi": "साँस छोड़ना (sāns choṛnā)",
        "Chinese (Simplified)": "呼气 (hūqì)"
    },
    "remain": {
        "Hindi": "बना रहना (banā rahanā)",
        "Chinese (Simplified)": "保持 (bǎochí)"
    },
    "remained": {
        "Hindi": "बने रहे (bane rahe)",
        "Chinese (Simplified)": "保持了 (bǎochí le)"
    },
    "remaining": {
        "Hindi": "बचे हुए (bache huye)",
        "Chinese (Simplified)": "剩下的 (shèngxià de)"
    },
    "reached": {
        "Hindi": "पहुँचा (pahunchā)",
        "Chinese (Simplified)": "到达了 (dàodá le)"
    },
    "reaching": {
        "Hindi": "पहुँचते हुए (pahunchte huye)",
        "Chinese (Simplified)": "正在到达 (zhèngzài dàodá)"
    },
    "reach": {
        "Hindi": "पहुँचना (pahunchnā)",
        "Chinese (Simplified)": "到达 (dàodá)"
    },
    "hunger": {
        "Hindi": "भूख (bhūkh)",
        "Chinese (Simplified)": "饥饿 (jī'è)"
    },
    "hungry": {
        "Hindi": "भूखा (bhūkhā)",
        "Chinese (Simplified)": "饿 (è)"
    },
    "throat": {
        "Hindi": "गला (galā)",
        "Chinese (Simplified)": "喉咙 (hóulóng)"
    },
    "thirsty": {
        "Hindi": "प्यासा (pyāsā)",
        "Chinese (Simplified)": "口渴 (kǒu kě)"
    },
    "thirst": {
        "Hindi": "प्यास (pyās)",
        "Chinese (Simplified)": "渴望 (kěwàng)"
    },
    "bring": {
        "Hindi": "लाना (lānā)",
        "Chinese (Simplified)": "带来 (dàilái)"
    },
    "bringing": {
        "Hindi": "ला रहा है (lā rahā hai)",
        "Chinese (Simplified)": "带来中 (dàilái zhōng)"
    },
    "dizzy": {
        "Hindi": "चक्कर (chakkar)",
        "Chinese (Simplified)": "头晕 (tóuyūn)"
    },
    "satisfaction": {
        "Hindi": "संतुष्टि (santuṣṭi)",
        "Chinese (Simplified)": "满足 (mǎnzú)"
    },
    "essence": {
        "Hindi": "सार (sār)",
        "Chinese (Simplified)": "本质 (běnzhì)"
    },
    "presence": {
        "Hindi": "उपस्थिति (upasthiti)",
        "Chinese (Simplified)": "存在 (cúnzài)"
    },
    "shiver": {
        "Hindi": "काँपना (kāmpnā)",
        "Chinese (Simplified)": "颤抖 (chàndǒu)"
    },
    "sense": {
        "Hindi": "अर्थ (arth)",
        "Chinese (Simplified)": "感觉 (gǎnjué)"
    },
    "moral": {
        "Hindi": "नैतिक (naitik)",
        "Chinese (Simplified)": "道德的 (dàodé de)"
    },
    "morality": {
        "Hindi": "नैतिकता (naitiktā)",
        "Chinese (Simplified)": "道德 (dàodé)"
    },
    "gentle": {
        "Hindi": "कोमल (komal)",
        "Chinese (Simplified)": "温柔的 (wēnróu de)"
    },
    "gently": {
        "Hindi": "धीरे से (dhīre se)",
        "Chinese (Simplified)": "轻轻地 (qīngqīng de)"
    },
    "murmurs": {
        "Hindi": "बड़बड़ाहट (baṛbaṛāhaṭ)",
        "Chinese (Simplified)": "低语 (dīyǔ)"
    },
    "bob": {
        "Hindi": "हिलाना (hilānā)",
        "Chinese (Simplified)": "上下摆动 (shàngxià bǎidòng)"
    },
    "bobbing": {
        "Hindi": "हिलाते हुए (hilāte huye)",
        "Chinese (Simplified)": "上下晃动 (shàngxià huàngdòng)"
    },
    "nods": {
        "Hindi": "सिर हिलाना (sir hilānā)",
        "Chinese (Simplified)": "点头 (diǎntóu)"
    },
    "embrace": {
        "Hindi": "गले लगाना (gale lagānā)",
        "Chinese (Simplified)": "拥抱 (yǒngbào)"
    },
    "impress": {
        "Hindi": "प्रभावित करना (prabhāvit karnā)",
        "Chinese (Simplified)": "留下深刻印象 (liúxià shēnkè yìnxiàng)"
    },
    "express": {
        "Hindi": "व्यक्त करना (vyakt karnā)",
        "Chinese (Simplified)": "表达 (biǎodá)"
    },
    "expressed": {
        "Hindi": "व्यक्त किया (vyakt kiyā)",
        "Chinese (Simplified)": "表达了 (biǎodále)"
    },
    "impressed": {
        "Hindi": "प्रभावित (prabhāvit)",
        "Chinese (Simplified)": "感到钦佩 (gǎndào qīnpèi)"
    },
    "expressing": {
        "Hindi": "व्यक्त करते हुए (vyakt karte huye)",
        "Chinese (Simplified)": "正在表达 (zhèngzài biǎodá)"
    },
    "impressing": {
        "Hindi": "प्रभावित करना (prabhāvit karnā)",
        "Chinese (Simplified)": "正在打动 (zhèngzài dǎdòng)"
    },
    "matters": {
        "Hindi": "मामले (māmlā)",
        "Chinese (Simplified)": "事情 (shìqíng)"
    },
    "matter": {
        "Hindi": "मामला (māmlā)",
        "Chinese (Simplified)": "重要 (zhòngyào)"
    },
    "brushing": {
        "Hindi": "ब्रश करना (braś karnā)",
        "Chinese (Simplified)": "刷 (shuā)"
    },
    "brush": {
        "Hindi": "ब्रश (braś)",
        "Chinese (Simplified)": "刷子 (shuāzi)"
    },
    "desperate": {
        "Hindi": "निराश (nirāś)",
        "Chinese (Simplified)": "绝望的 (juéwàng de)"
    },
    "each": {
        "Hindi": "प्रत्येक (pratyek)",
        "Chinese (Simplified)": "每个 (měi gè)"
    },
    "each them": {
        "Hindi": "उनमें से प्रत्येक (unmein se pratyek)",
        "Chinese (Simplified)": "他们每一个 (tāmen měi yī gè)"
    },
    "each other": {
        "Hindi": "एक दूसरे को (ek dūsre ko)",
        "Chinese (Simplified)": "彼此 (bǐcǐ)"
    },
    "itch": {
        "Hindi": "खुजली (khujlī)",
        "Chinese (Simplified)": "痒 (yǎng)"
    },
    "itched": {
        "Hindi": "खुजली की (khujlī kī)",
        "Chinese (Simplified)": "发痒了 (fāyǎng le)"
    },
    "itching": {
        "Hindi": "खुजला रहा है (khujlā rahā hai)",
        "Chinese (Simplified)": "正在发痒 (zhèngzài fāyǎng)"
    },
    "shoulder": {
        "Hindi": "कंधा (kandhā)",
        "Chinese (Simplified)": "肩膀 (jiānbǎng)"
    },
    "shoulders": {
        "Hindi": "कंधे (kandhe)",
        "Chinese (Simplified)": "双肩 (shuāng jiān)"
    },
    "soldier": {
        "Hindi": "सैनिक (sainik)",
        "Chinese (Simplified)": "士兵 (shìbīng)"
    },
    "soldiers": {
        "Hindi": "सैनिकों (sainikon)",
        "Chinese (Simplified)": "士兵们 (shìbīngmen)"
    },
    "brave": {
        "Hindi": "बहादुर (bahādur)",
        "Chinese (Simplified)": "勇敢的 (yǒnggǎn de)"
    },
    "dare": {
        "Hindi": "साहस करना (sāhas karnā)",
        "Chinese (Simplified)": "敢于 (gǎnyú)"
    },
    "roaming": {
        "Hindi": "घूमना (ghūmnā)",
        "Chinese (Simplified)": "漫游 (mànyóu)"
    },
    "pressed": {
        "Hindi": "दबाया हुआ (dabāyā huā)",
        "Chinese (Simplified)": "按下 (ànxià)"
    },
    "pressing": {
        "Hindi": "दबाते हुए (dabāte huye)",
        "Chinese (Simplified)": "按压中 (ànyā zhōng)"
    },
    "press": {
        "Hindi": "दबाना (dabānā)",
        "Chinese (Simplified)": "按 (àn)"
    },
    "shiver": {
        "Hindi": "काँपना (kāmpnā)",
        "Chinese (Simplified)": "颤抖 (chàndǒu)"
    },
    "dip": {
        "Hindi": "डुबकी (ḍubkī)",
        "Chinese (Simplified)": "浸 (jìn)"
    },
    "eye sight": {
        "Hindi": "दृष्टि (dṛṣṭi)",
        "Chinese (Simplified)": "视力 (shìlì)"
    },
    "sight": {
        "Hindi": "दृश्य (dṛśya)",
        "Chinese (Simplified)": "视线 (shìxiàn)"
    },
    "insight": {
        "Hindi": "अंतरदृष्टि (antaradṛṣṭi)",
        "Chinese (Simplified)": "洞察力 (dòngchálì)"
    },
    "lead": {
        "Hindi": "नेतृत्व करना (netṛtv karnā)",
        "Chinese (Simplified)": "领导 (lǐngdǎo)"
    },
    "leads": {
        "Hindi": "नेतृत्व करता है (netṛtv kartā hai)",
        "Chinese (Simplified)": "引导 (yǐndǎo)"
    },
    "relevant": {
        "Hindi": "संबंधित (sanbandhit)",
        "Chinese (Simplified)": "相关的 (xiāngguān de)"
    },
    "crap": {
        "Hindi": "बकवास (bakwās)",
        "Chinese (Simplified)": "废话 (fèihuà)"
    },
    "nap": {
        "Hindi": "झपकी (jhapkī)",
        "Chinese (Simplified)": "小睡 (xiǎoshuì)"
    },
    "arch": {
        "Hindi": "मेहराब (mehrāb)",
        "Chinese (Simplified)": "拱形 (gǒngxíng)"
    },
    "arc": {
        "Hindi": "धनुषाकार (dhanuṣākār)",
        "Chinese (Simplified)": "弧形 (húxíng)"
    },
    "arches": {
        "Hindi": "मेहराबें (mehrābeṃ)",
        "Chinese (Simplified)": "拱门 (gǒngmén)"
    },
    "flesh": {
        "Hindi": "मांस (māns)",
        "Chinese (Simplified)": "肉 (ròu)"
    },
    "gasps": {
        "Hindi": "हांफना (hāṅfnā)",
        "Chinese (Simplified)": "喘息 (chuǎnxī)"
    },
    "tight": {
        "Hindi": "तंग (tang)",
        "Chinese (Simplified)": "紧 (jǐn)"
    },
    "kite": {
        "Hindi": "पतंग (patang)",
        "Chinese (Simplified)": "风筝 (fēngzhēng)"
    },
    "midnight": {
        "Hindi": "आधी रात (ādhī rāt)",
        "Chinese (Simplified)": "午夜 (wǔyè)"
    },
    "fear": {
        "Hindi": "डर (ḍar)",
        "Chinese (Simplified)": "恐惧 (kǒngjù)"
    },
    "consequence": {
        "Hindi": "परिणाम (pariṇām)",
        "Chinese (Simplified)": "后果 (hòuguǒ)"
    },
    "consequences": {
        "Hindi": "परिणाम (pariṇām)",
        "Chinese (Simplified)": "结果 (jiéguǒ)"
    },
    "forbidden": {
        "Hindi": "निषिद्ध (niṣiddh)",
        "Chinese (Simplified)": "被禁止的 (bèi jìnzhǐ de)"
    },
    "desire": {
        "Hindi": "इच्छा (icchā)",
        "Chinese (Simplified)": "渴望 (kěwàng)"
    },
    "promise": {
        "Hindi": "वादा (vaada)",
        "Chinese (Simplified)": "承诺 (chéngnuò)"
    },
    "promise_opposite": {
        "Hindi": "अवहेलना (avahelna) / तोड़ना (toḍnā)",
        "Chinese (Simplified)": "违背 (wéibèi)"
    },
    "footsteps": {
        "Hindi": "कदमों के निशान (kadam ke nishan)",
        "Chinese (Simplified)": "脚步声 (jiǎobù shēng)"
    },
    "rage": {
        "Hindi": "क्रोध (krodh)",
        "Chinese (Simplified)": "愤怒 (fènnù)"
    },
    "ragged": {
        "Hindi": "फटेहाल (fatehaal)",
        "Chinese (Simplified)": "破烂的 (pòlàn de)"
    },
    "hang": {
        "Hindi": "लटकाना (latkāna)",
        "Chinese (Simplified)": "悬挂 (xuánguà)"
    },
    "convince": {
        "Hindi": "मनाना (manāna)",
        "Chinese (Simplified)": "说服 (shuōfú)"
    },
    "excuse": {
        "Hindi": "बहाना (bahāna)",
        "Chinese (Simplified)": "借口 (jièkǒu)"
    },
    "excusing": {
        "Hindi": "माफी मांगना (mafī māngnā)",
        "Chinese (Simplified)": "辩解 (biànjiě)"
    },
    "excused": {
        "Hindi": "माफ किया हुआ (maf kiyā huā)",
        "Chinese (Simplified)": "原谅的 (yuánliàng de)"
    },
    "spit": {
        "Hindi": "थूकना (thūknā)",
        "Chinese (Simplified)": "吐 (tǔ)"
    },
    "pause": {
        "Hindi": "ठहराव (ṭhahrāv)",
        "Chinese (Simplified)": "暂停 (zàntíng)"
    },
    "continue": {
        "Hindi": "जारी रखना (jārī rakhna)",
        "Chinese (Simplified)": "继续 (jìxù)"
    },
    "beat": {
        "Hindi": "धड़कन (dhadkan)",
        "Chinese (Simplified)": "跳动 (tiàodòng)"
    },
    "beats": {
        "Hindi": "धड़कनें (dhadkanen)",
        "Chinese (Simplified)": "节拍 (jiépāi)"
    },
    "vibrate": {
        "Hindi": "कंपन करना (kampan karnā)",
        "Chinese (Simplified)": "振动 (zhèndòng)"
    },
    "vibrating": {
        "Hindi": "कंपित (kampit)",
        "Chinese (Simplified)": "振动中 (zhèndòng zhōng)"
    },
    "stretch": {
        "Hindi": "खिंचाव (khinchāv)",
        "Chinese (Simplified)": "伸展 (shēnzhǎn)"
    },
    "stretched": {
        "Hindi": "खिंचा हुआ (khinchā huā)",
        "Chinese (Simplified)": "拉伸的 (lāshēn de)"
    },
    "ridiculous": {
        "Hindi": "हास्यास्पद (hāsyāspad)",
        "Chinese (Simplified)": "荒谬的 (huāngmiù de)"
    },
    "emphasize": {
        "Hindi": "जोर देना (zor denā)",
        "Chinese (Simplified)": "强调 (qiángdiào)"
    },
    "stroke": {
        "Hindi": "सहलाना (sahlānā)",
        "Chinese (Simplified)": "抚摸 (fǔmō)"
    },
    "stroking": {
        "Hindi": "सहलाना (sahlānā)",
        "Chinese (Simplified)": "抚摸中 (fǔmō zhōng)"
    },
    "triumphantly": {
        "Hindi": "विजयपूर्वक (vijaypūrvak)",
        "Chinese (Simplified)": "得意地 (déyì de)"
    },
    "vantage": {
        "Hindi": "लाभदायक स्थान (lābhdayak sthān)",
        "Chinese (Simplified)": "有利位置 (yǒulì wèizhì)"
    },
    "exchange": {
        "Hindi": "विनिमय (vinimay)",
        "Chinese (Simplified)": "交换 (jiāohuàn)"
    },
    "beneath": {
        "Hindi": "नीचे (nīche)",
        "Chinese (Simplified)": "在...之下 (zài...zhīxià)"
    },
    "steady": {
        "Hindi": "स्थिर (sthir)",
        "Chinese (Simplified)": "稳定的 (wěndìng de)"
    },
    "wrestling": {
        "Hindi": "कुश्ती (kushtī)",
        "Chinese (Simplified)": "摔跤 (shuāijiāo)"
    },
    "wrestlers": {
        "Hindi": "पहलवान (pahalwān)",
        "Chinese (Simplified)": "摔跤选手 (shuāijiāo xuǎnshǒu)"
    },
    "wrestler": {
        "Hindi": "पहलवान (pahalwān)",
        "Chinese (Simplified)": "摔跤手 (shuāijiāo shǒu)"
    },
    "wrestled": {
        "Hindi": "कुश्ती की (kushtī kī)",
        "Chinese (Simplified)": "摔跤了 (shuāijiāo le)"
    },
    "strained": {
        "Hindi": "तनावग्रस्त (tanāvgrast)",
        "Chinese (Simplified)": "紧张的 (jǐnzhāng de)"
    },
    "obscene": {
        "Hindi": "अश्लील (ashlīl)",
        "Chinese (Simplified)": "猥亵的 (wěixiè de)"
    },
    "quickly": {
        "Hindi": "तेजी से (tezī se)",
        "Chinese (Simplified)": "迅速地 (xùnsù de)"
    },
    "urgent": {
        "Hindi": "आपातकालीन (āpātkālīn)",
        "Chinese (Simplified)": "紧急的 (jǐnjí de)"
    },
    "urgently": {
        "Hindi": "तत्काल (tatkāl)",
        "Chinese (Simplified)": "紧急地 (jǐnjí de)"
    },
    "pounding": {
        "Hindi": "धड़कता हुआ (dhadkā huā)",
        "Chinese (Simplified)": "怦怦跳 (pēngpēng tiào)"
    },
    "intimate": {
        "Hindi": "घनिष्ठ (ghanishth)",
        "Chinese (Simplified)": "亲密的 (qīnmì de)"
    },
    "intimacy": {
        "Hindi": "निकटता (nikatā)",
        "Chinese (Simplified)": "亲密 (qīnmì)"
    },
    "determined": {
        "Hindi": "दृढ़ निश्चयी (dridh nishchayī)",
        "Chinese (Simplified)": "坚定的 (jiāndìng de)"
    },
    "determination": {
        "Hindi": "दृढ़ता (dridhatā)",
        "Chinese (Simplified)": "决心 (juéxīn)"
    },
    "determine": {
        "Hindi": "निर्धारित करना (nirdhārit karnā)",
        "Chinese (Simplified)": "决定 (juédìng)"
    },
    "effort": {
        "Hindi": "प्रयास (prayās)",
        "Chinese (Simplified)": "努力 (nǔlì)"
    },
    "efforts": {
        "Hindi": "प्रयास (prayās)",
        "Chinese (Simplified)": "努力 (nǔlì)"
    },
    "agitate": {
        "Hindi": "उत्तेजित करना (uttejit karnā)",
        "Chinese (Simplified)": "煽动 (shāndòng)"
    },
    "agitated": {
        "Hindi": "उत्तेजित (uttejit)",
        "Chinese (Simplified)": "焦虑的 (jiāolǜ de)"
    },
    "agitating": {
        "Hindi": "उत्तेजित कर रहा (uttejit kar rahā)",
        "Chinese (Simplified)": "煽动中 (shāndòng zhōng)"
    },
    "dimension": {
        "Hindi": "आयाम (āyām)",
        "Chinese (Simplified)": "维度 (wéidù)"
    },
    "combine": {
        "Hindi": "मिलाना (milānā)",
        "Chinese (Simplified)": "结合 (jiéhé)"
    },
    "combination": {
        "Hindi": "संयोजन (sanyojan)",
        "Chinese (Simplified)": "结合 (jiéhé)"
    },
    "combined": {
        "Hindi": "मिला हुआ (milā huā)",
        "Chinese (Simplified)": "结合的 (jiéhé de)"
    },
    "shaft": {
        "Hindi": "धुरी (dhurī)",
        "Chinese (Simplified)": "轴 (zhóu)"
    },
    "promising": {
        "Hindi": "आशाजनक (āśājanak)",
        "Chinese (Simplified)": "有前途的 (yǒu qiántú de)"
    },
    "betray": {
        "Hindi": "धोखा देना (dhokhā denā)",
        "Chinese (Simplified)": "背叛 (bèipàn)"
    },
    "promised": {
        "Hindi": "वादा किया हुआ (vāda kiyā huā)",
        "Chinese (Simplified)": "承诺了 (chéngnuò le)"
    },
    "indescribable": {
        "Hindi": "अवर्णनीय (avarṇanīya)",
        "Chinese (Simplified)": "难以形容的 (nányǐ xíngróng de)"
    },
    "sensation": {
        "Hindi": "अनुभूति (anubhūti)",
        "Chinese (Simplified)": "感觉 (gǎnjué)"
    },
    "swirl": {
        "Hindi": "घूमना (ghūmnā)",
        "Chinese (Simplified)": "旋转 (xuánzhuǎn)"
    },
    "sway": {
        "Hindi": "झूलना (jhūlnā)",
        "Chinese (Simplified)": "摇摆 (yáobǎi)"
    },
    "swirling": {
        "Hindi": "घूमता हुआ (ghūmtā huā)",
        "Chinese (Simplified)": "旋转中 (xuánzhuǎn zhōng)"
    },
    "widen": {
        "Hindi": "चौड़ा करना (chaudā karnā)",
        "Chinese (Simplified)": "扩大 (kuòdà)"
    },
    "wide": {
        "Hindi": "चौड़ा (chaudā)",
        "Chinese (Simplified)": "宽的 (kuān de)"
    },
    "spilled": {
        "Hindi": "गिरा हुआ (girā huā)",
        "Chinese (Simplified)": "溢出的 (yìchū de)"
    },
    "spill": {
        "Hindi": "गिराना (girānā)",
        "Chinese (Simplified)": "洒出 (sǎchū)"
    },
    "spelling": {
        "Hindi": "वर्तनी (vartnī)",
        "Chinese (Simplified)": "拼写 (pīnxiě)"
    },
    "deep breath": {
        "Hindi": "गहरी साँस (gahrī sāns)",
        "Chinese (Simplified)": "深呼吸 (shēn hūxī)"
    },
    "wheat": {
        "Hindi": "गेहूं (gehū)",
        "Chinese (Simplified)": "小麦 (xiǎomài)"
    },
    "rice": {
        "Hindi": "चावल (chāval)",
        "Chinese (Simplified)": "水稻 (shuǐdào)"
    },
    "corn": {
        "Hindi": "मक्का (makkā)",
        "Chinese (Simplified)": "玉米 (yùmǐ)"
    },
    "soybean": {
        "Hindi": "सोयाबीन (soyābīn)",
        "Chinese (Simplified)": "大豆 (dàdòu)"
    },
    "potato": {
        "Hindi": "आलू (ālū)",
        "Chinese (Simplified)": "土豆 (tǔdòu)"
    },
    "carrot": {
        "Hindi": "गाजर (gājar)",
        "Chinese (Simplified)": "胡萝卜 (húluóbo)"
    },
    "chili": {
        "Hindi": "मिर्च (mirch)",
        "Chinese (Simplified)": "辣椒 (làjiāo)"
    },
    "plow": {
        "Hindi": "हल (hal)",
        "Chinese (Simplified)": "犁 (lí)"
    },
    "hoe": {
        "Hindi": "कुदाल (kudāl)",
        "Chinese (Simplified)": "锄头 (chútou)"
    },
    "shovel": {
        "Hindi": "फावड़ा (phāvaṛā)",
        "Chinese (Simplified)": "铲子 (chǎnzi)"
    },
    "sickle": {
        "Hindi": "दरांती (darāntī)",
        "Chinese (Simplified)": "镰刀 (liándāo)"
    },
    "axe": {
        "Hindi": "कुल्हाड़ी (kulhāṛī)",
        "Chinese (Simplified)": "斧头 (fǔtóu)"
    },
    "watering can": {
        "Hindi": "पानी का डिब्बा (pānī kā dibbā)",
        "Chinese (Simplified)": "洒水壶 (sǎshuǐhú)"
    },
    "tractor": {
        "Hindi": "ट्रैक्टर (ṭraikaṭar)",
        "Chinese (Simplified)": "拖拉机 (tuōlājī)"
    },
    "seeder": {
        "Hindi": "बीज बोने की मशीन (bīj bone kī maśīn)",
        "Chinese (Simplified)": "播种机 (bōzhǒngjī)"
    },
    "harvester": {
        "Hindi": "कटाई मशीन (kaṭāī maśīn)",
        "Chinese (Simplified)": "收割机 (shōugējī)"
    },
    "wheelbarrow": {
        "Hindi": "ठेला (ṭhelā)",
        "Chinese (Simplified)": "手推车 (shǒutuīchē)"
    },
    "groan": {
        "Hindi": "कराहना (karāhnā)",
        "Chinese (Simplified)": "呻吟 (shēnyín)"
    },
    "groaning": {
        "Hindi": "कराहते हुए (karāhte huye)",
        "Chinese (Simplified)": "呻吟中 (shēnyín zhōng)"
    },
    "shockwaves": {
        "Hindi": "आघात तरंगें (āghāt taraṅgeṁ)",
        "Chinese (Simplified)": "冲击波 (chōngjībō)"
    },
    "greed": {
        "Hindi": "लालच (lālach)",
        "Chinese (Simplified)": "贪婪 (tānlán)"
    },
    "greedily": {
        "Hindi": "लालच से (lālach se)",
        "Chinese (Simplified)": "贪婪地 (tānlán de)"
    },
    "throb": {
        "Hindi": "धड़कना (dhaṛaknā)",
        "Chinese (Simplified)": "悸动 (jìdòng)"
    },
    "throbbing": {
        "Hindi": "धड़कता हुआ (dhaṛaktā huā)",
        "Chinese (Simplified)": "悸动的 (jìdòng de)"
    },
    "depravity": {
        "Hindi": "भ्रष्टता (bhraṣṭatā)",
        "Chinese (Simplified)": "堕落 (duòluò)"
    },
    "ecstasy": {
        "Hindi": "परमानंद (parmānand)",
        "Chinese (Simplified)": "狂喜 (kuángxǐ)"
        },
    "juxtaposition": {
        "Hindi": "सन्निकटन (sannikṭan)",
        "Chinese (Simplified)": "并列 (bìngliè)"
    },
    "ministrations": {
        "Hindi": "सेवाएँ (sevāeṁ)",
        "Chinese (Simplified)": "服侍 (fúshì)"
    },
    "dart": {
        "Hindi": "तीर (tīr)",
        "Chinese (Simplified)": "飞镖 (fēibiāo)"
    },
    "sharp": {
        "Hindi": "तेज़ (tez)",
        "Chinese (Simplified)": "锋利的 (fēnglì de)"
    },
    "enthusiasm": {
        "Hindi": "उत्साह (utsāh)",
        "Chinese (Simplified)": "热情 (rèqíng)"
    },
    "length": {
        "Hindi": "लंबाई (lambaī)",
        "Chinese (Simplified)": "长度 (chángdù)"
    },
    "width": {
        "Hindi": "चौड़ाई (chauṛāī)",
        "Chinese (Simplified)": "宽度 (kuāndù)"
    },
    "appreciative": {
        "Hindi": "कृतज्ञ (kṛtagya)",
        "Chinese (Simplified)": "感激的 (gǎnjī de)"
    },
    "approaching": {
        "Hindi": "पास आना (pās ānā)",
        "Chinese (Simplified)": "接近中 (jiējìn zhōng)"
    },
    "approached": {
        "Hindi": "पास आया (pās āyā)",
        "Chinese (Simplified)": "接近了 (jiējìn le)"
    },
    "seductively": {
        "Hindi": "मोहक ढंग से (mohak ḍhaṅg se)",
        "Chinese (Simplified)": "诱人地 (yòurén de)"
    },
    "imagination": {
        "Hindi": "कल्पना (kalpanā)",
        "Chinese (Simplified)": "想象力 (xiǎngxiànglì)"
    },
    "awake": {
        "Hindi": "जागना (jāgnā)",
        "Chinese (Simplified)": "清醒的 (qīngxǐng de)"
    },
    "awaked": {
        "Hindi": "जागा हुआ (jāgā huā)",
        "Chinese (Simplified)": "醒了 (xǐng le)"
    },
    "awaking": {
        "Hindi": "जाग रहा है (jāg rahā hai)",
        "Chinese (Simplified)": "正在醒来 (zhèngzài xǐnglái)"
    },
    "casual": {
        "Hindi": "आकस्मिक (ākasmik)",
        "Chinese (Simplified)": "随意的 (suíyì de)"
    },
    "fashion": {
        "Hindi": "फ़ैशन (fashion)",
        "Chinese (Simplified)": "时尚 (shíshàng)"
    },
    "fancy": {
        "Hindi": "आकर्षक (ākarṣak)",
        "Chinese (Simplified)": "华丽的 (huálì de)"
    },
    "damp": {
        "Hindi": "गीला (gīlā)",
        "Chinese (Simplified)": "潮湿的 (cháoshī de)"
    },
    "shower": {
        "Hindi": "बौछार (bauchār)",
        "Chinese (Simplified)": "淋浴 (línyù)"
    },
    "coating": {
        "Hindi": "परत (parat)",
        "Chinese (Simplified)": "涂层 (túcéng)"
    },
    "retention": {
        "Hindi": "धारण (dhāraṇ)",
        "Chinese (Simplified)": "保留 (bǎoliú)"
    },
    "challenging": {
        "Hindi": "चुनौतीपूर्ण (cunauteepūrṇ)",
        "Chinese (Simplified)": "具有挑战性的 (jùyǒu tiǎozhàn xìng de)"
    },
    "challenged": {
        "Hindi": "चुनौती दी गई (cunautee dī gaī)",
        "Chinese (Simplified)": "被挑战 (bèi tiǎozhàn)"
    },
    "torture": {
        "Hindi": "यातना (yātnā)",
        "Chinese (Simplified)": "折磨 (zhémó)"
    },
    "anticipation": {
        "Hindi": "प्रत्याशा (pratyāśā)",
        "Chinese (Simplified)": "期待 (qídài)"
    },
    "phantom": {
        "Hindi": "भूत (bhūt)",
        "Chinese (Simplified)": "幽灵 (yōulíng)"
    },
    "thrill": {
        "Hindi": "रोमांच (romānch)",
        "Chinese (Simplified)": "激动 (jīdòng)"
    },
    "suspect": {
        "Hindi": "संदिग्ध (sandigdh)",
        "Chinese (Simplified)": "嫌疑人 (xiányírén)"
    },
    "curtain": {
        "Hindi": "पर्दा (pardā)",
        "Chinese (Simplified)": "窗帘 (chuānglián)"
    },
    "relief": {
        "Hindi": "राहत (rāhat)",
        "Chinese (Simplified)": "缓解 (huǎnjiě)"
    },
    "discard": {
        "Hindi": "त्यागना (tyāgnā)",
        "Chinese (Simplified)": "丢弃 (diūqì)"
    },
    "discarding": {
        "Hindi": "त्याग रहा है (tyāg rahā hai)",
        "Chinese (Simplified)": "正在丢弃 (zhèngzài diūqì)"
    },
    "discarded": {
        "Hindi": "त्यागा हुआ (tyāgā huā)",
        "Chinese (Simplified)": "已丢弃 (yǐ diūqì)"
    },
    "cup": {
        "Hindi": "कप (kap)"
    },
    "cough": {
        "Hindi": "खांसी (khānsi)"
    },
    "bucket": {
        "Hindi": "बाल्टी (bālṭī)"
    },
    "mug": {
        "Hindi": "मग (mag)"
    },
    "note": {
        "Hindi": "नोट (noṭ)"
    },
    "optimize": {
        "Hindi": "सुधारना (sudhārnā)"
    },
    "creativity": {
        "Hindi": "रचनात्मकता (rachnātmaktā)"
    },
    "creative": {
        "Hindi": "रचनात्मक (rachnātmak)"
    },
    "keys": {
        "Hindi": "चाबियाँ (chābiyān)"
    },
    "scramble": {
        "Hindi": "घपला करना (ghaplī karnā)"
    },
    "glue": {
        "Hindi": "गोंद (gond)"
    },
    "occupy": {
        "Hindi": "अधिकार करना (adhikār karnā)"
    },
    "percentage": {
        "Hindi": "प्रतिशत (pratishat)"
    },
    "stake": {
        "Hindi": "दांव (dāṅv)"
    },
    "proceed": {
        "Chinese (Simplified)": "继续 (jì xù)",
        "Hindi": "जारी रखें (jaari rakhen)"
    },
    "kingdom": {
        "Chinese (Simplified)": "王国 (wáng guó)",
        "Hindi": "राज्य (raajy)"
    },
    "verification": {
        "Chinese (Simplified)": "验证 (yàn zhèng)",
        "Hindi": "सत्यापन (satyapan)"
    },
    "go through": {
        "Chinese (Simplified)": "经历 (jīng lì)",
        "Hindi": "सामना करना (saamna karna)"
    },
    "farmhouse": {
        "Chinese (Simplified)": "农舍 (nóng shè)",
        "Hindi": "कृषि गृह (krishi grih)"
    },
    "epic": {
        "Chinese (Simplified)": "史诗 (shǐ shī)",
        "Hindi": "महाकाव्य (mahaakavya)"
    },
    "garden": {
        "Chinese (Simplified)": "花园 (huā yuán)",
        "Hindi": "बाग (baag)"
    },
    "guard": {
        "Chinese (Simplified)": "守卫 (shǒu wèi)",
        "Hindi": "सुरक्षाकर्मी (surakshakarmi)"
    },
    "mosquito": {
        "Chinese (Simplified)": "蚊子 (wén zi)",
        "Hindi": "मच्छर (machhar)"
    },
    "housefly": {
        "Chinese (Simplified)": "苍蝇 (cāng yíng)",
        "Hindi": "मक्खी (makkhi)"
    },
    "don't stop": {
        "Chinese (Simplified)": "不要停止 (bù yào tíng zhǐ)",
        "Hindi": "रोकिए मत (rokiye mat)"
    },
    "era": {
        "Chinese (Simplified)": "时代 (shí dài)",
        "Hindi": "युग (yug)"
    },
    "let's talk": {
        "Chinese (Simplified)": "我们谈谈 (wǒ men tán tán)",
        "Hindi": "चलिए बात करते हैं (chaliye baat karte hain)"
    },
    "rotating": {
        "Chinese (Simplified)": "旋转 (xuán zhuǎn)",
        "Hindi": "घूमना (ghoomna)"
    },
    "rotate": {
        "Chinese (Simplified)": "旋转 (xuán zhuǎn)",
        "Hindi": "घुमाना (ghumaana)"
    },
    "flip": {
        "Chinese (Simplified)": "翻转 (fān zhuǎn)",
        "Hindi": "उलटना (ulṭnā)"
    },
    "hotline bling": {
        "Chinese (Simplified)": "热线铃声 (rè xiàn líng shēng)",
        "Hindi": "हॉटलाइन ब्लिंग (hotline bling)"
    },
    "magician": {
        "Chinese (Simplified)": "魔术师 (mó shù shī)",
        "Hindi": "जादूगर (jaadugar)"
    },
    "gardener": {
        "Chinese (Simplified)": "园丁 (yuán dīng)",
        "Hindi": "माली (maali)"
    },
    "clout": {
        "Chinese (Simplified)": "影响力 (yǐng xiǎng lì)",
        "Hindi": "प्रभाव (prabhaav)"
    },
    "pole": {
        "Chinese (Simplified)": "柱子 (zhù zi)",
        "Hindi": "खंभा (khamba)"
    },
    "sacred": {
        "Chinese (Simplified)": "神圣 (shén shèng)",
        "Hindi": "पवित्र (pavitra)"
    },
    "expected": {
        "Chinese (Simplified)": "预期 (yù qī)",
        "Hindi": "अपेक्षित (apekshit)"
    },
    "unexpected": {
        "Chinese (Simplified)": "出乎意料 (chū hū yì liào)",
        "Hindi": "अप्रत्याशित (apratyashit)"
    },
    "philosophical analysis": {
        "Chinese (Simplified)": "哲学分析 (zhé xué fēn xī)",
        "Hindi": "दार्शनिक विश्लेषण (darshanik vishleshan)"
    },
    "philosophy": {
        "Chinese (Simplified)": "哲学 (zhé xué)",
        "Hindi": "दार्शनिकता (darshanikta)"
    },
    "self knowledge": {
        "Chinese (Simplified)": "自我知识 (zì wǒ zhī shi)",
        "Hindi": "आत्मज्ञान (aatm gyaan)"
    },
    "wisdom": {
        "Chinese (Simplified)": "智慧 (zhì huì)",
        "Hindi": "ज्ञान (gyaan)"
    },
    "approximately": {
        "Chinese (Simplified)": "大约 (dà yuē)",
        "Hindi": "लगभग (lagbhag)"
    },
    "slur": {
        "Chinese (Simplified)": "污蔑 (wū miè)",
        "Hindi": "अपमान (apmaan)"
    },
    "offense": {
        "Chinese (Simplified)": "冒犯 (mào fàn)",
        "Hindi": "अपराध (apraadh)"
    },
    "orient": {
        "Chinese (Simplified)": "定向 (dìng xiàng)",
        "Hindi": "दिशा (dishā)"
    },
    "oriented": {
        "Chinese (Simplified)": "面向 (miàn xiàng)",
        "Hindi": "उन्मुख (unmukh)"
    },
    "fur": {
        "Chinese (Simplified)": "毛皮 (máo pí)",
        "Hindi": "रोम (rom)"
    },
    "feather": {
        "Chinese (Simplified)": "羽毛 (yǔ máo)",
        "Hindi": "पंख (pankh)"
    },
    "membership": {
        "Chinese (Simplified)": "会员资格 (huì yuán zī gé)",
        "Hindi": "सदस्यता (sadasyata)"
    },
    "life ruined": {
        "Chinese (Simplified)": "生活毁了 (shēng huó huǐ le)",
        "Hindi": "जीवन नष्ट हो गया (jeevan nasht ho gaya)"
    },
    "roadmap": {
        "Chinese (Simplified)": "路线图 (lù xiàn tú)",
        "Hindi": "रोडमैप (roadmap)"
    },
    "superpower": {
        "Chinese (Simplified)": "超级大国 (chāo jí dà guó)",
        "Hindi": "महाशक्ति (mahashakti)"
    },
    "timetable": {
        "Chinese (Simplified)": "时间表 (shí jiān biǎo)",
        "Hindi": "समय सारणी (samay saarnee)"
    },
    "click": {
        "Chinese (Simplified)": "点击 (diǎn jí)",
        "Hindi": "क्लिक (klik)"
    },
    "edit": {
        "Chinese (Simplified)": "编辑 (biān jí)",
        "Hindi": "संपादित करें (sampadit karein)"
    },
    "sudden": {
        "Chinese (Simplified)": "突然 (tū rán)",
        "Hindi": "अचानक (achanak)"
    },
    "suddenly": {
        "Chinese (Simplified)": "突然地 (tū rán de)",
        "Hindi": "अचानक (achanak)"
    },
    "compare": {
        "Chinese (Simplified)": "比较 (bǐ jiào)",
        "Hindi": "तुलना करें (tulna karein)"
    },
    "comparison": {
        "Chinese (Simplified)": "比较 (bǐ jiào)",
        "Hindi": "तुलना (tulna)"
    },
    "along": {
        "Chinese (Simplified)": "沿着 (yán zhe)",
        "Hindi": "साथ (saath)"
    },
    "empathy": {
        "Chinese (Simplified)": "同理心 (tóng lǐ xīn)",
        "Hindi": "सहानुभूति (sahanubhuti)"
    },
    "sympathy": {
        "Chinese (Simplified)": "同情 (tóng qíng)",
        "Hindi": "सहानुभूति (sahanubhuti)"
    },
    "encyclopedia": {
        "Chinese (Simplified)": "百科全书 (bǎi kē quán shū)",
        "Hindi": "विश्वकोश (vishwakosh)"
    },
    "volunteers": {
        "Chinese (Simplified)": "志愿者 (zhì yuàn zhě)",
        "Hindi": "स्वयंसेवक (swayamsevak)"
    },
    "host": {
        "Chinese (Simplified)": "主持人 (zhǔ chí rén)",
        "Hindi": "मेजबान (mejban)"
    },
    "hosted": {
        "Chinese (Simplified)": "主持 (zhǔ chí)",
        "Hindi": "मेजबानी की (mejbaani ki)"
    },
    "portal": {
        "Chinese (Simplified)": "门户 (mén hù)",
        "Hindi": "पोर्टल (portal)"
    },
    "maintain": {
        "Chinese (Simplified)": "维护 (wéi hù)",
        "Hindi": "रखना (rakhna)"
    },
    "maintaining": {
        "Chinese (Simplified)": "保持 (bǎo chí)",
        "Hindi": "बनाए रखना (banae rakhna)"
    },
    "maintained": {
        "Chinese (Simplified)": "维护 (wéi hù)",
        "Hindi": "रखा गया (rakha gaya)"
    },
    "presenting information": {
        "Chinese (Simplified)": "提供信息 (tí gōng xìn xī)",
        "Hindi": "सूचना प्रस्तुत करना (soochna prastut karna)"
    },
    "newspaper": {
        "Chinese (Simplified)": "报纸 (bào zhǐ)",
        "Hindi": "अखबार (akhbaar)"
    },
    "cafe": {
        "Chinese (Simplified)": "咖啡馆 (kā fēi guǎn)",
        "Hindi": "कैफ़े (café)"
    },
    "literature": {
        "Chinese (Simplified)": "文学 (wén xué)",
        "Hindi": "साहित्य (sahitya)"
    },
    "precedent": {
        "Chinese (Simplified)": "先例 (xiān lì)",
        "Hindi": "पारंपरिक उदाहरण (paaramparik udaharan)"
    },
    "relocated": {
        "Chinese (Simplified)": "重新安置 (chóng xīn ān zhì)",
        "Hindi": "स्थानांतरित (sthanantarit)"
    },
    "particularly": {
        "Chinese (Simplified)": "特别 (tè bié)",
        "Hindi": "विशेष रूप से (vishesh roop se)"
    },
    "impeached": {
        "Chinese (Simplified)": "弹劾 (tán hé)",
        "Hindi": "महाभियोग (mahaabheeyog)"
    },
    "peached": {
        "Chinese (Simplified)": "被表扬 (bèi biǎo yáng)",
        "Hindi": "प्रशंसा की (prashansa ki)"
    },
    "terrain": {
        "Chinese (Simplified)": "地形 (dì xíng)",
        "Hindi": "भू-भाग (bhoo-bhaag)"
    },
    "spectate": {
        "Chinese (Simplified)": "观看 (guān kàn)",
        "Hindi": "दृष्टा बनना (drishta banna)"
    },
    "acclaim": {
        "Chinese (Simplified)": "称赞 (chēng zàn)",
        "Hindi": "सराहना (saraahna)"
    },
    "circuit": {
        "Chinese (Simplified)": "电路 (diàn lù)",
        "Hindi": "परिपथ (paripath)"
    },
    "primitive": {
        "Chinese (Simplified)": "原始 (yuán shǐ)",
        "Hindi": "प्रारंभिक (prarambhik)"
    },
    "commentators": {
        "Chinese (Simplified)": "评论员 (píng lùn yuán)",
        "Hindi": "टिप्पणीकार (tippanikar)"
    },
    "furnace": {
        "Chinese (Simplified)": "炉子 (lú zi)",
        "Hindi": "भट्ठी (bhatti)"
    },
    "smoke": {
        "Chinese (Simplified)": "烟 (yān)",
        "Hindi": "धुआं (dhuaa)"
    },
    "cigarette": {
        "Chinese (Simplified)": "香烟 (xiāng yān)",
        "Hindi": "सिगरेट (cigarette)"
    },
    "alcohol": {
        "Chinese (Simplified)": "酒精 (jiǔ jīng)",
        "Hindi": "मद्यपान (madyapan)"
    },
    "vice versa": {
        "Chinese (Simplified)": "反之亦然 (fǎn zhī yì rán)",
        "Hindi": "इसके विपरीत (iske vipreet)"
    },
    "durable": {
        "Chinese (Simplified)": "耐用 (nài yòng)",
        "Hindi": "मजबूत (majboot)"
    },
    "durability": {
        "Chinese (Simplified)": "耐用性 (nài yòng xìng)",
        "Hindi": "मजबूती (majbooti)"
    },
    "overworld": {
        "Chinese (Simplified)": "上界 (shàng jiè)",
        "Hindi": "ऊपर की दुनिया (upar ki duniya)"
    },
    "consist": {
        "Chinese (Simplified)": "由...组成 (yóu...zǔ chéng)",
        "Hindi": "समाविष्ट होना (samaavishth hona)"
    },
    "novelist": {
        "Chinese (Simplified)": "小说家 (xiǎo shuō jiā)",
        "Hindi": "उपन्यासकार (upanyaskar)"
    },
    "novel": {
        "Chinese (Simplified)": "小说 (xiǎo shuō)",
        "Hindi": "उपन्यास (upanyas)"
    },
    "bottomless": {
        "Chinese (Simplified)": "无底的 (wú dǐ de)",
        "Hindi": "गहरा (gahara)"
    },
    "void": {
        "Chinese (Simplified)": "空虚 (kōng xū)",
        "Hindi": "शून्य (shoonya)"
    },
    "conclusion": {
        "Chinese (Simplified)": "结论 (jié lùn)",
        "Hindi": "निष्कर्ष (nishkarsh)"
    },
    "teleport": {
        "Chinese (Simplified)": "传送 (chuán sòng)",
        "Hindi": "टेलीपोर्ट (teleport)"
    },
    "time travel": {
        "Chinese (Simplified)": "时间旅行 (shí jiān lǚ xíng)",
        "Hindi": "समय यात्रा (samay yatra)"
    },
    "shelter": {
        "Chinese (Simplified)": "避难所 (bì nàn suǒ)",
        "Hindi": "आश्रय (aashray)"
    },
    "last longer": {
        "Chinese (Simplified)": "持续更长时间 (chí xù gèng cháng shí jiān)",
        "Hindi": "लंबे समय तक चले (lambe samay tak chale)"
    },
    "disturbance": {
        "Chinese (Simplified)": "干扰 (gān rǎo)",
        "Hindi": "विघटन (vighatan)"
    },
    "disturb": {
        "Chinese (Simplified)": "打扰 (dǎ rǎo)",
        "Hindi": "विघटित करना (vighatit karna)"
    },
    "disturbed": {
        "Chinese (Simplified)": "受干扰 (shòu gān rǎo)",
        "Hindi": "विचलित (vichlit)"
    },
    "eventually": {
        "Chinese (Simplified)": "最终 (zuì zhōng)",
        "Hindi": "अंततः (antatah)"
    },
    "attribute": {
        "Chinese (Simplified)": "属性 (shǔ xìng)",
        "Hindi": "गुण (gun)"
    },
    "inherit": {
        "Chinese (Simplified)": "继承 (jì chéng)",
        "Hindi": "विरासत में प्राप्त करना (virasat mein prapt karna)"
    },
    "inherited": {
        "Chinese (Simplified)": "继承的 (jì chéng de)",
        "Hindi": "विरासत में प्राप्त (virasat mein prapt)"
    },
    "arbitrate": {
        "Chinese (Simplified)": "仲裁 (zhòng cái)",
        "Hindi": "मध्यक्षता करना (maadhyakshata karna)"
    },
    "deal": {
        "Chinese (Simplified)": "交易 (jiāo yì)",
        "Hindi": "सौदा (sauda)"
    },
    "frequently": {
        "Chinese (Simplified)": "经常 (jīng cháng)",
        "Hindi": "बार-बार (baar-baar)"
    },
    "adjustments": {
        "Chinese (Simplified)": "调整 (tiáo zhěng)",
        "Hindi": "समायोजन (samaayojan)"
    },
    "rename": {
        "Chinese (Simplified)": "重命名 (chóng mìng míng)",
        "Hindi": "पुनः नामकरण (punah naamkaran)"
    },
    "better together": {
        "Chinese (Simplified)": "更好地在一起 (gèng hǎo de zài yī qǐ)",
        "Hindi": "साथ में बेहतर (saath mein behtar)"
    },
    "discontinued": {
        "Chinese (Simplified)": "停产 (tíng chǎn)",
        "Hindi": "बंद किया गया (band kiya gaya)"
    },
    "discontinue": {
        "Chinese (Simplified)": "停止 (tíng zhǐ)",
        "Hindi": "बंद करना (band karna)"
    },
    "further": {
        "Chinese (Simplified)": "进一步 (jìn yí bù)",
        "Hindi": "आगे (aage)"
    },
    "implementing": {
        "Chinese (Simplified)": "实施 (shí shī)",
        "Hindi": "लागू करना (laagu karna)"
    },
    "implement": {
        "Chinese (Simplified)": "实现 (shí xiàn)",
        "Hindi": "अमल में लाना (amal mein lana)"
    },
    "implementing": {
        "Chinese (Simplified)": "实施 (shí shī)",
        "Hindi": "लागू करना (laagu karna)"
    },
    "activate": {
        "Chinese (Simplified)": "激活 (jī huó)",
        "Hindi": "सक्रिय करना (sakriya karna)"
    },
    "deactivate": {
        "Chinese (Simplified)": "停用 (tíng yòng)",
        "Hindi": "निष्क्रिय करना (nishkriya karna)"
    },
    "activate": {
        "Chinese (Simplified)": "激活 (jī huó)",
        "Hindi": "सक्रिय करना (sakriya karna)"
    },
    "deactivate": {
        "Chinese (Simplified)": "停用 (tíng yòng)",
        "Hindi": "निष्क्रिय करना (nishkriya karna)"
    },
    "instability": {
        "Chinese (Simplified)": "不稳定 (bù wěn dìng)",
        "Hindi": "अस्थिरता (asthirta)"
    },
    "static": {
        "Chinese (Simplified)": "静态 (jìng tài)",
        "Hindi": "स्थिर (sthir)"
    },
    "dynamic": {
        "Chinese (Simplified)": "动态 (dòng tài)",
        "Hindi": "गतिशील (gatisheel)"
    },
    "feedback": {
        "Chinese (Simplified)": "反馈 (fǎn kuì)",
        "Hindi": "प्रतिक्रिया (pratikriya)"
    },
    "survival": {
        "Chinese (Simplified)": "生存 (shēng cún)",
        "Hindi": "जीवित रहना (jeevit rehna)"
    },
    "acquisition": {
        "Chinese (Simplified)": "收购 (shōu gòu)",
        "Hindi": "अधिग्रहण (adhigrahan)"
    },
    "validity": {
        "Chinese (Simplified)": "有效性 (yǒu xiào xìng)",
        "Hindi": "वैधता (vaidhata)"
    },
    "although": {
        "Chinese (Simplified)": "虽然 (suī rán)",
        "Hindi": "हालाँकि (haalanki)"
    },
    "contribute": {
        "Chinese (Simplified)": "贡献 (gòng xiàn)",
        "Hindi": "योगदान देना (yogdan dena)"
    },
    "contribution": {
        "Chinese (Simplified)": "贡献 (gòng xiàn)",
        "Hindi": "योगदान (yogdan)"
    },
    "contributors": {
        "Chinese (Simplified)": "贡献者 (gòng xiàn zhě)",
        "Hindi": "योगदानकर्ता (yogdan karta)"
    },
    "status": {
        "Chinese (Simplified)": "状态 (zhuàng tài)",
        "Hindi": "स्थिति (sthiti)"
    },
    "nope": {
        "Chinese (Simplified)": "不 (bù)",
        "Hindi": "नहीं (nahi)"
    },
    "ownership": {
        "Chinese (Simplified)": "所有权 (suǒ yǒu quán)",
        "Hindi": "स्वामित्व (swamitva)"
    },
    "classic": {
        "Chinese (Simplified)": "经典 (jīng diǎn)",
        "Hindi": "क्लासिक (classic)"
    },
    "adapt": {
        "Chinese (Simplified)": "适应 (shì yìng)",
        "Hindi": "अनुकूलित करना (anukoolit karna)"
    },
    "adapted": {
        "Chinese (Simplified)": "适应的 (shì yìng de)",
        "Hindi": "अनुकूलित (anukoolit)"
    },
    "adapting": {
        "Chinese (Simplified)": "适应 (shì yìng)",
        "Hindi": "अनुकूलित करना (anukoolit karna)"
    },
    "scar": {
        "Chinese (Simplified)": "疤痕 (bā hén)",
        "Hindi": "दाग (daag)"
    },
    "drown": {
        "Chinese (Simplified)": "淹死 (yān sǐ)",
        "Hindi": "डूबना (doobna)"
    },
    "potential": {
        "Chinese (Simplified)": "潜力 (qián lì)",
        "Hindi": "संभावना (sambhavna)"
    },
    "raft": {
        "Chinese (Simplified)": "木筏 (mù fá)",
        "Hindi": "पट्टी (patti)"
    },
    "tweaks": {
        "Chinese (Simplified)": "调整 (tiáo zhěng)",
        "Hindi": "सुधार (sudhaar)"
    },
    "monopoly": {
        "Chinese (Simplified)": "垄断 (lǒng duàn)",
        "Hindi": "एकाधिकार (ekadhikar)"
    },
    "duopoly": {
        "Chinese (Simplified)": "双头垄断 (shuāng tóu lǒng duàn)",
        "Hindi": "द्वैधाधिकार (dvaidhadhikar)"
    },
    "standalone": {
        "Chinese (Simplified)": "独立的 (dú lì de)",
        "Hindi": "स्वतंत्र (svatantra)"
    },
    "non standalone": {
        "Chinese (Simplified)": "非独立的 (fēi dú lì de)",
        "Hindi": "गैर-स्वतंत्र (gair-svatantra)"
    },
    "spectrum": {
        "Chinese (Simplified)": "光谱 (guāng pǔ)",
        "Hindi": "स्पेक्ट्रम (spectrum)"
    },
    "creed": {
        "Chinese (Simplified)": "信条 (xìn tiáo)",
        "Hindi": "विश्वास (vishwas)"
    },
    "odyssey": {
        "Chinese (Simplified)": "奥德赛 (ào dé sài)",
        "Hindi": "यात्रा (yatra)"
    },
    "clan": {
        "Chinese (Simplified)": "部落 (bù luò)",
        "Hindi": "कबीला (kabīlā)"
    },
    "clash": {
        "Chinese (Simplified)": "冲突 (chōng tú)",
        "Hindi": "टकराव (takraav)"
    },
    "what is happening": {
        "Chinese (Simplified)": "发生了什么 (fā shēng le shén me)",
        "Hindi": "क्या हो रहा है (kya ho raha hai)"
    },
    "genuine": {
        "Chinese (Simplified)": "真实的 (zhēn shí de)",
        "Hindi": "असली (asli)"
    },
    "i made it": {
        "Chinese (Simplified)": "我成功了 (wǒ chéng gōng le)",
        "Hindi": "मैंने इसे किया (maine ise kiya)"
    },
    "chuckle": {
        "Chinese (Simplified)": "轻笑 (qīng xiào)",
        "Hindi": "दबी हंसी (dabi hansi)"
    },
    "smirks": {
        "Chinese (Simplified)": "得意地笑 (dé yì de xiào)",
        "Hindi": "मुस्कान (muskaan)"
    },
    "kiddo": {
        "Chinese (Simplified)": "小孩 (xiǎo hái)",
        "Hindi": "बच्चा (bachcha)"
    },
    "chuckles softly": {
        "Chinese (Simplified)": "轻轻地笑 (qīng qīng de xiào)",
        "Hindi": "धीरे से हंसता है (dheere se hasta hai)"
    },
    "corner": {
        "Chinese (Simplified)": "角落 (jiǎo luò)",
        "Hindi": "कोना (kona)"
    },
    "private": {
        "Chinese (Simplified)": "私人 (sī rén)",
        "Hindi": "निजी (niji)"
    },
    "privatization": {
        "Chinese (Simplified)": "私有化 (sī yǒu huà)",
        "Hindi": "निजीकरण (nijikaran)"
    },
    "forehead": {
        "Chinese (Simplified)": "额头 (é tóu)",
        "Hindi": "माथा (maatha)"
    },
    "tingle": {
        "Chinese (Simplified)": "刺痛 (cì tòng)",
        "Hindi": "झनझनाहट (jhanjhanaahat)"
    },
    "relaxation": {
        "Chinese (Simplified)": "放松 (fàng sōng)",
        "Hindi": "आराम (aaram)"
    },
    "chores": {
        "Chinese (Simplified)": "家务活 (jiā wù huó)",
        "Hindi": "घरेलू काम (gharelu kaam)"
    },
    "suspect": {
        "Chinese (Simplified)": "怀疑 (huái yí)",
        "Hindi": "संदेह करना (sandeh karna)"
    },
    "stalk": {
        "Chinese (Simplified)": "跟踪 (gēn zōng)",
        "Hindi": "पीछा करना (peecha karna)"
    },
    "wink": {
        "Chinese (Simplified)": "眨眼 (zhǎ yǎn)",
        "Hindi": "आँख मारना (aankh maarna)"
    },
    "slack": {
        "Chinese (Simplified)": "松弛 (sōng chí)",
        "Hindi": "ढील (dheel)"
    },
    "flushing": {
        "Chinese (Simplified)": "脸红 (liǎn hóng)",
        "Hindi": "लाल होना (laal hona)"
    },
    "cheeks": {
        "Chinese (Simplified)": "脸颊 (liǎn jiá)",
        "Hindi": "गाल (gaal)"
    },
    "cheek": {
        "Chinese (Simplified)": "脸颊 (liǎn jiá)",
        "Hindi": "गाल (gaal)"
    },
    "flush": {
        "Chinese (Simplified)": "脸红 (liǎn hóng)",
        "Hindi": "लाल होना (laal hona)"
    },
    "suppose": {
        "Chinese (Simplified)": "假设 (jiǎ shè)",
        "Hindi": "मान लेना (maan lena)"
    },
    "turns back": {
        "Chinese (Simplified)": "转身 (zhuǎn shēn)",
        "Hindi": "पीछे मुड़ता है (peeche mudta hai)"
    },
    "choke": {
        "Chinese (Simplified)": "窒息 (zhì xī)",
        "Hindi": "घुटना (ghutna)"
    },
    "style": {
        "Chinese (Simplified)": "风格 (fēng gé)",
        "Hindi": "शैली (shailee)"
    },
    "smash": {
        "Chinese (Simplified)": "粉碎 (fěn suì)",
        "Hindi": "चूर-चूर करना (choor-choor karna)"
    },
    "fence": {
        "Chinese (Simplified)": "围栏 (wéi lán)",
        "Hindi": "बाड़ (baad)"
    },
    "configure": {
        "Chinese (Simplified)": "配置 (pèi zhì)",
        "Hindi": "कॉन्फ़िगर करना (configure karna)"
    },
    "pouch": {
        "Chinese (Simplified)": "小袋 (xiǎo dài)",
        "Hindi": "थैली (thaili)"
    },
    "traffic": {
        "Chinese (Simplified)": "交通 (jiāo tōng)",
        "Hindi": "यातायात (yaataayat)"
    },
    "landing": {
        "Chinese (Simplified)": "着陆 (zhuó lù)",
        "Hindi": "अवतरण (avataran)"
    },
    "candidate": {
        "Chinese (Simplified)": "候选人 (hòu xuǎn rén)",
        "Hindi": "उम्मीदवार (ummeedvaar)"
    },
    "goon": {
        "Chinese (Simplified)": "打手 (dǎ shǒu)",
        "Hindi": "गुंडा (gunda)"
    },
    "trap": {
        "Chinese (Simplified)": "陷阱 (xiàn jǐng)",
        "Hindi": "जाल (jaal)"
    },
    "mud": {
        "Chinese (Simplified)": "泥 (ní)",
        "Hindi": "कीचड़ (keechad)"
    },
    "wealthy": {
        "Chinese (Simplified)": "富有的 (fù yǒu de)",
        "Hindi": "धनी (dhani)"
    },
    "coupe": {
        "Chinese (Simplified)": "双门轿车 (shuāng mén jiào chē)",
        "Hindi": "कूपे कार (coupe car)"
    },
    "swat": {
        "Chinese (Simplified)": "拍打 (pāi dǎ)",
        "Hindi": "मारना (maar na)"
    },
    "bales": {
        "Chinese (Simplified)": "捆 (kǔn)",
        "Hindi": "गठरियाँ (gathriyan)"
    },
    "seal": {
        "Chinese (Simplified)": "封条 (fēng tiáo)",
        "Hindi": "सील (seal)"
    },
    "damn": {
        "Chinese (Simplified)": "该死 (gāi sǐ)",
        "Hindi": "धत्त (dhat)"
    },
    "wipe": {
        "Chinese (Simplified)": "擦拭 (cā shì)",
        "Hindi": "पोंछना (ponchna)"
    },
    "slat": {
        "Chinese (Simplified)": "条板 (tiáo bǎn)",
        "Hindi": "पट्टी (patti)"
    },
    "at": {
        "Chinese (Simplified)": "在 (zài)",
        "Hindi": "पर (par)"
    },
    "wish": {
        "Chinese (Simplified)": "愿望 (yuàn wàng)",
        "Hindi": "इच्छा (ichha)"
    },
    "last wish": {
        "Chinese (Simplified)": "最后的愿望 (zuì hòu de yuàn wàng)",
        "Hindi": "आखिरी इच्छा (aakhiri ichha)"
    },
    "further": {
        "Chinese (Simplified)": "进一步 (jìn yí bù)",
        "Hindi": "आगे (aage)"
    },
    "attempt": {
        "Chinese (Simplified)": "尝试 (cháng shì)",
        "Hindi": "प्रयास (prayaas)"
    },
    "authentic": {
        "Chinese (Simplified)": "真实的 (zhēn shí de)",
        "Hindi": "प्रामाणिक (praamaanik)"
    },
    "recover": {
        "Chinese (Simplified)": "恢复 (huī fù)",
        "Hindi": "पुनः प्राप्त करना (punah prapt karna)"
    },
    "factor": {
        "Chinese (Simplified)": "因素 (yīn sù)",
        "Hindi": "घटक (ghatak)"
    },
    "terrace": {
        "Chinese (Simplified)": "阳台 (yáng tái)",
        "Hindi": "छत (chhat)"
    },
    "dam": {
        "Chinese (Simplified)": "水坝 (shuǐ bà)",
        "Hindi": "बांध (baandh)"
    },
    "famous person": {
        "Chinese (Simplified)": "名人 (míng rén)",
        "Hindi": "प्रसिद्ध व्यक्ति (prasiddh vyakti)"
    },
    "throat": {
        "Chinese (Simplified)": "喉咙 (hóu lóng)",
        "Hindi": "गला (gala)"
    },
    "ago": {
        "Chinese (Simplified)": "以前 (yǐ qián)",
        "Hindi": "पहले (pehle)"
    },
    "anywhere": {
        "Chinese (Simplified)": "任何地方 (rèn hé dì fāng)",
        "Hindi": "कहीं भी (kahin bhi)"
    },
    "anytime": {
        "Chinese (Simplified)": "随时 (suí shí)",
        "Hindi": "कभी भी (kabhi bhi)"
    },
    "all at once": {
        "Chinese (Simplified)": "一下子 (yí xià zi)",
        "Hindi": "एक साथ (ek saath)"
    },
    "preserve": {
        "Chinese (Simplified)": "保存 (bǎo cún)",
        "Hindi": "सुरक्षित रखना (surakshit rakhna)"
    },
    "annual": {
        "Chinese (Simplified)": "年度的 (nián dù de)",
        "Hindi": "वार्षिक (varshik)"
    },
    "half": {
        "Chinese (Simplified)": "一半 (yí bàn)",
        "Hindi": "आधा (aadha)"
    },
    "policy": {
        "Chinese (Simplified)": "政策 (zhèng cè)",
        "Hindi": "नीति (neeti)"
    },
    "workspace": {
        "Chinese (Simplified)": "工作区 (gōng zuò qū)",
        "Hindi": "कार्यस्थल (karyasthal)"
    },
    "building": {
        "Chinese (Simplified)": "建筑 (jiàn zhù)",
        "Hindi": "भवन (bhavan)"
    },
    "castle": {
        "Chinese (Simplified)": "城堡 (chéng bǎo)",
        "Hindi": "किला (kila)"
    },
    "decide": {
        "Chinese (Simplified)": "决定 (jué dìng)",
        "Hindi": "निर्णय लेना (nirnay lena)"
    },
    "rude": {
        "Chinese (Simplified)": "粗鲁 (cū lǔ)",
        "Hindi": "असभ्य (asabhya)"
    },
    "instruction": {
        "Chinese (Simplified)": "指示 (zhǐ shì)",
        "Hindi": "निर्देश (nirdesh)"
    },
    "credentials": {
        "Chinese (Simplified)": "凭证 (píng zhèng)",
        "Hindi": "प्रमाण पत्र (pramaan patra)"
    },
    "credential": {
        "Chinese (Simplified)": "凭据 (píng jù)",
        "Hindi": "प्रमाण (pramaan)"
    },
    "ready to use": {
        "Chinese (Simplified)": "准备好使用 (zhǔn bèi hǎo shǐ yòng)",
        "Hindi": "उपयोग के लिए तैयार (upyog ke liye tayar)"
    },
    "notice": {
        "Chinese (Simplified)": "注意 (zhù yì)",
        "Hindi": "ध्यान देना (dhyaan dena)"
    },
    "noticed": {
        "Chinese (Simplified)": "注意到了 (zhù yì dào le)",
        "Hindi": "ध्यान दिया (dhyaan diya)"
    },
    "eye vision": {
        "Chinese (Simplified)": "视力 (shì lì)",
        "Hindi": "दृष्टि (drishti)"
    },
    "ceremony": {
        "Chinese (Simplified)": "仪式 (yí shì)",
        "Hindi": "समारोह (samaroh)"
    },
    "retire": {
        "Chinese (Simplified)": "退休 (tuì xiū)",
        "Hindi": "सेवानिवृत्त होना (sevanivritt hona)"
    },
    "retired": {
        "Chinese (Simplified)": "退休了 (tuì xiū le)",
        "Hindi": "सेवानिवृत्त (sevanivritt)"
    },
    "came out": {
        "Chinese (Simplified)": "出来了 (chū lái le)",
        "Hindi": "बाहर आया (baahar aaya)"
    },
    "mood": {
        "Chinese (Simplified)": "心情 (xīn qíng)",
        "Hindi": "मूड (mood)"
    },
    "boredom": {
        "Chinese (Simplified)": "无聊 (wú liáo)",
        "Hindi": "ऊब (oob)"
    },
    "engage": {
        "Chinese (Simplified)": "参与 (cān yù)",
        "Hindi": "सक्रिय करना (sakriya karna)"
    },
    "court": {
        "Chinese (Simplified)": "法院 (fǎ yuàn)",
        "Hindi": "कोर्ट (court)"
    },
    "seized": {
        "Chinese (Simplified)": "扣押 (kòu yā)",
        "Hindi": "जबरदस्ती किया (zabardasti kiya)"
    },
    "grant": {
        "Chinese (Simplified)": "授予 (shòu yǔ)",
        "Hindi": "अनुदान (anudaan)"
    },
    "granted": {
        "Chinese (Simplified)": "已授予 (yǐ shòu yǔ)",
        "Hindi": "अनुदानित (anudanit)"
    },
    "begins": {
        "Chinese (Simplified)": "开始 (kāi shǐ)",
        "Hindi": "शुरू होता है (shuru hota hai)"
    },
    "begin": {
        "Chinese (Simplified)": "开始 (kāi shǐ)",
        "Hindi": "शुरू करना (shuru karna)"
    },
    "i made it": {
        "Chinese (Simplified)": "我做到了 (wǒ zuò dào le)",
        "Hindi": "मैंने कर लिया (maine kar liya)"
    },
    "bail": {
        "Chinese (Simplified)": "保释 (bǎo shì)",
        "Hindi": "जमानत (jamaat)"
    },
    "injury": {
        "Chinese (Simplified)": "伤害 (shāng hài)",
        "Hindi": "चोट (chot)"
    },
    "injuries": {
        "Chinese (Simplified)": "伤害 (shāng hài)",
        "Hindi": "चोटें (choten)"
    },
    "report": {
        "Chinese (Simplified)": "报告 (bào gào)",
        "Hindi": "रिपोर्ट (report)"
    },
    "certificate": {
        "Chinese (Simplified)": "证书 (zhèng shū)",
        "Hindi": "प्रमाण पत्र (pramaan patra)"
    },
    "degree": {
        "Chinese (Simplified)": "学位 (xué wèi)",
        "Hindi": "डिग्री (degree)"
    },
    "reported": {
        "Chinese (Simplified)": "已报告 (yǐ bào gào)",
        "Hindi": "रिपोर्ट किया गया (report kiya gaya)"
    },
    "dial": {
        "Chinese (Simplified)": "拨号 (bō hào)",
        "Hindi": "डायल करना (dial karna)"
    },
    "committee": {
        "Chinese (Simplified)": "委员会 (wěi yuán huì)",
        "Hindi": "समिति (samiti)"
    },
    "inaugurated": {
        "Chinese (Simplified)": "开幕 (kāi mù)",
        "Hindi": "उद्घाटन किया (udghaatan kiya)"
    },
    "augurated": {
        "Chinese (Simplified)": "预示 (yù shì)",
        "Hindi": "आगमन (aagman)"
    },
    "convert": {
        "Chinese (Simplified)": "转化 (zhuǎn huà)",
        "Hindi": "रूपांतरित करना (roopantarit karna)"
    },
    "restore": {
        "Chinese (Simplified)": "恢复 (huī fù)",
        "Hindi": "पुनर्स्थापित करना (punarsthapit karna)"
    },
    "tie": {
        "Chinese (Simplified)": "平局 (píng jú)",
        "Hindi": "टाई (tie)"
    },
    "batter": {
        "Chinese (Simplified)": "打击手 (dǎ jí shǒu)",
        "Hindi": "बेटर (batter)"
    },
    "scheme": {
        "Chinese (Simplified)": "计划 (jì huà)",
        "Hindi": "योजना (yojana)"
    },
    "twist": {
        "Chinese (Simplified)": "扭曲 (niǔ qū)",
        "Hindi": "घुमा (ghuma)"
    },
    "hire": {
        "Chinese (Simplified)": "雇用 (gù yòng)",
        "Hindi": "भर्ती करना (bharti karna)"
    },
    "spend": {
        "Chinese (Simplified)": "花费 (huā fèi)",
        "Hindi": "खर्च करना (kharch karna)"
    },
    "spent": {
        "Chinese (Simplified)": "已花费 (yǐ huā fèi)",
        "Hindi": "खर्च किया (kharch kiya)"
    },
    "lots of time": {
        "Chinese (Simplified)": "大量时间 (dà liàng shí jiān)",
        "Hindi": "काफी समय (kaafi samay)"
    },
    "uncountable": {
        "Chinese (Simplified)": "不可计数 (bù kě jì shǔ)",
        "Hindi": "गिनती से बाहर (ginti se baahar)"
    },
    "qualify": {
        "Chinese (Simplified)": "资格 (zī gé)",
        "Hindi": "पात्र होना (paatra hona)"
    },
    "exhaust": {
        "Chinese (Simplified)": "排气 (pái qì)",
        "Hindi": "थकावट (thakavat)"
    },
    "casual": {
        "Chinese (Simplified)": "随意的 (suí yì de)",
        "Hindi": "आकस्मिक (aaksamik)"
    },
    "suffice": {
        "Chinese (Simplified)": "足够 (zú gòu)",
        "Hindi": "पर्याप्त होना (paryaapt hona)"
    },
    "syntax": {
        "Chinese (Simplified)": "语法 (yǔ fǎ)",
        "Hindi": "वाक्य रचना (vaakya rachna)"
    },
    "agreement": {
        "Chinese (Simplified)": "协议 (xié yì)",
        "Hindi": "समझौता (samjhauta)"
    },
    "script": {
        "Chinese (Simplified)": "脚本 (jiǎo běn)",
        "Hindi": "लिपि (lipi)"
    },
    "tone": {
        "Chinese (Simplified)": "声调 (shēng diào)",
        "Hindi": "स्वर (swar)"
    },
    "variety": {
        "Chinese (Simplified)": "多样性 (duō yàng xìng)",
        "Hindi": "विविधता (vividhata)"
    },
    "dish": {
        "Chinese (Simplified)": "菜 (cài)",
        "Hindi": "व्यंजन (vyanjan)"
    },
    "franchise": {
        "Chinese (Simplified)": "特许经营 (tè xǔ jīng yíng)",
        "Hindi": "फ्रेंचाइज़ (franchise)"
    },
    "flex": {
        "Chinese (Simplified)": "炫耀 (xuàn yào)",
        "Hindi": "दिखावा करना (dikhaava karna)"
    },
    "flexible": {
        "Chinese (Simplified)": "灵活的 (líng huó de)",
        "Hindi": "लचीला (lachila)"
    },
    "fetch": {
        "Chinese (Simplified)": "取回 (qǔ huí)",
        "Hindi": "लाना (laana)"
    },
    "wings": {
        "Chinese (Simplified)": "翅膀 (chì bǎng)",
        "Hindi": "पंख (pankh)"
    },
    "liberty": {
        "Chinese (Simplified)": "自由 (zì yóu)",
        "Hindi": "स्वतंत्रता (svatantrata)"
    },
    "statue": {
        "Chinese (Simplified)": "雕像 (diāo xiàng)",
        "Hindi": "प्रतिमा (pratima)"
    },
    "holy": {
        "Chinese (Simplified)": "神圣的 (shén shèng de)",
        "Hindi": "पवित्र (pavitra)"
    },
    "meditate": {
        "Chinese (Simplified)": "冥想 (míng xiǎng)",
        "Hindi": "ध्यान करना (dhyaan karna)"
    },
    "meditation": {
        "Chinese (Simplified)": "冥想 (míng xiǎng)",
        "Hindi": "ध्यान (dhyaan)"
    },
    "priest": {
        "Chinese (Simplified)": "牧师 (mù shī)",
        "Hindi": "पुजारी (pujaari)"
    },
    "band": {
        "Chinese (Simplified)": "乐队 (yuè duì)",
        "Hindi": "बैंड (band)"
    },
    "instrument": {
        "Chinese (Simplified)": "乐器 (yuè qì)",
        "Hindi": "संगीत वाद्य (sangeet vaadya)"
    },
    "dowry": {
        "Chinese (Simplified)": "嫁妆 (jià zhuāng)",
        "Hindi": "दहेज (dahej)"
    },
    "handshake": {
        "Chinese (Simplified)": "握手 (wò shǒu)",
        "Hindi": "हाथ मिलाना (haath milana)"
    },
    "energy": {
        "Chinese (Simplified)": "能量 (néng liàng)",
        "Hindi": "ऊर्जा (oorja)"
    },
    "crises": {
        "Chinese (Simplified)": "危机 (wēi jī)",
        "Hindi": "संकट (sankat)"
    },
    "marble": {
        "Chinese (Simplified)": "大理石 (dà lǐ shí)",
        "Hindi": "संगमरमर (sangmarmar)"
    },
    "premium": {
        "Chinese (Simplified)": "高级 (gāo jí)",
        "Hindi": "प्रीमियम (premium)"
    },
    "freemium": {
        "Chinese (Simplified)": "免费增值 (miǎn fèi zēng zhí)",
        "Hindi": "फ्रीमियम (freemium)"
    },
    "yeti": {
        "Chinese (Simplified)": "雪人 (xuě rén)",
        "Hindi": "येति (yeti)"
    },
    "speech": {
        "Chinese (Simplified)": "演讲 (yǎn jiǎng)",
        "Hindi": "भाषण (bhaashan)"
    },
    "teachings": {
        "Chinese (Simplified)": "教义 (jiào yì)",
        "Hindi": "शिक्षाएं (shikshaen)"
    },
    "fing": {
        "Chinese (Simplified)": "找不到对应词 (zhǎo bù dào duì yìng cí)",
        "Hindi": "इस शब्द का कोई स्पष्ट अर्थ नहीं है (is shabd ka koi spasht arth nahi hai)"
    },
    "bronze": {
        "Chinese (Simplified)": "青铜 (qīng tóng)",
        "Hindi": "कांस्य (kaansya)"
    },
    "pat": {
        "Chinese (Simplified)": "轻拍 (qīng pāi)",
        "Hindi": "थपथपाना (thapthapana)"
    },
    "big scam": {
        "Chinese (Simplified)": "大骗局 (dà piàn jú)",
        "Hindi": "बड़ा घोटाला (bada ghotala)"
    },
    "secretary": {
        "Chinese (Simplified)": "秘书 (mì shū)",
        "Hindi": "सचिव (sachiv)"
    },
    "alimony": {
        "Chinese (Simplified)": "赡养费 (shàn yǎng fèi)",
        "Hindi": "गुजारा भत्ता (guzaara bhatta)"
    },
    "injustice": {
        "Chinese (Simplified)": "不公正 (bù gōng zhèng)",
        "Hindi": "अन्याय (anyaay)"
    },
    "ego": {
        "Chinese (Simplified)": "自我 (zì wǒ)",
        "Hindi": "अहम (aham)"
    },
    "internship": {
        "Chinese (Simplified)": "实习 (shí xí)",
        "Hindi": "इंटर्नशिप (internship)"
    },
    "least": {
        "Chinese (Simplified)": "最少 (zuì shǎo)",
        "Hindi": "कम से कम (kam se kam)"
    },
    "atleast": {
        "Chinese (Simplified)": "至少 (zhì shǎo)",
        "Hindi": "कम से कम (kam se kam)"
    },
    "guilt": {
        "Chinese (Simplified)": "内疚 (nèi jiù)",
        "Hindi": "अपराधबोध (aparaadhbodh)"
    },
    "pie": {
        "Chinese (Simplified)": "馅饼 (xiàn bǐng)",
        "Hindi": "पाई (pai)"
    },
    "chance": {
        "Chinese (Simplified)": "机会 (jī huì)",
        "Hindi": "अवसर (avasar)"
    },
    "asleep": {
        "Chinese (Simplified)": "睡着的 (shuì zháo de)",
        "Hindi": "सोया हुआ (soya hua)"
    },
    "slept": {
        "Chinese (Simplified)": "睡了 (shuì le)",
        "Hindi": "सोया (soya)"
    },
    "nomad": {
        "Chinese (Simplified)": "游牧民 (yóu mù mín)",
        "Hindi": "घुमंतू (ghumantu)"
    },
    "pastoralist": {
        "Chinese (Simplified)": "牧民 (mù mín)",
        "Hindi": "चरवाहा (charwaha)"
    },
    "overpowered": {
        "Chinese (Simplified)": "压倒 (yā dǎo)",
        "Hindi": "प्रबल (prabal)"
    },
    "abandon": {
        "Chinese (Simplified)": "放弃 (fàng qì)",
        "Hindi": "त्याग देना (tyaag dena)"
    },
    "abolish": {
        "Chinese (Simplified)": "废除 (fèi chú)",
        "Hindi": "समाप्त करना (samaapt karna)"
    },
    "abscond": {
        "Chinese (Simplified)": "潜逃 (qián táo)",
        "Hindi": "फरार होना (faraar hona)"
    },
    "accelerate": {
        "Chinese (Simplified)": "加速 (jiā sù)",
        "Hindi": "तेज़ करना (tez karna)"
    },
    "advocate": {
        "Chinese (Simplified)": "提倡 (tí chàng)",
        "Hindi": "वकालत करना (vakalat karna)"
    },
    "backbite": {
        "Chinese (Simplified)": "背后诽谤 (bèi hòu fěi bàng)",
        "Hindi": "पीठ पीछे बुराई करना (peeth peeche buraai karna)"
    },
    "chasm": {
        "Chinese (Simplified)": "鸿沟 (hóng gōu)",
        "Hindi": "गहरा खाई (gehra khaai)"
    },
    "sarcasm": {
        "Chinese (Simplified)": "讽刺 (fěng cì)",
        "Hindi": "व्यंग्य (vyangya)"
    },
    "sarcastic": {
        "Chinese (Simplified)": "讽刺的 (fěng cì de)",
        "Hindi": "ताने भरा (taane bhara)"
    },
    "cringe": {
        "Chinese (Simplified)": "畏缩 (wèi suō)",
        "Hindi": "सिकुड़ना (sikudna)"
    },
    "phobia": {
        "Chinese (Simplified)": "恐惧症 (kǒng jù zhèng)",
        "Hindi": "फोबिया (phobia)"
    },
    "cliche": {
        "Chinese (Simplified)": "陈词滥调 (chén cí làn diào)",
        "Hindi": "घिसा-पिटा वाक्यांश (ghisa-pita vaakyansh)"
    },
    "delicate": {
        "Chinese (Simplified)": "精致的 (jīng zhì de)",
        "Hindi": "नाज़ुक (naazuk)"
    },
    "depict": {
        "Chinese (Simplified)": "描绘 (miáo huì)",
        "Hindi": "चित्रित करना (chitrit karna)"
    },
    "isolate": {
        "Chinese (Simplified)": "隔离 (gé lí)",
        "Hindi": "अलग करना (alag karna)"
    },
    "endure": {
        "Chinese (Simplified)": "忍受 (rěn shòu)",
        "Hindi": "सहना (sahana)"
    },
    "suffer": {
        "Chinese (Simplified)": "遭受 (zāo shòu)",
        "Hindi": "झेलना (jhelna)"
    },
    "extricate": {
        "Chinese (Simplified)": "解脱 (jiě tuō)",
        "Hindi": "मुक्त करना (mukt karna)"
    },
    "fidelity": {
        "Chinese (Simplified)": "忠诚 (zhōng chéng)",
        "Hindi": "निष्ठा (nishtha)"
    },
    "gamble": {
        "Chinese (Simplified)": "赌博 (dǔ bó)",
        "Hindi": "जुआ खेलना (jua khelna)"
    },
    "gaze": {
        "Chinese (Simplified)": "凝视 (níng shì)",
        "Hindi": "घूरना (ghurna)"
    },
    "genre": {
        "Chinese (Simplified)": "类型 (lèi xíng)",
        "Hindi": "शैली (shailee)"
    },
    "genial": {
        "Chinese (Simplified)": "和蔼的 (hé ǎi de)",
        "Hindi": "मिलनसार (milansaar)"
    },
    "haughty": {
        "Chinese (Simplified)": "傲慢的 (ào màn de)",
        "Hindi": "घमंडी (ghamandi)"
    },
    "imperative": {
        "Chinese (Simplified)": "必要的 (bì yào de)",
        "Hindi": "आवश्यक (aavashyak)"
    },
    "indigenous": {
        "Chinese (Simplified)": "本土的 (běn tǔ de)",
        "Hindi": "देशज (deshaj)"
    },
    "judicious": {
        "Chinese (Simplified)": "明智的 (míng zhì de)",
        "Hindi": "समझदार (samajhdar)"
    },
    "keen": {
        "Chinese (Simplified)": "热衷的 (rè zhōng de)",
        "Hindi": "उत्सुक (utsuk)"
    },
    "kickoff": {
        "Chinese (Simplified)": "开球 (kāi qiú)",
        "Hindi": "आरंभ (aarambh)"
    },
    "kindle": {
        "Chinese (Simplified)": "点燃 (diǎn rán)",
        "Hindi": "प्रज्वलित करना (prajwalit karna)"
    },
    "knight": {
        "Chinese (Simplified)": "骑士 (qí shì)",
        "Hindi": "योद्धा (yoddha)"
    },
    "lunatic": {
        "Chinese (Simplified)": "疯子 (fēng zi)",
        "Hindi": "पागल (paagal)"
    },
    "mandarin": {
        "Chinese (Simplified)": "普通话 (pǔ tōng huà)",
        "Hindi": "मंदारिन (mandarin)"
    },
    "mediocre": {
        "Chinese (Simplified)": "平庸的 (píng yōng de)",
        "Hindi": "सामान्य (saamanya)"
    },
    "merchandise": {
        "Chinese (Simplified)": "商品 (shāng pǐn)",
        "Hindi": "माल (maal)"
    },
    "nemesis": {
        "Chinese (Simplified)": "死敌 (sǐ dí)",
        "Hindi": "शत्रु (shatru)"
    },
    "nepotism": {
        "Chinese (Simplified)": "裙带关系 (qún dài guān xì)",
        "Hindi": "भाई-भतीजावाद (bhai-bhatijavaad)"
    },
    "niche": {
        "Chinese (Simplified)": "利基 (lì jī)",
        "Hindi": "स्थान (sthaan)"
    },
    "nirvana": {
        "Chinese (Simplified)": "涅槃 (niè pán)",
        "Hindi": "निर्वाण (nirvaan)"
    },
    "oblivious": {
        "Chinese (Simplified)": "忘记的 (wàng jì de)",
        "Hindi": "अनजान (anjaan)"
    },
    "obscure": {
        "Chinese (Simplified)": "模糊的 (mó hú de)",
        "Hindi": "अस्पष्ट (asparsh)"
    },
    "odor": {
        "Chinese (Simplified)": "气味 (qì wèi)",
        "Hindi": "गंध (gandh)"
    },
    "omen": {
        "Chinese (Simplified)": "预兆 (yù zhào)",
        "Hindi": "शकुन (shakun)"
    },
    "overwhelm": {
        "Chinese (Simplified)": "压倒 (yā dǎo)",
        "Hindi": "पराजित करना (parajit karna)"
    },
    "protocol": {
        "Chinese (Simplified)": "协议 (xié yì)",
        "Hindi": "प्रोटोकॉल (protocol)"
    },
    "remorse": {
        "Chinese (Simplified)": "悔恨 (huǐ hèn)",
        "Hindi": "पश्चाताप (pashchataap)"
    },
    "satire": {
        "Chinese (Simplified)": "讽刺 (fěng cì)",
        "Hindi": "व्यंग्य (vyangya)"
    },
    "seminal": {
        "Chinese (Simplified)": "开创性的 (kāi chuàng xìng de)",
        "Hindi": "प्रारंभिक (praarambhik)"
    },
    "tactical": {
        "Chinese (Simplified)": "战术的 (zhàn shù de)",
        "Hindi": "युद्धनीतिक (yuddhneetik)"
    },
    "taunt": {
        "Chinese (Simplified)": "嘲讽 (cháo fěng)",
        "Hindi": "ताना मारना (taana maarna)"
    },
    "wound": {
        "Chinese (Simplified)": "伤口 (shāng kǒu)",
        "Hindi": "घाव (ghaav)"
    },
    "termination": {
        "Chinese (Simplified)": "终止 (zhōng zhǐ)",
        "Hindi": "समाप्ति (samaapti)"
    },
    "utility": {
        "Chinese (Simplified)": "实用性 (shí yòng xìng)",
        "Hindi": "उपयोगिता (upayogita)"
    },
    "valour": {
        "Chinese (Simplified)": "英勇 (yīng yǒng)",
        "Hindi": "वीरता (veerata)"
    },
    "versatile": {
        "Chinese (Simplified)": "多才多艺的 (duō cái duō yì de)",
        "Hindi": "बहुमुखी (bahumukhi)"
    },
    "wardrobe": {
        "Chinese (Simplified)": "衣柜 (yī guì)",
        "Hindi": "अलमारी (almaari)"
    },
    "wanderlust": {
        "Chinese (Simplified)": "旅行癖 (lǚ xíng pǐ)",
        "Hindi": "यात्रा की लालसा (yaatra ki laalsa)"
    },
    "yank": {
        "Chinese (Simplified)": "猛拉 (měng lā)",
        "Hindi": "झटके से खींचना (jhatke se kheenchna)"
    },
    "yatter": {
        "Chinese (Simplified)": "喋喋不休 (dié dié bù xiū)",
        "Hindi": "बकबक (bakbak)"
    },
    "zest": {
        "Chinese (Simplified)": "热情 (rè qíng)",
        "Hindi": "उत्साह (utsah)"
    },
    "boy": {
        "Chinese (Simplified)": "男孩 (nán hái)",
        "Hindi": "लड़का (ladka)"
    },
    "girl": {
        "Chinese (Simplified)": "女孩 (nǚ hái)",
        "Hindi": "लड़की (ladki)"
    },
    "siblings": {
        "Chinese (Simplified)": "兄弟姐妹 (xiōng dì jiě mèi)",
        "Hindi": "भाई-बहन (bhai-behan)"
    },
    "parenting": {
        "Chinese (Simplified)": "育儿 (yù ér)",
        "Hindi": "पालन-पोषण (paalan-poshan)"
    },
    "babysitting": {
        "Chinese (Simplified)": "照看孩子 (zhào kàn hái zi)",
        "Hindi": "बच्चों की देखभाल (bachchon ki dekhbhal)"
    },
    "babysitter": {
        "Chinese (Simplified)": "保姆 (bǎo mǔ)",
        "Hindi": "शिशु-पालक (shishu-palak)"
    },
    "traits": {
        "Chinese (Simplified)": "特征 (tè zhēng)",
        "Hindi": "गुण (gun)"
    },
    "new year": {
        "Chinese (Simplified)": "新年 (xīn nián)",
        "Hindi": "नया साल (naya saal)"
    },
    "newyear": {
        "Chinese (Simplified)": "新年 (xīn nián)",
        "Hindi": "नया साल (naya saal)"
    },
    "christmas": {
        "Chinese (Simplified)": "圣诞节 (shèng dàn jié)",
        "Hindi": "क्रिसमस (krismas)"
    },
    "merry": {
        "Chinese (Simplified)": "愉快的 (yú kuài de)",
        "Hindi": "खुश (khush)"
    },
    "marry": {
        "Chinese (Simplified)": "结婚 (jié hūn)",
        "Hindi": "शादी करना (shaadi karna)"
    },
    "snowfall": {
        "Chinese (Simplified)": "降雪 (jiàng xuě)",
        "Hindi": "बर्फबारी (barfbaari)"
    },
}

def translate_word(word, language):
    word = word.lower()
    if word in translations_dict:
        return translations_dict[word].get(language, "Translation not available for this language.")
    else:
        return f"Sorry, the word '{word}' is not in the dictionary."
def main():
    print("--==} ENGLISH TO HINDI AND CHINESE TRANSLATOR {==--")
    print("Created By LUCKYS1NGHH (Github)")
    while True:
        language_choice = input("\nChoose the language -\n1. Hindi\n2. Chinese\nor type 'exit' to quit: ").strip().lower()
        if language_choice == "1" or "hindi" in language_choice:
            language = "Hindi"
            print(f"You chose: {language}")
        elif language_choice == "2" or "chinese" in language_choice:
            language = "Chinese (Simplified)"
            print(f"You chose: {language}")
        elif "exit" in language_choice:
            print("Goodbye!")
            break
        elif "printall" in language_choice:
            for index, (key, value) in enumerate(translations_dict.items(), start=1):
                print(f"{index}. {key}: {value}")
            break
        else:
            print("Invalid language choice, please choose either 'Hindi' or 'Chinese'.")
            continue

        word = input("Enter an English word to translate: ").strip()
        translation = translate_word(word, language)
        print(f"Translation in {language}: {translation}")

# Printing with numbered indexing
if __name__ == "__main__":
    main()
