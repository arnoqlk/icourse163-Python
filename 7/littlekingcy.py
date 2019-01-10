# 小王子词云
import wordcloud
from scipy.misc import imread
mask = imread(r"D:\PyCode\7\chinamap.jpg")
exclude = {}
f = open(r"D:\PyCode\7\Littleprince.txt", "r")
t = f.read()
f.close()
w = wordcloud.WordCloud(\
    width=1000, height=700, \
    background_color="white", \
    font_path="msyh.ttc", mask=mask
    )
w.generate(t)
w.to_file("litteprince.png")