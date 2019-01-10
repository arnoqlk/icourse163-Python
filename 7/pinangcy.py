import jieba
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

back_color = imread("D:\\PyCode\\7\\chinamap.jpg")     # 解析图片

wc = WordCloud(background_color="white",
                max_words=100,
                mask=back_color,
                max_font_size=100,
                # stopwords=STOPWORDS.add(""),  # 使用内置的方法添加屏蔽词
                font_path="C:/Windows/Fonts/STFANGSO.ttf",
                random_state=42,
                # width=1000,
                # height=860
                )

jieba.add_word("金三胖")    # 添加到词库,处理文本中歧义词为该指定词
text = open("D:/PyCode/7/pinang.txt").read()    # 打开词源文件

# 提前将屏蔽词存入stopwords.txt中
# def stop_words(texts):
    # words_list = []
    # word_generator = jieba.cut(texts, cut_all=False)    # 返回一个迭代器

    # word_list = jieba.lcut(texts)
    # with open(r"D:\PyCode\7\stopwords.txt","r") as f:
    #     f.read()
    #     # unicode_text = unicode(str_text, "utf-8")
    #     f.close()

    # for word in word_generator:       迭代器的惯用格式
    #     if word.strip() not in f:
    #         words_list.append(word)

    # return ' '.join(word_list)
    # return word_list

# text = stop_words(text)

wc.generate(text)
image_colors = ImageColorGenerator(back_color)
plt.imshow(wc)
plt.axis('off')

plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
wc.to_file('output.png')
