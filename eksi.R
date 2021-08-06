


library(SnowballC)
library(tm)
library(RCurl)
library(tidyverse)
library(Rcpp)


turkish_lexicon<-read.csv("turkish_lexicon.csv")


#lexicon'daki büyük harfleri küçük yapma: (daha kolay kod yazimi için)

lexicon2 <- turkish_lexicon %>% 
  select(c("WORD","POLARITY")) %>% 
  rename('word'="WORD",'value'="POLARITY")

lexicon2$value[lexicon2$value==1]<-"positive"
lexicon2$value[lexicon2$value==-1]<-"negative"


library(tidytext)

tokens <- tibble(text = morgomirtext) %>% unnest_tokens(word, text)

text_df <- morgomirtext %>% 
  mutate_all(as.character) %>% 
  unnest_tokens(word, text)

text_df2 <- texttest %>% 
  mutate_all(as.character) %>% 
  unnest_tokens(word, tweettext)


sentiments<-text_df2 %>%
  inner_join(lexicon2) %>% # pull out only sentiment words
  count(value) %>% # count the # of positive & negative words
  spread(value, n, fill = 0) %>% # made data wide rather than narrow
  mutate(value = positive - negative) # # of positive words - # of negat
summary(sentiments)






sentiments<-textt %>%
  inner_join(lexicon2) %>% # pull out only sentiment words
  count(value) %>% # count the # of positive & negative words
  spread(value, n, fill = 0) %>% # made data wide rather than narrow
  mutate(value = positive - negative) # # of positive words - # of negat
summary(sentiments)



