from wordcloud import WordCloudMaker

wc = WordCloudMaker(font_path='C:/Windows/Fonts/HGRSGU.TTC')
wc.read_file('annkert.txt')
wc.create('cloud.png')