import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import numpy as np
import string
from unidecode import unidecode


"""
# ==========================================================================================================================================================
#                                                                       Yazar Enes Altun
                                            Sadece 18. satırdaki "evet.csv" dosyasının ismini, çalışma dizininizde bulunan csv dosyanızla değiştirin.
# ==========================================================================================================================================================
"""


#input csv
df=pd.read_csv("evet.csv")

#lexicon
sent=pd.read_csv("turkish_lexicon.csv",encoding="utf-8-sig")

#stopwords
stop=pd.read_csv("edatbag.csv")


def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

df['entry']= df['entry'].apply(lambda x:remove_punctuation(x))

#ing stop wordslar da varsa onlar da...
stopWordsListEng = stopwords.words("english")
_new_stopwords_to_add=stop["kelime"]
stopWordsListEng.extend(_new_stopwords_to_add)
#ing uygulama
df['entry'] = df['entry'].apply(lambda x: ' '.join([item for item in x.split() if item not in stopWordsListEng]))
#büyük harf küçük harf

df['entry']= df['entry'].apply(lambda x: x.lower())
#bütün kelimeleri eng klavye
df['entry']=df['entry'].apply(unidecode)
sent["WORD"]=sent["WORD"].apply(unidecode)

# lexicon da 1 i pozitif, -1 i negatif
sent['POLARITY'] = np.where(sent['POLARITY']>=1, 'positive', 'negative')

sondf=pd.DataFrame()
#kelimeleri tokenize
sondf["WORD"]=df.entry.str.split(expand=True).stack()

sent=sent[["WORD","POLARITY"]]

#inner join
df_inner = pd.merge(sent,sondf,how="inner")
df_inner_count = df_inner.count()
#grupla
groups=df_inner.groupby(["POLARITY"]).size()
print(groups)

groups.plot.bar(color="green")
plt.show()
