library(tm)
library(tidyverse)
library(Rcpp)
library(tidyverse)
edatbag <- read_csv("edatbag.csv")  ### edatlar, baglaclar


doc.corpus<-Corpus(VectorSource(yazar$text)) #yazar adli dataframe'i xmlToDataFrame.R adli scriptte olusturmustuk

doc.corpus<-tm_map(doc.corpus,content_transformer(tolower))

doc.corpus<-tm_map(doc.corpus,content_transformer(removePunctuation))

doc.corpus<-tm_map(doc.corpus,content_transformer(removeNumbers))

doc.corpus<-tm_map(doc.corpus, removeWords, edatbag$kelime)

# doc.corpus<-tm_map(doc.corpus, removeWords, c("he","var","sen","gel","amk")) #buraya siz kendi verinize göre yeni custom kelimeler ekleyip filtrelemeler yapabilirsiniz

doc.corpus<-tm_map(doc.corpus, removeWords, stopwords("english"))

#özel isaretleri falan kaldirmak için basit bir fonksiyon yazimi:

removeURL<-function(x) gsub('http[[:alnum:]]*','',x)

myCorpus<-tm_map(doc.corpus,removeURL)

myCorpus<-tm_map(myCorpus,stripWhitespace)

tdm<-TermDocumentMatrix(myCorpus)

mtdm<-as.matrix(TermDocumentMatrix(myCorpus))


term_frequency<-rowSums(mtdm)

term_frequency<-sort(term_frequency,decreasing=TRUE)

#en çok kullanillan 70 kelimeyi sayilariyla birlikte yazdir:
term_frequency[1:70]


text_data<- data.frame(word = names(term_frequency),freq=term_frequency)
text_data<-remove_rownames(text_data)

#word cloud seklinde görsellestirme 

set.seed(1234) ### zar
wordcloud::wordcloud(words = text_data$word, freq = text_data$freq, min.freq = 85,
          max.words=30, random.order=FALSE, rot.per=0.35, 
          colors=RColorBrewer::brewer.pal(8, "Dark2"))


#bir subset islemi yapip kelime frekansina veya baska bir seye göre seçim yapip görsellestirme:

w<-subset(term_frequency,term_frequency>=70)

barplot(w, las = 2)





