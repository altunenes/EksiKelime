[![CodeFactor](https://www.codefactor.io/repository/github/altunenes/eksikelime/badge)](https://www.codefactor.io/repository/github/altunenes/eksikelime)
# EksiKelime
Ekşi Sözlük kelime+sentiment analizi

                                                                         # EksiKelime Güncelleme:



Bu scriptleri ilk yazdığımda, yazarın kendi datasını sözlüğe girip kendisi alması gerekmekteydi, ancak https://github.com/cagriozkurt/EksiYedek ile bu iş çok daha kolay hale getirilmiş. Bu adresten gidip ilgili scripti çalıştırdığınızda size XML dosyası halinde dilediğiniz yazarın bütün entryleri XML formatında veriyor. R içerisinde yapmak istiyorsanız XML dosyasını csv'e çevirmek için yine benim yazdığım R scriptini kullanabilirsiniz. Ancak Python için buna gerek yok, scriptlerin içerisine otomatik olarak ekledim, sadece EksiYedek scriptini çalıştırıp dilediğiniz yazarın XML dosyasını indirdikten sonra ilgili python scriptlerini çalıştırmanız yeterlidir. 

Son olarak, wordcloud ve yine vader tarzı sentiment analizi için R kodlarını Python diline çevirerek de ekledim; dilediğiniz dil ile bu işi yapabilirsiniz :)


                                                                          # EksiKelime




Sentimnent için keşke İngilizce'de olduğu gibi TR için de güzel bir derin öğrenme modelleri olsaydı ve daha fazla sınıf bulunsaydı, ancak bu veri seti bir doktora tezinden alınmış olunupözenle hazırlanmış bir veri seti; bundan dolayı da gayet güzel sonuçlar verebilmekte. Bununla birlikte doktora tezinde kullanılan metod; tamamen vader sentiment tarzı, yani -1 +1 olmak üzere iki sınıf var ve veriler bir txt dosyasının içinde. Basitçe bu dosyanın içine girip kendi datamızla karşılaştırma yapıyoruz (en azından ben öyle yaptım).

Ekşi Sözlük'de ayarlar seçeneğinden xml uzantılı yedeğinizi(sözlükte yazdığınız bütün entryler) aldıktan sonraki ilk işiniz mutlaka xml dosyasını data.frame'e çevirmek olsun. (xmlToDataFrame.R script'i tam olarak bunu yapmakta) 


sentiment datası icin daha detaylı incelemeyi buradan yapabilirsiniz: https://github.com/swnettr/SWNetTR



not: edatbag.csv hem başka kaynaklardan alıntı (örneğin aşağıdaki link) hem de sözlüğe özel custom bir şekilde oluşturulmuştur, kendi isteğinize göre yeni kelimeler ekleyebilir veya çıkartabilirsiniz oluştururken kendi amacım daha fazla "isim" yapısındaki sözcüklere ulaşmak ve yazarı tanımasak bile hakkında daha isabetli tahminler yapabilmek içindi.
https://github.com/ahmetax/trstop/blob/master/dosyalar/turkce-stop-words
