library(SnowballC)
library(tm)
library(RCurl)
library(tidyverse)
library(Rcpp)

#lexicon icin: bkz F. Saglam, B. Gen�, H. Sever, "Extending a Sentiment Lexicon with Synonym-Antonym Datasets: SWNetTR++", Turkish Journal of Electrical Engineering and Computer Sciences, 27 (2019) 1806-1820.

turkish_lexicon<-read.csv("SWNetTR.csv")

#lexicon'daki b�y�k harfleri k���k yapma: (daha kolay kod yazimi i�in)

lexicon2 <- turkish_lexicon %>% 
  select(c("WORD","POLARITY")) %>% 
  rename('word'="WORD",'value'="POLARITY")

lexicon2$value[lexicon2$value==1]<-"positive"
lexicon2$value[lexicon2$value==-1]<-"negative"

#bu lexicon'da 1 ifadesi kelime i�in pozitif, -1 ifadesi negatif anlaminda bunari degistirdim


library(tidytext)

tokens <- tibble(text = yazar$text) %>% unnest_tokens(word, text)

# duygu y�kl� kelimeleri s�zl�kte kullanilan kelimelerle birlestirme ve bunlarin frekanslarini �ikartma:

sentiments<-tokens %>%
  inner_join(lexicon2) %>% 
  count(value) %>% 
  spread(value, n, fill = 0) %>%
  mutate(value = positive - negative) 

#�zet istatistigi:
summary(sentiments)


