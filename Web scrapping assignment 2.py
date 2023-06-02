#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer 1
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Get the webpage
url = 'https://www.naukri.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search button
search_skill = 'Data Analyst'
search_location = 'Bangalore'

search_form = soup.find('form', {'name': 'searchForm'})
search_form.find('input', {'id': 'root-autocomplete'}).attrs['value'] = search_skill
search_form.find('input', {'id': 'root-autocomplete-keywords'}).attrs['value'] = search_location

# Step 3: Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 4: Scrape data for the first 10 job results
job_results = soup.find_all('article', {'itemtype': 'http://schema.org/JobPosting'})[:10]

data = []
for result in job_results:
    job_title = result.find('a', {'class': 'title'}).text.strip()
    company_name = result.find('a', {'class': 'subTitle'}).text.strip()
    experience_required = result.find('li', {'class': 'experience'}).text.strip()
    job_location = result.find('li', {'class': 'location'}).text.strip()

    data.append({
        'Job Title': job_title,
        'Company Name': company_name,
        'Experience Required': experience_required,
        'Job Location': job_location
    })

# Step 5: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 2
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Get the webpage
url = 'https://www.naukri.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search button
search_skill = 'Data Scientist'
search_location = 'Bangalore'

search_form = soup.find('form', {'name': 'searchForm'})
search_form.find('input', {'id': 'root-autocomplete'}).attrs['value'] = search_skill
search_form.find('input', {'id': 'root-autocomplete-keywords'}).attrs['value'] = search_location

# Step 3: Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 4: Scrape data for the first 10 job results
job_results = soup.find_all('article', {'itemtype': 'http://schema.org/JobPosting'})[:10]

data = []
for result in job_results:
    job_title = result.find('a', {'class': 'title'}).text.strip()
    company_name = result.find('a', {'class': 'subTitle'}).text.strip()
    job_location = result.find('li', {'class': 'location'}).text.strip()

    data.append({
        'Job Title': job_title,
        'Company Name': company_name,
        'Job Location': job_location
    })

# Step 5: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 3

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Get the webpage
url = 'https://www.naukri.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search button
search_skill = 'Data Scientist'

search_form = soup.find('form', {'name': 'searchForm'})
search_form.find('input', {'id': 'root-autocomplete'}).attrs['value'] = search_skill

# Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 3: Apply location and salary filters
location_filter = 'Delhi/NCR'
salary_filter = '3-6 Lakhs'

filter_form = soup.find('form', {'id': 'filtersForm'})
filter_form.find('label', {'for': 'locationDelhi/NCR'}).find('input').attrs['checked'] = 'checked'
filter_form.find('label', {'for': 'salary36'}).find('input').attrs['checked'] = 'checked'

# Submit the filter form
response = requests.post(url, data=filter_form.form_data())

# Step 4: Scrape data for the first 10 job results
job_results = soup.find_all('article', {'itemtype': 'http://schema.org/JobPosting'})[:10]

data = []
for result in job_results:
    job_title = result.find('a', {'class': 'title'}).text.strip()
    company_name = result.find('a', {'class': 'subTitle'}).text.strip()
    job_location = result.find('li', {'class': 'location'}).text.strip()
    experience_required = result.find('li', {'class': 'experience'}).text.strip()

    data.append({
        'Job Title': job_title,
        'Company Name': company_name,
        'Job Location': job_location,
        'Experience Required': experience_required
    })

# Step 5: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 4

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to Flipkart webpage
url = 'https://www.flipkart.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search icon
search_query = 'sunglasses'

search_form = soup.find('form', {'class': '_2M8cLY'})
search_form.find('input', {'type': 'text'}).attrs['value'] = search_query

# Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 3: Scrape data for the first 100 sunglasses listings
data = []
review_count = 0

while review_count < 100:
    product_cards = soup.find_all('div', {'class': '_2kHMtA'})
    for card in product_cards:
        brand = card.find('div', {'class': '_2WkVRV'}).text.strip()
        description = card.find('a', {'class': 'IRpwTa'}).text.strip()
        price = card.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()

        data.append({
            'Brand': brand,
            'Product Description': description,
            'Price': price
        })

        # Step 4: Scrape data for reviews
        product_url = 'https://www.flipkart.com' + card.find('a', {'class': '_1fQZEK'})['href']
        product_response = requests.get(product_url)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')

        reviews = product_soup.find_all('div', {'class': '_3gijNv'})
        for review in reviews:
            rating = review.find('div', {'class': '_3LWZlK _1BLPMq'}).text.strip()
            review_summary = review.find('p', {'class': '_2-N8zT'}).text.strip()
            full_review = review.find('div', {'class': 't-ZTKy'}).text.strip()

            data.append({
                'Rating': rating,
                'Review Summary': review_summary,
                'Full Review': full_review
            })

            review_count += 1
            if review_count >= 100:
                break

    # Go to the next page
    next_button = soup.find('a', {'class': '_1LKTO3'})
    if next_button:
        next_url = 'https://www.flipkart.com' + next_button['href']
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

# Step 5: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 5

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to the Flipkart product reviews page for iPhone 11
url = 'https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Scrape data for the first 100 reviews
data = []
review_count = 0

while review_count < 100:
    reviews = soup.find_all('div', {'class': '_27M-vq'})
    for review in reviews:
        rating = review.find('div', {'class': '_3LWZlK _1BLPMq'}).text.strip()
        review_summary = review.find('p', {'class': '_2-N8zT'}).text.strip()
        full_review = review.find('div', {'class': 't-ZTKy'}).text.strip()

        data.append({
            'Rating': rating,
            'Review Summary': review_summary,
            'Full Review': full_review
        })

        review_count += 1
        if review_count >= 100:
            break

    # Go to the next page
    next_button = soup.find('a', {'class': '_1LKTO3'})
    if next_button:
        next_url = 'https://www.flipkart.com' + next_button['href']
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

# Step 3: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 6

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to Flipkart webpage
url = 'https://www.flipkart.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search icon
search_query = 'sneakers'

search_form = soup.find('form', {'class': '_2M8cLY'})
search_form.find('input', {'type': 'text'}).attrs['value'] = search_query

# Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 3: Scrape data for the first 100 sneakers
data = []

while len(data) < 100:
    product_cards = soup.find_all('div', {'class': '_2kHMtA'})
    for card in product_cards:
        brand = card.find('div', {'class': '_2WkVRV'}).text.strip()
        description = card.find('a', {'class': 'IRpwTa'}).text.strip()
        price = card.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()

        data.append({
            'Brand': brand,
            'Product Description': description,
            'Price': price
        })

        if len(data) >= 100:
            break

    # Go to the next page
    next_button = soup.find('a', {'class': '_1LKTO3'})
    if next_button:
        next_url = 'https://www.flipkart.com' + next_button['href']
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

# Step 4: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 7

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to the Amazon India webpage
url = 'https://www.amazon.in/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Enter search criteria and click the search icon
search_query = 'Laptop'

search_form = soup.find('form', {'id': 'nav-search-form'})
search_form.find('input', {'type': 'text'}).attrs['value'] = search_query

# Submit the search form
response = requests.post(url, data=search_form.form_data())

# Step 3: Set the CPU Type filter to "Intel Core i7"
filter_form = soup.find('form', {'id': 'leftNavContainer'})
cpu_type_checkbox = filter_form.find('input', {'aria-label': 'Intel Core i7'})
cpu_type_checkbox.attrs['checked'] = 'true'

# Submit the filter form
response = requests.post(url, data=filter_form.form_data())

# Step 4: Scrape data for the first 10 laptops
data = []

laptops = soup.find_all('div', {'data-component-type': 's-search-result'})
for laptop in laptops[:10]:
    title = laptop.find('h2', {'class': 'a-size-mini'}).text.strip()
    ratings = laptop.find('span', {'class': 'a-icon-alt'}).text.strip()
    price = laptop.find('span', {'class': 'a-price-whole'}).text.strip()

    data.append({
        'Title': title,
        'Ratings': ratings,
        'Price': price
    })

# Step 5: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 8

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to the azquotes webpage
url = 'https://www.azquotes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Click on Top Quotes
top_quotes_link = soup.find('a', text='Top Quotes')
top_quotes_url = url + top_quotes_link['href']
response = requests.get(top_quotes_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Scrape data for the top 1000 quotes
data = []

quotes = soup.find_all('div', {'class': 'title'})
for quote in quotes:
    quote_text = quote.find('a').text.strip()
    author = quote.find_next_sibling('div', {'class': 'author'}).text.strip()
    quote_type = quote.find_next_sibling('div', {'class': 'kw-box'}).text.strip()

    data.append({
        'Quote': quote_text,
        'Author': author,
        'Type of Quote': quote_type
    })

    if len(data) >= 1000:
        break

# Step 4: Create a dataframe of the scraped data
df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 9

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to the jagranjosh webpage
url = 'https://www.jagranjosh.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Click on the GK option
gk_link = soup.find('a', text='GK')
gk_url = url + gk_link['href']
response = requests.get(gk_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Click on the List of all Prime Ministers of India
pm_link = soup.find('a', text='List of all Prime Ministers of India')
pm_url = url + pm_link['href']
response = requests.get(pm_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Scrape the mentioned data and create the DataFrame
data = []

table = soup.find('table', {'class': 'table4'})
rows = table.find_all('tr')[1:]  # Skip the header row

for row in rows:
    columns = row.find_all('td')
    name = columns[0].text.strip()
    born_dead = columns[1].text.strip()
    term_of_office = columns[2].text.strip()
    remarks = columns[3].text.strip()

    data.append({
        'Name': name,
        'Born-Dead': born_dead,
        'Term of Office': term_of_office,
        'Remarks': remarks
    })

df = pd.DataFrame(data)
print(df)


# In[ ]:


#Answer 10

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Go to the motor1 webpage
url = 'https://www.motor1.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Type in the search bar '50 most expensive cars'
search_input = soup.find('input', {'id': 'js-search-bar'})
search_input['value'] = '50 most expensive cars'

# Step 3: Click on '50 most expensive cars in the world'
search_button = soup.find('button', {'class': 'header-search__button'})
search_url = url + 'search/?q=' + search_input['value'].replace(' ', '+')
response = requests.get(search_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Scrape the mentioned data and create the dataframe
data = []

cars = soup.find_all('div', {'class': 'list-item'})
for car in cars:
    name = car.find('h3', {'class': 'list-item-title'}).text.strip()
    price = car.find('span', {'class': 'list-item-price'}).text.strip()

    data.append({
        'Car Name': name,
        'Price': price
    })

df = pd.DataFrame(data)
print(df)


# In[ ]:





# In[ ]:




