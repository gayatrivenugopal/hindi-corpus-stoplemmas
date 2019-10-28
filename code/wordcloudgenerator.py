from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

words = {'का':8,
'कर':8,
'है':8,
'में':8,
'यह':8,
'हो':6,
'जा':6,
'और':6,
'से':6,
'वह':5,
'को':3,
'नहीं':1,
'दे':1,
'ले':1,
'राजा':1,
'था':1,
'मैं':1,
'आप':1,
'एक':1
}

wc = WordCloud(font_path='/usr/share/fonts/truetype/mangal/MANGAL.TTF', background_color="white",width=1000,height=1000, max_words=100,relative_scaling=0.25,normalize_plurals=False).generate_from_frequencies(words)
plt.imshow(wc)
plt.show()
