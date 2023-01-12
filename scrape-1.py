# %%
## Importing packages ----------------
import requests
from bs4 import BeautifulSoup
# import line_profiler
import lxml
import cchardet
# from tqdm.notebook import tqdm
# import re
# import json
from tqdm.notebook import tqdm
import pandas as pd
import numpy as np

# %%
pages = []
for x in range(203):
    page = requests.get('https://www.indcareer.com/find/all-colleges-in-maharashtra?page='+str(x))
    pages.append(page)


# %%
soups = []
for x in range(len(pages)):
    soup = BeautifulSoup(pages[x].content, 'html.parser')
    soups.append(soup)

# %%
links = []
for x in soups:
    # print ("Page ------")
    for y in x.find_all("h4"):  
        # print (str(y)[13:].split('" title=')[0])
        link = str(y)[13:].split('" title=')[0]
        links.append(link)
        # print (str(y).split('" title=')[0].split('href="')[1])     
        # print (y.split("title=")[0])
        # break
        # links.append((str(y).split('" title=')[0].split('href="')[1]))
    # break

# %%
links

# %%
links_clean = []

for x in links:
    if (x != 'dal-title" id="myModalLabel">Maharashtra</h4>'):
        links_clean.append(x)

# %%
links_clean

# %%
names = []
phones = []
# names_phones = np.zeros(2).reshape(1, 2)
for x in tqdm(range(len(links_clean))):
    college = requests.get('https://www.indcareer.com' + links_clean[x])
    # soup = BeautifulSoup(college.content, 'html.parser')
    soup = BeautifulSoup(college.content, 'lxml')

    # if (str(soup.find_all('caption'))[29:].split(' </b>')[0] != "Secondary Education Society Shyamrao Bapu Kapgate Arts College, Bhandara"):
    #     try:
    #         print (str(soup.find_all('caption'))[29:].split(' </b>')[0])
    #         # print (str(soup).split('Phone </th><td> ')[1].split('</td>')[0])
    #     except IndexError:
    #         pass
    #         name = str(soup.find_all('caption'))[29:].split(' </b>')[0]
    #         names.append(name)
    #     try:
    #         print (str(soup).split('Phone </th><td> ')[1].split('</td>')[0])
    #     except IndexError:
    #     # continue
    #         pass
    #         phone = str(soup).split('Phone </th><td> ')[1].split(' </td>')[0]
    #         phones.append(phone)

    try:
        print (str(soup.find_all('caption'))[29:].split(' </b>')[0])
        name = str(soup.find_all('caption'))[29:].split(' </b>')[0]
        # print (str(soup).split('Phone </th><td> ')[1].split('</td>')[0])
    except IndexError:
        # pass 
        # name = str(soup.find_all('caption'))[29:].split(' </b>')[0]
        names.append(name)

    try:
        print (str(soup).split('Phone </th><td> ')[1].split('</td>')[0])
        phone = str(soup).split('Phone </th><td> ')[1].split(' </td>')[0]
        phones.append(phone)
    except IndexError:
        phones.append(name)
        # continue
        # pass
        # phone = str(soup).split('Phone </th><td> ')[1].split(' </td>')[0]
        # phones.append(phone)


# %%
len(names)

# %%
phones

# %%
names_phones

# %%
names = np.array(names)
phones = np.array(phones)
names_phones = np.hstack((names[:-1].reshape(len(names)-1, 1), phones.reshape(len(phones), 1)))
names_phones = pd.DataFrame(names_phones)
names_phones.to_excel("names_phones.xlsx", index=False)

# %%
# college.text.split("caption class")[1].split("Email")[1][:300]

# %%
# def decodeEmail(e):
#     de = ""
#     k = int(e[:2], 16)

#     for i in range(2, len(e)-1, 2):
#         de += chr(int(e[i:i+2], 16)^k)

#     return de

# %%
# <span id="signature_email"><a class="__cf_email__" href="/cdn-cgi/l/email-protection" data-cfemail="30425f5e70584346515c5c531e535f5d">[email&#160;protected]</a><script data-cfhash='f9e31' type="text/javascript">/* <![CDATA[ */!function(t,e,r,n,c,a,p){try{t=document.currentScript||function(){for(t=document.getElementsByTagName('script'),e=t.length;e--;)if(t[e].getAttribute('data-cfhash'))return t[e]}();if(t&&(c=t.previousSibling)){p=t.parentNode;if(a=c.getAttribute('data-cfemail')){for(e='',r='0x'+a.substr(0,2)|0,n=2;a.length-n;n+=2)e+='%'+('0'+('0x'+a.substr(n,2)^r).toString(16)).slice(-2);p.replaceChild(document.createTextNode(decodeURIComponent(e)),c)}p.removeChild(t)}}catch(u){}}()/* ]]> */</script></span></span> <span class="separator">|</span>

# %%



