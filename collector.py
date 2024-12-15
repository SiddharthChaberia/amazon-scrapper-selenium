from random import betavariate
from bs4 import BeautifulSoup
import os
import pandas as pd

df={
    'title': [], 
    'orig_p': [],
    'disc_p': [], 
    'link': []
}

for files in os.listdir("data"):
    try:
        with open(f"data/{files}", 'r', encoding='utf-8') as f:
            html_doc=f.read()

        soup=BeautifulSoup(html_doc, 'html.parser')

        t=soup.find('h2')  
        title= t.get_text() #product title
        
        l=soup.find('a')
        link='https://amazon.in/' + l['href']  #product link

        dp=soup.find('span', attrs={"class": 'a-price-whole'})
        disc_p=dp.get_text() if dp else 0   #product market price
        
        op=soup.find('div', attrs={"class":"a-section aok-inline-block"})
        op2=op.find('span', attrs={"class":'a-offscreen'}) if op else 0
        orig_p=op2.get_text()[1:] if op2 else 0    #product original price

        df['title'].append(title)
        df['link'].append(link)
        df['disc_p'].append(disc_p)
        df['orig_p'].append(orig_p)

    except Exception as e:
        print(e)
    
data=pd.DataFrame(data=df)
data.to_csv("data.csv")