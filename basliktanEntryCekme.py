########### yalnizca dilediğiniz başlığı girin, csv olarak kayıt edecektir. Sonraki aşamalarda diğer scriptleri kullanabilirsiniz ###############


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
baslik=input("Çekmek istediğiniz başlık adını girin: ")
  driver=webdriver.Chrome(executable_path=r"C:\Users\Yol Gezer\Desktop\EksiKelime\chromedriver.exe")
driver.get("http://www.eksisozluk.com")
print("Browser Window opened")
input=driver.find_element(By.ID, "search-textbox")
input.send_keys(baslik)
input.send_keys(Keys.ENTER)
url=driver.current_url
source=driver.page_source
soup=BeautifulSoup(source, "html.parser")
try:
    page_count=len(soup.find("div",{"class":"clearfix sub-title-container"}).find("div",{"class":"pager"}).find_all("option"))
except:
    page_count=1
print("Page Count: ",page_count)
headers= {'User-Agent': 'Yol Gezer'}
df=pd.DataFrame(columns=["entry"])
for i in tqdm(range(1,page_count+1)):
    response=requests.get(url+"?p="+str(i),headers=headers)
    time.sleep(2)
    soup=BeautifulSoup(response.content, "html.parser")
    entrys=soup.find_all("div",{"class":"content"})
    for entry in tqdm(entrys):
        df=df.append({"entry":entry.text},ignore_index=True)

df.to_csv(baslik+".csv",encoding="utf-8")
driver.close()
