#Source: stackoverflow.com/questions/53278942/how-to-send-another-request-and-get-result-in-scrapy-parse-function
# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import unquote
from scrapy.http import Request

class MetadataSpider(scrapy.Spider):
    name = 'metadata'
    #start_urls = ['https://www.google.co.in/search?q=hindisamay+अतिथि-तुम-कब-जाओगे']
    index = -1
    
    start_urls = ['https://www.google.co.in/search?q=hindisamay+अनुपमा-का-प्रेम',
'https://www.google.co.in/search?q=hindisamay+अन्तिम-प्यार',
'https://www.google.co.in/search?q=hindisamay+अन्नपूर्णा-मंडल-की-आखिरी-चिट्ठी',
'https://www.google.co.in/search?q=hindisamay+अपना-खाना-ख़ुद-गर्म-करो',
'https://www.google.co.in/search?q=hindisamay+अपने-विरुद्ध',
'https://www.google.co.in/search?q=hindisamay+अपरिचिता',
'https://www.google.co.in/search?q=hindisamay+अमरीखान-के-लमडे',
'https://www.google.co.in/search?q=hindisamay+अमृतसर-आ-गया-है',
'https://www.google.co.in/search?q=hindisamay+अर्धांगिनी',
'https://www.google.co.in/search?q=hindisamay+अलिफ-लैला',
'https://www.google.co.in/search?q=hindisamay+अलिफ-लैला1',
'https://www.google.co.in/search?q=hindisamay+अलिफ-लैला2',
'https://www.google.co.in/search?q=hindisamay+अलिफ-लैला3',
'https://www.google.co.in/search?q=hindisamay+अवांतर-कथा',
'https://www.google.co.in/search?q=hindisamay+अशोक',
'https://www.google.co.in/search?q=hindisamay+असलियत',
'https://www.google.co.in/search?q=hindisamay+अहिंसा---विश्वकोश',
'https://www.google.co.in/search?q=hindisamay+आलोचना',
'https://www.google.co.in/search?q=hindisamay+आषाढ़-का-एक-दिन',
'https://www.google.co.in/search?q=hindisamay+एक-छाया-चेहरे-से-गुजरी-जैसे-पत्ता-खड़का-हो',
'https://www.google.co.in/search?q=hindisamay+एनिमल-फार्म',
'https://www.google.co.in/search?q=hindisamay+कमजोर-की-मजबूती',
'https://www.google.co.in/search?q=hindisamay+कर्मभूमि',
'https://www.google.co.in/search?q=hindisamay+कविता-में-इतिहास-बोध-और-इतिहास-बोध-की-कविता',
'https://www.google.co.in/search?q=hindisamay+कस्तूरी-कुंडल-बसै',
'https://www.google.co.in/search?q=hindisamay+किडनी-चोर-को-रिहा-करो',
'https://www.google.co.in/search?q=hindisamay+कॉमरेड-का-कहना-है',
'https://www.google.co.in/search?q=hindisamay+गरीब-कौन',
'https://www.google.co.in/search?q=hindisamay+गांधी-का-सर्वोत्तम-उपवास-और-अहिंसा-की-असहायता',
'https://www.google.co.in/search?q=hindisamay+गांधी-बनाम-गांधी',
'https://www.google.co.in/search?q=hindisamay+गांधी-विचार-की-सब-से-बड़ी-कमी',
'https://www.google.co.in/search?q=hindisamay+चरित्र-शोधन',
'https://www.google.co.in/search?q=hindisamay+चरित्रपालन',
'https://www.google.co.in/search?q=hindisamay+चाँदी-का-जूता',
'https://www.google.co.in/search?q=hindisamay+चारुचरित्र',
'https://www.google.co.in/search?q=hindisamay+चिड़िया',
'https://www.google.co.in/search?q=hindisamay+चित्त-और-चक्षु-का-घनिष्ठ-संबंध',
'https://www.google.co.in/search?q=hindisamay+चीन-से-कौन-डरता-है',
'https://www.google.co.in/search?q=hindisamay+चौराहे-पर-लड़की',
'https://www.google.co.in/search?q=hindisamay+जाति',
'https://www.google.co.in/search?q=hindisamay+जो-गिरफ्तार-नहीं-हुए',
'https://www.google.co.in/search?q=hindisamay+जोश-में-न-आइये',
'https://www.google.co.in/search?q=hindisamay+ज्ञाति-विवेकिनी-सभा',
'https://www.google.co.in/search?q=hindisamay+झाँकी-हिन्दुस्तान-की',
'https://www.google.co.in/search?q=hindisamay+तीन-सिद्धान्तवादी',
'https://www.google.co.in/search?q=hindisamay+तो',
'https://www.google.co.in/search?q=hindisamay+द',
'https://www.google.co.in/search?q=hindisamay+दल-का-अगुआ-कैसा-हो',
'https://www.google.co.in/search?q=hindisamay+दलित-अस्मिता-और-एजेंडा-जाति-विनाश-का',
'https://www.google.co.in/search?q=hindisamay+दलित-की-बेटी',
'https://www.google.co.in/search?q=hindisamay+दिल-बहलाव',
'https://www.google.co.in/search?q=hindisamay+दीप-की-अभिलाषा',
'https://www.google.co.in/search?q=hindisamay+दीपमाला',
'https://www.google.co.in/search?q=hindisamay+दो-अंधों-की-बातचीत',
'https://www.google.co.in/search?q=hindisamay+दौड़',
'https://www.google.co.in/search?q=hindisamay+दौड़-धूप',
'https://www.google.co.in/search?q=hindisamay+धर्म-की-आड़',
'https://www.google.co.in/search?q=hindisamay+नई-बात-की-चाह-लोगों-में-क्यों-होती-है',
'https://www.google.co.in/search?q=hindisamay+नक्सलवादियों-से-बातचीत',
'https://www.google.co.in/search?q=hindisamay+नदी-के-द्वीप',
'https://www.google.co.in/search?q=hindisamay+नाक',
'https://www.google.co.in/search?q=hindisamay+नाम',
'https://www.google.co.in/search?q=hindisamay+नारायण',
'https://www.google.co.in/search?q=hindisamay+निठारी-चलो',
'https://www.google.co.in/search?q=hindisamay+निठारी-वाले-अंकल',
'https://www.google.co.in/search?q=hindisamay+नियति-के-हाथों-में-झूलती-जु-डोउ',
'https://www.google.co.in/search?q=hindisamay+निर्मला',
'https://www.google.co.in/search?q=hindisamay+पत्रकार-कला-पुस्तक-की-भूमिका',
'https://www.google.co.in/search?q=hindisamay+परिवार-में-पुलिस',
'https://www.google.co.in/search?q=hindisamay+पार्क-में-आंबेडकर',
'https://www.google.co.in/search?q=hindisamay+पिटने-पिटने-में-फर्क',
'https://www.google.co.in/search?q=hindisamay+पौगंड-या-कैशोर',
'https://www.google.co.in/search?q=hindisamay+प्रकाश',
'https://www.google.co.in/search?q=hindisamay+बदरंग-वीसा',
'https://www.google.co.in/search?q=hindisamay+बना-रहे-बनारस',
'https://www.google.co.in/search?q=hindisamay+बन्दर-सभा',
'https://www.google.co.in/search?q=hindisamay+बात',
'https://www.google.co.in/search?q=hindisamay+बातचीत',
'https://www.google.co.in/search?q=hindisamay+बाबा',
'https://www.google.co.in/search?q=hindisamay+बाल्यविवाह-विषयक-एक-चोज',
'https://www.google.co.in/search?q=hindisamay+बेटी',
'https://www.google.co.in/search?q=hindisamay+भविष्य-का-भारत',
'https://www.google.co.in/search?q=hindisamay+भारत-का-त्रिकाल',
'https://www.google.co.in/search?q=hindisamay+भारत-को-चाहिए-जादूगर-और-साधु',
'https://www.google.co.in/search?q=hindisamay+भारत-सरकार-के-तीन-वक्तव्य',
'https://www.google.co.in/search?q=hindisamay+भारतीय-अपराध-अकादमी',
'https://www.google.co.in/search?q=hindisamay+भाषा',
'https://www.google.co.in/search?q=hindisamay+भाषा-और-साहित्या',
'https://www.google.co.in/search?q=hindisamay+भाषाओं-का-परिर्वतन',
'https://www.google.co.in/search?q=hindisamay+भीम-राव-अंबेडकर-और-दलित-चिंतन-की-प्रतिबद्धता-परिवर्ती-अंबेडकरवाद-या-दलित-नवजागरण-युग',
'https://www.google.co.in/search?q=hindisamay+भूल-सुधार',
'https://www.google.co.in/search?q=hindisamay+भोलाराम-का-जीव',
'https://www.google.co.in/search?q=hindisamay+भौं',
'https://www.google.co.in/search?q=hindisamay+मतवालों-की-समझ',
'https://www.google.co.in/search?q=hindisamay+मत्स्य-न्याय',
'https://www.google.co.in/search?q=hindisamay+मन-और-नेत्र',
'https://www.google.co.in/search?q=hindisamay+मन-और-प्राण',
'https://www.google.co.in/search?q=hindisamay+मन-के-गुण',
'https://www.google.co.in/search?q=hindisamay+मनुष्य-की-बाहरी-आकृति-मन-की-एक-प्रतिकृति-है',
'https://www.google.co.in/search?q=hindisamay+मनुष्य-के-जीवन-की-सार्थकता',
'https://www.google.co.in/search?q=hindisamay+महँगाई-देवी',
'https://www.google.co.in/search?q=hindisamay+महँगाई-में-प्रधानमंत्री',
'https://www.google.co.in/search?q=hindisamay+महत्व',
'https://www.google.co.in/search?q=hindisamay+महर्षि-दादाभाई-नौरोजी',
'https://www.google.co.in/search?q=hindisamay+महात्मा-प्रिंस-क्रोपटकिन',
'https://www.google.co.in/search?q=hindisamay+महाशक्ति-की-दीनता',
'https://www.google.co.in/search?q=hindisamay+माँ-के-आँचल-में',
'https://www.google.co.in/search?q=hindisamay+माता-का-स्नेह',
'https://www.google.co.in/search?q=hindisamay+माधुर्य',
'https://www.google.co.in/search?q=hindisamay+मानना-और-मनाना',
'https://www.google.co.in/search?q=hindisamay+मानव-स्वत्व',
'https://www.google.co.in/search?q=hindisamay+मायावती-से-मिलने-के-बाद',
'https://www.google.co.in/search?q=hindisamay+मार्क्स-की-वापसी',
'https://www.google.co.in/search?q=hindisamay+मार्क्स-के-संस्मरण',
'https://www.google.co.in/search?q=hindisamay+मित्र-कपटी-भी-बुरा-नहीं-होता',
'https://www.google.co.in/search?q=hindisamay+मीडिया-के-सामाजिक-सरोकार',
'https://www.google.co.in/search?q=hindisamay+मैंनेजमेंट-की-सोच',
'https://www.google.co.in/search?q=hindisamay+मॉडल-छात्र-प्रतियोगिता-2007',
'https://www.google.co.in/search?q=hindisamay+मौलाना-हसरत-मोहानी',
'https://www.google.co.in/search?q=hindisamay+यथार्थ-का-अनुभव-और-अनुभव-का-यथार्थ-पक्ष-प्रतिपक्ष',
'https://www.google.co.in/search?q=hindisamay+यस-सर',
'https://www.google.co.in/search?q=hindisamay+यौन-प्रदूषण-बाल-शोषण',
'https://www.google.co.in/search?q=hindisamay+रक्ताश्रु',
'https://www.google.co.in/search?q=hindisamay+रणधीर-प्रेममोहिनी-की',
'https://www.google.co.in/search?q=hindisamay+रणभूमि-में-भाषा',
'https://www.google.co.in/search?q=hindisamay+रसिक-समाज',
'https://www.google.co.in/search?q=hindisamay+राजा-और-प्रजा',
'https://www.google.co.in/search?q=hindisamay+राम',
'https://www.google.co.in/search?q=hindisamay+राष्ट्र-की-आशा',
'https://www.google.co.in/search?q=hindisamay+राष्ट्र-की-नींव',
'https://www.google.co.in/search?q=hindisamay+राष्ट्रवाद-का-अंबेडकरी-पाठ',
'https://www.google.co.in/search?q=hindisamay+राष्ट्रीय-शिक्षा-II',
'https://www.google.co.in/search?q=hindisamay+राष्ट्रीयता',
'https://www.google.co.in/search?q=hindisamay+रिशवत',
'https://www.google.co.in/search?q=hindisamay+रेनकोट',
'https://www.google.co.in/search?q=hindisamay+रोने-का-राज',
'https://www.google.co.in/search?q=hindisamay+लक्ष्मी',
'https://www.google.co.in/search?q=hindisamay+लक्ष्य-से-दूर',
'https://www.google.co.in/search?q=hindisamay+लगाम',
'https://www.google.co.in/search?q=hindisamay+लड़की-की-पुनर्रचना',
'https://www.google.co.in/search?q=hindisamay+लिव-इन-रिलेशनशिप',
'https://www.google.co.in/search?q=hindisamay+लो-मैं-आ-गई',
'https://www.google.co.in/search?q=hindisamay+लोक-एषणा',
'https://www.google.co.in/search?q=hindisamay+लोक-सेवा',
'https://www.google.co.in/search?q=hindisamay+लोकमान्य-की-विजय',
'https://www.google.co.in/search?q=hindisamay+वज्रपात-देशबंधु-दास',
'https://www.google.co.in/search?q=hindisamay+वरदान',
'https://www.google.co.in/search?q=hindisamay+वर्ण-व्यवस्था-का-भंडाफोड़-वर्ण-व्यवस्था-विध्वंस',
'https://www.google.co.in/search?q=hindisamay+वर्षारंभ',
'https://www.google.co.in/search?q=hindisamay+वह-अधनंगा-फकीर',
'https://www.google.co.in/search?q=hindisamay+वह-जो-आदमी-है-न',
'https://www.google.co.in/search?q=hindisamay+वह-स्कूल-खोलेगा',
'https://www.google.co.in/search?q=hindisamay+वही-हूँ',
'https://www.google.co.in/search?q=hindisamay+वाजिदअलीशाह',
'https://www.google.co.in/search?q=hindisamay+वायु',
'https://www.google.co.in/search?q=hindisamay+विक्टिर-ह्यूगो',
'https://www.google.co.in/search?q=hindisamay+वियोगी-बाबा',
'https://www.google.co.in/search?q=hindisamay+विलायत-यात्रा',
'https://www.google.co.in/search?q=hindisamay+विश्वास',
'https://www.google.co.in/search?q=hindisamay+वीजा-के-लिए-इंतजार',
'https://www.google.co.in/search?q=hindisamay+शब्द-मौन-अस्तित्व',
'https://www.google.co.in/search?q=hindisamay+शब्दों-की-आकर्षण-शक्ति',
'https://www.google.co.in/search?q=hindisamay+शर्म-की-बात-पर-ताली-पीटना',
'https://www.google.co.in/search?q=hindisamay+शहर-में',
'https://www.google.co.in/search?q=hindisamay+शहर-में-कर्फ्यू',
'https://www.google.co.in/search?q=hindisamay+शिक्षा-का-प्रथम---I',
'https://www.google.co.in/search?q=hindisamay+शेर-की-गुफा-में-न्याय',
'https://www.google.co.in/search?q=hindisamay+सच-अपने-हिसाब-से',
'https://www.google.co.in/search?q=hindisamay+सच-का-सामना',
'https://www.google.co.in/search?q=hindisamay+सच्ची-समालोचना',
'https://www.google.co.in/search?q=hindisamay+सतपुड़ा-के-भीतर-से',
'https://www.google.co.in/search?q=hindisamay+सती-प्रताप',
'https://www.google.co.in/search?q=hindisamay+सती-मैया-का-चौरा',
'https://www.google.co.in/search?q=hindisamay+सत्य-हरिश्चन्द्र',
'https://www.google.co.in/search?q=hindisamay+सदा-आनंद-रहे-एहि-द्वारे',
'https://www.google.co.in/search?q=hindisamay+सन-1950-ईसवी',
'https://www.google.co.in/search?q=hindisamay+सबसे-बड़ी-चुनौती',
'https://www.google.co.in/search?q=hindisamay+समकालीन-हिंदी-कविता-और-दलित-चेतना',
'https://www.google.co.in/search?q=hindisamay+समय',
'https://www.google.co.in/search?q=hindisamay+समुद्र-मंथन',
'https://www.google.co.in/search?q=hindisamay+सर्वदलीय-सांसद-महासंघ-का-प्रस्ताव',
'https://www.google.co.in/search?q=hindisamay+सलीम-को-दया-और-सुहानुभूति-नहीं-रोशनी-का-पता-बताने-वाला-कोई-चाहिए-सलीम-लंगड़े-पे-मत-रो',
'https://www.google.co.in/search?q=hindisamay+सहबास-बिल-अवश्य-पास-होगा',
'https://www.google.co.in/search?q=hindisamay+साँची-कहौ-व्रजराज-तुम्हें-रतिराज-किधौ-रितुराज-कियौ-है',
'https://www.google.co.in/search?q=hindisamay+साँझ-भई',
'https://www.google.co.in/search?q=hindisamay+साझा-दुख',
'https://www.google.co.in/search?q=hindisamay+सांसदों-की-कीमत',
'https://www.google.co.in/search?q=hindisamay+साहब-का-बसंत',
'https://www.google.co.in/search?q=hindisamay+साहित्य-बोध-आधुनिकता-के-तत्त्व',
'https://www.google.co.in/search?q=hindisamay+साहित्य-संस्कृति-और-समाज-परिवर्तन-की-प्रक्रिया',
'https://www.google.co.in/search?q=hindisamay+सिद्धांतों-की-व्यर्थता',
'https://www.google.co.in/search?q=hindisamay+सिपाही-की-माँ',
'https://www.google.co.in/search?q=hindisamay+सिर-पर-शौचालय',
'https://www.google.co.in/search?q=hindisamay+सीमा-पर-नागरिक',
'https://www.google.co.in/search?q=hindisamay+सोश्यल-कान्फरेंस',
'https://www.google.co.in/search?q=hindisamay+स्केंडल',
'https://www.google.co.in/search?q=hindisamay+स्त्री-स्वर',
'https://www.google.co.in/search?q=hindisamay+हकीकत',
'https://www.google.co.in/search?q=hindisamay+हम-डार-डार-तुम-पात-पात',
'https://www.google.co.in/search?q=hindisamay+हम-सब-चोर-हैं',
'https://www.google.co.in/search?q=hindisamay+हमारा-दास्य-भाव',
'https://www.google.co.in/search?q=hindisamay+हमारा-सार्वजनिक-जीवन',
'https://www.google.co.in/search?q=hindisamay+हमारी-मृगतृष्णा',
'https://www.google.co.in/search?q=hindisamay+हमारी-विश्रृंखलता',
'https://www.google.co.in/search?q=hindisamay+हमारे-गुमशुदा-बच्चे',
'https://www.google.co.in/search?q=hindisamay+हमारे-जातीय-जीवन-के-दोष',
'https://www.google.co.in/search?q=hindisamay+हमारे-वे-मतवाले-निर्वासित-वीर',
'https://www.google.co.in/search?q=hindisamay+हल्दी-दूब-और-दधि-अच्छत',
'https://www.google.co.in/search?q=hindisamay+हिंदी-जाति-की-समस्याएँ',
'https://www.google.co.in/search?q=hindisamay+हिंदी-पत्रकारिता-की-भाषा',
'https://www.google.co.in/search?q=hindisamay+हिंदू-जाति-का-स्वाभाविक-गुण',
'https://www.google.co.in/search?q=hindisamay+हिंदू-मुस्लिम-विद्वेष-और-भारत-सरकार',
'https://www.google.co.in/search?q=hindisamay+हिन्दी-की-शोक-सभा',
'https://www.google.co.in/search?q=hindisamay+हिम्मत-राखो-एक-दिन-नागरी-का-प्रचार-होहीगा',
'https://www.google.co.in/search?q=hindisamay+हो-ओ-ओ-ली-है',
'https://www.google.co.in/search?q=hindisamay+होरहा'
]

   # override method
    def start_requests(self):
        for url in self.start_urls:
            #url = url.replace('https','http')
            #url = unquote(url)
            item = {'start_url': url}
            request = Request(url)
            # set the meta['item'] to use the item in the next call back
            request.meta['item'] = item
            yield request

    def parse(self, response):
        dirpath = 'hindisamay/metadata/'
        url = response.meta['item']['start_url']
        url = unquote(url)
        filename = url[url.find('+')+1:]
        print('Title: ', filename)
        text = response.xpath("//body//div[@id='main']//div[@class='r']//a/@href").extract_first()
        print(text)
        url = text
	#url = text[text.find('=')+1:]
        #url = url.replace('https','http')
        url = unquote(url)
        print('URL: ', url)
        yield scrapy.Request(url, callback=self.parse_content, meta={'filename': filename})
    
    def parse_content(self, response):
        dirpath = 'hindisamay/metadata/'
        filename = response.meta['filename']
        url = response.xpath("//body//span[@id='lblWriterImage']//a/@href").extract_first().replace('http:','https:')
        print('URL:' + url)
        url = unquote(url)
        yield scrapy.Request(url, callback=self.parse_author, meta={'filename': filename})

    def parse_author(self, response):
        dirpath = 'hindisamay/metadata/'
        filename = response.meta['filename']
        text = response.xpath("//body//span[@id='ContentPlaceHolder1_lblName']//p/text()").extract_first()
        author = text
        print('author: ', author)
        text = response.xpath("//body//span[@id='ContentPlaceHolder1_lblLeft']//span/../text()").extract_first()
        dob = text[text.find(':')+1:text.find(',')]
        print('dob: ', dob)
        place = text[text.rfind(',')+1:]
        print('place: ', place)
        text = response.xpath("//body//span[@id='ContentPlaceHolder1_lblLeft']//div/text()")[-1].extract()
        if text.find('निधन') != -1:
            text = response.xpath("//body//span[@id='ContentPlaceHolder1_lblLeft']//p/text()")[-1].extract()
            death = text
            if death.find(',') != -1:
                death = death[:death.rfind(',')]
        else:
            death = ''
        print('death: ', death)
        print(filename + ',' + author + ',' + dob + '-' + death + ',' + place)
        file = open(dirpath + 'metadata.txt', 'a', encoding = 'utf-8')
        file.write(filename + ',' + author + ',' + dob + '-' + death + ',' + place + '\n')
        file.close()
