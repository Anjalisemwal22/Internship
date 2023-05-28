#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ANSWER 1
# import required modules
import requests
 
# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
 
# display status code
print(page.status_code)
 
# display scraped data
print(page.content)


# In[10]:


#ANSWER 5
import requests
from bs4 import BeautifulSoup

url='https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
for x in headlines:
    print(x.text.strip())


# In[ ]:




