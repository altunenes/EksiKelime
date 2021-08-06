library(xml2)

#mevcut working directory'i g�rmek i�in konsola getwd() yazin
doc <-read_xml("yazar.xml") #eks'den alinan 


#xml'dek entrylerin hepsini alma ve bunlari yeni bir data.frame'e aktarma:

recs <- xml_find_all(doc, "//entry")  
vals <- trimws(xml_text(recs))

yazar<-data.frame(text=vals)

# opsiyonel: entrylerinizi d�zenli bir excel dosyasina d�n�st�rme  
# write.csv(yazar,"dosyaismi.csv")