# -*- coding: utf-8 -*-



import requests
from bs4 import BeautifulSoup

#get the html code   
print("URL->")
URL = input("Enter the url :")
r = requests.get(URL)
   
#parse the html
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
print('\n')


#NAME
txt1=soup.find('div',class_='styles_headerInfo__3h0jF')
name=txt1.h1.a.text
print('NAME:')
print(name)
print("\n")

#DESCRIPTION
txt2=soup.find('div',class_='styles_headerInfo__3h0jF')
des1=txt2.h2.text
print('ONE LINE DESCRIPTION:')
print(des1)
print("\n")

#TAG
#txt3=soup.find('div',class_='styles_font__2Nqit styles_grey__3J1TQ styles_xSmall__1eYHj styles_normal__iGf4Q styles_item__13V32 styles_button__3TLZg styles_lineHeight__2RYYy styles_underline__20yPd styles_uppercase__2YIgd')
print("TAGS:")
tags=[]
table = soup.find('div', attrs = {'class':'styles_topicPriceWrap__2fqZ7'}) 
for row in table.findAll('div',attrs = {'class':'styles_font__2Nqit styles_grey__3J1TQ styles_xSmall__1eYHj styles_normal__iGf4Q styles_item__13V32 styles_button__3TLZg styles_lineHeight__2RYYy styles_underline__20yPd styles_uppercase__2YIgd'}):
    tag={}
    tag['Tags']=row.a.text
    tags.append(tag)
print(tags)    
print("\n")

#LONG DESCRIPTION
print("LONG DESCRIPTION:")
txt4=soup.find('div',class_='styles_font__2Nqit styles_small__2bw6M styles_normal__iGf4Q styles_format__219oD styles_lineHeight__2RYYy styles_underline__20yPd')
des2=txt4.text
print(des2)
print("\n")



    