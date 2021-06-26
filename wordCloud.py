from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


f_font = "./src/AaChaoMianJin.ttf"
f_text = "./files/part-r-00000.txt"
f_mask = "./src/leimu.png"

def plt_imshow(freq = {}, ax = None, show = True):
    mask = np.array(Image.open(f_mask))
    color = ImageColorGenerator(mask)
    wcd = WordCloud(font_path=f_font, background_color='white',
                    mask = mask)
    wcd.generate_from_frequencies(freq)
    wcd.recolor(color_func = color)
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(wcd)
    ax.axis('off')

    if show:
        plt.show()
        fig.savefig(f'./files/wordCloud.png', bbox_inches='tight', dpi = 1000)

def count_freq(word_list_path):
    freq_dict = dict()
    with open(word_list_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip().split()
            k = line[0]
            v = int(line[1])
            freq_dict[k] = v
    f.close()
    return freq_dict

if __name__=='__main__':
    plt_imshow(count_freq(f_text))