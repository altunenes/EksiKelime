

import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string
import nltk


"""
# ==========================================================================================================================================================
#                                                                       Yazar Enes Altun 10/30/2021
                                            Sadece 15. satırdaki "yazaradi.xml" dosyasının ismini, çalışma dizininizde bulunan XML dosyanızla değiştirin.
                                                         not: edatbag.csv ve turkish_lexicon.csv'nin çalışma dizininde bulunması gerekmekte.
                                                        XML Dosyasini nereden elde edeceğinize ilişkin bilgi için ana sayfaya bakınız.
# ==========================================================================================================================================================
"""
df = pd.read_xml("yazaradi.xml", xpath=".//entry")

sent=pd.read_csv("SWNetTR.csv",encoding="utf-8-sig")

stop=pd.read_csv("edatbag.csv")

nltk.download('stopwords')


def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree



df['entry']= df['entry'].apply(lambda x:remove_punctuation(x))
#ing
stopWordsListEng = stopwords.words("english")
_new_stopwords_to_add=stop["kelime"]
stopWordsListEng.extend(_new_stopwords_to_add)
df['entry'] = df['entry'].apply(lambda x: ' '.join([item for item in x.split() if item not in stopWordsListEng]))
df['entry']= df['entry'].apply(lambda x: x.lower())




def word_frequency(df):
    #create a list of all the words in the dataframe
    word_list = []
    for i in range(len(df)):
        word_list.append(df.iloc[i][0])
    #create a list of all the unique words in the dataframe
    unique_word_list = []
    for i in range(len(word_list)):
        if word_list[i] not in unique_word_list:
            unique_word_list.append(word_list[i])
    #create a dictionary of the frequency of each word
    word_frequency_dict = {}
    for i in range(len(unique_word_list)):
        word_frequency_dict[unique_word_list[i]] = word_list.count(unique_word_list[i])
    #create a dataframe of the word frequency dictionary
    word_frequency_df = pd.DataFrame(word_frequency_dict, index = [0])
    word_frequency_df = word_frequency_df.T
    word_frequency_df.columns = ['frequency']
    #sort the dataframe by the frequency of each word
    word_frequency_df = word_frequency_df.sort_values(by = 'frequency', ascending = True)
    return word_frequency_df


def get_word_frequency(df, column):
    #create a list of all the words in the phrase
    words = []
    for i in range(len(df)):
        words.append(df[column][i].split())
    #create a list of all the unique words in the phrase
    unique_words = []
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in unique_words:
                unique_words.append(words[i][j])
    #create a dictionary of the frequency of each unique word in the phrase
    word_frequency = {}
    for i in range(len(unique_words)):
        word_frequency[unique_words[i]] = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            word_frequency[words[i][j]] += 1
    return word_frequency



#data + sütun inputu

word_frequency=get_word_frequency(df,"entry")
from wordcloud import WordCloud



def plot_word_cloud(wordfrequency):
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(wordfrequency)
    plt.figure(figsize = (15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


plot_word_cloud(word_frequency)
