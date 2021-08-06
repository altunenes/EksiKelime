library(tm)
library(RCurl)
library(tidyverse)
library(Rcpp)

#lexicon icin: bkz F. Saglam, B. Genç, H. Sever, "Extending a Sentiment Lexicon with Synonym-Antonym Datasets: SWNetTR++", Turkish Journal of Electrical Engineering and Computer Sciences, 27 (2019) 1806-1820.

turkish_lexicon<-read.csv("SWNetTR.csv")

#lexicon'daki büyük harfleri küçük yapma: (daha kolay kod yazimi için)

lexicon2 <- turkish_lexicon %>% 
  select(c("WORD","POLARITY")) %>% 
  rename('word'="WORD",'value'="POLARITY")

lexicon2$value[lexicon2$value==1]<-"positive"
lexicon2$value[lexicon2$value==-1]<-"negative"

#bu lexicon'da 1 ifadesi kelime için pozitif, -1 ifadesi negatif anlaminda bunari degistirdim



tokens <- tibble(text = yazar$text) %>% unnest_tokens(word, text)

# duygu yüklü kelimeleri sözlükte kullanilan kelimelerle birlestirme ve bunlarin frekanslarini çikartma:

sentiments<-tokens %>%
  inner_join(lexicon2) %>% 
  count(value) %>% 
  spread(value, n, fill = 0) %>%
  mutate(value = positive - negative) 

#özet istatistigi:
sentiments



