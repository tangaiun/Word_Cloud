# ライブラリのインポート
from wordcloud import WordCloud

# テキストのサンプル
text = 'キャノン RX100 富士通 富士通 リコー RX100 RX100 RX100 キャノン ソニー ニコン ソニー パナソニック RX100 RX100 ソニー'


# Windowsにインストールされているフォントを指定 
wc_py = WordCloud(font_path='C:/Windows/Fonts/HGRSGU.TTC')
# ワードクラウドの作成
wc_py.generate(text)
# WindowsパソコンのPドライブ直下に画像を保存
wc_py.to_file('wc.jpg') 