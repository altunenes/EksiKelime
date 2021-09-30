[![CodeFactor](https://www.codefactor.io/repository/github/emportent/eksikelime/badge)](https://www.codefactor.io/repository/github/emportent/eksikelime)

# EksiKelime
Ekşi Sözlük kelime+sentiment analizi


Sentimnent için keşke İngilizce'de olduğu gibi R için de güzel bir derin öğrenme modeli olsaydı ve daha fazla sınıf bulunsaydı, ancak bu veri seti de özenle hazırlanmış bir veri seti olduğu için gayet güzel sonuçlar verebilmekte. Bununla birlikte doktora tezinde kullanılan metod; tamamen vader sentiment tarzı, yani -1 +1 olmak üzere iki sınıf var ve veriler bir txt dosyasının içinde. Basitçe bu dosyanın içine girip kendi datamızla karşılaştırma yapıyoruz (en azından ben öyle yaptım).

Ekşi Sözlük'de ayarlar seçeneğinden xml uzantılı yedeğinizi(sözlükte yazdığınız bütün entryler) aldıktan sonraki ilk işiniz mutlaka xml dosyasını data.frame'e çevirmek olsun. (xmlToDataFrame.R script'i tam olarak bunu yapmakta) 


sentiment datası icin daha detaylı incelemeyi buradan yapabilirsiniz: https://github.com/swnettr/SWNetTR



not: edatbag.csv hem başka kaynaklardan alıntı (örneğin aşağıdaki link) hem de sözlüğe özel custom bir şekilde oluşturulmuştur, kendi isteğinize göre yeni kelimeler ekleyebilir veya çıkartabilirsiniz oluştururken kendi amacım daha fazla "isim" yapısındaki sözcüklere ulaşmak ve yazarı tanımasak bile hakkında daha isabetli tahminler yapabilmek içindi.
https://github.com/ahmetax/trstop/blob/master/dosyalar/turkce-stop-words
