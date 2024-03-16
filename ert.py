from flask import Flask
import random
app = Flask(__name__)
facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.", "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.", "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.", "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.", "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.", "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.", "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.", "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

@app.route("/")
def merhaba():
    return f'<h1>Merhaba! sitede <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüleyebilirsiniz!</a>'

@app.route("/rastgele_gercek")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'
    return f'<a href="/i">Eğer baktıysan şimdide biraz bilgi zamanı!</a>'

@app.route("/i")
def bilgi():
    return f'<p>Teknoloji bağımlısı olmamak için önce kendimizi kıısıtlamalıyız, yani sınır koymalıyız. Bazen de olsa egzesiz, spor sohbet ve benzeri şeylerde yapmalıyız. Haydi şimdi birlikte teknoloji bağımlılığına dur diyelim!</p>'

app.run(debug=True)
