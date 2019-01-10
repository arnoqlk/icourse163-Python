from os import path
from wordcloud import WordCloud, ImageColorGenerator
import jieba.analyse
import matplotlib.pyplot as plt
from scipy.misc import imread

class cloud:
    def __init__(self, filename, image_filename, font_filename):
        self.d = path.dirname(__name__)
        content = open(path.join(self.d, filename), 'rb').read()
        # 基于TF-IDF算法的关键字抽取, topK返回频率最高的几项, 默认值为20, withWeight
        # 为是否返回关键字的权重
        tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
        self.text = " ".join(tags)
        # 需要显示的背景图片
        self.img = imread(path.join(self.d, image_filename))
        # 指定中文字体, 不然会乱码的
        self.wc = WordCloud(font_path=font_filename, background_color='white',
                        max_words=300, mask=self.img, max_font_size=40,
                        random_state=42)
        self.wc.generate(self.text)


    def show_wc(self):
        '''显示生成的词云图'''
        # 让词的颜色和图片的颜色一样
        img_color = ImageColorGenerator(self.img)
        plt.imshow(self.wc.recolor(color_func=img_color))
        plt.axis("off")
        plt.show()

    def save_wc(self, out_filename):
        '''保存到当前目录下'''
        self.wc.to_file(path.join(self.d, out_filename))

if __name__ == '__main__':
    wc = cloud("pinang.txt", "chinamap.jpg", "font.ttc")
    wc.show_wc()
    wc.save_wc('output.jpg')